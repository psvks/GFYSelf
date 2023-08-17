import os


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
