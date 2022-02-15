from utility import getColoumnRowByQuad

# elimina da i possibili candidati tutti i numeri presenti nella riga (cambio quindi l'indice della colonna)
#modifico la variabile candidates passata per parametro, NON il puntatore
def findCandOnRow(myDict, coloumn, row, candidates):
    for i in range(1, 10):
        n = myDict[str(coloumn) + str(i)]
        if row != i and n in candidates and type(n) is int:
            candidates.remove(n)

# elimina da i possibili candidati tutti i numeri presenti nella colonna (cambio quindi l'indice della riga)
#modifico la variabile candidates passata per parametro, NON il puntatore
def findCandOnColoumn(myDict, coloumn, row, candidates):
    for i in range(1, 10):
        n = myDict[str(i) + str(row)]
        if coloumn != i and n in candidates and type(n) is int:
            candidates.remove(n)

# elimina da i possibili candidati tutti i numeri presenti nel quadrante di @coloumn e @row
#modifico la variabile candidates passata per parametro, NON il puntatore
def findCandInQuad(myDict, coloumn, row, candidates):
    nColoumn, nrow = getColoumnRowByQuad(coloumn, row)
    for i in range(nColoumn, nColoumn + 3):
        for j in range(nrow, nrow + 3):
            n = myDict[str(i) + str(j)]
            if coloumn != i and row != j and n in candidates and type(n) is int:
                candidates.remove(n)

# scrive in @myDict tutte le possibilita per ogni quadretto in posizione coloumn e row
def getPossibilities(myDict, coloumn, row):
        #per future implementazioni e per efficienza, leggo le possibilita gia scritte nell'esecuzione prima
        if type(myDict[str(coloumn) + str(row)]) is list:
            candidates = myDict[str(coloumn) + str(row)]
        else:
            candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # se è un numero "in penna", non ci posso fare nulla e faro return
        if type(myDict[str(coloumn) + str(row)]) is int and myDict[str(coloumn) + str(row)] != 0:
            return myDict[str(coloumn) + str(row)]

        # scorro la linea
        findCandOnRow(myDict, coloumn, row, candidates)

        # scorro la colonna
        findCandOnColoumn(myDict, coloumn, row, candidates)

        # cerco nel quadrante
        findCandInQuad(myDict, coloumn, row, candidates)

        return candidates