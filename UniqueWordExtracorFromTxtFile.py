openFile = open("data/dont_touch.txt", "r")
with open("data/UniqueWordFile", "w") as writeFile:
    tmp = set()
    for txtLine in openFile:
        if txtLine not in tmp:
            writeFile.write(txtLine)
            tmp.add(txtLine)
    openFile.close()
