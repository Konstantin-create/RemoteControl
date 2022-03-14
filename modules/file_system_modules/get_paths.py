def get_paths_from_root(path):
    import os

    tabindex = 0
    output = ""
    output += str(path[path.rfind('\\'):]) + "\n"
    for root, dirs, files in os.walk(path):
        try:
            output += "\n" + (' ' * tabindex) + root.replace(root[:root.rfind('\\')], '') + "\n"
            for file in files:
                try:
                    output += (' ' * (tabindex + 1)) + file.replace(root, '') + "\n"
                except:
                    pass
            tabindex += 1
        except:
            pass
    return output


def write_paths_to_file(path):
    with open('paths.txt', "w") as file:
        file.write(get_paths_from_root(path))
        file.close()
    with open('finished.txt', "w") as file:
        file.write("true")
        file.close()
    return True

