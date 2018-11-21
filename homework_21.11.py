#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 19:30:55 2018

@author: anikkengjeruldsen
"""

#%%

#Excercise 1 6 2 v.2

class Student:
    name = ""
    last_name = ""
    age = 0
    master = ""
    
    def __init__(self, name, last_name, age, master):
        self.name = name
        self.last_name= last_name
        self.age = age
        self.master = master
    
    def print_student(self):
        str1 = self.name+ ' ' +self.last_name+' is a '+str(self.age)+' year old student of the ' +self.master+' master program'
        print(str1)

li = []  
s1 = ["Alejandro", "Meneses", 27, "MDBI"]
li.append(s1)
s2 = ["Agata", "Kaczmarek", 31,"MDBI"]
li.append(s2)
s3 = ["Anastasia", "Lasunina", 25, "MDBI"]
li.append(s3)
s4 = ["Anikken", "Gjeruldsen", 27, "MDBI"]
li.append(s4)
s5 = ["Candela", "Noya", 24, "MDBI"]
li.append(s5)
s6 = ["Daniil", "Osipov", 21, "MDBI"]
li.append(s6)
s7 = ["David", "Barrero Gonzalez", 31, "MCSBT"]
li.append(s7)
s8 = ["Edem", "Francois", 28, "MCSBT"]
li.append(s8)
s9 = ["Eduardo", "Paraja", 23, "MDBI"]
li.append(s9)
s10 = ["Florian", "Diegruber", 25, "MCSBT"]
li.append(s10)
s11 = ["Hannah", "Oldorf", 23, "MCBT"]
li.append(s11)
s12 = ["Isabella", "Rosenthal", 27, "MDBI"]
li.append(s12)
s13 = ["Javier", "Fernandez", 24, "MCSBT"]
li.append(s13)
s14 = ["Lukas", "Hauser", 28,"MDBI"]
li.append(s14)
s15 = ["Leila", "Tazi", 27, "MCSBT"]
li.append(s15)
s16 = ["Laura", "Kageneck", 23, "MCSBT"]
li.append(s16)
s17 = ["Monica", "Alvarenga",28, "MDBI"]
li.append(s17)
s18 = ["Natalie", "Cedeno", 26, "MDBI"]
li.append(s18)
s19 = ["Octavio", "RamÃƒÂ­rez", 28, "MDBI"]
li.append(s19)
s20 = ["Tancredi", "Bernard", 21, "MCSBT"]
li.append(s20)
s21 = ["Yasmine", "Lyagoubi", 23, "MDBI"]
li.append(s21)
s22 = ["Arthur", "Maroquene-Froissart",23, "MCSBT"]
li.append(s22)
s23 = ["Zineb ", "Mezzour",22,"MCSBT"]
li.append(s23)
s24 = ["Felix ", "Fastrich", 23, "MDBI"]
li.append(s4)
s25 = ["Marius", "Diedrich", 23, "MDBI"]
li.append(s25)
s26 = ["Julie", "De Neys", 23, "MDBI"]
li.append(s26)
s27 = ["Thibault", "Moeyersoms",44, "MCSDBI"]
li.append(s27)

def main():
    li.append(["Anikken", "Barstad Gjeruldsen", 27, "MCSDBI"])
    for i in range(27):
        studentObject = Student(li[i][0], li[i][1], li[i][2], li[i][3])
        studentObject.print_student()
        
if __name__ == '__main__':
    main()
