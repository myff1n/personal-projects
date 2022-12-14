import re

global chrName

#input name
print("What is your character's name?")

inp = input("")

inp = inp.strip().lower()

matches = re.finditer("\s+", inp)
for m in matches:
    inp = inp[:m.start()] + " " + inp[m.end():]

#  strip of spaces --> lowercase --> "comma space" --> "the space" --> remove double spaces in the middle
chrName = inp.title()

#if chrName is excessively long (36 or more characters), throw an "error"
if len(chrName) >= 36:
    print("Sorry, that name is too long.")
else:
    print("Hello, " + chrName)
