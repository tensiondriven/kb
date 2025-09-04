# Instructions

Goal: Convert meetings into tactical and governance records, update existing records, delete etc.

1. List the contents of 'meetings'
2. Find a meeting that has not been processed (check for processed frontmatter)
3. Read the file, and slowly, process it by updating the governance records and tactical records. Note: Usually a meeting will be all governance or all tactical or sometimes combined. Meetings where we work ON the business (structure, roles, power, chain of command) is the realm of Governance, while projects, tasks, and so on are the realm of Tactical or Operations. (Tactical and Operations are synonymous)
4. Stick to templates and structures in `gov/` and `ops/`. Include references to the meeting line and file whenever possible to maintain a chain of custody.
5. Update relevant CHANGELOG.md files (`gov/CHANGELOG.md` or `ops/CHANGELOG.md`) with a summary of changes made, including meeting references.
6. After processing, add frontmatter to the meeting file:

   ```yaml
   ---
   processed_at: YYYY-MM-DD HH:MM:SS
   processed_by: [agent/human name]
   summary: [brief summary of what was processed]
   notes: [any relevant processing notes]
   changes:
     - path: gov/roles/example.md
       line: 15
       description: Updated role responsibilities based on meeting discussion
     - path: ops/projects/project_name.md
       line: 23
       description: Added new project requirements from meeting
   ---
   ```
