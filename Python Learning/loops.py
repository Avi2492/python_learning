#loops in python
#while loop
#i = 1   #intialization
#while i<=5:  #condition
 #   print("Python", i) #if we want values also
  #  i=i+1 #increment/decrement

#multiple while 
#i = 1   #intialization
#j = 1
#while i<=5:  #condition
 #   print("Python", i) #if we want values also
  #  while j<=4:
   #     print("rocks")
    #    j=j+1
    #i=i+1
#but it not goes to the statement 1
#solution of above mistake is to use end dont go new line stay on same
#i = 1
#while i<=5:
    #print("Python", end="")
 #  j = 1
    #while j<=4:
     #   print("Programming", end="")
      #  j=j+1
    #i=i+1        
    #print()

#for loop is used to print one by one in a list
#x = ['Avinash', 21, 5.4]
#x = 'Avinash' #if this is string 

#for i in [2, 6, 'paul']:
#for i in range(11, 21, 2):#diff of two
 #   print(i)
#reverse order
for i in range(20, 10, -1):
     print(i)    