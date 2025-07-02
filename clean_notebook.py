#!/usr/bin/env python3
"""
Script to clean Jupyter notebooks for GitHub compatibility
Removes widget metadata that causes rendering errors
"""

import json
import sys
import os

def clean_notebook(notebook_path):
    """Clean a Jupyter notebook by removing problematic widget metadata"""
    
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Remove widget metadata from the notebook level
    if 'metadata' in notebook and 'widgets' in notebook['metadata']:
        print(f"Removing widget metadata from notebook: {notebook_path}")
        del notebook['metadata']['widgets']
    
    # Clean each cell
    for cell in notebook.get('cells', []):
        # Remove widget metadata from cell level
        if 'metadata' in cell and 'widgets' in cell['metadata']:
            del cell['metadata']['widgets']
        
        # Remove widget state from outputs
        if 'outputs' in cell:
            for output in cell['outputs']:
                if 'metadata' in output and 'widgets' in output['metadata']:
                    del output['metadata']['widgets']
    
    # Create backup
    backup_path = notebook_path + '.backup'
    with open(backup_path, 'w', encoding='utf-8') as f:
        with open(notebook_path, 'r', encoding='utf-8') as original:
            f.write(original.read())
    print(f"Created backup: {backup_path}")
    
    # Write cleaned notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"Cleaned notebook saved: {notebook_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_notebook.py <notebook_path>")
        sys.exit(1)
    
    notebook_path = sys.argv[1]
    
    if not os.path.exists(notebook_path):
        print(f"Error: File not found: {notebook_path}")
        sys.exit(1)
    
    clean_notebook(notebook_path)