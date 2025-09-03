# Team Wiki

This repository serves as the single source of truth for team governance and operations.

## Structure

- `gov/` - Governance information
  - `roles/` - Role definitions and responsibilities (hierarchical structure)
  - `policies/` - Team policies and procedures
  - `schedules/` - Cron jobs, meeting schedules, and other time-based information
  
- `ops/` - Operations information
  - `projects/` - Project documentation and status
  - `tasks/` - Task tracking and assignment
  - `research/` - Research notes and findings
  - `synthesis/` - Synthesized insights and recommendations

## Role Hierarchy

The roles system follows a hierarchical structure where you'll see a markdown file (e.g., `ai_developer.md`) and sometimes a folder of the same name containing child roles. This allows for nested role definitions and specializations.

Use the `set_role` command to set your current working role for commits:

```bash
set_role ai_developer    # Set role to AI Developer
set_role                 # Clear current role
set_role --list          # List available roles
```

When a role is set, git commits will use the role name as the author (e.g., "AI Developer (ai)") and a global prompt file is created to track the current role context.

## Contributing

All team members and AI agents should contribute to this knowledge base to maintain a complete picture of team activities and decisions.