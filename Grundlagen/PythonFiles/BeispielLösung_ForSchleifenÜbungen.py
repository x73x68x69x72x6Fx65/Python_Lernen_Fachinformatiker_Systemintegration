#variablen deklaration
userEingabe = None
breakLKoop = False

#----------------------------------------------Erste Aufgabe------------------------------------------------------------------------------


while not breakLKoop:
    print("_____________________Sternen Muster-1_____________________\n")
    print("Wie viele Reihen sollen erzeugt werden? \n")
    
    try:
        userEingabe = int(input())
        if userEingabe < 3:
            print("Bitte versuche es erneut. Es können keine Negativen Werte verwendet werden - Min Value 3")
        else:
            breakLKoop = True
    except ValueError:
        print("\n Keine gültige Zahl - Bitte versuche es erneut\n")


for zahl in range(0, userEingabe, 1):
    print("*"*zahl)
    
    
#---------------------------------------Zweite Aufgabe-------------------------------------------------------------------------------


print("\n--------------------------------------------------\n\n")
breakLKoop = False

while not breakLKoop:
    print("_____________________Sternen Muster-2_____________________\n")
    print("Wie viele Reihen sollen erzeugt werden? \n")
    
    try:
        userEingabe = int(input())
        if userEingabe < 5:
            print("Bitte versuche es erneut. Es können keine Negativen Werte verwendet werden - Min Value 5\n")
        else:
            breakLKoop = True
    except ValueError:
        print("\n Keine gültige Zahl - Bitte versuche es erneut\n")
    
nhoehe = userEingabe * 2 - 1
for i in range(userEingabe + 1):
    for j in range(nhoehe):
        if (j > (nhoehe // 2) - i) and (j < (nhoehe // 2) + i):
            print('*', end='')
        else:
            print(" ", end='')
    print()
    
    
#-------------------------------------------BonusAufgabe-----------------------------------------------------------------------------

print("\n--------------------------------------------------\n\n")
breakLKoop = False

while not breakLKoop:
    print("_____________________Sternen Muster-3 Bonusaufgabe_____________________\n")
    print("Wie viele Reihen sollen erzeugt werden? \n")
    
    try:
        userEingabe = int(input())
        if userEingabe < 5:
            print("Bitte versuche es erneut. Es können keine Negativen Werte verwendet werden - Min Value 5\n")
        else:
            breakLKoop = True
    except ValueError:
        print("\n Keine gültige Zahl - Bitte versuche es erneut\n")

print("\n")
#userEingabe als Kantenlaenge
neueKantenlaenge = userEingabe // 3
for i in range(userEingabe + neueKantenlaenge + 1):
    for j in range(userEingabe + neueKantenlaenge + 1):
        if (j > neueKantenlaenge) and (i == 0 or i == userEingabe):
            print('*', end='')
        elif (j < userEingabe) and (i == neueKantenlaenge or i == userEingabe + neueKantenlaenge):
            print('*', end='')
        elif (i >= neueKantenlaenge) and (j == 0 or j == userEingabe):
            print('*', end='')
        elif (i <= userEingabe) and (j == neueKantenlaenge or j == userEingabe + neueKantenlaenge):
            print('*', end='')
        elif (i + j) == neueKantenlaenge or (i + j) == (userEingabe + userEingabe + neueKantenlaenge):
            print('*', end='')
        elif (i + j) == userEingabe + neueKantenlaenge and (j < neueKantenlaenge or j > userEingabe):
            print('*', end='')
        else:
            print(" ", end='')
    print()


