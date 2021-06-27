#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 23:00:46 2021

@author: madhusharma
"""

message = "Hello madhu"
print(message)

message = 'madhu \'s madhu'

print(message)

m3 = "madhu's madhu"
print(m3)


m4 = """ my name is madhu 
I am a good girl"""
print(m4)

print(len(m4))

print(m4[0:5])

# slicing 
print(m4[:5])
print(m4[5:])

# count

print(message.count('m'))


# find = returns index if the word or character exists else it will return -1 

print(message.find('l'))

# replace one word with another

print(message.replace('madhu', 'Tinku'))

# Concatenation

message = "Hello "+" "+"Tinku"+" "+"Sweety"+" "+"Bittu"

print(message)

# formatted string
greeting = "Hello "
name = "Prashant "

message = '{},{}. Welcome'.format(greeting , name)

message = f'{greeting },{name.upper()}. Welcome'
print(message)

# all methods and attributes available with this variabele
print(dir(name))

# To see details of the function use help 
print(help(str.lower))