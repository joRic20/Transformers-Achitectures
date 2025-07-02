#!/usr/bin/env python3
"""
Carefully clean only widget metadata without removing outputs
"""
import json
import sys

def clean_widgets_only(notebook_path):
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Remove ONLY widget metadata, keeping all outputs
    if 'metadata' in notebook and 'widgets' in notebook['metadata']:
        print("Removing notebook-level widget metadata")
        del notebook['metadata']['widgets']
    
    # Clean cells but preserve outputs
    for i, cell in enumerate(notebook.get('cells', [])):
        # Remove widget metadata from cell level
        if 'metadata' in cell and 'widgets' in cell['metadata']:
            print(f"Removing widget metadata from cell {i}")
            del cell['metadata']['widgets']
    
    # Save the cleaned notebook
    output_path = notebook_path.replace('.ipynb', '_cleaned.ipynb')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"Cleaned notebook saved as: {output_path}")
    print(f"Original notebook unchanged: {notebook_path}")
    print("\nTo use the cleaned version:")
    print(f"mv {output_path} {notebook_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_widgets_only.py <notebook_path>")
        sys.exit(1)
    
    clean_widgets_only(sys.argv[1])