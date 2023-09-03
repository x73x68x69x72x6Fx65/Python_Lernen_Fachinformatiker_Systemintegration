# In dieser Datei werden wir Ebenfalls den BMI-Rechner schreiben, aber diesesmal mit einer 
# User Eingabe für Gewicht und Körpergröße und einer Bewertung des BMI-Wertes

""" 
Wie geht man nun am besten vor? 

1. Überlege was für Variablen benötigst du für einen BMI-Rechner - Koerpergröße, Gewicht, BMI-Wert, geschlecht
2. Deklariere alle Variablen
3. Erstelle eine Ausgabe in der Konsole, damit der User weis was er zu erledigen hat - Eingabe Körpergröße und Gewicht
4. Überlege dir, wie die Berechnung umgesetzt werden muss - BMI = Körpergewicht (in KG) geteilt durch Körpergröße im Quadrat
5. Beginne die Logik umzusetzen 
"""
geschlecht = None
koerpergroesse_in_m = None
koerpergewicht_in_Kg = None
bmi_Wert = None

# Da Kommazahlen nur mit einem . in python zu verwenden sind, sollte der User darauf hingewiesen werden seine
# Eingabe entsprechend anzupassen.
print("============================BMI-Berechnung================================\n")
print("Bitte gebe deine Körpergröße in Meter an: \nHinweis: Die Körpergröße muss mit . angegeben werden bsp: 1.76 \n")

# Eine Usereingabe kann über input() erfolgen. Input lässt den User in der Konsole einen Wert eingeben
# und gibt dir diesen Wert als String - Zeichenkette zurück. Liest man Zahlen ein, müssen diese erst zu einer Zahl konvertiert werden
# in unserem Fall wird eine Fließkommazahl benötigt, somit wird der eingebene Text zu einem Float konvertiert.
koerpergroesse_in_m = float(input())

print("\nBitte gebe nun dein Körpergewicht an: \nHinweis: Das Körpergewicht muss mit . angegeben werden bsp: 56.77\n")
koerpergewicht_in_Kg = float(input())

print("\nBitte gebe dein Geschlecht an:\n[1] Weiblich\n[2] Männlich")
geschlecht = int(input())

print("\nDein BMI-Wert wird berechnet!\n")

#Berehcnung des BMI-Wertes durchführen
bmi_Wert = koerpergewicht_in_Kg / (koerpergroesse_in_m**2)

#Nun folgt eine If-Abfrage - Diese wird verwendet um verschiedene Fälle abnzufragen. Es spiegelt Wenn ... Dann ... wieder.
#Man verwendet If-Abfragen um Festzustellen ob eine Eingabe einem Wert oder einem Zeichen entspricht. Falls ja soll ein Code ausgeführt
#werden, welcher nur dann ausgeführt ist und ansonsten übersprungen wird
#Hierbei verwendet man == um festzustellen ob etwas identisch ist
# != um festzustellen ob etwas ungleich ist
# ! um einen Wert zu negieren -> !True ist somit False man kann also sagen ! entspricht dem Wort nicht

#Normalgewicht	Männer: 20 - 24,9	Frauen: 19 - 23,9
#Übergewicht	Männer: 25 - 29,9	Frauen: 24 - 29,9
#Starkes Übergewicht (Adipositas Grad I)	Männer: 30 - 34,9	Frauen: 30 - 34,9

#Abfrage ist User Weiblich?
if geschlecht == 1:
    #Wenn ja Führe den eingrückten Code aus
    # Nun Frage ab wie hoch oder niedrig der BMI ist, da es jeweils Reichenweiten sind müssen wir mehrere If-Abfragen
    # durchführen um zum Ergbnis zu kommen. 
    #Hierfür werden folgende Vergleichsoperatoren benötigt
    """
    < - kleiner
    > - größer
    <= - kleiner gleich
    >= - größer gleich
    and - Und Verknüpfung verschiedener Abfragen
    or - Entweder oder, schaut ob einer von zwei Fällen eintritt
    """
    # nach einem if können weitere Abfragen durchgeführt werden indem man elif verwendet, dies schaut ob die vorherige if abfrage 
    # Fehlschlägt, falls ja geht es in die elif Abfrage und überprüft diesen Fall. Sollte eine Elif Abfrage nun erfüllt sein, werden 
    # alle folgenden Elifs ignoriert und das Programm beendet
    # else ist eine art zu sagen, wenn alle abfragen ungültig sind dann führe ... aus.  
    if bmi_Wert < 19.00:
        #Wenn kleiner als 19 - Untergewicht
        print("Dein BMI-Wert ist ", bmi_Wert, " - Dieser Wert entspricht einem Untergewicht")
    elif bmi_Wert >= 19.00 and bmi_Wert <= 23.9:
        #Wenn größer oder gleich 19 und kleiner oder gleich 23.9
        print("Dein BMI-Wert ist ", bmi_Wert, " - Dieser Wert entspricht einem Normalgewicht")
    elif bmi_Wert >= 24 and bmi_Wert <= 29.9:
        #Wenn größer oder gleich 24  und kleiner oder gleich 29.9 - Übergewicht
        print("Dein BMI-Wert ist ", bmi_Wert, " - Dieser Wert entspricht einem Übergewicht")
    else:
        #In allen anderen Fällen - Starkes Übergewicht
        print("Dein BMI-Wert ist ", bmi_Wert, " - Dieser Wert entspricht einem starken Übergewicht")
