import ast
from normalMethods import only1numberPerRow, only1numberPerQuad, only1numberPerColoumn, only1numberPerCell
from possiblities import getPossibilities
from utility import toDict, toGrid, printGrid, printPossibilities

"""
a = [[0, 0, 0,  0, 0, 0,    0, 0, 0],
     [0, 0, 0,  0, 0, 0,    0, 0, 0],
     [0, 0, 0,  0, 0, 0,    0, 0, 0],

     [0, 0, 0,  0, 0, 0,    0, 0, 0],
     [0, 0, 0,  0, 0, 0,    0, 0, 0],
     [0, 0, 0,  0, 0, 0,    0, 0, 0],

     [0, 0, 0,  0, 0, 0,    0, 0, 0],
     [0, 0, 0,  0, 0, 0,    0, 0, 0],
     [0, 0, 0,  0, 0, 0,    0, 0, 0]
     ]
"""
a = [[2, 0, 0,  0, 6, 0,    0, 1, 0],
     [0, 5, 0,  0, 7, 9,    8, 0, 4],
     [0, 0, 0,  0, 0, 4,    0, 6, 0],

     [0, 0, 0,  7, 5, 0,    3, 9, 0],
     [7, 0, 0,  4, 0, 1,    0, 0, 6],
     [0, 9, 5,  0, 8, 2,    0, 0, 0],

     [0, 2, 0,  8, 0, 0,    0, 0, 0],
     [8, 0, 1,  9, 0, 0,    0, 3, 0],
     [0, 3, 0,  0, 2, 0,    0, 0, 1]
]

#controlla la griglia con possibilita e applica un metodo base per modificarla
#@param la dict della griglia, NON l'array
#@return true se ha fatto qualcosa, false se non è riuscito a trovare nulla
#@warning so che sarebbe piu efficiente mettere l'ultimo metodo per primo ma seguo la logica che seguirebbe un umano,
#quindi prima controllo quadranti e righe/colonne
def applyNormalMethods(gridConPossibilita):
    #scorro tutte le posizioni della griglia e controllo se posso fare qualcosa con quella cella
    for i in range(1, 10):
        for j in range(1, 10):
            poss = gridConPossibilita[str(i) + str(j)]
            if type(poss) is not int:  # se non è gia un numero finale, quindi se ci sono delle possibilita [1,5]
                #controlla se in quella cella ho un numero presente solo in quel quadrante, se si lo scrive "in penna" e ritorna true
                if only1numberPerQuad(gridConPossibilita, poss, i, j):
                    return True
                # controlla se in quella cella ho un numero presente solo in quella riga, se si lo scrive "in penna" e ritorna true
                if only1numberPerRow(gridConPossibilita, poss, i, j):
                    return True
                # controlla se in quella cella ho un numero presente solo in quella colonna, se si lo scrive "in penna" e ritorna true
                if only1numberPerColoumn(gridConPossibilita, poss, i, j):
                    return True
                 # controlla se in quella cella ho solo un numero, se si lo scrive "in penna" e ritorna true
                if only1numberPerCell(gridConPossibilita, poss, i, j):
                    return True
    return False

#inserisce nella dict della griglia le possibilita per casella (Es. in pos 1 1 [1,5]
#@param la dict della griglia, NON l'array
def fill(gridConPossibilita):
    for i in range(1, 10):
        for j in range(1, 10):
            poss = getPossibilities(gridConPossibilita, i, j)
            gridConPossibilita[str(i) + str(j)] = poss


#converto l'array in una dictionary del tipo {'11': 3, '12': 8,...}
#è piu facile lavorarci
#la key sara la somma del numero colonna e numero riga  Es. '53' sarà 5 colonna, terza riga
gridConPossibilita = ast.literal_eval(toDict(a))


while True:
    fill(gridConPossibilita)
    if not applyNormalMethods(gridConPossibilita): #se non ho modificato niente (o ho finito o non so andare avanti)
        break


printPossibilities(gridConPossibilita)

#riconverto la mia dict in array
#piu facile visualizzarla
resolvedGrid = toGrid(gridConPossibilita)
printGrid(resolvedGrid)
