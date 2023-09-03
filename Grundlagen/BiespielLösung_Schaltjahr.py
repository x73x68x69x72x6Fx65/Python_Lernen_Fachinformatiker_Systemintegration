#variablen deklaration
userEingabe = None
breakLoop = False

while not breakLoop:
    print("===============Schaltjahrermittlung=======================\n")
    print("Bitte gib das zu überprüfende Jahr ein: ")
    try:
        userEingabe = int(input())
        # Wenn die Usereingabe nicht durch 100 teilbar ist oder Usereingabe durch 4 Teilbar
        if (userEingabe % 100 != 0 and userEingabe % 4 == 0) or (userEingabe % 400 == 0):
            print("Das Jahr - ", userEingabe, " - Ist ein Schaltjahr")
        else:
            print("Das Jahr - ", userEingabe, " - Ist kein Schaltjahr")
        print("\n Soll noch ein Jahr überprüft werden? \n[1] Ja [2] Nein\n")
        userEingabe = int(input())
        if userEingabe == 1:
            pass
        else:
            breakLoop = True
    except ValueError:
        print("\nUngültige Eingabe! Bitte gib ein Jahr ein: \n\n")
        
print("Programm wird beendet! ")
        

    
