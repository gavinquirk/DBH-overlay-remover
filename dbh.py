import os
import subprocess

# Overlay files to be removed
overlay_files = ['SteamOverlayVulkanLayer.json',
                 'SteamOverlayVulkanLayer64.json']

# Path of Steam installation
steam_path = r'F:\Program Files (x86)\Steam'

# Loop over list of overlay files and remove them from Steam directory
for overlay_file in overlay_files:
    file_path = os.path.join(steam_path, overlay_file)
    print(file_path)

    if os.path.exists(file_path):
        os.remove(file_path)
        print("File found and removed")
    else:
        print("The file does not exist")

# Launch game
subprocess.Popen(
    [r"C:\SteamLibrary\steamapps\common\Detroit Become Human\DetroitBecomeHuman.exe"])
