x=1
while(x<=50):
    print('cool')
    x+=19
for num in range(1,10,2):
    print(num) 
for num in "rhythm":
    print(num)
print(list(range(0,10,2)))
var=8
var3=int(input())
if var3>var:
    print('greater')
else:
    print('smaller')
#in keyword returns true false
list=[8,3,4,5]

print( 15 in list)     
if 8 in list:
     print('good') 
print('write your age') 
ag=int(input())
if ag>18:
    print('you can drivr')

elif ag<18:
    print('you cant')  
else :
    print('physical testing')

def name():
    print("shubh")

name()
def name_of(na):
    print('hello'+na)
name_of("shub")    

def add_func(m,n):
    return n+m
a=add_func(9,8)
print(a)
def print_result(a,b):
    return a*b
def return_result(m,n):
    print(m*n)
o=print_result(6,7)
d=return_result(7,6)
for i in range(4):
    for j in range(4):
        print("#",end="")
    print()  
for i in range(4):
    for j in range(i+1):
        print('@',end='')
    print()    








