def get_args(arg):
    if arg.find("(") == -1:
        return ""
    else:
        output_tmp = arg[arg.find("(") + 1:arg.find(")")].split(';')
        output = []
        for el in output_tmp:
            output.append(el.strip())
        return output
