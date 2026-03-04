import os
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent

INPUTS_DIR = PROJECT_ROOT / 'inputs'
OUTPUTS_DIR = PROJECT_ROOT / 'outputs'

def read_text_file(filename: str) -> str:
    """
    Reads a text file from the inputs folder.
    
    Args:
        filename (str): The name or relative path of the file to read.
        
    Returns:
        str: The contents of the text file.
    """
    file_path = INPUTS_DIR / filename
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_text_file(filename: str, content: str) -> None:
    """
    Writes content to a text file in the outputs folder.
    
    Args:
        filename (str): The name or relative path of the file to write.
        content (str): The text content to write to the file.
    """
    file_path = OUTPUTS_DIR / filename
    # Ensure the directory exists in case of nested paths
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def print_inputs_menu() -> list[str]:
    """
    Prints a menu listing all files in the inputs folder.
    
    Returns:
        list[str]: A list of filenames available in the inputs folder.
    """
    if not INPUTS_DIR.exists():
        print(f"Inputs directory '{INPUTS_DIR.name}' not found.")
        return []

    files = [f.name for f in INPUTS_DIR.iterdir() if f.is_file()]
    
    if not files:
        print(f"No files found in the '{INPUTS_DIR.name}' folder.")
        return []
        
    print("--- Select a option ---")
    for i, filename in enumerate(files, 1):
        print(f"{i}. {filename}")
    print("0. Exit")
    print("-" * 23)
    
    return files
