print("Day 2  python basic :")
dict1={"name":"preeti","age":2}
print(dict1)
# dict2={,}
# print(type(dict))  this give syntax error 
dict3={}
print(type(dict3))
# dictionary methods
print(dict1.keys())
print(dict1.values())
print(dict1.get("name"))

print(print("hello"))        # ouptut hello none dega
print(True+True+False)        # output 2 dega

# print="save krega but print nhi krega"
# print(print) error dega

# print="456" # jupyter notebook  m chl jayega ye 

print(dict1.items())

dict1['work']='jaipur' # add new value 
print(dict1)

dict1.update({"name":"komal"})      # update name value in dict
print((dict1))

dict1.update({"naam":"komal"})
print(dict1)

a,b,c,d=1,2,3,4
print(type(a))     #this is int datatype

e=1,2,3,4,5
print(type(e))     # this is tuple datatype

# arithmetic operators

# 1. ADDITION OPERATOR
a,b=10,20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)

#comparison operator

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# assignement operator
# x=5
# print(x)
# print(x+=5)
# print(x-=3)
# print(x*=3)
# print(x/=3)
# print(x%=3)
# print(x//=3)


# bitwise operator 

print(a&b)
print(a|b)
print(a^b)

# identity operator 

print(a is b)
print(a is not b)

# membership operator

f=[1,2,3]
print(2 in f)
print(2 not in f)

# conditional statement 

age=15
if (age>18):
    print("jao vaote dalo")
elif(age==18):
    print("wait for vote")
else:
    print("nhi tum vote dalne mt jao")

num=20
if (num%2==0):
    print("even")
else:
    print("odd")

# marks= int(input("enter marks "))
# if marks>90:
#     print("grade A")
# elif  80<marks<79:
#     print("B")
# else:
#     print("fail")

# looping statement 

for i in range(10):
    print(i)

lst=[1,2,3,4,5]
for i in lst:
    print(i*2)

dictt={"naam":"koamll","age":"30"}
for i in dictt.keys():
    print(i)

for i in dictt.items():
    print(i)

for i in dictt.values():
    print(i)

for i in range(10):
    print(i)
    if i==3:
        break 

for i in range(10):
    
    if i==3:
        continue
    print(i) 

i=0
while i<=5:
    print(i)
    i+=1

# function 

