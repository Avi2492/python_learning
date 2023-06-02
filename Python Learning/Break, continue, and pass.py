#Break, continue, and pass
x = int(input("How many candies do you want?"))
i = 1
while i <= x:
    print("candy")
    i+=1
#if we want 100 candy and machine have only 50 then two choice first stop the transaction  
av = 5
x = int(input("How many candies do you want?"))
i = 1
while i <= x:
    if i>av:
        print("put of stock") #2nd method
        break #just come out from the block
    print("candy")
    i+=1  
print("Get Lost")  
#continue statement  
#print 1 to 100 but skipp those didvisible by 3
for i in range(1, 101):
    if i%3==0 and i%5==0: #use or also
        continue #skip the remaining statements not loop
    print(i)
print("Bye")


#pass statement i dont want print like odd value
#pass simply means we dont have code simply pass to the next statement
for i in range(1, 10):
    if(i%2!=0):
        pass
    else:
        print(i)
print("Bye")        