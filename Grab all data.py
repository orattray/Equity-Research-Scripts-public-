import subprocess
from pathlib import Path
import time

script_directory = Path(__file__).parent.absolute()
relative_pathEA = Path("MultiGameStats/MultiGameAPIEA.py")
absolute_pathEA = script_directory / relative_pathEA
relative_pathYT = Path("Youtube Streams/youtubegamesscraperv2.py")
absolute_pathYT = script_directory / relative_pathYT
relative_pathSteam = Path("Steam/SteamDBScraperv1.py")
absolute_pathSteam = script_directory / relative_pathSteam
relative_pathMultiGame = Path("MultiGameStats/MultiGameAPI.py")
absolute_pathMultiGame = script_directory / relative_pathMultiGame
relative_pathFifaA = Path("MultiGameStats/EAfifaApexSeperate.py")
absolute_pathFifaA = script_directory / relative_pathEA
relative_pathCombine = Path("Combine all data.py")
absolute_pathCombine = script_directory / relative_pathCombine


scripts = [absolute_pathEA, absolute_pathYT, absolute_pathSteam, absolute_pathMultiGame, absolute_pathFifaA ,absolute_pathCombine]

for script in scripts:
    try:
        subprocess.run(['python', script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}: {e}")
        break
else:
    print("All scripts completed successfully!")

time.sleep(30)