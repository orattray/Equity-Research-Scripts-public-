import pandas as pd
from pathlib import Path
import os
import time

script_directory = Path(__file__).parent.parent.absolute()
csv_paths = [
    Path("MultiGameStats/EAMultiGame.csv"),
    Path("Youtube Streams/youtubetopgames.csv"),
    Path("Steam/steamdbmostplayed.csv"),
    Path("MultiGameStats/Multigameapi.csv"),
    Path("MultiGameStats/FIFAAPEX.csv"),
    Path("MultiGameStats/UbisoftData.csv"),
    Path("MultiGameStats/ActivisionData.csv"),
    Path("MultiGameStats/MicrosoftData.csv"),
]

absolute_csv_paths = [script_directory / path for path in csv_paths]

user_confirmation = input("Are you sure you want to clear the contents of all CSV files? (yes/no): ")

if user_confirmation.lower() == 'yes':
    for path in absolute_csv_paths:
        try:
            # Open the file in write mode (w) and immediately close it, which will effectively clear it
            with open(path, 'w') as file:
                pass
            print(f'Successfully cleared the contents of {path.name}!')
        except Exception as e:
            print(f'Could not clear the contents of {path.name}. The following error occurred: {e}')
else:
    print("Operation cancelled by the user.")

time.sleep(10)