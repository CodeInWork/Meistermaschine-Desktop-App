from pathlib import Path

from PyQt6 import QtCore

from MEISTERMASCHINE.sd_utilities.sd_export import export_preset_to_sd


class SDExportWorker(QtCore.QObject):

    progress = QtCore.pyqtSignal(int, int, str)
    finished = QtCore.pyqtSignal(str)
    failed = QtCore.pyqtSignal(str)

    def __init__(
        self,
        sd_root: str,
        preset_name: str,
        application_path: str,
        music_buttons,
        setting_buttons,
        weather_buttons,
        special_buttons,
        replace_existing: bool = False,
    ):
        super().__init__()

        self.sd_root = sd_root
        self.preset_name = preset_name
        self.application_path = application_path

        self.music_buttons = music_buttons
        self.setting_buttons = setting_buttons
        self.weather_buttons = weather_buttons
        self.special_buttons = special_buttons

        self.replace_existing = replace_existing

    @QtCore.pyqtSlot()
    def run(self) -> None:
        try:
            export_directory = export_preset_to_sd(
                sd_root=self.sd_root,
                preset_name=self.preset_name,
                application_path=self.application_path,
                music_buttons=self.music_buttons,
                setting_buttons=self.setting_buttons,
                weather_buttons=self.weather_buttons,
                special_buttons=self.special_buttons,
                progress_callback=self._report_progress,
                replace_existing=self.replace_existing,
            )

        except Exception as error:
            self.failed.emit(str(error))
            return

        self.finished.emit(str(export_directory))

    def _report_progress(
        self,
        copied_bytes: int,
        total_bytes: int,
        current_file: Path,
    ) -> None:

        self.progress.emit(
            copied_bytes,
            total_bytes,
            current_file.name,
        )