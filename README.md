# gref1

A command-line interface for Formula 1 data powered by the [FastF1](https://github.com/theOehrly/Fast-F1) Python library. Get race results, lap times, telemetry, tyre stints, weather data and more — straight from your terminal.

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv)

## Installation

```bash
git clone https://github.com/HypatiaG/gref1.git
cd gref1
uv sync
cd src
```

## Usage

```bash
uv run main.py [command] [options]
```

### Schedule

```bash
# Full race calendar for a season
uv run main.py calendar schedule --year 2024

# Next upcoming race
uv run main.py calendar next
```

### Results

```bash
# Race, qualifying or practice results
uv run main.py session race --year 2024 --round 5
uv run main.py session qualifying --year 2024 --round 5 --session Q
```

### Laps & Stints

```bash
# Tyre stints and compounds
uv run main.py race stint --year 2024 --round 5 --driver VER
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
    │   ├── schedule.py
    │   ├── results.py
    │   ├── race.py
    └── utils/
        └── loading.py
```

## Cache

FastF1 caches session data locally to avoid re-downloading. The cache is stored at `~/.cache/fastf1` by default. You can clear it manually if it gets too large.


