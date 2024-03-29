# Grundwissen zur Python Programmierung als Fachinformatiker für Systemintegration

# Vorab solltest du dies beachten:

Dies ist nur eine kleine Zusammenfassung meines Schulunterrichts als Fachinformatiker für Systemintegration und soll dazu dienen, anderen Fachinformatikern, welche Schwierigkeiten haben, sich in der Programmierung zurechtzufinden, und Ihnen den Einstieg in die verschiedenen Themen der Python Programmierung zu erleichtern. Es kann sein, dass hierbei Dinge behandelt werden, welche nicht überall abgefragt werden, aber für das Verständnis einer Programmiersprache wichtig sind.
Um dem Rest der Grundlagen Folgen zu können solltest du die Begriffe Variable und Datentyp kennen und die verschiedenen Datentypen der Sprache Python unterscheiden können. Was es für Datentypen gibt und wie man diese unterscheidet findet du weiter unten beim Punkt **1.2 Datentypen**.
Diese sollte man einfach Auswendig lernen.


## 1. GrundBegriffe für die Programmierung

------------------------------------------------------------------------------------------------------------------------------------------------

## 1.1 Was ist eine Variable?
Eine Variable ist ein Behälter für einen Wert, wie z.B eine Zahl, auf die im späteren Verlauf zugegriffen werden soll.
Im Quelltext / Code wird jeder Variable ein eindeutiger Name zugeordnet, damit man beim lesen eines Codes schon eine 
grobe Vorahnung erhält was genau umgesetzt werden soll. Die Bennung von Variablen ist, auch wenn es teils nicht so wirkt, 
einer der wichtigsten Punkte, die man beachten sollte. Versuche daher immer den abgespeicherten Wert schon im Namen zu definieren.
Bei der Bennung von Variablen ist ebenfalls darauf zu achten, dass keine Leerzeichen im Namen vorhanden sind.

Besipiele für Bennungen von Variablen:

- Es soll die Körpergröße von einem User eingelesen werden. Dafür wird eine Variable erstellt.

$${\color{green}So \space \color{green}könnte \space \color{green}eine \space \color{green}Bennenung \space \color{green}aussehen:}$$
<p align="center">koerpergroesse_in_cm = 175</p>

$${\color{red}So \space \color{red}sollte \space \color{red}eine \space \color{red}Bennenung \space \color{red}in \space \color{red}diesem \space \color{red}Beispiel \space \color{red}nicht \space \color{red}aussehen:}$$
<p align="center">x = 175 </p>

- Es sollen die Koordinaten von einem Spieler eines MMO´s gespeichert werden. Dafür wird eine Variable erstellt und mit einem Standardwert befüllt.

$${\color{green}So \space \color{green}könnte \space \color{green}eine \space \color{green}Bennenung \space \color{green}aussehen:}$$
<p align="center"> spieler_Koordinate_X = -3.662 </p>
<p align="center">spieler_Koordinate_Y = 5.8112 </p>

$${\color{red}So \space \color{red}sollte \space \color{red}eine \space \color{red}Bennenung \space \color{red}in \space \color{red}diesem \space \color{red}Beispiel \space \color{red}nicht \space \color{red}aussehen:}$$
<p align="center">d = 3.662 </p>
<p align="center">e = 5.811</p>



## 1.2 Was sind Datentypen?
Mit dem Wort Datentypen werden Daten in verschiedene Arten untereilt. Ein Datentyp bezieht sich darauf, welche Art von Wert eine Varaible hat
und welche Art von Operationen verwenden werden können, ohne Fehler zu verursachen.

In Python gibt es Folgende Datentypen:

* Integer - ganze Zahlen: Eine ganzzahl im Bereich zwischen -9,223,372,036,854,775,808 und 9,223,372,036,854,775,807 z.B -55  

* Float - Fließkommazahlen: Eine Zahl mit Kommastellen im Code dargestellt durch einen Punkt statt einem Komma. z.B 3.882

* String - Zeichenkette: Eine Zeichenkette wird durch " am Anfang und am Ende gekennzeichnet. z.B "Hallo123!?". Es können hierbei Groß- und Kleinbuchstaben, sowie Zahlen und Sonderzeichen verwendet werden.

* Boolean - boolesche Werte bestehend aus True oder False

* List - Liste: In einer Liste können mehrere Elemente / Werte untergebracht werden. Die Werte in einer Liste können jederzeit verändert werden und sind nicht an einen Datentyp gebunden. z.B liste1 = [True, "StringValue", 22, 5.775]. Sollte man nun einzelne Werte daraus benötigen, so muss man von 0 Anfangen zu zählen, da eine Liste immer bei 0 beginnt. Der Wert 22 ist somit nur über Position 2 abzufragen.

