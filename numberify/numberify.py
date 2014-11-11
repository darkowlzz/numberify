#!/usr/bin/env python2.7

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from sys import argv, exc_info


class Numberify():

    def __init__(self):
        pass

    def numberify_file(self, filename):
        '''Prepend each line of a file with the line number
        Argument:
        filename - name of the file to be numberified
        '''
        try:
            fd = open(filename, 'r+')
            lines = fd.readlines()
            for i in range(len(lines)):
                if lines[i][0:len(str(i+1))] != str(i+1):
                    lines[i] = str(i+1) + ' ' + lines[i]
                else:
                    print "File already numbered"
                    return False
            fd.seek(0)
            fd.writelines(lines)
            fd.close()
            return True
        except IOError as e:
            print 'I/O error({0}): {1}'.format(e.errno, e.strerror)
        except:
            print 'Unexpected error:', exc_info()[0]
            raise

    def numberify_data(self, source, start=1):
        '''Return a dictionary with numberified data
        Arguments:
        source -- source of data(filename or a list)
        start  -- starting index of numbering
        '''
        if type(source) is str:
            try:
                fd = open(source, 'r+')
                data = fd.readlines()
                for index, item in enumerate(data):
                    data[index] = item.strip('\n')
                fd.close()
            except IOError as e:
                print 'I/O error({0}): {1}'.format(e.errno, e.strerror)
                return False
        elif type(source) is list:
            data = source
        else:
            print 'Data error. Pass a filename or a list'
            return False
        return dict(list(enumerate(data, start)))


if __name__ == '__main__':
    if len(argv) == 2:
        filename = argv[1]
        nfy = Numberify()
        nfy.numberify_file(filename)
    else:
        print 'Usage: numberify <filename>'
