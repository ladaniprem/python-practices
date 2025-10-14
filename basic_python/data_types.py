# String data types

#literal assignment 

first = 'prem'
last = 'ladani'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first,str))

# Constructor function

# pizza = str("domino")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza,str))

# concatenation
# fullname = first + '' + last
# print(fullname)

# fullname += "!"
# print(fullname)

#casting a number to a string 
# decade = str(1900)
# print(type(decade))
# print(decade)

# statement = 'I like rock music from the ' + decade
# print(statement)

#multiple lines 

multiline = '''
hey,how ary you ?

I was just checking in.
                            All good ?
'''
# print(multiline)

#Escaping spacial characters

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located'
print(sentence)

#String method

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good","ok"))
print(multiline)

print(len(multiline))
multiline+= '                                    '
multiline = "            " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rsplit()))

print("")

#Bulid a men
title = 'menu'.upper()
#print(title)
print(title.center(20,'='))
#print("coffee".ljust(16,"."))
print("coffee".ljust(16,".")+ "$1".rjust(4))
print("cheesecake".ljust(16,".") + "$4".rjust(4))
print("tea".ljust(16,".")+ "$3".rjust(4))

print("")

#string Index values 

print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])


#some method return boolean data 

print(first.startswith("p"))
print(first.endswith("z"))

#boolean data type 

myvalue = True
x = bool(False)
print(type)
print(isinstance(myvalue,bool))

#numeric data types

#interger type

price = 100
best_price =  int(80)
print(type(price))
print(isinstance(best_price,int))

#float type 
gpa = 9.10
y = float(8.0)
print(type(gpa))

#complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#bulit- in function for numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa,1))

import math 

print(math.pi)
print(math.e)
print(math.log10)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Casting a string to a number

zipcode  = "360459"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data 

zip_value = int("Gujarat") 
# Traceback (most recent call last):
#   File "d:\prem\coding\code with python\data_types.py", line 146, in <module>
#     zip_value = int("Gujarat")
# ValueError: invalid literal for int() with base 10: 'Gujarat'



