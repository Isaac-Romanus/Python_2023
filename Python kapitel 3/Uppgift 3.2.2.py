# Uppgift 3.2.2 (2p): 
# Bestäm utan dator storleken för matrisen A i följande uttryck:

1) A = vstack([zeros((2,2)),zeros((2,2)),zeros((2,2))])
# Bör vara 2 + 2 + 2 * 2, dvs 6x2 fylld med nollor. 

2) A = hstack([A,zeros((6,4))])
# Slår nu samman tidigare matris med en Matris av 6x4.
# Sammanslagningen är horisontel så nästa bör ha dinemsionerna 6x6

3) A = concatenate([A,zeros((6,4))],axis=1)
# numpy.concatenate slår ihop en sekvens av arrayer längs en angiven axis, 1 ger horisontal
# Således blir det här en 6x6 matris som slås ihop horisontellt med en 6x4 och bildar en 6x10

4) A = concatenate([A,zeros((2,10))],axis=0)
# axis 0 som också är default värdet slår istället ihop dem på vertikal led
# det ger oss nu en 8x10 matris efter denna

5) A = delete(A,[8,9],axis = 1)
# numpy.delete ger en ny array med sub-arrayer längs den borttagna axisen. 
# Andra argumentet: "obj", indicerar vilka som skall tas bort.
# Här är axis 1 vilket indicerar vertikal borttagning, column 8 och 9? 
# Objektet här är i form av två columner 8 och 9 och i och med start på 0 blir det de yttersta 
# columnerna, har kvar 8x8 med nollor

6) A = diag(A).reshape(4,-1)
# Diag returnerar en vektor mer diagnoalen, vilket här borde vara 8 nollor.
# Reshape ger ene array ny form utan att ändra dess innehåll. (rader, Kolumner)
# -1 som dimensionsvärde tar värdet från längden av arrayen och de återstående dimensionerna,
# Gissningsvis 2 i detta fall då för att ge en 4x2 tabell med nollor
