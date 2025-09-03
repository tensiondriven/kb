#!/usr/bin/env python3
"""
AI Agent Example Script

This script demonstrates how an AI agent can automatically contribute to the knowledge base.
"""

import os
import subprocess
from datetime import datetime


def create_project_report(project_name, status, summary):
    """Create a project report in the knowledge base."""
    # Create the project file path
    project_file = f"docs/ops/projects/{project_name.lower().replace(' ', '_')}.md"
    
    # Create the content
    content = f"""# {project_name}

**Status:** {status}

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary

{summary}

## Details

This project was automatically documented by an AI agent.
"""
    
    # Write the file
    os.makedirs(os.path.dirname(project_file), exist_ok=True)
    with open(project_file, 'w') as f:
        f.write(content)
    
    print(f"Created project report: {project_file}")
    return project_file


def commit_and_push_changes(file_path, commit_message):
    """Commit and push changes to the repository."""
    try:
        # Add the file
        subprocess.run(['git', 'add', file_path], check=True)
        
        # Commit the changes
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        
        # Push the changes
        subprocess.run(['git', 'push'], check=True)
        
        print("Changes successfully committed and pushed!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error committing and pushing changes: {e}")
        return False


def main():
    """Main function to demonstrate AI agent contribution."""
    print("AI Agent: Contributing to knowledge base...")
    
    # Create a sample project report
    project_file = create_project_report(
        "VegaViz Dashboard",
        "In Progress",
        "Developing a visualization dashboard using Vega-Lite for interactive data exploration."
    )
    
    # Commit and push the changes
    if commit_and_push_changes(project_file, "add: VegaViz project documentation"):
        print("Successfully contributed to the knowledge base!")
    else:
        print("Failed to contribute to the knowledge base.")


if __name__ == "__main__":
    main()