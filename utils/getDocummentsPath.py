import os
from pathlib import Path

def getDocumentsPath():
    home = Path(os.environ['USERPROFILE'])
    documents_path = home / 'Documents'
    return str(documents_path)


