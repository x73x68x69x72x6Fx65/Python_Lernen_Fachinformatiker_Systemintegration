#Eine der wichtigsten Einstiges-Methoden von Python ist die Grundfunktion etwas in einem Konsolenfenster anzuzeigen. 
#Dies kann in Python mit print("") und einem Text zwischen den Anführungszeichen erfolgen.
#Üblicher Weise ist ein "Hello World" Programm die erste Aufgabe um eine Programmiersprache zu erlernen.
print("Hello World") 

#als erste kleine Aufgabe könntest du versuchen den Text Hello World in einer Python Datei mehrfach auszugeben ohne den Text selbst mehrfach 
#schreiben zu müssen

#-------------------------------------------------------------------------------------------------------------------------------

# Variablen-Deklarationen
# In Python müssen Variablen nicht genauer mit einem Datentyp definiert werden, es reicht also sich einen Namen für die Variable zu überlegen
# und dieser einen Wert zuzuweisen. 

koepergroesse_in_cm = 178
koerpergewicht_in_Kg = 69.77
user_Ausgabe = "Ihr BMI-Wert liegt bei: "
koepergroesse_in_m = None


bmi_Wert = None # None steht hierbei für eine Variable welche noch keinen Wert zugeordnet bekommen hat - wird für Wertlose
# Variablen per Zuweisungsoperator = das Schlüsselwort None vergeben. Zu einem späteren Zeitpunkt wird dies 
# dann durch den richtigen Wert ersetzt.

#Variablen können jederzeit von den Werten her kopiert oder Überschrieben werden indem man Ihnen nach dem Aufruf über den
#Variablennamen den Zuweisungsoperator = hinter den Namen schreibt und danach den neuen wert oder den namen einer anderen 
# Variable um den Wert zu kopieren
#BSP:
kopie_Koerpergroesse = koepergroesse_in_cm
#neuzuweisung der Werte in koepergroesse_in_cm
koepergroesse_in_cm = 183.5
print("kopie der Körpergröße: ", kopie_Koerpergroesse)
print("\nNeuer Wert von koepergroesse_in_cm: ", koepergroesse_in_cm)


"""
Beispiel für Berechnungen:

Folgende Rechen-Operatoren können unter Python verwendet werden

- +: Additions-Operator
- -: Subtraktions-Operator
- /: Divisions-Operator
- %: Modolo-Operator - Gibt den Rest zurück nach einer Division
- //: Ganzzahlige Divison - Nur mit Ganzzahlen verwendbar
- *: Multiplikations-Operator
- **: Potenz-Operator 2**3 -> 2*2*2 = 8
"""

# um nun den BMI-Wert zu berechnen, muss man auf die oben deklarierten Variablen zugreifen, dies 
# geschieht über den festgelegten Namen der Variablen
#Formel für den BMI - Wert:     BMI = Körpergewicht(in KG) geteilt durch Körpergröße(in Meter) zum Quadrat

#umrechnung cm in m - 100cm = 1m, somit muss nur durch 100 geteilt werden
#hierfür weist man der vorher deklarierten Variable koerpergroesse_in_m einen neuen Wert zu, welche sich aus dem Wert von 
#koerpergroesse_in_cm geteilt durch 100 zusammensetzt
koepergroesse_in_m = koepergroesse_in_cm / 100

#nun überschreibt man den None Wert um das Ergebnis der BMI-Berechnung zu sichern
# Die Klammern um koepergroesse_in_m, stellen sicher, dass dies als erstes ausgeführt wird, bevor die Division erfolgt.
bmi_Wert = koerpergewicht_in_Kg / (koepergroesse_in_m**2)

# mit print() können Dinge ausgegeben werden - Hiertbei können direkt Ausgaben per ""-Kennzeichner ausgegeben werden
# oder Variablen ausgegeben werden
print("BMI wurde Berechnet. Ergebnis wird ausgegeben: \n") # \n bewirkt einen Zeilen-Umbruch 

# Gibt es mehrere Variablen die man nacheinander in der selben Zeile ausgeben möchte kann man dies mit einem , zwischen
# den beiden Namen bewirken.
print(user_Ausgabe , bmi_Wert)
# Anstatt print(user_Ausgabe , bmi_Wert) könnte man auch print("Ihr BMI-Wert liegt bei: ", bmi_Wert) verwenden, die 
# Ausgabe bleibt hierbei die Gleiche. Die Variable user_Ausgabe erfüllt hierbei nur die Funktion den String bzw die Zeichenkette
# abrufbar zu machen ohne den ganzen Text erneut schreiben zu müssen. Dies macht vorallem Sinn, wenn man einen Text mehrfach wiederholt 
# ausgeben möchte

# Lässt man das ganze Programm nun durchlaufen Erscheint die Ausgabe:
# Ihr BMI-Wert liegt bei:  20.75811134957707

#Versuche jetzt selbst kleinere Rechnung mit Variablen und dem Print Befehl durchzuführen. Am besten wäre es wenn du versuchst
#das Volumen von einem Würfel in einem Pythonscript zu berechnen. Die Kantenlänge des Würfels beträgt 5cm.
#Formel zur Berechnung des Volumens: Volumen = Kantenlänge hoch 3. Du kannst überprüfen ob deine Rechnung richtig ist, wenn als
#Ergebnis 125 herauskommt.

