from utility import getColoumnRowByQuad

#se in una cella si ha solo una possibilità la scrive "in penna"
#return true se scrive un numero, false altrimenti
def only1numberPerCell(myDict, poss, i, j):
    if len(poss) == 1:
        myDict[str(i) + str(j)] = poss[0]
        print("Aggiunto in pos", i, j, "il numero", poss[0])
        print("Metodo: unico candidato in quella casella\n")
        return True
    else:
        return False

#se in una cella si ha un numero che non si trova da nessuna altra parte nel quadrante, lo scrive "a penna"
#return true se scrive un numero, false altrimenti
def only1numberPerQuad(myDict, poss, coloumn, row):
    if type(poss) is not list:
        return
    localPoss=poss.copy()
    nColoumn,nrow=getColoumnRowByQuad(coloumn,row)#inizio del quadrato
    for i in range(nColoumn, nColoumn + 3):
        for j in range(nrow, nrow + 3):
            n = myDict[str(i) + str(j)]
            if i!=coloumn or j!=row: #se non è la casella
                if type(n) is list:
                    for el in n:
                        if el in localPoss:
                            localPoss.remove(el)
    if len(localPoss)==1:
        myDict[str(coloumn) + str(row)] = localPoss[0]
        print("Aggiunto in pos", coloumn, row, "il numero", localPoss[0])
        print("Metodo: unico",localPoss[0],"in quel quadrante\n")
        return True
    else:
        return False

#se in una cella si ha un numero che non si trova da nessuna altra parte nella riga, lo scrive "a penna"
#return true se scrive un numero, false altrimenti
def only1numberPerRow(myDict, poss, coloumn, row):
    if type(poss) is not list:
        return
    localPoss=poss.copy()
    for i in range(1, 10):
        n = myDict[str(coloumn) + str(i)]
        if i!=row: #se non è la casella
            if type(n) is list:
                for el in n:
                    if el in localPoss:
                        localPoss.remove(el)
    if len(localPoss)==1:
        myDict[str(coloumn) + str(row)] = localPoss[0]
        print("Aggiunto in pos", coloumn, row, "il numero", localPoss[0])
        print("Metodo: unico",localPoss[0],"in quella riga\n")
        return True
    else:
        return False

#se in una cella si ha un numero che non si trova da nessuna altra parte nella colonna, lo scrive "a penna"
#return true se scrive un numero, false altrimenti
def only1numberPerColoumn(myDict, poss, coloumn, row):
    if type(poss) is not list:
        return
    localPoss=poss.copy()
    for i in range(1, 10):
        n = myDict[str(i) + str(row)]
        if i!=coloumn: #se non è la casella
            if type(n) is list:
                for el in n:
                    if el in localPoss:
                        localPoss.remove(el)
    if len(localPoss)==1:
        myDict[str(coloumn) + str(row)] = localPoss[0]
        print("Aggiunto in pos", coloumn, row, "il numero", localPoss[0])
        print("Metodo: unico",localPoss[0],"in quella colonna\n")
        return True
    else:
        return False