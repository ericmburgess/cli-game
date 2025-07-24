# CLI Game: Discovery-Based Command Line Learning

## Core Concept
A CLI game that teaches real Linux command line skills through progressive discovery. Players start with only `help` and `ls`, gradually unlocking more powerful command features that evolve toward real Linux implementations.

## Key Mechanics

### Progressive Command Evolution
- Commands start simple and gain flags/options through discovery
- Evolution path mirrors real Linux: `cat` → `cat -n` → `cat -A`, etc.
- Early commands have friendly error messages, gradually becoming more terse/realistic
- Final goal: players gain genuine shell fluency (tens of hours of content)

### Discovery-Driven Progression
- Hidden files revealed through `-a` flag discovery incentivizes re-exploration
- Files that hint at needed commands: `type-cat-now.txt`, `count-these-lines.txt`
- Meta-discovery: `man` pages populate as features are found
- Achievement system for discovering new flags/capabilities

### Learning Scaffolding
- Linux-ish but not identical (to avoid overwhelming beginners)
- Commands may start with descriptive names: `show-file` → `cat`
- Safe environment: `rm` moves to `.trash/` instead of deleting
- Breadcrumb files that require specific command combinations

## Advanced Concepts

### Command Composition
- Pipes (`|`) and redirection (`>`) introduced gradually
- Files designed to need multi-step processing
- Progress from single commands → composition → scripting basics
- Environment variables and parameter passing (`$1`, `$2`)

### Narrative Possibilities
- Abandoned system exploration / digital archaeology
- System debugging scenario
- Previous "users" leave story fragments in files
- System itself as character (personal comments in configs)

## Technical Considerations
- Tab completion that improves with progress
- `history` command shows player journey and hints
- Potential "graduation" to real shell sandbox
- Bridge to real-world: help text mentions Linux compatibility

## Target Experience
Tens of hours of content, scalable based on player drive and existing knowledge. Goal: transform GUI users into confident command line users through gameplay.