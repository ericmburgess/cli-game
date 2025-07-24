# End Development Session

Document a completed work session and prepare for the next.

## Usage

```
/endsession <instructions>
```

**Parameters:**
- `instructions`: Additional instructions to be followed while completing the command.

## What it does

- Documents the work done according to the instructions in
  `vibes/instructions/documenting-a-session.md`.
- Offers to execute `git add .`, telling the user they may hit Esc and stage the files themselves if they prefer.
- Offers to execute `git commit -m <message>` following the format specified in `vibes/instructions/git-commit-message-format.md`.
- Prompts the user to use /clear and /startsession to continue development.