* Tuple - Tupel: Eine bestimmte Art von Liste, in welcher alle Elemente durch ein Beginnendes und ein beendendes einfaches Anführungszeichen gekennzeichnet sind. Wenn diese einmal Festgelegt wurden, können sie nicht mehr Verändert werden. z.B Pizzabelag = ('Salami', 'Paprika', 'Käse')

* None - Ein Datentyp speziell für leere Objekte. Hiermit können Variablen ohne Werte erstellt werden.


## 1.3 Wie können Berechnungen im Code durchgeführt werden?
Dies ist eine Frage dir häufig im Unterricht gefallen ist, da viele nicht verstanden haben wie Variablen in einem Code verwendet werden. 

Hierfür stellt man sich das ganze am besten wie eine Matheaufgabe vor:

Angenommen wir haben die Aufgabe 2 + 3 zu Rechnen, dann erstellen wir für die 2 und die 3 jeweils eine Variable und eine Dritte mit welcher wir das Ergebnis der Rechnung speichern.
Das ganze sieht dann wie folgt aus:

```
Ergebnis = None
additionsZahl_Eins = 2
additionsZahl_Zwei = 3
```
Um die Berechnung durchzuführen, wird schließlich der entsprechende Rechenoperator verwendet. Die Berechnung wird auf Grundlage der gewählten Variablennamen durchgeführt. Sie sind eine Art verweis auf die dort gespeicherten Werte.
```
Ergebnis = additionsZahl_Eins + additionsZahl_Zwei
```
Damit erhält die Variable Ergebnis den Wert 5, welcher sich durch 2 + 3 ergibt.


## 2. Was sind Methoden / Funktionen?
Mit Funktionen lassen sich unter Python Teilbereiche eines Programms zusammenfassen. Damit kann der Code strukturiert gestaletet werden und einfacher von anderen Personen gelesen werden. Zudem wird für wiederkehrende Aufgaben eine redundanz des Codes erspart.
Eine Methode kennzeichnet sich durch das Schlüsselwort *def* gefolgt von einem Namen einer geöffneten Klammer, gefolgt von den so genannten Paramtern (Übergabeparametern).
Code Beispiel:
```
def summeBilden(zahl1, zahl2, zahl3):
    return zahl1 + zahl2 + zahl3

print(summeBilden(5,7,12))
#Ausgabe 24
```
Mit *def* wird eine Methode deklariert, anschließend wird ein Name gewählt, gefolgt von einer geöffneten Klammer und den Übergabewerten. Wenn man ein Ergebnis zurückgeben möchte, wird dies über das Schlüsselwort return gemacht. Im oberen Beispiel wird dadurch 5+7+12 gerechnet und das Ergebnis direkt in der Print()-Funktion ausgegeben. 

Der Aufruf solcher Methoden erfolgt immer durch den Namen der Funktion gefolgt von den definierten Paramtern innerhalb der Klammern. Sollte man den Rückgabewert hierbei speichern wollen, so muss man dafür einfach eine Variable erstellen.

Beispiel:
```
def summeBilden(zahl1, zahl2, zahl3):
    return zahl1 + zahl2 + zahl3

summe = summeBilden(5,7,12)
print(summe)
#Ausgabe 24
```
Hierbei wird der Rückgabewert der Funktion in der Variable Summe gespeichert.


## 3. In welcher Reihenfolge sollte ich die Python-Dateien verwenden?
Beginne als Erstes mit **Variablen_Deklarationen_und_Rechenoperatoren.py** 
Darin wird ein Beispiel eines BMI-Rechners mit fixen Werten dargestellt. Hierbei kann man am besten lernen, wie man variablen deklariert, und mit Ihnen Rechnet und Ausgaben in der Konsole darstellt. 

Danach solltest du mit **Rechenoperationen_und_Schleifen.py** weiter machen. In dieser Datei werden die Grundlagen zu If-Abfragen, For-Schleifen und While-Schleifen behandelt. Diese Schleifen und If-Abfragen bilden die Grundlage für die Gesamte Programmierung und sind somit einer der Wichtigsten Punkte. Hat man dies einmal verstanden, kann man ohne Probleme alle Berufsschulaufgaben erledigen.

Anschließend kannst du dich selbst an einigen Aufgaben Versuchen. Unter der **Beispielaufgaben.md** können die Aufgabenstellungen gefunden werden. Ein Beispiellösungsweg kann jederzeit unter den **BeispielLösung_Aufgabenname.py**-Dateien angesehen werden. Diese Aufgaben helfen dabei dein Grundwissen zu festigen und zu verbessern. 


