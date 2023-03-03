import re

volume = r'[A-Z]:\\'
v = re.compile(volume)

print(v.match('C:\\'))
print(v.match('c:\\'))
