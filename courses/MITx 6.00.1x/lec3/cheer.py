# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:51:57 2016

@author: ericgrimson
"""

an_letters = "aefhilmnorsxAEFHILMNORSX"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
for i in range(len(word)):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a  " + char + "! " + char)
print("What does that spell?")
for _ in range(times):
    print(word, "!!!")
