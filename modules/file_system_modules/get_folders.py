import os


def get_folders(path):
    dirname = path
    dirfiles = os.listdir(dirname)

    fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

    dirs = []

    for file in fullpaths:
        if os.path.isdir(file):
            dirs.append(file)
    return dirs
