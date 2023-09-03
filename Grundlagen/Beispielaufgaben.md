# Grundübungen zum Verständnis von Print Befehlen

*Alle Lösungen zu den Grundübungen zum Verständnis von Print Befehlen befinden sich in der Datei* **BeispielLösung_Grundaufgaben.py**

## Übung 1:
Versuche die Wörter Kaffe, Zucker und Tee genau in dieser Reihenfolge, jeweils mit einem Leerzeichen dazwischen mit einem Print-Befehl auszugeben.

## Übung 2:
Versuche 3 mal hintereinander den Satz PythonIstSimpel und ohne Leerzeichen dazwischen auszugeben.

## Übung 3:
Versuche die Ausgabe in der Konsole für Folgenden Python Code vorherzusagen:
```
alter = 21
name = "Kevin"
print("Hey, Ich bin", name, "!", "In 5 Jahren bin ich ", alter + 5, "Jahre alt.")
```

## Übung 4:
Schau dir folgenden Code an und entscheide dich, was auf der Console ausgegeben wird:
```
zahl1 = 23
zahl2 = 9.6
print(zahl1 >= zahl2, zahl1 <= zahl2, not zahl1, zahl1 % 5 != 0)
```

## Übung 5:
Nutze die 3 Variablen,
```
zahl1 = 10
zahl2 = 4.77
zahl3 = 2
```
um Folgende Ausgabe zu erreichen:
*124.77*
Hierfür sollen keine weiteren Variablen erstellt werden. Es dürfen nur die Print Funktion und die Variablen zur Lösung des Problems verwendet werden.

## Übung 6:
Überlege dir wie du mit einer einzigen Variable und mehreren Print-Funktionsaufrufen folgende Konsolenanzeige replizieren kannst:
```
True
False
True False False
789
```

# _______________________________________________________________________________________________________________________________________________

**Hinweis für alle Aufgaben wird empfohlen sich davor zu Erkundigen, wie man mit dem print Befehl auch in der selben Zeile ohne Zeilenumbruch wieder eine Ausgabe erzeugen kann. Zudem solltest du immer im Hinterkopf behalten, dass es für eine Aufgabe mehrere Lösungen gibt und es nicht nur eine Richtige Lösung gibt. Je nach Denk- und Vorgehensweise unterscheiden sich die Lösungen hierbei stark. Die vorhanden Lösungen sind nur Beispiele oder Vorschläge, wie ich diese Probleme gelöst hätte.**


# Aufgabe 1 - TemperaturUmrechnung

Es soll ein Konsolenprogramm erstellt werden, in welchem es ein Auswahlmenü mit folgenden Punkten gibt
* (1) Umrechnung von Celsius nach Kelvin
* (2) Umrechnung von Celsius nach Fahrenheit
* (3) Umrechnung von Kelvin nach Celsius
* (4) Umrechnung von Kelvin nach Fahrenheit
* (5) Umrechnung von Fahrenheit nach Celsius
* (6) Umrechnung von Fahrenheit nach Kelvin

Der User soll sich anhand des Menüs mit den Zahlen 1-6 zwischen den Umrechnungsvarianten entscheiden können und anschließend seine Umzurechnende Temperatur eingeben. Die umgerechnete Temperatur soll am Ende in der Konsole ausgegeben werden.

# Aufgabe 2 - Schaltjahr

Es soll ein Konsolenprogramm geschrieben werden, welches ermittelt, ob ein Eingebenes Jahr ein Schaltjahr ist oder nicht.
Dafür gibt es folgende Hilfestellung:
* nicht durch 4 teilbar | kein Schaltjahr
* durch 4 teilbar       | Schaltjahr
* durch 100 teilbar     | kein Schaltjahr
* durch 400 teilbar     | Schaltjahr

Beispiele: 2000 Schaltjahr, 2008 Schaltjahr, 2009 Kein Schaltjahr, ...

# Aufgabe 3 - Listen erweitern und kombinieren

Erstelle ein Programm welches zwei listen mit den Werten:
* 1. [5,7,1,6,7,9]
* 2. [1,3,7,9,0,12,24]
enthält. 

