Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(num)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    type(num)
NameError: name 'num' is not defined
>>> num = 2.6
>>> type(num)
<class 'float'>
>>> num = 5
>>> type(num)
<class 'int'>
>>> num = 6+9j
>>> type(num)
<class 'complex'>
>>> # convert in int
>>> a = 5.6
>>> b = int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> #int to float
>>> k = float(b)
>>> k
5.0
>>> #convert normal to complex
>>> k = 6
>>> c = complex(b, k)
>>> c
(5+6j)
>>> #bool
>>> b<k
True
>>> bool = b<k
>>> bool
True
>>> type(bool)
<class 'bool'>
>>> b>k
False
>>> #true = 1, false = 0
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined
>>> int(True)
1
>>> lst = [25, 45, 56, 67]
>>> type(lst)
<class 'list'>
>>> s = {3, 56, 78, 69}
>>> s
{56, 3, 69, 78}
>>> type(s)
<class 'set'>
>>> t = (2, 4, 5, 5)
>>> t
(2, 4, 5, 5)
>>> type(t)
<class 'tuple'>
>>> str = "avinash"
>>> st = 'a'
>>> type(st)
<class 'str'>
>>> #range
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> #all even
>>> list(range(2, 10, 2))
[2, 4, 6, 8]
>>> type(range(10))
<class 'range'>
>>> #dictionary
>>> # assign a key for every index
>>> d = {'avinash':'samsung', 'rahul':'iphone'}
>>> d.keys()
dict_keys(['avinash', 'rahul'])
>>> d.value()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    d.value()
AttributeError: 'dict' object has no attribute 'value'
>>> d.values()
dict_values(['samsung', 'iphone'])
>>> d.get('rahul')
'iphone'
>>> d.get('avinash')
'samsung'
>>> 