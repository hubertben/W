import sys

def commandLineArgs():
    return sys.argv[1:]


def openAndReadFile(path):
    file = open(path)
    text = file.read().split()
    file.close()
    return list(text)


print(openAndReadFile(commandLineArgs()[0]))