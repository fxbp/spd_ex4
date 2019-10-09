


def readFile():
    path ='paraules.txt'
    with open(path) as fp:
        line=fp.readline()
        while line:
            line=line[:-1] # per eliminar l'ultim caracter que hi ha a la linia (salt de linia)
            print(line)
            line =fp.readline()

readFile()
