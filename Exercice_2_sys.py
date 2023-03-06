import sys
import re

def process(datatxt):
    pattern = re.compile (r'[-+]?[0-9]\d*')
    with open(datatxt) as file :
        for i, line in enumerate(file):
            L = pattern.findall(line)
            print ('Line {}: {}'.format(i+1,','.join(L)))

# def main():
#     if len(sys.argv)>1:
#         process(sys.argv[1])
#     else :
#         print('Usage: python labo.py <datatxt>')
    
# if __name__ == '__main__':
#     main()

print(process('data.txt'))