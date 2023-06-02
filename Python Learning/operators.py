Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #operators in python
>>> x = 2
>>> y = 3
>>> x+y
5
>>> x-y
-1
>>> x*y
6
>>> x/y
0.6666666666666666
>>> #assignment operator
>>> x = x+2
>>> x
4
>>> x+=2
>>> x
6
>>> x-=2
>>> x
4
>>> x*=2
>>> x
8
>>> a, b = 5, 6
>>> a
5
>>> b
6
>>> #assign the values in one line
>>> #unary operator
>>> n = 7
>>> n
7
>>> -n
-7
>>> n
7
>>> n = -n
>>> n
-7
>>> #relational operator
>>> #compareision
>>> a <b
True
>>> a>b
False
>>> a == b
False
>>> a = 6
>>> a
6
>>> a == b
True
>>> a <= b
True
>>> a >= b
True
>>> a != b
False
>>> b = 7
>>> b
7
>>> a !=b
True
>>> #logical operators
>>> #and, or, not
>>> a = 5
>>> b = 4
>>> #check both
>>> a <8 and b<5
True
>>> a<8 and b<2
False
>>> #if both true in and case then it true
>>>  a < 8 or b < 2
 
SyntaxError: unexpected indent
>>> a<8 or b<2
True
>>> x = true
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    x = true
NameError: name 'true' is not defined
>>> x = True
>>> x
True
>>> not x
False
>>> x = not x
>>> x
False
>>> 