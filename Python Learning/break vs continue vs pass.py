#break vs continue vs pass
for i in range(5):
    if i==3:
        continue
    print("Hello", i)


for i in range(5):
    if i==3:
        break
    print("Hello", i)

def fun():
    pass #to keep empty dont know what toprint
a=5    