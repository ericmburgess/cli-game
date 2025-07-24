# Build Change History from Git

Analyze git history and generate initial `WORKLOG.md` for an existing project.

## Usage

```
/vibes:build-change-history
```

## What it does

- **Verifies** that you're in a project with vibes installed (`vibes/` directory exists)
- **Analyzes** the git commit history and **generates** an initial `vibes/worklogs/WORKLOG.md` following the directions in `vibes/instructions/build-worklog-from-git.md`
- **Asks clarifying questions** only when truly necessary for understanding major milestones

## Output

- A populated `WORKLOG.md` that provides historical context for the project
- Summary of development evolution to orient future vibes sessions

## Notes

This creates a historical overview from git commits, not individual session files. Refer to the detailed instructions in `vibes/instructions/build-worklog-from-git.md` for the complete process.