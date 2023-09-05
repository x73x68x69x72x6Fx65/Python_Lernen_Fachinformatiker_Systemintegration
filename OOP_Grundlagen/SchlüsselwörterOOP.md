# Objekt Orientierte Programmierung mit Python

## 1. Wichtige Schlüsselwörter

### *Attribut / Eigenschaft*
Ein Attribut / Eigenschaft, beschreibt eine Klassenspezifische Variable oder eine Instanzvariable.
Instanzvariablen sind Variablen, welche innerhalb des Konstruktors oder innerhalb einer Methode definiert werden und nur zur aktuellen Instanz einer Klasse gehören.

### *Class*
"Class" Leitet eine Klassendefinition ein

### *self*
"self" wird als Parameter einer Funktion / Methode oder einer Prozedur übergeben.

Self verwendung in Bezug auf:
  - Eine Prozedur oder Funktion / Methode gehört zu einer Klasse und deren Objekte
  - Variablen: Sollte self. vor einer Variable stehen, so gehört Sie zu einer Klasse bzw. zum Klassenobjekt


### *def __init__(self)*
Wird verwendet um die Initialisierung einer Klasse durchzuführen. Der Code der init-Funktion läuft nur einmal beim Erstellen eines Klassenobjektes durch und ist danach nicht mehr aufrufbar. In der Init-Methode kann festgehalten werden, welche Varibalen mit welchen Werten Initialisiert werden sollen oder welche Methoden bei der Erstellung der Klasse aufgerufen werden sollen.

Beispielcode:

```
class Auto:

    def __init__(self, modell, kennzeichen, ps):
        self.__modell = modell
        self.__kennzeichen = kennzeichen
        self.__ps = ps
        self.__returnCarInformation()

    def __returnCarInformation(self):
        print("Das Auto ist ein", self.__modell, "\nEs hat das Kennzeichen: ", self.__kennzeichen, "\nUnd hat ", self.__ps, "PS")

mycar = Auto("VW-Polo", "WN-JJ-2020", "96")
#Ausgabe: 
#Das Auto ist ein VW-Polo 
#Es hat das Kennzeichen: WN-JJ-2020
#Und hat 96 PS
```
Hierbei wird die Klasse Auto erstellt, welche 3 Parameter für die Erstellung eines Klassenobjektes benötigt. Hierbei übergeben wir das Modell, das Kennzeichen und die PS. Um ein Klassenobjekt zu erzeugen, muss der Name der Klasse geschrieben werden, gefolgt von den Paramtern in einer Klammer. 

Die Init-Methode, erstellt hierbei 3 Klassenspezifische Variablen, welche innerhalb der Klasse über das Self-Schlüsselwort aufgerufen werden können. Anschließend wird die Funktion __returnCarInformation() ausgeführt, welche alle Informationen der Klasse über ein Print in der Konsole anzeigt. Ebenfalls ist die Init-Methode der sogeannnte Konstruktor der Klasse. 

Der Begriff Konstruktor steht für eine spezielle Methode, welche zur Erzeugung von Instanzen einer Klasse verwendet wird. Zum Entfernen oder Löschen einer Klasse wird eine so genannte Destruktor-Methode verwendet.


## 2. Basiskonzept OOP
Eine Klasse ermöglicht die Definiton von Objekten mit gleichen Attributen und Methoden. Die Klasse legt somit immer fest, welche Methoden und Attribute ein Objekt der Klasse besitzt.

Beispielcode für die Verwendung von Python-Klassen:
```
class Auto(): #Erstellung der Klasse
    counter = 0
    
    def __init__(self, modell, kennzeichen, ps):    #Initialisierung des Konstruktors
        self.__modell = modell                      #Erzeugung des Attributs
        self.__kennzeichen = kennzeichen            #Erzeugung des Attributs
        self.__ps = ps                              #Erzeugung des Attributs
        self.__countClassObjects()                  #Aufruf der Methode, bei jedem neuen Klassenobjekt

    def _returnCarInformation(self):               #Erzeugung der Methode
        print("Das Auto ist ein", self.__modell, "\nEs hat das Kennzeichen: ", self.__kennzeichen, "\nUnd hat ", self.__ps, "PS")
        
    def __countClassObjects(self):
        Auto.counter += 1 #Zähle Klassenobjekte
        print("Initialiserung Abgeschlossen! \nEs wurden bisher ", self.counter, "Objekte der Klasse Auto erzeugt\n")
        
        
myCar = Auto("VW-Polo", "WN-JJ-2020", "96")
yourCar = Auto("Honda", "WN-BB-2222", "71")
theirCar = Auto("Honda2", "WN-ZZ-3422", "128")

print("\n\n")
myCar._returnCarInformation()
print("\n\n")
yourCar._returnCarInformation()
print("\n\n")
theirCar._returnCarInformation()
```

Wie man hierbei gut sehen kann, werden die Klassenspezifischen Methoden von außerhalb der Klasse immer über das Klassenobject aufgerufen.
Das Schema ist hierbei immer Variablenname des Klassenobjects.Methodenname(Übergabeparamter (falls erforderlich)).


