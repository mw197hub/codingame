from re import A
import sys
import math

'''

English is sometimes an annoying language. 
With this, we often describe nouns, i.e., person, place, or thing, with adjectives, 
or descriptive words. For instance, 
The dog is brown. We can also say Joe is smart. 
We can combine this with a conjunction to get a phrase like, "John is a cool and smart person." 
However, we often see sentences like, "John is a cool person and smart person." 
This is redundant, and can be shortened to just "John is a cool and smart person."
Write a program that condenses sentences like this. In other words, 
given a sentence of the form, "X ... Y Z and W Z", rewrite it to say "X ... Y and W Z".

'''

a = "John is a cool person".split(" ")
b = "John is a smart person".split(" ")
o = []

for i in range(len(a)):
    if a[i] == b[i]:
        o+=(a[i]),
    else:
        o+=(a[i]),
        o+=("and"),
        o+=(b[i]),
        o+=("person."),
        break
print(*o)