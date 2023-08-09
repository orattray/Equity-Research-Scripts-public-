import subprocess
from pathlib import Path
import time

errorpresent = False

script_directory = Path(__file__).parent.absolute()
relative_pathYT = Path("Youtube Streams/youtubegamesscraperv2.py")
absolute_pathYT = script_directory / relative_pathYT
relative_pathSteam = Path("Steam/SteamDBScraperv1.py")
absolute_pathSteam = script_directory / relative_pathSteam

relative_pathCombine = Path("Combine all data.py")
absolute_pathCombine = script_directory / relative_pathCombine
relative_pathbackup = Path("BackupCSVs.py")
absolute_pathbackup = script_directory / relative_pathbackup


scripts = [ absolute_pathYT, absolute_pathSteam,  absolute_pathCombine, absolute_pathbackup]

for script in scripts:
    try:
        subprocess.run(['python', script], check=True)
        time.sleep(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}: {e}")
        print("Please refer to the error message above to see which script failed and check documentation on https://github.com/orattray/Equity-Research-Scripts-public- for help")
        errorpresent = True
        errorscript = script
        time.sleep(5)
        continue
else:
    print("All scripts completed successfully!")
    print("To view the graphs, run Generate all graphs.py")
    print("This window will autoclose in 30 seconds")

if errorpresent == True:
    print("There was an error with one of the scripts, please refer to the error message above to see which script failed and check documentation")
    print ("Last recorded error was with script: " + str(errorscript))
    input("Press enter to close this window")

time.sleep(30)