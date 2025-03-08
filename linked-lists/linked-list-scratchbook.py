###[Stack overflow question](https://stackoverflow.com/questions/3106689/pointers-in-python)a = [0]

# pointers could give behavior like this, but python doesn't have a good way to do that
# a = 1
# b = a
# a = 2
# b == 2
# # in actuality, b != 2 :(

# something reminiscent of pointers
# b = a
# a[0] = 2
# print(f"a[0]: {a[0]}, b[0]: {b[0]}")
# # a == b

# b = (1, 0)
# b = a
# a = (2, 0)
# print(f"a[0]: {a[0]}, b[0]: {b[0]}")

###########################################################################

###[Real Python](https://realpython.com/pointers-in-python/)
#### Mutable and immutable objects

# tuple1 = (0, 1, 2, 3)
# tuple1[0] = 4
# print(tuple1)
#
# # Output:
# # Traceback (most recent call last):
# # File "C:\Users\bergc\Projects\datastructures-practice\linked-lists\linked-list-scratchbook.py", line 27, in <module>
# # tuple1[0] = 4
# # ~~~~~~^^^
# # TypeError: 'tuple' object does not support item assignment

# GPT's method for differentiating mutable and immutable objects
#these two IDs are different because ints are immutable, so the object 'a' was replaced
# a = 0
# print(id(a))
# a+=1
# print(id(a))

#these two IDs are equal because the object was modified not replaced
# a = [0]
# print(id(a))
# a[0]+=1
# print(id(a))

#This ID will be the same every time I run this program because 0 has a constant unique ID.
# a = 0
# print(id(a))

#These have different IDs shows they don't use constant IDs. I don't think it would make sense for mutable objects to
#use constant IDs as the entire point of mutable objects is that they have their own memory space that can be modified.
# a = [0]
# print(id(a))
# b = [0]
# print(id(b))

#this isn't guaranteed to give the same id to give the same ID both times, but it usually does because the environment
#isn't changing between assignments. However, if you run the program multiple times, you will see different IDs
# a = 999999799
# print(id(a))
#
# del a
#
# a = 999999799
# print(id(a))

#programiz says the id of 0.0 and a=0.0 should be different, but they're not. This leads me to believe id values have
#some non-deterministic behavior. My experience troubleshooting segmentation faults in C tells me that memory addresses
#assignment is a very complex process, and as IDs appear to be directly associated with memory space, understanding the
#ID assignment of non-constant IDs is likely a waste of time for something as basic as determining whether an object is
#mutable or not
# print(id(5))
# a = 5
# print(id(a))
#
# print(id(0.0))
# a=0.0
# print(id(a))