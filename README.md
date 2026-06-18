# Smart Downloads Folder Organizer

A Python automation tool that automatically organizes files in the Downloads folder into categorized directories.

## Features
- Organizes files by type
- Supports Images, Documents, Videos, Music, and Archives
- Prevents filename collisions
- Generates activity logs
- Dry Run mode for safe testing

## Technologies Used
- Python
- pathlib
- shutil
- datetime

## How It Works
The script scans the Downloads folder and moves files into folders based on their file extension.

Example:
Downloads/
├── Images/
├── Documents/
├── Videos/
├── Music/
└── Archives/

## Usage
Run:
```bash
python organizer.py
```

To actually move files, set:
```python
DRY_RUN = False
```
# Author
Midhat Fatima
