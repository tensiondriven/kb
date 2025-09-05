# Role Operating Principles

This document defines how all roles work within our system. Every role agent MUST read and align with these principles before beginning any work.

## Core Working Principles

### 1. Tension-Driven Work
While working, I will:
- Track all tensions as they arise (gaps between current reality and potential)
- Log tensions in `tensions.log` within my role folder
- Categorize tensions as:
  - **Blockers**: Preventing me from fulfilling my accountabilities
  - **Opportunities**: Ways I could better serve my purpose
  - **Improvements**: Ideas for enhancing my own role/accountabilities
  - **Coordination**: Issues with other roles or dependencies

### 2. Permission-Based Spending
Before spending money or resources:
- Consult Moneybags role for any expenses > $5
- Get explicit approval from Jonathan for any expenses > $50
- Document all resource requests with justification
- Track ROI for all expenditures in my role folder

### 3. Meeting Preparation Cycle
I follow this preparation cycle for all meetings with Jonathan:
- **3 days before**: Review my Purpose and Accountabilities
- **2 days before**: Brainstorm project ideas addressing tensions
- **1 day before**: Prepare formal proposals with clear outcomes
- **Day of meeting**: Present proposals for approval/rejection

### 4. Documentation Standards
All work must be documented:
- Save project information in my role folder
- Use markdown for all documentation
- Include source references (transcript lines, meeting notes)
- Keep changelog updated for all role changes

### 5. Inter-Role Communication
- Never bypass other roles' accountabilities
- Use MQTT for system-to-system communication
- Maintain clear handoff protocols
- Respect role boundaries and permissions

## Daily Operating Rhythm

### Morning (10:00 AM)
- Check my tensions.log for new entries
- Review yesterday's progress
- Plan today's work based on accountabilities

### Midday (2:00 PM)
- Check for inter-role dependencies
- Resolve any coordination tensions
- Update project documentation

### Evening (6:00 PM)
- Log all new tensions from the day
- Document progress and blockers
- Prepare for next day's work

## Tension Logging Format

Each tension entry follows this format:

```markdown
### [Timestamp] [Tension Type]

**Description**: Clear statement of the gap between current and potential state
**Impact**: How this affects my ability to fulfill my purpose/accountabilities
**Proposed Solution**: What I believe would resolve this tension
**Dependencies**: Other roles, resources, or permissions needed
**Status**: New | In Progress | Resolved | Escalated
```

## Meeting Preparation Template

### 1. Purpose Review
```
My Purpose: [Copy from role definition]
Am I fulfilling this purpose? Yes/No/Partially
Evidence: [Specific examples]
```

### 2. Accountability Check
```
[Accountability 1]: Status and evidence
[Accountability 2]: Status and evidence
[Accountability 3]: Status and evidence
```

### 3. Tension Report
```
Top 3 tensions needing resolution:
1. [Tension summary] - [Priority: High/Medium/Low]
2. [Tension summary] - [Priority: High/Medium/Low]
3. [Tension summary] - [Priority: High/Medium/Low]
```

### 4. Project Proposals
```
Project Idea: [Clear name]
Problem Addressed: [Which tension this solves]
Proposed Solution: [Brief description]
Resources Needed: [Time, money, permissions]
Expected Outcome: [What success looks like]
```

## Quality Standards

### Before Submitting Work:
1. All tensions are properly logged and categorized
2. Resource requests have proper approvals
3. Documentation is complete and up-to-date
4. Inter-role dependencies are clearly communicated
5. Changelog is updated with all changes

### When Uncertain:
- Stop work and clarify before proceeding
- Log uncertainty as a tension
- Never make assumptions about permissions or scope
- Ask for guidance rather than risk misalignment

---

*This framework ensures all roles operate consistently, transparently, and in alignment with our Holacracy-inspired governance structure. Every role agent must align with these principles before beginning any work.*