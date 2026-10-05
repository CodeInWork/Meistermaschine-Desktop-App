import json
from pathlib import Path
import tempfile
import unittest
from types import SimpleNamespace

from MEISTERMASCHINE.example_assets import validate_examples
from MEISTERMASCHINE.audio.playlist import Playlist
from MEISTERMASCHINE.preset_utilities.preset_io import load_preset_json, save_preset_json
from MEISTERMASCHINE.sd_utilities.sd_export import collect_audio_files


class ExampleAssetsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.package = Path(self.tmp.name)
        self.audio = self.package / "assets/examples/audio"
        self.audio.mkdir(parents=True)
        self.preset = self.package / "assets/examples/presets/Medieval.json"
        self.preset.parent.mkdir()
        (self.audio / "track.wav").write_bytes(b"test")

    def write_preset(self, path):
        self.preset.write_text(json.dumps({"channels": {"music": {
            "buttons": [{"index": 0, "playlist": [path]}]}}}), encoding="utf-8")

    def test_valid_reference_and_both_separators(self):
        for separator in ("/", "\\"):
            self.write_preset(separator.join(("assets", "examples", "audio", "track.wav")))
            self.assertEqual(validate_examples(self.package), {self.audio / "track.wav"})

    def test_missing_and_escaping_references_rejected(self):
        (self.package / "private.wav").write_bytes(b"private")
        for path in ("assets/examples/audio/missing.wav", "assets/examples/audio/../../../private.wav",
                     "private.wav", str(self.audio / "track.wav"), "C:\\private.wav",
                     "C:private.wav", "\\\\server\\share\\private.wav", "", None):
            with self.subTest(path=path):
                self.write_preset(path)
                with self.assertRaises(ValueError):
                    validate_examples(self.package)

    def test_local_paths_still_round_trip_and_export(self):
        local = self.package / "sounds/local.wav"
        local.parent.mkdir()
        local.write_bytes(b"local")
        external = self.package / "user/track.wav"
        external.parent.mkdir()
        external.write_bytes(b"external")
        button = SimpleNamespace(playlist=Playlist())
        controller = SimpleNamespace(channels={"music": SimpleNamespace(buttons=[button], loop=True)})
        for stored, expected in (("sounds/local.wav", local), (str(external), external),
                                 ("assets/examples/audio/track.wav", self.audio / "track.wav")):
            self.write_preset(stored)
            load_preset_json(controller, self.preset)
            self.assertEqual(collect_audio_files([[button]], str(self.package)), [expected])
            save_preset_json(controller, self.preset)
            load_preset_json(controller, self.preset)
            self.assertEqual(button.playlist.tracks[0][0], stored)


if __name__ == "__main__":
    unittest.main()
