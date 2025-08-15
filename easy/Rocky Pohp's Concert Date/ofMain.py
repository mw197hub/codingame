
def areValidFactors (a : int, b : int) -> bool :
    n = a * b
    if n == 0 :
        return False
    div = int (n ** .5)
    while n % div : div -= 1
    return div in (a, b)

def concatDate (a : int, b : int) -> str :
    return str (a*b).zfill (len ("YYYYMMDD"))

def reverseConcat (concat_date : str) -> str :
    return concat_date[:4] + '-' + concat_date[4:6] + '-' + concat_date[6:]

def isValidDate (date : str) -> bool :
    _, month, day = date.split ("-")
    return "01" <= month <= "12" and "01" <= day <= "31" 

s = "200104091"
for i in range (1, len (s)) :
    a = int (s[:i])
    b = int (s[i:])
    if areValidFactors (a, b) :
        concat_date = concatDate (a, b)
        date = reverseConcat (concat_date)
        if isValidDate (date) :
            print (date)
            break