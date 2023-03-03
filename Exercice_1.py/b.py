import re

nombre = r'[+-?]\d+'
n = re.compile(nombre)

print(n.match('32'))
print(n.match('+32'))
print(n.match('232'))
print(n.match('*47'))