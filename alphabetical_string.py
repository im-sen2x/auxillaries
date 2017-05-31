"""Shows the longest sequence of strings that are in alphabetical order in a given string"""
"""v1.0 only deals with continuous strings"""

s= "adgodotidgkmdlkmkfdhmorhrop"

prev = s[0]
composition = ""
most = ""

for letter in s:
    if prev <= letter: 
        composition += letter
        prev = letter
        if(len(composition) > len(most)):
            most = composition
    else:
        composition = letter
        prev = letter

print(most)
