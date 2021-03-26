import sys
script = sys.argv[0]
def print_usage():
    sys.exit(f'usage:python {script} pattern')
def main (argv):
    if not len (argv)==1 :
        print_usage()
    pattern = argv[0]
    for line in sys.stdin:
        if pattern in line :
            print (line.strip())
if_name_=='_main_':
    main(sys.argv[1:])
