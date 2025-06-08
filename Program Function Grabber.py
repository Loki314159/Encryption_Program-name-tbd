with open("Encryption w Tkinter.py", "r") as main:
    for line in main:
        linelist=list(line)
        if linelist[0] == "d":
            if linelist[1] == "e":
                if linelist[2] == "f":
                    if not line == '\n': 
                        print(line[4:])