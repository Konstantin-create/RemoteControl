import os


def get_filenames(path):
    dirname = path
    dirfiles = os.listdir(dirname)

    fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

    files = []

    for file in fullpaths:
        if os.path.isfile(file):
            files.append(file)

    return files
