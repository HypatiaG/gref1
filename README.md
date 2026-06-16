# f1-cli

A command-line interface for Formula 1 data powered by the [FastF1](https://github.com/theOehrly/Fast-F1) Python library. Get race results, lap times, telemetry, tyre stints, weather data and more — straight from your terminal.

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv)

## Installation

```bash
git clone https://github.com/yourname/f1-cli
cd f1-cli
uv sync
```

To install globally so you can run `f1` from anywhere:

```bash
uv tool install .
```

## Usage

```bash
f1 [command] [options]
```

### Schedule

```bash
# Full race calendar for a season
f1 schedule --year 2024

# Next upcoming race
f1 next
```

### Results

```bash
# Race, qualifying or practice results
f1 results --year 2024 --round 5 --session R
f1 results --year 2024 --round 5 --session Q
f1 results --year 2024 --round 5 --session FP1

# Fastest laps in a session
f1 fastest --year 2024 --round 5 --session R
```

### Laps & Stints

```bash
# All laps for a driver
f1 laps --year 2024 --round 5 --driver VER

# Tyre stints and compounds
f1 stints --year 2024 --round 5 --driver VER
```

### Telemetry

```bash
# Speed, throttle, brake and gear data for a lap
f1 telemetry --year 2024 --round 5 --driver VER --lap 10

# Compare two drivers side by side
f1 compare --year 2024 --round 5 --drivers VER,HAM --lap fastest
```

### Weather

```bash
# Track and air temperature, rainfall during a session
f1 weather --year 2024 --round 5 --session R
```

### Drivers & Teams

```bash
# All drivers in a season
f1 drivers --year 2024

# All constructors in a season
f1 teams --year 2024
```

## Session types

| Flag | Session        |
|------|----------------|
| `R`  | Race           |
| `Q`  | Qualifying     |
| `S`  | Sprint         |
| `FP1` | Practice 1   |
| `FP2` | Practice 2   |
| `FP3` | Practice 3   |

## Project structure

```
f1-cli/
├── pyproject.toml
├── README.md
└── f1/
    ├── __init__.py
    ├── main.py
    ├── commands/
    │   ├── schedule.py
    │   ├── results.py
    │   ├── laps.py
    │   ├── telemetry.py
    │   └── weather.py
    └── utils/
        ├── cache.py
        └── display.py
```

## Cache

FastF1 caches session data locally to avoid re-downloading. The cache is stored at `~/.cache/fastf1` by default. You can clear it manually if it gets too large.


