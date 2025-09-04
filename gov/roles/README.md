# Roles

Roles at Indigo are different from other places. A role is a collection of responsibilities that helps to build "roleationships" (role-relationships).

Take a look at the ai-developer.md for an example.

## Role Structure

To be valid, a role must have:

- A name (text, short) - should almost NEVER be a traditional role name, be playful/inspiring (derived from H1 title "Role: X")
- A short name (text, short) - may be the same as the role name, should be casual/colloquial
- A Purpose (text, sentence) - should be inspiring, less formal, make people pause, diverse statements
- At least one Responsibility (list of text sentences)
- H1 title should use "Role:" prefix format, e.g. "# Role: IT Infrastructure"

**Important**: The canonical role name is derived from the H1 title (everything after "Role: "). Filenames must be kept in sync with role names using kebab-case (e.g., "Role: IT Infrastructure" → `it-infrastructure.md`). When renaming roles, always update both the H1 title and filename, and check for any references that need updating. (AI)

We are evolving the structure of roles, so any information that is specifically mentioned which does not fit should go in a section called "Additional Info". Over time we will update our lightweight role "schema" to support common features. The "Additional Info" section should be thought of as a bucket for overflow when our role abstraction leaks, when we can't capture all the details in other fields. It should contain ADDITIONAL details mentioned or discussed which are NOT included in the other fields. (AI)

## Creating Roles

If you are responsible for updating roles, you must hold it. Add or update specific context and never make anything up. My view: comment here in our line brief, fill in, or ensure what the user mentioned is your main purpose in this interview is to extract information and promotion. Write it.

### AI Content Rule

If you don't find a purpose or a single responsibility, or if you EVER need to fill in or make something up, you MUST append (AI) to the end of the line or paragraph. If it's several paragraphs, each one must end with (AI), e.g. "The quick brown fox got lazy. (AI)". (AI)

### Grammar and Spelling

You are welcome and encouraged to fix grammar and spelling issues in all role documentation. (AI)

## Purpose

"Purpose" means something specific; it is a statement about the world, which if true, would mean this role would not need to exist. It is usually unattainable, aspirational, and the statement itself is inspirational. Purpose statements should be diverse, inspiring, and less formal. They don't need to follow the "A world where..." pattern and should make people pause. Role names should similarly be playful and inspiring, almost NEVER traditional role names. (AI)

## Responsibility

"Responsibility" means something specific; it is identical to the idea of "Accountabilities" in Holacracy. That is, each Responsibility must begin with an "-ing" word, a gerund verb.  So, "Make sure the mail gets checked evcery day" is invalid while "Checking the mail daily" is valid.

A well-written responsibility will:

- MUST Start with -ing word
- MAY Mention any roles that depend on it or it depends on, and how (e.g. Providing Accounting with up to date reciepts by end of month) is good
- MAY Includes heuristic for how much / how often, e.g. "upon request", "daily", "according to client schedule"
- MAY include "Additional Info" section
- MAY include "Processing Notes" section, to capture confusion, questions, ambiguity, and suggested opportunities for improvement during role creation
- MUST include a Changelog section at the end

There are other criteria, which will be updated here.

### Questions

If you are processing a role and are less than 90% confident in the conversion, stop the process to ask for clarification.

### Reference Format

For referencing meeting sources, use standard markdown links like `[ref](meetings/2025-09-03-initial-setup.md:16-20)`. (AI)


