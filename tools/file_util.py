import os
import shutil


class FileUtil:
    def __init__(self):
        pass

    @staticmethod
    def read_lines(file_path):
        """
        Read the content of the file line by line
        :param file_path: The path of the target file to read
        :return: A list of the read content
        """
        with open(file_path, "r+", encoding='utf-8') as file:
            return file.readlines()

    @staticmethod
    def read(file_path):
        """
        Read the content of the file
        :param file_path: The path of the target file to read
        :return: The read content
        """
        with open(file_path, "r+", encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def write_lines(file_path, lines):
        """
        Write lines to a file
        :param file_path: The path of the target file to write
        :param lines: A list of data to write to the file;
        :return: None
        """
        with open(file_path, "w+", encoding='utf-8') as f:
            f.writelines(f"{line}\n" for line in lines)

    @staticmethod
    def write_line(file_path, line):
        """
        Write a line to a file
        :param line: A line of data to write to the file; this method adds a newline at the end
        :param file_path: The path of the target file to write
        :return: None
        """
        with open(file_path, "a", encoding='utf-8') as f:
            f.write(f"{line}\n")

    @staticmethod
    def clear(file_path):
        """
        Clear the content of file
        :param file_path: The file to clear content
        :return: None
        """
        with open(file_path, "w", encoding='utf-8'):
            pass

    @staticmethod
    def write(file_path, data):
        """
        Write data to a file
        :param data: The data to write to the file; this method adds a newline at the end
        :param file_path: The path of the target file to write
        :return: None
        """
        with open(file_path, "a", encoding='utf-8') as f:
            f.write(f"{data}\n")

    @staticmethod
    def makedirs_if_not_exist(*paths):
        """
        Create directories if they do not exist
        :param paths: The paths to check and create directories, can pass multiple
        :return: None
        """
        for path in paths:
            if not os.path.exists(path):
                print(f"{path} not exist, make it.")
                os.makedirs(path)

    @staticmethod
    def create_file_if_not_exist(file_path):
        """
        Create file when file_path is not exist
        :param file_path: The file_path that want to create
        :return: None
        """
        with open(file_path, "a"):
            pass

    @staticmethod
    def remove_if_exist(*paths):
        """
        Remove directories or files
        :param paths: The paths of the directories or files to remove, can pass multiple
        :return: None
        """
        for path in paths:
            if not os.path.exists(path):
                continue
            print(f"{path} exists, deleting it.")
            if os.path.isdir(path):
                shutil.rmtree(path)
                continue
            if os.path.isfile(path):
                os.remove(path)

    @classmethod
    def list_all_files(cls, dir_path):
        """
        Recursively list all directories and files under the specified directory
        :param dir_path: The path of the directory to list files and directories
        :return: A list of all directories and file paths under dir_path
        """
        files = []
        file_list = os.listdir(dir_path)  # List all directories and files under the folder
        for file_path in file_list:
            path = os.path.join(dir_path, file_path)
            if os.path.isdir(path):
                files.extend(cls.list_all_files(path))
            if os.path.isfile(path):
                files.append(path)
        return files

    @staticmethod
    def get_root_dir_path():
        return os.getcwd()

    @staticmethod
    def get_absolute_file_path(file_path):
        return os.path.join(os.getcwd(), file_path)


if __name__ == "__main__":
    FileUtil.write_lines("test.txt", [1, 2, 3, 4])
    FileUtil.clear("test.txt")
    FileUtil.create_file_if_not_exist("demo.txt")
    FileUtil.remove_if_exist("test.txt", "demo.txt")
