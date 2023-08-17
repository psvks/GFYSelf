import os
from pathlib import Path

def getDesktopPath():
    home = Path(os.environ['USERPROFILE'])
    documents_path = home / 'Desktop'
    return str(documents_path)


