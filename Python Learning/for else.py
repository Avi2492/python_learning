#for else didvisvble by 5 check and print only first
nums = [10, 12, 31, 41, 71]
for num in nums:
    if num % 5 ==0:
        print(num)
        break#complusary
else:
    print("Not found")

#prime or not
num = 7
for i in range(1, num):
    if num % i == 0:
        print("not prime")
else:
    print("prime") 

