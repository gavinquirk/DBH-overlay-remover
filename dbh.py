import os
import subprocess
import tkinter as tk
from tkinter import filedialog
import json

root = tk.Tk()
root.withdraw()

# Overlay files
overlay_files = ['SteamOverlayVulkanLayer.json',
                 'SteamOverlayVulkanLayer64.json']

# Initialize variables
steam_path = ''
dbh_path = ''

print('Searching for previous settings...')

# Open settings.json and retreive data
try:
    with open('settings.json') as json_file:
        data = json.load(json_file)
        steam_path = data['steamPath']
        dbh_path = data['dbhPath']
except:
    print('Previous settings file not found')


# Check if steam and dbh file paths exist in json
# If not, ask user for file paths
if steam_path and dbh_path:
    print('File paths found')
else:
    print('Select Steam installation path')
    steam_path = filedialog.askdirectory()
    print('Select Detroit: Become Human installation path')
    dbh_path = filedialog.askopenfilename()
    # Write file paths to json
    data = {
        'steamPath': steam_path,
        'dbhPath': dbh_path
    }
    with open('settings.json', 'w') as outfile:
        json.dump(data, outfile)

# Loop over list of overlay files and remove them from Steam directory
for overlay_file in overlay_files:
    file_path = os.path.join(steam_path, overlay_file)
    print(file_path)

    if os.path.exists(file_path):
        os.remove(file_path)
        print(overlay_file + " removed")
    else:
        print(overlay_file + " not found")

# Launch game
print('Launching game')
subprocess.Popen(
    [dbh_path])
