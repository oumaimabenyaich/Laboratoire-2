import re

number = r'\+[0-9]{2} [0-9]{3} [0-9]{2} [0-9]{2}'
n = re.compile(number)

pattern = r'\+\d{2} \d{3} \d{2} \d{2}'
p = re.compile(pattern)

print (n.match('+32 489 28 35 29'))
print (n.match('0489 28 35 29'))

print(p.match('+32 477 43 15 95'))