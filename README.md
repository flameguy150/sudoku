# Sudoku

Made with pygame

Second implementation

* Game Icon
* Animations and Title Screen
* Settings
* Saves game progress and can start a new game
* Winner Screen

![title](/assets/img/title.png)
![game](/assets/img/game.png)
![settings](/assets/img/settings.png)

## Controls

f: screen info

s: settings

m: mute music

number pad: change number to input

## Project Structure

```
sudoku
|-- assets
|   |-- art
|   |   |-- flower
|   |   |   |-- ff1_64.png
|   |   |   |-- ff2_64.png
|   |   |   |-- ff3_64.png
|   |   |   |-- flower_frame1.png
|   |   |   |-- flower_frame2.png
|   |   |   `-- flower_frame3.png
|   |   `-- icon
|   |       |-- icon_128.png
|   |       |-- icon_256.png
|   |       |-- icon_32.png
|   |       `-- icon_64.png
|   |-- fonts
|   |   |-- FSEX300.TTF
|   |   `-- JetBrainsMonoNerdFont-ExtraLightItalic.ttf
|   |-- img
|   |   |-- game.png
|   |   |-- settings.png
|   |   `-- title.png
|   `-- sounds
|       `-- flowers.mp3
|-- src
|   `-- neo
|       |-- config
|       |   |-- __init__.py
|       |   |-- constants.py
|       |   `-- globals.py
|       |-- core
|       |   |-- __init__.py
|       |   |-- board.py
|       |   |-- cell.py
|       |   |-- controls.py
|       |   `-- grid.py
|       |-- ui
|       |   |-- flower.py
|       |   `-- gameState.py
|       `-- utils
|           |-- __init__.py
|           `-- utilities.py
|-- .gitignore
|-- devlog.txt
|-- main.py
|-- project_struct.py
|-- README.md
|-- requirements.txt
`-- todo.txt

```

## How to run

1. Clone the repository

```bash
git clone https://github.com/flameguy150/sudoku.git
cd sudoku
```

2. Create and activate a virtual environment

```bash
py -m venv .venv

(Windows)
.\.venv\Scripts\Activate.ps1

(Mac/Linux)
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt

```

4. Run file

```bash
windows: py main.py
mac/linux: python3 main.py
```
