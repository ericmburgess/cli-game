# Start Development Session

Gather relevant information before starting work.

## Usage

```
/startsession <goal>
```

**Parameters:**
- `goal`: Main objective for the session  

## What it does

- **WARNS** the user if there are any unstaged/uncommtted files by checking
   `git status`.
- **Reviews** the project structure and relevant prior work:
    - Reads `vibes/project/CODEBASE.md`.
    - Reads relevant session logs at `vibes/worklogs/`:
        - Any found in the git log that are closely related to the goal.
        - The three most recent.
    - Reads `vibes/project/TODO.md` and notes any items related to the current planned
      work.
- **BRIEFLY summarizes** this information for the user.
- **Defines requirements** by asking clarifying questions and proposing approaches
  until the user agrees. **NO CODE CHANGES** are proposed yet.

## Output

- An agreed-upon set of requirements for the new session's goal.
- A breakdown of self-contained steps to achieve the goal incrementally.
    - The first step is always to understand, at the code level, how to accomplish
      the most central functionality.
        - For example, if the goal is to add username/password authentication,
          the first step is to understand how to fetch a token using those
          credentials.
        - When possible, test this with a MINIMAL script written in the git-ignored
          `scratch/` folder. This script should have NO validation, error checking,
          usage info, etc. IT IS ONLY FOR YOU to test your approach.
    - Following steps will build toward achieving the full goal.
- Prompt the user to begin work on the first step with the /task command.

