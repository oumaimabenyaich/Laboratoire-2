import re 

def process(datatxt):
    pattern = re.compile(r'[-+]?[0-9]\d*')
    with open(datatxt) as file :
        for i, line in enumerate(file):
            L = pattern.findall(line)
            print ('Line {}: {}'.format(i+1,','.join(L)))

print(process('data.txt'))