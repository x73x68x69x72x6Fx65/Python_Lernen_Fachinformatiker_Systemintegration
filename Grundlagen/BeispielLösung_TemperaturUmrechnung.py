# Erstelle eine Methode für jede Umrechnungsart
# def wird verwendet um eine sogenannte Methode zu erstellen. Sie werden verwendet um an unterschiedlichen Stellen im Code
# auf die selbe Rechnung mit unterschiedlichen Paramtern (Übergabewerten) nicht immer alles neu schreiben zu müssen.
# nach dem def folgt ein Name was die Methode macht und in den Klammern steht der name der variable welche übergeben
# wird - diese kann beliebig benannt werden
# Das Schlüsselwort return legt dabei fest was nach dem Aufruf der Methode zurück gegeben werden soll.

def umrechnung_Celsius_Kelvin(celsius):
    return celsius + 273.15

def umrechnung_Celsius_Fahrenheit(celsius):
    return (celsius * (9/5) + 32)

def umrechnung_Kelvin_Celsius(kelvin):
    return kelvin - 273.15

def umrechnung_Kelvin_Fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def umrechnung_Fahrenheit_Celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def umrechnung_Fahrenheit_Kelvin(fahrenheit):
    return (fahrenheit -32) * 5/9 + 273.15

#variablen - Benötigt zum toggeln der While Schleife, zum tracken der Userauswahl und Temperatureingabe
auswahlMenue = True
userAuswahl = None
temperature = None

while auswahlMenue:
    #erstelle layout für Umrechnungsmöglichkeiten
    print("\n===================Temperatur-Umrechnung==================\n")
    print("Was soll umgerechnet werden? \n\n")
    print("[1] - Umrechnung von Celsius nach Kelvin\n")
    print("[2] - Umrechnung von Celsius nach Fahrenheit\n")
    print("[3] - Umrechnung von Kelvin nach Celsius\n")
    print("[4] - Umrechnung von Kelvin nach Fahrenheit\n")
    print("[5] - Umrechnung von Fahrenheit nach Celsius\n")
    print("[6] - Umrechnung von Fahrenheit nach Kelvin\n\n")
    #versuche die Eingabe in einen Integer zu konvertieren
    try:
        userAuswahl = int(input())
        auswahlMenue = False
    #Falls ein Fehler dabei Auftritt - ValueError (Eingabe eines Zeichens anstatt einer Zahl) wiederhole die Eingabe mit Hinweis für den User
    except ValueError:
        print("\nUngültige Eingabe erkannt! Probiere es erneut \n")
# checke welche Umrechnung ausgewählt wurde und nehme Temperatur zur Umrechnung entgegen 
#statt einem match case kann auch eine gewöhnliche if / elif / else Abfrage erfolgen
match userAuswahl:
    case 1:
        print("Bitte Celsius eingeben: \nHinweis bei Temperaturen wie 12,6°C bitte nur 12.6 eingeben\n")
        temperature = float(input(""))
        print("\nUmrechnung abgeschlossen! Temperatur in Celsius: ", temperature,"°C", " - in Kelvin: ", umrechnung_Celsius_Kelvin(temperature),"°K")
    case 2:
        print("Bitte Celsius eingeben: \nHinweis bei Temperaturen wie 12,6°C bitte nur 12.6 eingeben\n")
        temperature = float(input(""))
        print("\nUmrechnung abgeschlossen! Temperatur in Celsius: ", temperature,"°C", " - in Fahrenheit: ", umrechnung_Celsius_Fahrenheit(temperature),"°F")
    case 3:
        print("Bitte Kelvin eingeben: \nHinweis bei Temperaturen wie 299,6°K bitte nur 299.6 eingeben\n")
        temperature = float(input(""))
        print("\nUmrechnung abgeschlossen! Temperatur in Kelvin: ", temperature,"°K", " - in Celsius: ", umrechnung_Kelvin_Celsius(temperature),"°C")
    case 4:
        print("Bitte Kelvin eingeben: \nHinweis bei Temperaturen wie 299,6°K bitte nur 299.6 eingeben\n")
        temperature = float(input(""))
        print("\nUmrechnung abgeschlossen! Temperatur in Kelvin: ", temperature,"°K", " - in Fahrenheit: ", umrechnung_Kelvin_Fahrenheit(temperature),"°F")
    case 5:
        print("Bitte Fahrenheit eingeben: \nHinweis bei Temperaturen wie 78,7°F bitte nur 78.7 eingeben\n")
        temperature = float(input(""))
        print("\nUmrechnung abgeschlossen! Temperatur in Fahrenheit: ", temperature,"°F", " - in Celsius: ", umrechnung_Fahrenheit_Celsius(temperature),"°C")
    case 6:
        print("Bitte Fahrenheit eingeben: \nHinweis bei Temperaturen wie 78,7°F bitte nur 78.7 eingeben\n")
        temperature = float(input(""))
        print("\nUmrechnung abgeschlossen! Temperatur in Fahrenheit: ", temperature,"°F", " - in Kelvin: ", umrechnung_Fahrenheit_Kelvin(temperature),"°K")
        


