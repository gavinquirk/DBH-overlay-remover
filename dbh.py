import os

# Overlay files to be removed
overlay_files = [r'\SteamOverlayVulkanLayer.json',
                 r'\SteamOverlayVulkanLayer64.json']

# Path of Steam installation
steam_path = r'F:\Program Files (x86)\Steam'

# Loop over list of overlay files and remove them from Steam directory
for overlay_file in overlay_files:
    file_path = steam_path + overlay_file

    if os.path.exists(file_path):
        os.remove(file_path)
        print("File found and removed")
    else:
        print("The file does not exist")
