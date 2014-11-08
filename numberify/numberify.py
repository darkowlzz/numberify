from sys import argv, exc_info


def numberify(filename):
    '''Prepend each line of a file with the line number
    Argument:
    filename - name of the file to be numberified
    '''
    try:
        fd = open(filename, 'r+')
        lines = fd.readlines()
        for i in range(len(lines)):
            lines[i] = str(i+1) + ' ' + lines[i]

        fd.seek(0)
        fd.writelines(lines)
        fd.close()
        return True
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        print 'Unexpected error:', exc_info()[0]
        raise


if __name__ == '__main__':
    if len(argv) == 2:
        filename = argv[1]
        numberify(filename)
    else:
        print 'Usage: numberify <filename>'
        exit()
