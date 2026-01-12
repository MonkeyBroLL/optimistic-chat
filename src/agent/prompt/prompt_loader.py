"""
Prompt loader module for the optimistic multilingual chat agent.

This module handles loading the prompt from the optimistic.md file.
"""

import os
from pathlib import Path
from enum import Enum


class PromptType(Enum):
    OPTIMISTIC = "optimistic"
    SUMMARY = "summary"


class PromptLoader:
    def __init__(self):
        self._optimistic_prompt = self._load_optimistic_prompt()
        self._summary_prompt = self._load_summary_prompt()
    
    def _load_prompt_from_md(self, filepath: str, prompt_start: str) -> str:
        """
        Load the prompt from a markdown file.
        
        Args:
            filepath (str): Path to the markdown file to load
            
        Returns:
            str: The content of the prompt loaded from the markdown file
        """
        md_file_path = Path(filepath)
        
        # Check if the file exists
        if not md_file_path.exists():
            raise FileNotFoundError(f"Markdown file not found at {md_file_path}")
        
        # Read the content of the markdown file
        with open(md_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Extract just the prompt part (after the header)
        lines = content.splitlines()
        prompt_lines = []
        
        # Find the line that contains the prompt (after the header)
        found_prompt_start = False
        for line in lines:
            if line.startswith(prompt_start):
                found_prompt_start = True
                continue
            if found_prompt_start:
                prompt_lines.append(line)
        
        # Join the prompt lines and return
        prompt_content = "\n".join(prompt_lines).strip()
        return prompt_content

    def _load_optimistic_prompt(self) -> str:
        """
        Load the optimistic multilingual prompt from the optimistic.md file.
        
        Returns:
            str: The content of the prompt loaded from optimistic.md
        """
        # Get the path to the optimistic.md file
        md_file_path = Path(__file__).parent / "optimistic.md"
        return self._load_prompt_from_md(str(md_file_path), "## Optimistic chat Prompt")

    def _load_summary_prompt(self) -> str:
        """
        Load the summary prompt from the chat_summary.md file.
        
        Returns:
            str: The content of the prompt loaded from chat_summary.md
        """
        # Get the path to the chat_summary.md file
        md_file_path = Path(__file__).parent / "chat_summary.md"
        return self._load_prompt_from_md(str(md_file_path), "# Chat Summary Prompt")
    
    def load_prompt(self, prompt_type: PromptType) -> str:
        """
        Load the prompt based on the given prompt type.
        
        Args:
            prompt_type (PromptType): The type of prompt to load
            
        Returns:
            str: The content of the requested prompt
        """
        if prompt_type == PromptType.OPTIMISTIC:
            return self._optimistic_prompt
        elif prompt_type == PromptType.SUMMARY:
            return self._summary_prompt
        else:
            raise ValueError(f"Unknown prompt type: {prompt_type}")
        
# if __name__ == "__main__":
#     # Example usage
#     prompt_loader = PromptLoader()
#     print("Optimistic Multilingual Prompt:")
#     print(prompt_loader.load_prompt(PromptType.OPTIMISTIC))
#     print("\nSummary Prompt:")
#     print(prompt_loader.load_prompt(PromptType.SUMMARY))