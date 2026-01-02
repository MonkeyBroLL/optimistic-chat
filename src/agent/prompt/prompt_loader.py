"""
Prompt loader module for the optimistic multilingual chat agent.

This module handles loading the prompt from the optimistic.md file.
"""

import os
from pathlib import Path


def load_optimistic_prompt() -> str:
    """
    Load the optimistic multilingual prompt from the optimistic.md file.
    
    Returns:
        str: The content of the prompt loaded from optimistic.md
    """
    # Get the path to the optimistic.md file
    md_file_path = Path(__file__).parent / "optimistic.md"
    
    # Check if the file exists
    if not md_file_path.exists():
        raise FileNotFoundError(f"optimistic.md file not found at {md_file_path}")
    
    # Read the content of the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract just the prompt part (after the second header)
    lines = content.splitlines()
    prompt_lines = []
    
    # Find the line that contains the prompt (after the header)
    found_prompt_start = False
    for line in lines:
        if line.startswith("## Prompt"):
            found_prompt_start = True
            continue
        if found_prompt_start:
            prompt_lines.append(line)
    
    # Join the prompt lines and return
    prompt_content = "\n".join(prompt_lines).strip()
    return prompt_content


# Load the prompt content
OPTIMISTIC_MULTILINGUAL_PROMPT = load_optimistic_prompt()

def load_prompt() -> str:
    """
    Load the prompt from the optimistic.md file.
    
    Returns:
        str: The content of the prompt loaded from optimistic.md
    """
    return OPTIMISTIC_MULTILINGUAL_PROMPT


if __name__ == "__main__":
    # Example usage
    print("Optimistic Multilingual Prompt:")
    print(OPTIMISTIC_MULTILINGUAL_PROMPT)