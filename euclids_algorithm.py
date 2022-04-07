def euclid(x,y):
    r = x%y

    if(r==0):
        return y
    else:
        return euclid(y,r)

num1 = int(input('enter first number -> '))
num2 = int(input('enter second number -> '))

x = max(num1,num2)
y = min(num1,num2)

print(euclid(x,y))


