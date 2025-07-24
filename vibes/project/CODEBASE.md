# INSTRUCTIONS FOR CLAUDE

- The purpose of this codebase summary is for YOU to orient YOURSELF at the
  start of each coding session.
- It is NOT intended to be comprehensive. It's just a high-level ROADMAP.
- KEEP THIS DOCUMENT VERY LEAN! You're going to be revising it at the end of
  most coding sessions. You do not want it changing every time you change a
  function signature or add a class method!

# CLI Game Project Codebase Summary
  
## Project Overview

CLI learning game that teaches real Linux skills through progressive command discovery. Uses MVC architecture with prompt-toolkit for terminal interface.

## Structure

- `cli_game/` - Main package
  - `models.py` - Model layer (FileSystem, Shell, Host) with full type annotations
  - `controller.py` - Controller layer (CommandParser, GameLoop) with persistent history
  - `game_state.py` - Game state persistence with JSON serialization (shell state only)
  - `constants.py` - Shared configuration (data directory paths, filesystem root)
  - `scripts/` - Entry point scripts
    - `main.py` - Interactive GameLoop
    - `server.py` - Long-running game server using named pipes
    - `client.py` - Command-line client for non-blocking interaction
- `lint` - Executable script for comprehensive code quality checks
- `.mypy.ini` - Strict type checking configuration
- `scratch/` - Development testing scripts
- `vibes/` - AI coding framework (not part of main codebase)

## Architecture

**MVC Pattern:**
- **Model**: FileSystem (real file operations under ~/.cli-game/fs/), Shell (environment state), Host (machine state)
- **View**: Command implementations (ls, pwd, etc.) - to be implemented
- **Controller**: prompt-toolkit interface + argparse command parsing

## Design principles

- Linux-like terminal experience with authentic command behavior
- Clean separation between filesystem operations and shell environment
- Command discovery mechanics for educational progression
- Single host implementation, designed for multiple hosts later

## Tooling

- Python 3.13 with prompt-toolkit for terminal interface
- Modern type system with strict mypy configuration and full type annotations
- Comprehensive linting: ruff (formatting/linting), isort (imports), mypy (types)
- Single `./lint` command for all code quality checks with auto-fixing
- argparse for command parsing with structured command system
- uv for dependency management with development dependency groups

## Current Status

Working command loop with `whoami` command and full type safety. Client-server architecture enables AI interaction without hanging. Complete game state persistence implemented with JSON serialization and auto-save after every command. Modern Python tooling with comprehensive code quality pipeline. Ready for implementing filesystem operations and additional commands.