import sys
import re

def process(data.txt):
    pattern = re.compile (r'[-+]?[1-9]\d*')
    with open('data.txt') as file :
        for i, line in enumerate(file):
            L = pattern.findall(line)
            print ('Line {}: {}'.format(i+1,','.join(L)))

def main():
    if len(sys.argv)>1:
        process(sys.argv[1])
    else :
        print('Usage: python labo.py <data.txt>')
    
if __name__ == '__main__':
    main()