from shutil import copyfile
from os import remove, path
from numberify.numberify import Numberify

this_dir, this_filename = path.split(__file__)
file1 = path.join(this_dir, 'foo.list')
file2 = path.join(this_dir, 'bar.list')
testData = ['pen', 'ruler', 'paper', 'ink']


def test_numberify_file():
    '''testing numberify_file'''
    num = Numberify()
    copyfile(file1, file2)
    result = num.numberify_file(file2)
    assert result is True
    result = num.numberify_file(file2)
    assert result is False
    fd = open(file2, 'r')
    lines = fd.readlines()
    length = len(lines)
    assert '1' in lines[0]
    assert str(length) in lines[length - 1]
    remove(file2)


def test_numberify_data():
    '''testing numberify_data'''
    num = Numberify()
    result1 = num.numberify_data(testData)
    assert result1[1] == 'pen'
    assert result1[4] == 'ink'
    result2 = num.numberify_data(file1)
    assert result2[1] == 'balbasaur'
    assert result2[6] == 'pidgeotto'
    result3 = num.numberify_data('notexistingfile')
    assert result3 is False
    result4 = num.numberify_data({1: 'foo'})
    assert result4 is False
