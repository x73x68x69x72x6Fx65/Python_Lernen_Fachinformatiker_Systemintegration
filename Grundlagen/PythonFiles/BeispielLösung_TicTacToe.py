import os
import time

def printSpielfeld(spieler, zeichen):
    os.system('cls' if os.name == 'nt' else 'clear')  # Löscht den Bildschirm (Windows oder Unix-basierte Systeme)
    print("Spieler,", spieler, ",ist am Zug! Welches Feld möchtest du verwenden?\n")
    print(" -------------------")
    print(" | ", spielfeld[0], " | ", spielfeld[1], " | ", spielfeld[2], " | ")
    print(" | ", spielfeld[3], " | ", spielfeld[4], " | ", spielfeld[5], " | ")
    print(" | ", spielfeld[6], " | ", spielfeld[7], " | ", spielfeld[8], " | ")
    print(" -------------------")
    breakLoop = False
    while not breakLoop:
        try:
            user = int(input()) - 1
            if spielfeld[user] != "X" or spielfeld[user] != "O":
                setzteZeichen(position=user, zeichen=zeichen)
                breakLoop = True
                return user
            else:
                print("Ungültiger Spielzug!")
        except ValueError:
            print("\nKein Gültiger Spielzug, Bitte probiere es erneut!\n")
            
def pruefeSpielfeld():
    if spielfeld[0] == "X" and spielfeld[1] == "X" and spielfeld[2] == "X":
        print("\n",spieler1, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[3] == "X" and spielfeld[4] == "X" and spielfeld[5] == "X":
        print("\n",spieler1, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[6] == "X" and spielfeld[7] == "X" and spielfeld[8] == "X":
        print("\n",spieler1, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[0] == "X" and spielfeld[4] == "X" and spielfeld[8] == "X":
        print("\n",spieler1, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[6] == "X" and spielfeld[4] == "X" and spielfeld[2] == "X":
        print("\n",spieler1, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[0] == "X" and spielfeld[6] == "X" and spielfeld[3] == "X":
        print("\n",spieler1, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[1] == "X" and spielfeld[4] == "X" and spielfeld[6] == "X":
        print("\n",spieler1, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[2] == "X" and spielfeld[5] == "X" and spielfeld[8] == "X":
        print("\n",spieler1, "Du hast Gewonnen!\n\n")
        return True
    
    if spielfeld[0] == "O" and spielfeld[1] == "O" and spielfeld[2] == "O":
        print("\n",spieler2, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[3] == "O" and spielfeld[4] == "O" and spielfeld[5] == "O":
        print("\n",spieler2, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[6] == "O" and spielfeld[7] == "O" and spielfeld[8] == "O":
        print("\n",spieler2, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[0] == "O" and spielfeld[4] == "O" and spielfeld[8] == "O":
        print("\n",spieler2, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[6] == "O" and spielfeld[4] == "O" and spielfeld[2] == "O":
        print("\n",spieler2, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[0] == "O" and spielfeld[6] == "O" and spielfeld[3] == "O":
        print("\n",spieler2, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[1] == "O" and spielfeld[4] == "O" and spielfeld[6] == "O":
        print("\n",spieler2, "Du hast Gewonnen!\n\n")
        return True
    if spielfeld[2] == "O" and spielfeld[5] == "O" and spielfeld[8] == "O":
        print("\n",spieler2, "Du hast Gewonnen!\n\n")
        return True

def setzteZeichen(zeichen, position):
    spielfeld[position] = zeichen
    
# erstelle spielfeld
spielfeld = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
]
spieler1 = ""
spieler2 = ""

print("=======================TicTacToe=========================\n")
print("Jeder Spieler soll sich einen Namen geben, bitte trage deinen Namen ein Spieler1: \n")

spieler1 = input("")

print("\nJeder Spieler soll sich einen Namen geben, bitte trage deinen Namen ein Spieler2: \n")

spieler2 = input("")

print(f"\n{spieler1}: X", f"{spieler2}: O\n")
time.sleep(2.559)
beendet = False

while not beendet:
    printSpielfeld(spieler=spieler1, zeichen="X")
    if (pruefeSpielfeld()):
        beendet = True
    else:
        printSpielfeld(spieler=spieler2, zeichen="O")
        if(pruefeSpielfeld()):
            beendet = True
    

