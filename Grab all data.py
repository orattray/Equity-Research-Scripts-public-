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
absolute_pathFifaA = script_directory / relative_pathFifaA
relative_pathUbisoft = Path("MultiGameStats/Ubisoft.py")
absolute_pathUbisoft = script_directory / relative_pathUbisoft
relativepath_Activision = Path("MultiGameStats/Activision.py")
absolute_pathActivision = script_directory / relativepath_Activision
relative_pathMicrosoft = Path("MultiGameStats/Microsoft.py")
absolute_pathMicrosoft = script_directory / relative_pathMicrosoft
relative_pathCombine = Path("Combine all data.py")
absolute_pathCombine = script_directory / relative_pathCombine


scripts = [absolute_pathEA, absolute_pathYT, absolute_pathSteam, absolute_pathMultiGame, absolute_pathFifaA , absolute_pathUbisoft, absolute_pathActivision, absolute_pathMicrosoft, absolute_pathCombine]

for script in scripts:
    try:
        subprocess.run(['python', script], check=True)
        time.sleep(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}: {e}")
        print("Please refer to the error message above to see which script failed and check documentation on https://github.com/orattray/Equity-Research-Scripts-public- for help")
        time.sleep(30)
        break
else:
    print("All scripts completed successfully!")
    print("To view the graphs, run Generate all graphs.py")
    print("This window will autoclose in 30 seconds")

time.sleep(30)