import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import time

script_directory = Path(__file__).parent.absolute()
relative_pathEAGraphs = Path("MultiGameStats/EAGameGrapher.py")
absolute_pathEAGraphs = script_directory / relative_pathEAGraphs
relative_pathYTGraphs = Path("Youtube Streams/YoutubeGrapher.py")
absolute_pathYTGraphs = script_directory / relative_pathYTGraphs
relative_pathSteamGraphs = Path("Steam/SteamDBGrapher.py")
absolute_pathSteamGraphs = script_directory / relative_pathSteamGraphs
relative_pathMultiGameGraphs = Path("MultiGameStats/MultiGameGrapher.py")
absolute_pathMultiGameGraphs = script_directory / relative_pathMultiGameGraphs
relative_pathFifaAGraphs = Path("MultiGameStats/FifaApexGrapher.py")
absolute_pathFifaAGraphs = script_directory / relative_pathFifaAGraphs
relative_pathUbisoftGraphs = Path("MultiGameStats/UbisoftGrapher.py")
absolute_pathUbisoftGraphs = script_directory / relative_pathUbisoftGraphs
relative_pathActivisionGraphs = Path("MultiGameStats/ActivisionGrapher.py")
absolute_pathActivisionGraphs = script_directory / relative_pathActivisionGraphs
relative_pathMicrosoftGraphs = Path("MultiGameStats/MicrosoftGrapher.py")
absolute_pathMicrosoftGraphs = script_directory / relative_pathMicrosoftGraphs
relative_pathGraphsfolder = Path("Graphs")
absolute_pathGraphsfolder = script_directory / relative_pathGraphsfolder

scripts = [absolute_pathEAGraphs, absolute_pathYTGraphs, absolute_pathSteamGraphs, absolute_pathMultiGameGraphs, absolute_pathFifaAGraphs, absolute_pathUbisoftGraphs, absolute_pathActivisionGraphs, absolute_pathMicrosoftGraphs]

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(subprocess.run, ['python', script], check=True) for script in scripts]

for future in futures:
    try:
        future.result()
    except subprocess.CalledProcessError as e:
        print(f"Error running {future}: {e}")
        break
else:
    print("Graphs generated successfully!")


time.sleep(5)


