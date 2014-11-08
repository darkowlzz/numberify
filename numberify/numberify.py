#!/usr/bin/env python

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
