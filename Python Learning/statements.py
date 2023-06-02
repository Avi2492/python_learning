#if else elif statements
#if statements works syntax
if True:
   print("Im right")
print("Bye") #because this is not belong to if so bye prints

#odd or even check
x = 7
r = x % 2
if r==0:
    print("even")
if r==1:    
    print("odd")  


x = 8
r = x % 2
if r==0:
    print("even")
else:    
    print("odd") 


x = 3
r = x % 2
if r==0:
    print("even")
    if x>5:    #nested if after first if check second if
        print("Great")
    else:
        print("not so great")    
else:    
    print("odd") 

#if elif statements
x = 4
if(x==1):
    print("one")
elif x==2:
    print("two")
elif x==3:
    print("three")
elif x==4:
    print("four")  
else:
    print("wrong input")                 