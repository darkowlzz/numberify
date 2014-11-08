from shutil import copyfile
from os import remove
from numberify.numberify import numberify

file1 = 'test/foo.list'
file2 = 'test/bar.list'


def test():
    '''testing numberify'''
    copyfile(file1, file2)
    numberify(file2)
    fd = open(file2, 'r')
    lines = fd.readlines()
    length = len(lines)
    assert '1' in lines[0]
    assert str(length) in lines[length - 1]
    remove(file2)
