

#zeilen = int(input("Wie viele Nachkommastellen möchtest du berechnen lassen?"))
zeilen = 300000


from decimal import getcontext, Decimal
getcontext().prec = zeilen
import time

a = 1
b = 1 / Decimal(2).sqrt()
s = 1 / Decimal(4)
n = 0
counter = 1
new_time = time.time()
old_time = time.time()
answer_new = 0
answer_old = 1

print("Rechnet...:")                                        #Drucke "Rechnet...:" aus
print("")                                                   #Drucke 1 Zeile weiter unten

start = time.time()
while answer_new != answer_old:                             #Solange answer_new nicht answer_old ist, soll ... passieren
    if counter > 1:                                         #Wenn die Variabele counter größer ist als 1, dann...
        old_time = new_time                                 #Variabele old_time ist gleich die Variable new_time
        new_time = time.time()                              #Variabele new_time ist gleich der Funktion time.time()
       # print(new_time - old_time)                          #Drucke die Variable new_time minus der Variabel old_time
    answer_new = answer_old                                 #Variabele answer_new ist gleich die Variable answer_old
    counter += 1                                            #Variable counter soll einz größer werden

    A = (a + b) / 2                                         #Rechnung...
    B = Decimal(a * b).sqrt()                               #Rechnung...
    S = s - 2 ** n * (a - A) ** 2                           #Rechnung...
    answer_old = (A ** 2 / s)                               #Rechnung...

    a = A                                                   #klein a ist gleich groß A
    b = B                                                   #klein b ist gleich groß B
    s = S                                                   #klein s ist gleich groß S

    n += 1                                                  #Variable n soll einz größer werden

   # datei = open('Pi', 'w')                                 #Erstelle eine Datei namens "Pi" im Programmordnder
   # datei.write(str(answer_new))     
print(answer_new)                       #Schreibe Pi in die gerade erstellte Datei

end = time.time()                                           #Variabele end ist gleich der Funktion time.time()

print("Wurde in einer neuen Datei namens Pi Gespeichert")   #Drucke "Wurde in einer neuen Datei namens Pi Gespeichert" aus
print("")
print("Durchgänge:")
print(n)
print("")
print("Zeit:")
print(end - start)

datei = open('Pi', 'w')
datei.write(str(answer_new))

while 0 == 0:
  mach_nichts = 0
  exit(0)
