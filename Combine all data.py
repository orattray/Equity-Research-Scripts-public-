import pandas as pd
import time
from pathlib import Path

script_directory = Path(__file__).parent.absolute()
relative_pathEAdata = Path("MultiGameStats/EAMultiGame.csv")
absolute_pathEAdata = script_directory / relative_pathEAdata
relative_pathYTdata = Path("Youtube Streams/youtubetopgames.csv")
absolute_pathYTdata = script_directory / relative_pathYTdata
relative_pathSteamdata = Path("Steam/Steamdbmostplayed.csv")
absolute_pathSteamdata = script_directory / relative_pathSteamdata
relative_pathMultiGamedata = Path("MultiGameStats/Multigameapi.csv")
absolute_pathMultiGamedata = script_directory / relative_pathMultiGamedata
relative_pathnewdata = Path("combined_data.csv")
absolute_pathnewdata = script_directory / relative_pathnewdata

# Define the file paths for the four separate CSV files
csv_paths = [
    absolute_pathEAdata,
    absolute_pathYTdata,
    absolute_pathMultiGamedata
]

# Create an empty list to store the dataframes
dfs = []

# Loop through the CSV files and read them into dataframes
# Note that the encoding is specified to ensure that the data is read in correctly
# The encoding may need to be changed depending on the data
df = pd.read_csv(absolute_pathSteamdata, encoding='windows-1252')
dfs.append(df)

for path in csv_paths:
    df = pd.read_csv(path, encoding='utf-8')
    dfs.append(df)

# Merge the dataframes into one large dataframe, with each CSV file's data in a separate column
combined_df = pd.concat(dfs, axis=1, keys=['Steam', 'EA', 'YT', 'MultiGame'])

try:
    # Write the combined dataframe to a new CSV file
    combined_df.to_csv(absolute_pathnewdata, index=False)
    print("Data combined successfully!")
except PermissionError:
    print("Permission denied. Please make sure the csv isn't open and try again.")

time.sleep(10)