else:
    # Abfrage für Männer 
    if bmi_Wert < 20.00:
        #Wenn kleiner als 20 - Untergewicht
        print("Dein BMI-Wert ist ", bmi_Wert, " - Dieser Wert entspricht einem Untergewicht")
    elif bmi_Wert >= 20.00 and bmi_Wert <= 24.9:
        #Wenn größer oder gleich 20 und kleiner oder gleich 24.9
        print("Dein BMI-Wert ist ", bmi_Wert, " - Dieser Wert entspricht einem Normalgewicht")
    elif bmi_Wert >= 25 and bmi_Wert <= 29.9:
        #Wenn größer oder gleich 25  und kleiner oder gleich 29.9 - Übergewicht
        print("Dein BMI-Wert ist ", bmi_Wert, " - Dieser Wert entspricht einem Übergewicht")
    else:
        #In allen anderen Fällen - Starkes Übergewicht
        print("Dein BMI-Wert ist ", bmi_Wert, " - Dieser Wert entspricht einem starken Übergewicht")
        
print("\n\n------------------------Abschluss BMI-Rechner-------------------------------\n\n")
#Abschluss BMI-Rechner
# ----------------------------------------------------------------------------------------------------------------------------
# Forschleifen werden verwendet um hoch oder runter zu zählen und für jeden Zählvorgang einen Code auszuführen
# Es folgt immer dem selben schema, man definiert eine Variable innerhalb der For-Schleife und definiert einen Bereich in welchem hoch oder 
# runter gezählt werden soll

#range wird verwendet um einer forschleife zu sagen, an welchem wert sie starten und enden soll, sowie mit welcher
#Schrittweise gearbeitet werden soll. 
# Range verwendung:
#Alle Zahlen von 0 bis 10 range(0,10) - 1 2 3 4 5 6 7 8 9 10
#Jede 4 Zahl von 0 bis 12 range(0,12,4) - 0 4 8 12
# Jede Zahl von 10 bis -10 range(10, -10, -1) 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
for zahl in range(0,-10,-2):
    print(zahl)
"""Ausgabe:
0
-2
-4
-6
-8
"""
liste = ["Meine", "Liste", "Mit", "Wichtigen", "Daten", 123, True]    
# For Schleifen können auch verwendet werden um elemnte aus einer Liste anzuzeigen
# Dafür wird die Methode len() verwendet, Sie gibt die Länge eines Objektes zurück - Bei einer Liste enbtspricht dies der Anzahl an Daten
for zahl in range(0,len(liste)):
    print("Listenposition ", zahl, " - Wert: ", liste[zahl])
"""Ausgabe:
Listenposition  0  - Wert:  Meine
Listenposition  1  - Wert:  Liste
Listenposition  2  - Wert:  Mit
Listenposition  3  - Wert:  Wichtigen
Listenposition  4  - Wert:  Daten
Listenposition  5  - Wert:  123
Listenposition  6  - Wert:  True
"""
# Sollte man die Position der Daten nicht benötigen kann man die Daten auch so abfragen
# element kann durch jede andere Bezeichnung ersetzt werden, es ist die Variable, welche bei 
# jedem Druchlauf die einzelnen Werte der Liste enthält
for element in liste:
    print("Wert: ", element)
"""Ausgabe:
Wert:  Meine
Wert:  Liste
Wert:  Mit
Wert:  Wichtigen
Wert:  Daten
Wert:  123
Wert:  True
"""
#Es gibt auch While Schleifen, welche mit einer Bedingung laufen:
# in diesem Fall der Bedingung, dass die Variable Var den Wert 0 nicht besitzt
#solange diese Bedingung erfüllt ist wird der Wert von var in der Konsole angezeigt und anschließend um 1 gesenkt
print("\n")
var = 5
while var != 0:
    print(var)
    # ziehe mit jedem durchlauf 1 von der Variable var ab
    var -= 1
    
#While Schleifen können auch mit booleans verwendet werden
breakLoop = False
count = 0
print("\n")

while breakLoop == False: # Kann auch durch while not breakLoop: dargestellt werden - Diese kürzeren Schreibweisen empfehle ich erst wenn man ein gutes Grundwissen hat
    print(count)
    count += 1
    # entspricht count dem Wert 5?
    if count == 5:
        #falls ja beende die While-Schleife
        breakLoop = True
    else:
        #falls nicht, ignoriere den Fall - pass wird verwendet um einfach im Code weiter zu springen
        pass