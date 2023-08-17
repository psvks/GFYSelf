import subprocess

# Function to set ownership of a folder
def SetOwnership(path):
    command = ['takeown', '/F', path]
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        return str(e)

