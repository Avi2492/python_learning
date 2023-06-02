Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = [1, 2, 3, 4]
>>> nums
[1, 2, 3, 4]
>>> nums[0]
1
>>> nums[3]
4
>>> nums[-1]
4
>>> nums[0:3]
[1, 2, 3]
>>> nums[0:]
[1, 2, 3, 4]
>>> names = ['Avinash', 'Karan', 'Janhvi']
>>> names
['Avinash', 'Karan', 'Janhvi']
>>> values = [9.7, 'Avinash', 25]
>>> values
[9.7, 'Avinash', 25]
>>> mil = [names , nums]
>>> mil
[['Avinash', 'Karan', 'Janhvi'], [1, 2, 3, 4]]
>>> nums.append(45)
>>> nums
[1, 2, 3, 4, 45]
>>> nums.clear(2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    nums.clear(2)
TypeError: list.clear() takes no arguments (1 given)
>>> nums.clear(0)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    nums.clear(0)
TypeError: list.clear() takes no arguments (1 given)
>>> nums.copy(2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    nums.copy(2)
TypeError: list.copy() takes no arguments (1 given)
>>> nums.insert(32)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    nums.insert(32)
TypeError: insert expected 2 arguments, got 1
>>> nums.insert(2, 78)
>>> nums
[1, 2, 78, 3, 4, 45]
>>> nums.remove(2)
>>> nums
[1, 78, 3, 4, 45]
>>> nums.pop(-1)
45
>>> nums
[1, 78, 3, 4]
>>> nums.pop()
4
>>> nums
[1, 78, 3]
>>> del nums[2:]
>>> nums
[1, 78]
>>>  nums.extend([25, 67, 89])
 
SyntaxError: unexpected indent
>>> nums.extend([25,34, 65, 987])
>>> nums
[1, 78, 25, 34, 65, 987]
>>> min(nums)
1
>>> max(nums)
987
>>> sum(nums)
1190
>>> mul(nums)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    mul(nums)
NameError: name 'mul' is not defined
>>> sub(nums)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    sub(nums)
NameError: name 'sub' is not defined
>>> nums.sort()
>>> nums
[1, 25, 34, 65, 78, 987]
>>> 