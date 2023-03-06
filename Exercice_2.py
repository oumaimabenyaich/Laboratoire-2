import sys 
import re 

with open('data.txt') as file :
    lignes = file.readlines()

for line in lignes : 
    a = line.split()
    print(a)
    