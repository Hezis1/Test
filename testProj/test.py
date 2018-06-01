import sys, os

def main():

    try:

        strName = []
        for st in sys.argv [ 1 : ]:
        
            strName.append(st)

        print ('[%s]' % ', '.join(map(str, strName)))
        
    except Exception as e:

        print (e)
        sys.exit(-1)

if (__name__ == "__main__"):

    main()