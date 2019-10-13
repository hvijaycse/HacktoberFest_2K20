# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 09:24:14 2019

@author: PRASHANT
"""

a=input("Enter a string: ")
s=a.lower()
s1=set("aeiou")
vowelcount=0
for j in s:
    if j in s1:
        vowelcount+=1
print("Number of vowels:",vowelcount)


