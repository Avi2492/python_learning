Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #import math functions
>>> #square root
>>> x = sqrt(25)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x = sqrt(25)
NameError: name 'sqrt' is not defined
>>> import math
>>> x = math.sqrt(25)
>>> x
5.0
>>> x=math.sqrt(15)
>>> x
3.872983346207417
>>> print(math.floor(2.8))
2
>>> print(math.ceil(2.8))
3
>>> print(math.pow(2, 3))
8.0
>>> print(math.pi)
3.141592653589793
>>> print(math.e)
2.718281828459045
>>> m.sqrt()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    m.sqrt()
NameError: name 'm' is not defined
>>> import math as m
>>> math.sqrt(25)
5.0
>>> m.sqrt(25)
5.0
>>> #only some function import
>>> from math import sqrt, pow
>>> pow(4, 5)
1024.0
>>> help('math')

>>> 