Nun soll eine leere Liste mit den Werten beider oben aufgeführten Listen gefüllt werden, ohne dass man die Werte Händisch überträgt.
Anschließend sollen alle Werte der Liste umgedreht werden. **Hinweis: Die Methode Liste.reverse() gibt es zwar, soll aber bei dieser Aufagbe nicht verwendet werden. Ziel ist es selbst zu überlegen wie man diese Funktion umsetzen kann**


# Aufgabe 4 - Zahlen Raten

Schreibe eine Konsolenanwendung, welche eine Zufallszahl generiert (Zahl zwischen 0 und 100) und den User bittet über die Eingabe die Zahl zu erraten. Sollte der User mit seiner geratenen Zahl falsch liegen, soll Ihm ein Hinweis ausgegeben werden, ob die gesuchte Zahl niedriger oder höher ist. Sobald der User die Zahl erraten hat, soll angezeigt werden, wieviele Versuche er benötigt hat.
**Hinweis: Um Zufallszahlen zu genieren, muss zuvor in Zeile 1 deines Pythonscripts import random hinzugefügt werden. Über random.randint(startzahl,endzahl) kann schließlich eine Zufallszahl für den Bereich zwischen starttahl und endzahl generiert werden.**


# Aufgabe 5 - ForSchleifen Übungen

Erstelle 2 Programme mit Folgenden Ausgaben: 

Als Erstes soll folgendes Muster erzeugt werden:
```
*      
**     
***    
****   
*****  
****** 
```
Hierbei soll eine Art Treppe aus * gezeichnet werden, wobei der User selbst entscheiden soll wieviele Reihen gezeichnet werden sollen


Als zweites soll eine Pyramide mit Sternen gezeichnet werden.
```
    *
   ***
  *****
 *******
*********
```
Auch hierbei soll der User selbst bestimmen können, in wieviele Zeilen bzw. welche Höhe die Pyramide bekommen soll.

**Bonusaufagbe für Forschleifen - Schwierige Aufgabe**
Als Bonus soll Folgendes Muster gezeichnet werden:
```
  *********
 **      **
********* *
* *     * *
* *     * *
* *     * *
* *     * *
* *     * *
* *********
**      **
*********
```
Hierbei soll ein 3D Würfel erstellt werden, bei welchem der User selbst festlegen kann, wie hoch der Würfel gezeichnet werden soll.

# Aufgabe 6 String Übungen

## Übung 1
Du hast folgenden Code:
```
satz = "Hello World!"
print("Der Satz ist:", satz)
buchstabe = satz[0]
print("Der Buchstabe lautet: ",buchstabe)
```
Was wird in der Konsole ausgegeben?

## Übung 2
Erstelle einen String mit einer Länge von 23 und überprüfe es, indem du die len() Funktion verwendest und die Länge des Strings ausgibst.
Hierfür ist es eigentlich egal welche Länge du genau nimmst, wichtig ist nur dass die länge über 10 ist und es ein Satz ist mit mehreren Wörtern ist.

## Übung 3
Finde in dem Satz
```
Ich habe Hunger!
```
mit Hilfe der find()-Funktion die Position des ersten "h" und des ersten "x" und gebe die jeweilige Position in der Konsole aus.

## Übung 4
Du hast folgenden Satz:
```
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
```
Zähle alle E-Buchstaben, S-Buchstaben und L-Buchstaben in diesem Satz, gib diese anschließend per Konsole aus.

## Übung 5
Du hast folgenden Satz:
```
Lorem ipsum dolor sit amet consetetur sadipscing elitr sed diam voluptua.
```
Nutze die split()-Funktion, um in einer Liste alle Einzelnen Wörter zu speichern und gib diese in der Konsole aus. 

## Übung 6
Du hast den Satz:

```
lorem ipsum dolor sit amet consetetur sadipscing elitr sed diam voluptua.
```
Gib Ihn in einer Print-Funktion aus, ändere hierbei jeden kleingeschriebenen Buchstaben mit einem Großgeschriebenen Buchstaben und drehe diesen zuvor um.

Die Ausgabe sollte so aussehen:
".AUTPULOV MAID DES RTILE GNICSPIDAS RUTETESNOC TEMA TIS ROLOD MUSPI MEROL"

