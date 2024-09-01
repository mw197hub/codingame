#  https://www.codingame.com/ide/puzzle/escape-the-madness

import sys,math,re

text="Some very old keyboards lack necessary characters to program in C, such as ??=, ??', ??(??), ??! and ??-."
text="\U00000048e\U0000006C\U0000006c\x6F \x77o\rl\u0064!"

print(type(text),file=sys.stderr)

'''
step1={"??=":"#","??/":"\\","??'":"^","??(":"[","??)":"]","??!":"|","??-":"~"}
# step2:  
step3={'&amp;':'&','&lt;':'<','&gt;':'>','&bsol;':'\\'}

ausgabe=""
pos=0
while True:    
# print(text[pos:pos+3])
    if text[pos:pos+3] in step1:
        ausgabe+=step1[text[pos:pos+3]]
        pos+=3
    else:
        ausgabe+=text[pos]
        pos+=1
    if pos >= len(text):
        break

text=ausgabe
#print(text,file=sys.stderr)
ausgabe=""
pos=0
while True:
    if text[pos] == "\\":        
        if text[pos:pos+2] == "\\x":
            ausgabe+= text[pos:pos+4].encode("ascii",'replace')
            pos+=4
        elif text[pos:pos+2] == "\\u":
            ausgabe+= text[pos:pos+6].encode("ascii",'replace')
            pos+=6
        elif text[pos:pos+2] == "\\U":
            ausgabe+= text[pos:pos+10].encode("ascii",'replace')
            pos+=10
        else:
            ausgabe+=text[pos+1]
            pos+=2

    else:
        ausgabe+=text[pos]
        pos+=1
    if pos >= len(text):
        break

print(ausgabe)
'''



step1 = {'=': '#', '/': '\\', "'": '^', '(': '[', ')': ']', '!': '|', '-': '~'}
step3 = {'amp': '&', 'lt': '<', 'gt': '>', 'bsol': '\\'}

text = re.sub(
    r'\?\?([' + re.escape(''.join(step1)) + '])', 
    lambda a: step1[a.group(1)],
    text,
)
print(text,file=sys.stderr)
text = re.sub(
    r'\\(?:x([0-9a-fA-F]{2})|u([0-9a-fA-F]{4})|U([0-9a-fA-F]{8})|(.))',
    lambda t: t.group(4) if t.group(4) else chr(int(t.group(1) or t.group(2) or t.group(3), 16)),
    text
)
print(text,file=sys.stderr)
text = re.sub(
    r'&(?:#([0-9]+)|(' + '|'.join(map(re.escape, step3)) + '));',
    lambda c: chr(int(c.group(1))) if c.group(1) else step3[c.group(2)],
    text,
)

print(text)