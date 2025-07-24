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

- `main.py` - Entry point, runs interactive GameLoop
- `server.py` - Long-running game server using named pipes
- `client.py` - Command-line client for non-blocking interaction
- `cli_game/` - Main package
  - `models.py` - Model layer (FileSystem, Shell, Host)
  - `controller.py` - Controller layer (CommandParser, GameLoop)
- `scratch/` - Development testing scripts
- `vibes/` - AI coding framework (not part of main codebase)

## Architecture

**MVC Pattern:**
- **Model**: FileSystem (data operations), Shell (environment state), Host (machine state)
- **View**: Command implementations (ls, pwd, etc.) - to be implemented
- **Controller**: prompt-toolkit interface + argparse command parsing

## Design principles

- Linux-like terminal experience with authentic command behavior
- Clean separation between filesystem operations and shell environment
- Command discovery mechanics for educational progression
- Single host implementation, designed for multiple hosts later

## Tooling

- Python 3.13+ with prompt-toolkit, mypy
- argparse for command parsing
- Git version control with vibes framework for AI-assisted development

## Current Status

Working command loop with `whoami` command. Client-server architecture enables AI interaction without hanging. Complete game state persistence implemented with JSON serialization and auto-save after every command. Ready for implementing filesystem operations and additional commands.