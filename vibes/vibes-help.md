# Vibe-coding workflow

The `vibes` workflow is organized around two concepts, **sessions** and
**tasks**, which are designed to keep Claude focused and allow you to direct
his work as you like.

- In a **session**, you and Claude work together to accomplish a significant unit of work, e.g., add a new feature, improve existing functionality, or fix a bug.

- Sessions are broken down into **tasks**, which are focused, self-contained units of work.

# Begin a session

A **session** corresponds to a focused set of changes that would typically correspond to a single issue ticket, which usually means a new feature, an improvement, a bug fix, etc.

It **also** corresponds to a single Claude session. This ensures that Claude stays on task and doesn't get confused by having too much stuff in his context. (See **Starting a new session** below).

Start a coding session with `/vibes:startsession <goal>`. The `goal` should be a high-level description of the work to be done. The body of a typical issue ticket is a good example. But you can also keep it brief and Claude will help you flesh it out into a well-defined goal.

Claude will then work with you to define the requirements for the session, and break the work down into a list of self-contained **tasks**. Once you are satisfied, you can begin the first task.

# Work through the tasks

Each **task** is a self-contained, focused unit of work which accomplishes part of the session goal. Begin working on the next task with the `/vibes:task` command. You may optionally add instructions, e.g., 

``` /vibes:task and remember to put the commands in their own modules ```

Claude will work with you to make a concrete plan for accomplishing the task. Once you're satisfied, tell him to start. Claude will work on the task, making necessary changes and getting your input when needed.

Claude will usually recognize correctly when the task is complete, but you can always pile more work on if you like. Once the task is completed to your satisfaction, use `/vibes:task` to move on to the next one.

# Complete the session

After completing some number of **tasks**, the **session goal** will have been achieved. Use `/vibes:endsession` to tell Claude to wrap up the task. He will take care of recording a log of the work and updating the codebase structure document, then he will offer to stage the changes and commit them with a suggested commit message.

# Starting a new session

As mentioned, keeping work confined to **sessions** helps Claude to stay focused. So use the `/clear` command before `/vibes:startsession`. Claude will remind you to do this after wrapping up.
