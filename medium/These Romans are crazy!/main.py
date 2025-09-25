# https://www.codingame.com/ide/puzzle/these-romans-are-crazy!

import sys,math

def roman_to_decimal(roman_numeral):
    """
    Wandelt eine römische Zahl als String in eine Dezimalzahl um.
    """
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_value = 0
    prev_value = 0

    for symbol in reversed(roman_numeral):
        value = roman_map[symbol]
        if value < prev_value:
            decimal_value -= value
        else:
            decimal_value += value
        prev_value = value
    return decimal_value

def dezimal_zu_roemisch(zahl):
    """Wandelt eine Dezimalzahl in eine römische Zahl um."""
    # Liste der Dezimal-Römisch-Paare, sortiert absteigend
    werte = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    roemische_zahl = ""
    for dezimal_wert, roemisches_zeichen in werte:
        # Subtrahiere den Wert so oft wie möglich und füge das Zeichen hinzu
        while zahl >= dezimal_wert:
            roemische_zahl += roemisches_zeichen
            zahl -= dezimal_wert
            
    return roemische_zahl

rom_1="VI";rom_2="VII"

wert1=roman_to_decimal(rom_1)
wert2=roman_to_decimal(rom_2)
print(dezimal_zu_roemisch(wert1+wert2))