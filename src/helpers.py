import os
from pathlib import Path

def ensure_directory_exists(directory_path):
    """Ensure the directory exists, creating it if necessary."""
    Path(directory_path).mkdir(parents=True, exist_ok=True)

# def create_file(file_path, content=""):
#     """Create a file with the given content, ensuring its directory exists."""
#     ensure_directory_exists(os.path.dirname(file_path))
#     with open(file_path, 'w') as file:
#         file.write(content)
