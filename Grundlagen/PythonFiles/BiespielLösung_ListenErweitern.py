#----------------------------------Teilaufgabe 1--------------------------------------------------------------
#deklaration der variablen
liste1 = [5,7,1,6,7,9,2]
liste2 = [1,3,7,9,0,12,24]

listenKombination = []

# loope durch jedes element / jeden Wert einer Liste und speichere es in der leeren liste
for element in liste1:
    listenKombination.append(element)
    
for element in liste2:
    listenKombination.append(element)
    
print("liste1: ", liste1)
print("liste2: ", liste2)
print("listenKombination: ", listenKombination)
    
#----------------------------------Teilaufgabe 2--------------------------------------------------------------

umgedrehteListe = []
# range (startpunkt, endpunkt, schrittweise), len() gibt die länge eines Objektes wieder
for position in range(len(listenKombination)-1, -1, -1):
    umgedrehteListe.append(listenKombination[position])

print("umgedrehteListe: ", umgedrehteListe)