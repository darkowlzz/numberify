Numberify
=========

.. image:: https://badge.fury.io/py/numberify.png
    :target: http://badge.fury.io/py/numberify
    
.. image:: https://travis-ci.org/darkowlzz/numberify.svg?branch=master
    :target: https://travis-ci.org/darkowlzz/numberify

.. image:: https://coveralls.io/repos/darkowlzz/numberify/badge.png
    :target: https://coveralls.io/r/darkowlzz/numberify

Add line number to file, create a numbered dictionary object of a list and import numbered dictionary from a file list.

Installation
------------

The script is `available on PyPI`_. To install with pip::

  pip install numberify

Usage
-----

To use the script in command line::

  numberify <filename>
  
To use as a python package:

.. code-block:: pycon

    >> from numberify.numberify import Numberify
    >> nfy = Numberify()
    >> nfy.numberify_data(['foo', 'bar'])
    {1: 'foo', 2: 'bar'}
    >> nfy.numberify_data(['foo', 'bar'], start=55)
    {55: 'foo', 56: 'bar'}
    
Let a file afile.txt contain:

.. code-block::

    milk
    potatoes
    biscuits
    sugar
    
Import the file data numberifies as:

.. code-block:: pycon

    ...
    >> nfy.numberify_data('afile.txt')
    {1: 'milk', 2: 'potatoes', 3: 'biscuits', 4: 'sugar'}
    >> nfy.numberify_data('afile.txt', start=15)
    {15: 'milk', 16: 'potatoes', 17: 'biscuits', 18: 'sugar'}
    
To numberify the whole file (apply changes to the file):

.. code-block:: pycon

    ...
    >> nfy.numberify_file('filename')

Tests
-----

Run test::

  python setup.py nosetests
  
Docs
----

For detailed docs of the package use python's help utility.

License
-------

This project is released under a `GPL License`_.

.. _GPL License: http://www.gnu.org/licenses/
.. _available on PyPI: http://pypi.python.org/pypi/numberify
