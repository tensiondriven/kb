# Command Examples Catalog

This file catalogs useful command examples for interacting with the knowledge base.

## File System Operations

### Open folder in file explorer
```
bash open ~/Code/kb
```

### List directory contents
```
bash ls -la ~/Code/kb
```

### Create directory structure
```
bash mkdir -p ~/Code/kb/docs/gov/{roles,responsibilities,policies,schedules}
```

### Move files
```
bash mv team-wiki ~/Code/kb
```

## Git Operations

### Initialize repository
```
bash cd ~/Code/kb && git init
```

### Add remote repository
```
bash cd ~/Code/kb && git remote add origin https://github.com/tensiondriven/kb.git
```

### Commit changes
```
bash cd ~/Code/kb && git add . && git commit -m "Initial commit"
```

### Push to remote
```
bash cd ~/Code/kb && git push -u origin main
```

### Change remote URL to SSH
```
bash cd ~/Code/kb && git remote set-url origin git@github.com:tensiondriven/kb.git
```

## GitHub CLI Operations

### Create repository
```
bash cd ~/Code/kb && gh repo create tensiondriven/kb --public --push --source .
```

### Check authentication status
```
bash gh auth status
```

## Python Script Execution

### Run AI agent example
```
bash cd ~/Code/kb && python3 ai_agent_example.py
```

## File Permissions

### Make script executable
```
bash cd ~/Code/kb && chmod +x ai_agent_example.py
```