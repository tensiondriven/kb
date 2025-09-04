# Directory Structure

## Overview

This repository uses a selective publishing model:

### Working Directories (Root Level)

- `gov/` - Active governance files (roles, policies, responsibilities, schedules)
- `ops/` - Active operations files (projects, tasks, research, synthesis)
- `meetings/` - Meeting transcripts to be processed

These are the **working directories** where all content is actively managed and updated.

### Published Site (`published/`)

- `published/gov/` - Symlink to `gov/` (published governance)
- `published/ops/` - Symlink to `ops/` (published operations)
- `published/index.md` - Symlink to `docs/index.md`

The `published/` directory contains **symlinks** to content you want public on the **GitHub Pages site** at <https://tensiondriven.github.io/kb/> (built with MkDocs).

## Workflow

1. **Work** in root `gov/` and `ops/` directories
2. **Symlink** desired content into `published/` for publication
3. **Agents** reference root paths (`gov/`, `ops/`) in processing
4. **MkDocs** builds site from `published/` content (`docs_dir: published`)

## Key Files

- `mkdocs.yml` - Site configuration (uses `docs_dir: published`)
- `AGENTS.md` - Processing instructions (uses root paths)
- `published/` - Symlinked content for public site
