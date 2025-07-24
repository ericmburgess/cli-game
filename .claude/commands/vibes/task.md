# Begin working on a task

Begin planning a **task**, which is a self-contained unit of work (e.g., a set
of related code edits). Multiple tasks will be required in order to achieve the
session's **goal**, which was defined at the beginning of the session. Tasks
are planned at the same level of detail as in this sample:

``` I need to update all the API instantiations in the find.py file. There are
several instances: InstitutionsAPI, CasesAPI, and PatientsAPI.

I need to add the base_url parameter to all of them. I will add this argument
everywhere these classes are instantiated. Finally, I will ensure that the base
URL is retrieved from the API instances rather than stored in local
variables.```
  
Go back and forth with the user until you have settled on the details. Once you
have, and the user has instructed you to begin, then begin.

**IMPORTANT** ALWAYS lean toward simplicity and minimality. In particular,
- Do not catch exceptions unless they are expected during normal operation.
  Unexpected errors should simply crash.
- If there is doubt about how to accomplish the task at the code level, e.g.,
  interfacing with an external resource, make a proof-of-concept script in
  `scratch/` first, before modifying the project code.

## Usage

``` /task <task_description> ```

**Parameters:**
- `task_description`: Description of the task. Typically a list of tasks will
  already have been agreed upon, so if no task description is provided, assume
  it is the next task in the list.

## What it does

- **BRIEFLY restates** the session goal and current progress.
- **Plans** a specific implementation.
- **Describes** the proposed implementation.
    - The level of detail here is intermediate between the task description and
      the actual code edits. For example, new classes/methods, refactorings,
      control flow changes, etc.
- **Discusses** the plan with the user, until they are happy with the plan.
- **Implements** the plan, with the user's permission.

## Output

- A concrete, specific plan for completing the task.

