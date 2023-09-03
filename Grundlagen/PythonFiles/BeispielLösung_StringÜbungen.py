# Übung 1
# Ausgabe :
# Der Satz ist: Hello World!
# Der Buchstabe lautet: H
satz = "Hello World!"
print("Der Satz ist:", satz)
buchstabe = satz[0]
print("Der Buchstabe lautet: ",buchstabe)

#Übung 2
satz = "Ich habe erneut Hunger!"
print(len(satz))

#Übung 3
satz = "Ich habe Hunger!"
zeichen = "h"
print("Das erste", zeichen, "befindet sich an der Position: ", satz.find(zeichen))
zeichen = "x"
print("Das erste", zeichen, "befindet sich an der Position: ", satz.find(zeichen))

#Übung 4
satz = "Lorem ipsum dolor sit amet, consetetur sadipscing"
satz += "elitr, sed diam nonumy eirmod tempor invidunt ut labore et"
satz += "dolore magna aliquyam erat, sed diam voluptua."

eCounter = 0
sCounter = 0
lCounter = 0

for char in satz:
    #finde alle e
    if char == "e" or char == "E":
        eCounter += 1
    #finde s
    if char == "s" or char == "S":
        sCounter += 1
    #finde l   
    if char == "l" or char == "L":
        lCounter += 1
print("Es gibt ", eCounter, "E´s, ", sCounter, "S´s, sowie ", lCounter, "l´s in dem vorhanden Satz!")
    
#Übung 5
satz = "Lorem ipsum dolor sit amet consetetur sadipscing elitr sed diam voluptua."
woerter = satz.split(" ")
print(woerter)

#Übung 6
satz = "lorem ipsum dolor sit amet consetetur sadipscing elitr sed diam voluptua."
reversed = ""
for i in range(len(satz)-1, -1, -1):
    reversed += satz[i]
print(reversed.upper())