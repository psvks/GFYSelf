import os

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

