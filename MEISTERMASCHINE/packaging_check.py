"""Opt-in build verification: cli.py --smoke-test <absolute JSON report path>."""
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import traceback
import wave


def run(report_path):
    report = {"frozen": bool(getattr(sys, "frozen", False))}
    try:
        os.environ["QT_QPA_PLATFORM"] = "offscreen"
        # Verify automatic discovery, without a machine-specific override.
        os.environ.pop("IMAGEIO_FFMPEG_EXE", None)
        import imageio_ffmpeg
        from PyQt6 import QtCore, QtGui, QtMultimedia, QtWidgets
        from MEISTERMASCHINE.GUI_qtDesign import Ui_MainWindow
        from MEISTERMASCHINE.sd_utilities.sd_export import _convert_to_mp3

        class CheckUi(Ui_MainWindow):
            def restore_last_preset(self):
                pass  # Do not read or change the user's last-preset setting.

            def refresh_sd_cards(self):
                pass  # No removable-drive access is needed for this check.

        app = QtWidgets.QApplication([])
        window = QtWidgets.QMainWindow()
        ui = CheckUi()
        ui.setupUi(window)
        window.show()
        app.processEvents()
        resources = Path(ui.application_path)
        for name in ("icons", "sounds", "presets"):
            assert (resources / name).is_dir(), f"Missing resource folder: {name}"
        assert not QtGui.QIcon(str(resources / "icons/icon_circle.png")).isNull()
        buttons = list(ui.playerController.all_buttons())
        assert len(buttons) == 20
        assert all(not button.icon().isNull() for button in buttons)
        report["resources"] = str(resources)
        report["buttons"] = len(buttons)
        report["sound_files"] = len(list((resources / "sounds").rglob("*.*")))

        ffmpeg = Path(imageio_ffmpeg.get_ffmpeg_exe()).resolve()
        assert ffmpeg.is_file()
        if report["frozen"]:
            assert ffmpeg.is_relative_to(Path(sys._MEIPASS).resolve())
        report["ffmpeg"] = str(ffmpeg)
        with tempfile.TemporaryDirectory(prefix="meistermaschine-check-") as tmp:
            source = Path(tmp) / "silence.wav"
            target = Path(tmp) / "converted.mp3"
            with wave.open(str(source), "wb") as audio:
                audio.setnchannels(1)
                audio.setsampwidth(2)
                audio.setframerate(44100)
                audio.writeframes(b"\0\0" * 44100)
            _convert_to_mp3(source, target)
            assert target.stat().st_size > 0
            player = QtMultimedia.QMediaPlayer()
            player.setSource(QtCore.QUrl.fromLocalFile(str(target)))
            deadline = time.monotonic() + 15
            while player.duration() == 0 and time.monotonic() < deadline:
                app.processEvents()
                if player.error() != QtMultimedia.QMediaPlayer.Error.NoError:
                    raise RuntimeError(player.errorString())
                time.sleep(0.02)
            assert player.duration() > 0, "Qt could not load the converted MP3"
            report["mp3_duration_ms"] = player.duration()
            player.setSource(QtCore.QUrl())
            app.processEvents()
        window.close()
        report["ok"] = True
    except Exception:
        report["ok"] = False
        report["error"] = traceback.format_exc()
    Path(report_path).write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 0 if report["ok"] else 1
