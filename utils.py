def read_file():
    words = dict()
    path ='words.txt'
    with open(path) as fp:
        line=fp.readline()
        while line:
            line=line[:-1] # per eliminar l'ultim caracter que hi ha a la linia (salt de linia)
            charNum = len(line)
            if charNum not in words.keys():
                words[charNum]=0
            words[charNum]+=1
            line =fp.readline()

    return words
