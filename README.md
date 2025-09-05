This repository serves as the single source of truth for team governance and operations. This includes project lists, status, and support materials. It also includes a wiki

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

- `wiki/` - Shared Knowledge
,.
## Role Hierarchy

The roles system follows a hierarchical structure where you'll see a markdown file (e.g., `ai_developer.md`) and sometimes a folder of the same name containing support documetns. 

Use the `set_role` command to set your current working role for commits:

```bash
set_role ai_developer    # Set role to AI Developer
set_role                 # Clear current role
set_role --list          # List available roles
```

When a role is set, git commits will use the role name as the author (e.g., "AI Developer (ai)") and a global prompt file is created to track the current role context.

## Core Governance

All agents performing work in any role **must** adhere to the [Governance Constitution](gov/governance.md). This document establishes foundational operating principles, tension-driven workflows, and permission-based decision making for our entire system.

**Non-negotiable requirements:**
- Every role tracks tensions in their role folder
- All money >$5 requires approval from an authorized role
- All new projects need an approval request and approval unless requested
- No markdown file is valid unless linked from this root README
- Agents scan this file first, then follow linked documentation