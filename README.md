# Advent of Code 2025

[Challenge](https://adventofcode.com/2025)

## Setup

This project uses `justfile` for task automation. Install `just` if you don't have it:

```bash
# macOS
brew install just

# Linux (Arch)
sudo pacman -S just

# Or from source
cargo install just
```

### Environment Setup

Set up your AOC session cookie:

```bash
export AOC_SESSION="your_session_id_here"
```

Find your session ID:
1. Visit https://adventofcode.com/2025
2. Open browser DevTools (F12)
3. Go to Application/Storage > Cookies
4. Copy the `session` cookie value
5. Export it in your shell: `export AOC_SESSION="<value>"`

For persistence, add to `~/.bashrc`:
```bash
export AOC_SESSION="your_session_id"
```

## Commands

All commands use `just` to run. The default `DAY` variable is today's date.

### `just md [day]`

**Setup a new day's directory and download inputs.**

Creates the directory structure for a puzzle day and downloads both the actual input and example input.

**What it does:**
1. Creates directory `d{day}/` with template files (`p1.py`, `justfile`)
2. Downloads the puzzle input to `d{day}/r.in` (real input)
3. Downloads the example input to `d{day}/t.in` (test input)

**Parameters:**
- `day` (optional, default: today's date)

**Examples:**
```bash
just md           # Setup today's puzzle
just md 5         # Setup day 5
just md 15        # Setup day 15
```

**Files created:**
- `d{day}/p1.py` - Template for part 1 solution
- `d{day}/p2.py` - Template for part 2 solution (create manually)
- `d{day}/justfile` - Local commands for testing solutions
- `d{day}/r.in` - Actual puzzle input
- `d{day}/t.in` - Example/test input

### `just desc [day]`

**Download and save the problem descriptions.**

Fetches the problem descriptions from Advent of Code and saves them as plain text files in the day's directory.

**What it does:**
1. Fetches the problem page from adventofcode.com using your session cookie
2. Extracts Part One description and saves to `d{day}/desc1.txt`
3. Extracts Part Two description and saves to `d{day}/desc2.txt` (if available)
4. Converts HTML to clean plain text

**Parameters:**
- `day` (optional, default: today's date)

**Examples:**
```bash
just desc         # Get descriptions for today
just desc 10      # Get descriptions for day 10
just desc 25      # Get descriptions for day 25
```

**Notes:**
- Part Two descriptions are only available after you complete Part One on AOC
- HTML is automatically cleaned and converted to plain text
- Files are saved in the day directory: `d{day}/desc1.txt` and `d{day}/desc2.txt`

## Project Structure

```
aoc2025/
├── d1/                 # Day 1 directory
│   ├── p1.py          # Part 1 solution
│   ├── p2.py          # Part 2 solution
│   ├── justfile       # Local test commands
│   ├── r.in           # Real puzzle input
│   ├── t.in           # Test/example input
│   ├── desc1.txt      # Part 1 description
│   └── desc2.txt      # Part 2 description
├── d2/                # Day 2 directory
├── ...
├── utils/             # Shared utilities
│   ├── make_day.py   # Creates day directories
│   └── fetch_desc.py # Fetches problem descriptions
├── justfile           # Main commands
├── pyproject.toml     # Python project config
└── README.md          # This file
```

## Local Day Commands

Each day's `justfile` has commands to run your solutions:

```bash
cd d5/
just t1           # Test part 1 with example input (t.in)
just r1           # Run part 1 with real input (r.in)
just t2           # Test part 2 with example input (t.in)
just r2           # Run part 2 with real input (r.in)
```

## Workflow Example

```bash
# Setup day 5
just md 5

# Get problem descriptions
just desc 5

# Write your solution in d5/p1.py

# Test with example input
cd d5 && just t1

# Run with real input
just r1

# Write part 2 solution in d5/p2.py
# Test and verify
just t2
just r2

# Go back to main directory
cd ..
```

## Dependencies

- Python 3.10+
- `uv` (Python package manager)
- `just` (command runner)
- `requests` library (installed automatically with `uv run --with requests`)

The project uses [advent-of-code-data](https://pypi.org/project/advent-of-code-data/) (`aocd`) for downloading puzzle inputs.

## Tips

- Use `just -l` to list all available commands
- Use `just --help` for help with just syntax
- Each day's folder is independent - you can jump between days easily
- The template `p1.py` uses `icecream` for debugging (import available via `from icecream import ic`)
- Puzzle inputs and examples are downloaded automatically - no manual copying needed
