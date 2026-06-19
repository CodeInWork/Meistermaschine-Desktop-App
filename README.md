# Meistermaschine-Desktop-App

How to run it

The app is set up to use uv. So, install instruction beneath.
Simply execute:

</> Bash

uv sync

uv run python cli.py

in the project root folder

## Requirements

- Python 3.11 or newer
- uv

Install uv:

https://docs.astral.sh/uv/

## First-time setup

Clone the repository:

```bash
git clone <repository-url>
cd Meistermaschine-Desktop-App
```

Create the project environment and install all dependencies:

```bash
uv sync
```

## Running the application

Start the application with:

```bash
uv run python cli.py
```

## Development

If additional packages are required (PyQt6):

```bash
uv add <package>
```

Install a development dependency:

```bash
uv add --dev <package>
```

Update the lockfile:

```bash
uv lock
```

Synchronize the environment:

```bash
uv sync
```

Run via:
```bash
uv run python cli.py
```



Diese App wurde speziell für Table-Top-Rollenspiele entwickelt und soll es dem Meister ermöglichen für jede Spielsituation die passende Musik und Hintergrundgeräusche auszuwählen ohne dabei von seiner Rolle als Spielmeister abgelenkt zu werden. Dazu ermöglicht die App das Zusammenstellen von Presets die sich den jeweiligen Anforderungen des Abenteuers und der dazugehörigen Welt anpassen lassen.

Die App ist gegliedert in drei Bereiche:

1. Sound Interface (mitte)

Hier befinden sich die Buttons die das Abspielen von Soundfiles während des Abenteuers ermöglichen. Sie sind in vier Spalten gegliedert, von denen jeweils nur ein Button aktiviert werden kann Jede und über einen eigenen Lautstärkeregler verfügt. Es können also insgesamt vier Soundfiles gleichzeitig abgespielt werden.
Die Buttons können zwar frei mit Audiofiles via drag and drop vom rechten Dateibaum belegt werden, snd jedoch für unterschiedliche Situationen konzipiert:

Grün: Hintergrundmusik; jeder Button kann mit mehreren Soundfiles belegt werden die eine Playlist bilden. Wenn ein Button aktiviert wurde, wird die Plalist im Loop abgespielt, sodass keine Pause entsteht. Die Smileys dienen der Einordnung nach passender Stimmungslage.

Gelb: Ort bzw. Situation; jeder Button kann nur mit einem einzigen Soundfile belegt werden, das sich aber wiederholt solange der Button aktiv ist. Die Icons entsprechen den generischen Settings eines Rollenspiels: Taverne, Stadt, Land, Dungeon und Kampf

Blau: Wetter bzw. Tageszeit; jeder Button kann nur mit einem einzigen Soundfile belegt werden, das sich aber wiederholt solange der Button aktiv ist. Die Icons entsprechen den generischen Wetterbedingungen oder Tageszeiten eines Rollenspiels: Nacht, Wellen, Wind, Regen/Sturm, Schneesturm

Bunt: Spezial;  jeder Button kann nur mit einem einzigen Soundfile belegt werden, das nach Aktivierung auch nur ein einziges mal abgespielt wird. Die Icons und Farben dienen als Gedächtnisstütze. Diese Buttons sind für spezielle Soundeffekte reserviert, wie der Schrei eines Drachen oder Ähnliches.


2. Sound Control (unten links)

Hier können mit den gängigen Buttons (Play, Zurück, Vor, Stop) das Abspielen der Musik (Grüne Buttons), die Gesamtlautstärke (Master Volume) und die Position im Stück (Progress Bar) kontrolliert bzw. angezeigt werden. Das rechte Feld zeigt die Playlist des aktiven Buttons an über dem sich der Mauszeiger befindet. Ist der Zeiger nicht über einem Button wird die Playlist des aktiven Musikbuttons (Grüne Buttons) angezeigt. Die Liste kann mit Drag and Drop neu angeordnet oder durch Klicken ein anderes File abgespielt werden. Ein Doppelklick löscht das Soundfile aus der Liste.


3. Optionale Reiter (rechts)

a) Dateisystem
Hier befinden sich die Soundfiles die via Drag and Drop den jeweiligen Buttons zugeordnet werden können. Der Button 'Change Folder' ändert hierbei den Root Folder, sodass auch files z.Bsp. von der Festplatte angezeigt werden können. Es wird aber empfohlen die gewünschten Stücke in die angezeigten Ordner zu kopieren und von dort den Buttons zuzuordnen. Im Moment werden die Formate *.mp3, *.wav und *.ogg unterstützt.
Die SD-Kartenoption ist für zukünftige Anwendungen vorgesehen und ist noch nicht einsatzbereit.

b) Würfel
Hier finden sich alle gängigen Rollenspielwürfel (W2, W4, W6, W8, W10, W12, W20 und W100). Das Ergebnis wird 30 Sekunden angezeigt. Wird innerhalb dieser Zeit der selbe Würfelbutton erneut betätigt, so wird zusätzlich zum Ergebnis auch die Summe der vorhergegangenen Augen angezeigt. Nach Ablauf der Zeit wird der Würfel gelöscht. Zusätzlich steht der Schicksalswürfel zur Verfügung. Er verfügt über keine Augen, sondern gibt ein Spektrum zwischen sehr schlecht (Kritischer Misserfolg) und sehr gut (kritischer Erfolg) an. Die Wahrscheinlichkeiten sind:
  
  Kritischer Misserfolg   (Leuchtender Totenschädel)    1/20
  sehr schlecht           (zwei Totenschädel)           3/20
  schlecht                (Totenschädel)                4/20
  neutral                 (Herz/Totenschädel)           4/20
  gut                     (Herz)                        4/20
  sehr gut                (Zwei Herzen)                 3/20
  Kritischer Erfolg       (Leuchtendes Herz)            1/20  


5. Menüleiste (oben)

Hier befinden sich die Optionen zum anlegen und speichern neuer Presets (Gespeicherte Belegungen von Buttons).
Im Reiter 'File' können neue Presets angelegt ('New'), alte geöffnet ('Open'), die jetzige Konfiguration überschrieben ('Save', 'Strg+S') oder unter neuem Namen gespeichert werden ('Save as'). Rechts befindet sich ein Drop-Down-Menü aller im gleichnamigen Ordner gespeicherten Presets. Durch Auswahl wird das neue Preset automatisch geladen.


5. Statusleiste (unten)

Hier wird der Abspielstatus des aktiven Musikbuttons angezeigt (Grüne Buttons).


Anregungen, Bugs, Ideen, Geld und Liebesbriefe an: fischerp@gmx.de
