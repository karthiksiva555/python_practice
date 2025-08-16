

class FileManager:
    def __init__(self):
        self.file_name = "my_file.txt"

    def read_file_manual_close(self):
        """Returns the contents of a file with open and close manually"""
        file = open(self.file_name)
        contents = file.read()
        file.close()
        return contents

    def read_file_context_manager(self , file_name = None):
        """Returns the content of the file with context manager

        Reads from a given file name if given, or self.file_name by default
        """
        if file_name is None:
            file_name = self.file_name

        with open(file_name) as file:
            contents = file.read()
            return contents

    def write_to_file(self, content: str):
        """Overwrites the existing contents of the file"""
        with open(self.file_name, mode="w") as file:
            file.write(content)

    def append_to_file(self, content: str):
        """Appends the input content to the existing contents of the file"""
        with open(self.file_name, mode="a") as file:
            file.write(content)

    @staticmethod
    def create_and_write_to_file(file_name, content):
        """Writes the given content into the file_name.

        Creates the file_name if it doesn't exist already.
        """
        with open(file_name, mode="a") as file:
            file.write(content)