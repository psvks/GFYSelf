import subprocess


def getOwnerShip(path):
    command = ['icacls', path]  # Construct the command
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        return output
    except subprocess.CalledProcessError as e:
        return str(e)