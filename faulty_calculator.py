print("Enter 1st no.")
a=int(input())
print("Enter 2nd no.")
b=int(input())
print("InpuT operetor")
o=input()
c=a*b
d=a/b
e=a+b
f=a-b
if (o=="*" and (a==45 and b==3) or (b==45 and a==3) ):
    print(555)
elif (o=="*"):
    print(c)
elif (o=="+" and (a==56 and b==9) or(b==56 and a==9) ):
    print(77)
elif (o == "+"):
    print(e)
elif (o=="/" and a==56 and b==6 ):
    print(77)
elif (o == "/"):
    print(d)
elif (o == "-"):
    print(e)


