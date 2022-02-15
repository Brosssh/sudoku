#dato una cella, trova la colonna e la riga in cui si trova la prima cella del quadrante dove essa è contenuta
#@param col,row la colonna e la riga della cella
#@return ncoloumn, nrow ovvero la colonna e la riga dove si trova la prima cella del quadrante dove essa è contenuta
def getColoumnRowByQuad(col,row):
    ncoloumn = 1  # la posizione del quadrante
    if 6 >= col > 3:
        ncoloumn = 4
    elif 9 >= col > 6:
        ncoloumn = 7

    nrow = 1  # la posizione del quadrante
    if 6 >= row > 3:
        nrow = 4
    elif 9 >= row > 6:
        nrow = 7
    return ncoloumn,nrow

def printPossibilities(myDict):
    for i in range(1,10):
        for j in range(1,10):
            if type(myDict[str(i)+str(j)]) is not int:
                print("Possibilita nella cella",i,j,myDict[str(i)+str(j)])

#stampa l'array strutturato come un sudoku
def printGrid(myList):
    for i in range(len(myList)):
        if i % 3 == 0 and i != 0:
            print("----------------------")
        for j in range(len(myList[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(myList[i][j]) if type(myList[i][j]) is int else print("  ")
            else:
                print(str(myList[i][j]) + " ", end="") if type(myList[i][j]) is int else print("  ",end="")

#converte un array in una dictionary
#@param la lista/array
#@return la dict
def toDict(a):
    newDict = "{"
    for i in range(9):
        for j in range(9):
            possibilita = ""
            possibilita += ("'" + str(i + 1) + str(j + 1) + "' : ")
            possibilita += (str(a[i][j]) + " , ")
            newDict += (str(possibilita))
    d = newDict[:len(newDict) - 3]
    d += "}"
    return d

#converte un dictionary in un array
#@param la dict
#@return la lista/array
def toGrid(myDict):
    g = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]
         ]

    for i in range(9):
        for j in range(9):
            g[i][j] = myDict[str(i + 1) + str(j + 1)]
    return g


