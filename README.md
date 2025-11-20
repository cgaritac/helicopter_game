# Helicopter Game

Arcade-style survival game built with Python and Pygame. Pilot a helicopter through procedurally generated block walls, survive as long as possible, and push your score higher as the difficulty ramps up.

## Gameplay

- Use the arrow up key to gain altitude; releasing the key makes the helicopter descend.
- Procedurally generated obstacles create upper and lower barriers with a gap you must traverse.
- Speed increases and the safe gap narrows as your score climbs, keeping the challenge fresh.

## Features

- Lightweight Python/Pygame implementation.
- Simple but responsive controls for quick pick-up-and-play sessions.
- Dynamic difficulty curve that reacts to player performance.
- Score feedback rendered directly on the play surface.

## Requirements

- Python 3.8+
- [Pygame](https://www.pygame.org/news) 2.x

## Installation

```bash
git clone https://github.com/<tu_usuario>/helicopter_game.git
cd helicopter_game
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt  # or: pip install pygame
```

If you do not maintain a `requirements.txt`, install Pygame directly:

```bash
pip install pygame
```

## Running the Game

```bash
python game.py
```

The helicopter sprite is loaded from `Docs/Helicopter.png`, so keep that asset path intact when moving files.

## Project Structure

- `game.py` – main game loop, rendering, input handling, collision logic.
- `Docs/Helicopter.png` – helicopter sprite.
- `Docs/` – supplementary resources such as tutorial experiments.

## Roadmap Ideas

- Add a start menu, pause state, and in-game sound effects.
- Record high scores to disk for replay value.
- Offer multiple control schemes (mouse/spacebar) and difficulty presets.
- Replace placeholder graphics with themed art packs.