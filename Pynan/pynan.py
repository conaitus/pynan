



def check_line(line, linecount):
    linearg = line.split(" ")

    if linearg[0].startswith("//"):
        return False
    if linearg[0] == "print":
        if len(linearg) > 2:
            print(f"Error on line {linecount}: print only needs 2 args!!")
            return True
        else:
            line = f"print({linearg[1]})"

    return line




with open("file.pn") as file_in: # open file
    script = []
    linecount = 0
    for line in file_in:
        linecount += 1
        line = check_line(line, linecount) #checking if is false or a line
        if line == False: # false is empty line
            pass
        elif line == True:# True is error
            exit(1)
        else:
            script.append(line)

    for line in script: #running script
        exec(line)