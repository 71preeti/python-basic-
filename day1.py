print("komal jii heyy")
a=3
print(type(a))
str="   python    is     a     easy language   "
print(str)
print(str[0])           #string indexing or slicing
print(str[1:])
print(str[::-1])
print(str[-1])
print(str[-4:-1])
print(str[-1:-4]) # not give any element 

# string method functions

print(str.upper())
print(str.lower())
print(str.split()) # break whole string into individual elements into list 
print(str.strip()) # used for remove extra spaces from start and endnot from middle
print(str.splitlines()) # break whole string into one elements 
print(str.replace("easy","12345"))
print(str.find("python")) # give index of first p letter of python intial give 0
# string concatenation 
str1="hy i am learning python in my crt college"
print(str+str1) # by default it don't give space 
print (str+"123"+str1)
# str1[0]="hello"           # that show immutable nature of string
print (str,"123",str1)            # it give space by default
# tuples = immutable or unchangeable made by ()
tup=(1,2.3,"python",True)
print(tup)
print(tup[2])
print(tup[0])
print(tup[3])
# tup[0]="python"  # that show immutable nature of string
print(tup)

print(tup*3)
print(tup.count("python"))

# list = mutable ,changeable
lst=[1,2,3,2.4,"hello",True]
print(lst)
print(type(lst))
print(lst[-1:-3])
print(lst[0:3])
print(lst[-3:-5])      # do research  on this 
lst[2]="heeeeeeee"     # that shows the mutable nature of list
print(lst)

# list methods 
lst.append("append at the end not give index only element give") # only give eleement
print(lst)
lst.insert(2,"insert at 2 index")  # give index the element
print(lst)
lst1=[1,2,1,1,2,2,2]
lst1.remove(1)       # remove element first occurence of 1
print(lst1)
lst.pop()
print(lst)
lst1.sort()
print(lst1)
lst1.reverse()
print(lst1)