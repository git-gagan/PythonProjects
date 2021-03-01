#Project 1
#String Interpolation or concatenation
'''
Ways of doing concatenation
1) using  +
2) using .format()
3) using F-strings (used here)
'''
name=input("Name: ")
mood=input("Mood: ")
series=input("Series: ")
Char1=input("Character1: ")
Char2=input("Character2: ")
quote=input("Quote: ")
creator=input("Creator: ")

#f-strings and escape character
madlibs=f'Welcome to the Madlibs {name}! I guess my mood is {mood}. Leave it and and let\'s talk about\
 my favourite series {series}. I loved the interaction between {Char1} and {Char2}. My favourite quote\
 till now is :-"{quote}". I will always remember this one. Thanks {creator}.\n'

print(madlibs)   

