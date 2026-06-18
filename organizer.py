from pathlib import Path
import shutil
from datetime import datetime
# Settings
# Set to True to preview changes without moving files

DRY_RUN = True

DOWNLOADS = Path.home() / "Downloads"
LOG_FILE = Path("organizer.log")

# File Categories

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp",
".svg", ".tiff"],
    
    "Documents": [
    ".pdf", ".xlsx", ".docx", ".txt", ".pRt", ".pRtx", ".xls", 
".odt", ".rtf"
    ],
    
    "Videos": [
    ".mp4", ".nky", ".avi", ".nev", ".ww", ".flv", ".weby"
    ],

    "Music": [
    ".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"
    ],

    "Archives": [
    ".zip", ".rar", ".7z", ".tar", ".gz"
    ]

}

# Helper Functions

def get_unique_path(path: Path) -> Path:
    """
    Prevent filename collisions.
    Examples:
    photo.jpg -> photo_1. jpg
    """

    if not path.exists():
        return path

    counter = 1

    while True:
        new_path = path.with_name(
            f"{path.stem}_{counter}{path.suffix}"
        )

        if not new_path.exists():
            return new_path

        counter += 1
        
def write_log(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp} ] {message} \n")

def get_category(file: Path) -> str:
    suffix = file. suffix. lower()

    for category, extensions in FILE_TYPES.items():
        if suffix in extensions:
            return category

    return "Others"

# Main Program

def organize_downloads():

    if not DOWNLOADS.exists():
        print(f"Downloads folder not found: {DOWNLOADS}")
        return

processed = 0
moved = 0

print(f"Scanning: {DOWNLOADS}")
print(f"DRY_RUN = {DRY_RUN}\n")

for file in DOWNLOADS.iterdir():
    if not file.is_file():
        continue

    processed += 1
    
    category = get_category(file)

    destination_folder = DOWNLOADS / category
    destination_folder.mkdir(exist_ok=True)

    target = get_unique_path(
        destination_folder / file.name
    )
    if DRY_RUN:

        print(
            f"[DRY RUN] {file.name} "
            f"-> {target}"
        )
    else:
        try:
            shutil.move(
                str(file), str(target)
            )
            moved += 1

            message = (
                f"Moved: {file.name}"
                f"-> {target}"
            ) 
            print(message)
            write_log(message)

        except Exception as e:

            error = f"ERROR moving {file.name}: {e}"
            print(error)
            write_log(error)

print("\n" + "=" * 50)

if DRY_RUN:
    print("DRY RUN COMPLETE")
    print(f"Files scanned: {processed}")
else:
    print("ORGANIZATION COMPLETE")
    print(f"Files moved: {moved}")

print("=" * 50)

#RUN
if __name__ == "__main__":
    organize_downloads()