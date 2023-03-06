import re 

def main():
    pattern = re.compile(r'(?P<protocol>[a-z]+)://(?P<domain>[^/]+)/(?P<path>.*)')
    res = pattern.match('https://www.perdu.com/yop')
    print(res.group('protocol'))
    print(res.group('domain'))
    print(res.group('path'))


if __name__ == '__main__':
    main()