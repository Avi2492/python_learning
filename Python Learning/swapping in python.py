Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #swap 2 no. in python
>>> a = 5
>>> b = 6
>>> a = b
>>> b = a
>>> print(a)
6
>>> print(b)
6
>>> temp = a
>>> a = b
>>> b = temp
>>> print(a)
6
>>> print(b)
6
>>> #formula
>>> a = 4
>>> b = 3
>>> a = a+b
>>> b = a-b
>>> a = a-b
>>> print(a)
3
>>> print(b)
4
>>> #xor
>>> #not waste extra bits
>>> a=a^b
>>> b=a^b
>>> a=a^b
>>> print(a)
4
>>> print(b)
3
>>> #another way special in python not works in multiple lines but in single line
>>> a, b = b, a
>>> print(a)
3
>>> print(b)
4
>>> 