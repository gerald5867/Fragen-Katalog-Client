file = "C:/Users/gerald.fischer/Desktop/Fragen Katalog Client/Theorien pdagogischer Handlungsfelder.txt"
lineNumber = 0
with open(file) as f:
	for line in f:
		lineNumber += 1
		splittedLine = line.split('=')
		if len(splittedLine) != 3:
			print "Fehler in der Frage "+splittedLine[0]+" Zeile :  "+str(lineNumber)+" es fehlen '='!!!!"
			continue
		if splittedLine[0] == "":
			print "Fehler in der Frage auf Zeile : "+str(lineNumber) +" die Frage ist leer!"
		if splittedLine[1] == "":
			print "Fehler in der Frage auf Zeile : "+str(lineNumber) +" die Antwortmoeglichkeiten sind leer!"
		if splittedLine[2] == "":
			print "Fehler in der Frage auf Zeile : "+str(lineNumber) +" die richtigen Antworten sind leer!"
			