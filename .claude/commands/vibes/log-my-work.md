# Log My Work

Document work that has already been completed and is currently staged.

## Usage

```
/log-my-work <instructions>
```

**Parameters:**
- `instructions`: Additional instructions to be followed while completing the command.

## What it does

- **Confirms** that there are staged changes to document by checking `git status --porcelain --cached`.
- **Analyzes** the staged changes using `git diff --cached` to understand what work was completed.
- **Documents** the work done according to the instructions in `vibes/instructions/documenting-a-session.md`.
- **Stages** the vibes directory (`git add vibes`).

- Offers to execute `git commit -m <message>` following the format specified in `vibes/instructions/git-commit-message-format.md`.
- Prompts the user to use /clear and /startsession to continue development.


## Output

- Session documentation file with analysis of the staged work
- Updated worklog entry summarizing the completed tasks
- Updated CODEBASE.md if the staged changes affect project structure
