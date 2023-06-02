Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'Avinash'
'Avinash'
>>> print('Avinash')
Avinash
>>> print('AVINASH'S LAPTOPS')
      
SyntaxError: invalid syntax
>>> print("avinash's laptops")
avinash's laptops
>>> print('avinash "laptop"')
avinash "laptop"
>>> print('avinash's "laptop"')
      
SyntaxError: invalid syntax
>>> print('avinash\'s "laptop"')
avinash's "laptop"
>>> 'avinash' + 'avinash'
'avinashavinash'
>>> 10*'avinash'
'avinashavinashavinashavinashavinashavinashavinashavinashavinashavinash'
>>> name = 'youtube'
>>> name
'youtube'
>>> name + 'rocks'
'youtuberocks'
>>> name ' rocks'
SyntaxError: invalid syntax
>>> name[0]
'y'
>>> name[-1]
'e'
>>> name[0:2]
'yo'
>>> name[1:4]
'out'
>>> name[-1:-4]
''
>>> name[3:6]
'tub'
>>> name[3:7]
'tube'
>>> 'my ' + name[3:]
'my tube'
>>> 