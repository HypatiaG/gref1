# gref1

A command-line interface for Formula 1 data powered by the [FastF1](https://github.com/theOehrly/Fast-F1) Python library. Get race results, lap times, tyre stints and more straight from your terminal.

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv)

## Installation

```bash
git clone https://github.com/HypatiaG/gref1.git
cd gref1
uv sync
```

## Usage

```bash
uv run src/main.py --help
```

## Quick Start

```bash
uv sync

# View available commands
uv run src/main.py --help

# Show the 2025 calendar
uv run src/main.py calendar schedule -y 2025

# Show race results
uv run src/main.py session race -y 2025 -r 7
```

### Schedule

```bash
# Full race calendar for a season
uv run src/main.py calendar schedule --year 2024

# Next upcoming race
uv run src/main.py calendar next
```

### Results

```bash
# Race, qualifying or practice results
uv run src/main.py session race --year 2024 --round 5
uv run src/main.py session qualifying --year 2024 --round 5
```

### Laps & Stints

```bash
# Tyre stints and compounds
uv run src/main.py race stint --year 2024 --round 5 --driver VER
```

## Session types

| Flag | Session        |
|------|----------------|
| `R`  | Race           |
| `Q`  | Qualifying     |


## Project structure

```
gref1/
├── pyproject.toml
├── README.md
└── src/
    ├── main.py
    ├── commands/
    │   ├── calendar.py
    │   ├── race.py
    │   ├── session.py
    └── utils/
        └── loading.py
```

## Cache

FastF1 caches session data locally to avoid re-downloading. The cache is stored at `~/.cache/fastf1` by default. You can clear it manually if it gets too large.


