import random
#Zahlen Raten 
userEingabe = None
zufallszahl = random.randint(0,100)
breakLoop = False

while not breakLoop:
    print("======================Zahlenraten======================= \n")
    print("Es wird eine Zahl zwischen 0 und 100 gesucht. Gebe deinen Tipp ab: \n")
    try: 
        userEingabe = int(input())
    except: 
        print("\nEs wurde keine Zahl eingeben! Versuche es erneut.\n")
    if userEingabe > zufallszahl:
        print("\nDie gesuchte Zahl ist kleiner!\n")
    elif userEingabe < zufallszahl:
        print("Die gesuchte Zahl ist größer!\n")
    elif userEingabe == zufallszahl:
        print("Klasse! Du hast die Zahl erraten!\n")
        print("\nMöchtest du eine neue Runde spielen? \n[1] Ja \n[2] Nein\n") 
        userEingabe = int(input()) 
        if userEingabe == 1:
            zufallszahl = random.randint(0,100)
        elif userEingabe == 2:
            print("Programm wird beendet!")
            breakLoop = True
    