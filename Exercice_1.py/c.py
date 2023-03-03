import re 

plaque = r'\d?[A-Z]{3}\d{3}||\d?\d{3}[A-Z]{3}'
p = re.compile(plaque)

print(p.match('3DZE324'))
print(p.match('ZSE345'))