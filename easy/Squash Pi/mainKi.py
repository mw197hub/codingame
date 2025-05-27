#https://www.codingame.com/ide/puzzle/squash-pi


import decimal
from decimal import Decimal, getcontext
from math import factorial

def compute_pi_chudnovsky(digits):
    getcontext().prec = digits + 10  # Sicherheitszuschlag für Genauigkeit

    # Konstanten
    C = 426880 * Decimal(10005).sqrt()
    
    def chudnovsky_term(k):
        # Einzelner Summand der Chudnovsky-Reihe
        numerator = Decimal(factorial(6 * k)) * (13591409 + 545140134 * k)
        denominator = Decimal(factorial(3 * k)) * (factorial(k) ** 3) * Decimal(640320) ** (3 * k)
        return numerator / denominator

    # Schleife über die Reihen-Terme
    total = Decimal(0)
    k = 0
    term = chudnovsky_term(k)
    while term > Decimal(10) ** -(digits + 5):  # Abbruchbedingung
        total += term * (-1) ** k
        k += 1
        term = chudnovsky_term(k)

    pi = C / total
    return +pi  # Rundung anwenden

# Beispiel: 1000 Stellen berechnen
stellen = 100000
pi_decimal = compute_pi_chudnovsky(stellen)

# Ausgabe
pi_str = str(pi_decimal)[:stellen + 2]  # +2 für "3."
print(pi_str)


