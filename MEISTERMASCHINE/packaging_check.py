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
        from MEISTERMASCHINE.sd_utilities.sd_export import collect_audio_files
        from MEISTERMASCHINE.example_assets import validate_examples
        from MEISTERMASCHINE.preset_utilities.preset_io import load_preset_json

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
        for name in ("icons", "assets/examples/audio", "assets/examples/presets"):
            assert (resources / name).is_dir(), f"Missing resource folder: {name}"
        assert not QtGui.QIcon(str(resources / "icons/icon_circle.png")).isNull()
        buttons = list(ui.playerController.all_buttons())
        assert len(buttons) == 20
        assert all(not button.icon().isNull() for button in buttons)
        report["resources"] = str(resources)
        report["buttons"] = len(buttons)
        expected_audio = validate_examples(resources)
        load_preset_json(ui.playerController, resources / "assets/examples/presets/Medieval.json")
        actual_audio = set(collect_audio_files([buttons], ui.application_path))
        assert actual_audio == expected_audio
        report["sound_files"] = len(actual_audio)
        report["audio_browser_root"] = ui.default_soundFile_path
        assert any(ui.presetCombobox.itemText(i) == "Medieval (Example)"
                   for i in range(ui.presetCombobox.count()))
        if report["frozen"]:
            assert not (resources / "sounds").exists()
            assert not (resources / "presets").exists()
        # Exercise the application's playback path for every example track.
        checked = []
        channel = ui.playerController.channels["music"]
        channel.player.setAudioOutput(None)  # Silent automated playback.
        for source in sorted(actual_audio):
            relative = str(source.relative_to(resources))
            ui.playerController.play_channel(channel, (relative, source.stem), ui.application_path)
            deadline = time.monotonic() + 15
            while channel.player.duration() == 0 and time.monotonic() < deadline:
                app.processEvents()
                if channel.player.error() != QtMultimedia.QMediaPlayer.Error.NoError:
                    raise RuntimeError(f"{source}: {channel.player.errorString()}")
                time.sleep(0.02)
            assert channel.player.duration() > 0, f"Qt could not load {source}"
            assert Path(channel.player.source().toLocalFile()).resolve() == source
            checked.append(relative)
            channel.player.stop()
            channel.player.setSource(QtCore.QUrl())
            app.processEvents()
        report["example_tracks_loaded"] = checked
        if not report["frozen"] and (resources / "presets/Medieval.json").is_file():
            load_preset_json(ui.playerController, resources / "presets/Medieval.json")
            local_audio = collect_audio_files([buttons], ui.application_path)
            assert len(local_audio) == len(expected_audio)
            assert all(path.is_file() and path.is_relative_to(resources / "sounds") for path in local_audio)
            assert Path(ui.default_soundFile_path) == resources / "sounds"
            report["legacy_local_tracks_resolved"] = len(local_audio)

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
