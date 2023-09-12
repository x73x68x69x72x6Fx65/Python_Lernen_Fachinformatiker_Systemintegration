def ist_pangramm(text):
    #Erstelle Variable mit allen Möglichkeiten a-z
    possibleChars = "abcdefghijklmnopqrstuvwxyz"
    #loope durch jeden Buchstaben 
    for char in possibleChars:
        #checke ob der buchstabe nicht im text vorkommt
        if char not in str(text).lower():
            return False
    return True

print("===================Pangramm-Checker======================\n\n")
print("Gib den Text ein, welcher Überprüft werden soll: \n")
text = input("")
print("\n")
print(" Der gegebene Text: \n", str(text), "\n", f"Pangramm: {ist_pangramm(text)}\n")

# Beispiel Pangramm:
#
# How quickly daft jumping zebras vex.
# Sphinx of black quartz, judge my vow.
# Glib jocks quiz nymph to vex dwarf.
