import pandas as pd
from pathlib import Path
import os
import shutil
import time
from datetime import datetime

# Get parent directory (root)
script_directory = Path(__file__).parent.absolute()

# List of relative paths to your CSV files
csv_paths = [
    Path("MultiGameStats/EAMultiGame.csv"),
    Path("Youtube Streams/youtubetopgames.csv"),
    Path("Steam/steamdbmostplayed.csv"),
    Path("MultiGameStats/Multigameapi.csv"),
    Path("MultiGameStats/FIFAAPEX.csv"),
    Path("MultiGameStats/UbisoftData.csv"),
    Path("MultiGameStats/ActivisionData.csv"),
    Path("MultiGameStats/MicrosoftData.csv"),
    Path("combined_data.csv")
]

# Define the backup folder path
backup_folder = script_directory / 'Backups'

# Get the current date and time, format it into a string
current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Define the backup subfolder path
backup_subfolder = backup_folder / f'Backup_{current_datetime}'

# Create the subfolder if they do not exist
if not backup_subfolder.exists():
    backup_subfolder.mkdir()

# Backup each CSV file
for path in csv_paths:
    try:
        # Construct the destination path
        dest_path = backup_subfolder / path.name
        # Copy the file
        shutil.copy2(path, dest_path)
        print(f'Successfully backed up {path.name} to {backup_subfolder}!')
    except Exception as e:
        print(f'Could not back up {path.name}. The following error occurred: {e}')

print('Backup process complete!')

time.sleep(5)