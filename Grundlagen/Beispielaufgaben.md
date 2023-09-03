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
