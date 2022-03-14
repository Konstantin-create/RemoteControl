import os
import shutil


def move(file_source, file_destination):
    shutil.move(file_source, file_destination)


def rename(path, new_name):
    os.rename(path, path[:path.rfind('\\')] + '\\' + new_name)


def remove(path):
    os.remove(path)


def make_zip(path):
    filename = path[path.rfind("\\"):]
    output_filename = os.path.abspath(os.curdir) + "\\" + f'ZipFiles\\{filename}'
    return shutil.make_archive(output_filename, 'zip', path)
