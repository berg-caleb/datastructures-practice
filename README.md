I want to create a bunch of the simple, most common data structures from scratch in various programing languages. This is a project I did in C++ in my intro to CS 2 class at UMD, and I think it's a great way to become more familiar with different languages and their quirks. Because the main goal of this project is to learn major features of different languages, I will be allowing my study to wander to include concepts I see repeated in multiple places, even when they might not be directly applicable to the structure I'm working on. Let's start with Python.

# [Lists](https://www.geeksforgeeks.org/python-lists/)

While lists are simple enough that I won't try to recreate them in Python, they are certainly worth talking about. Lists are Python's alternative to arrays. They are dynamicly sized, and may contain mixed types because it (usually, but maybe not always) "stores references at contiguous locations and it's actual items maybe stored at different locations" (I'm sure mixed types will never get confusing 🙄).

![pythonlist.webp](assets/python-list.webp?t=1740768088261)[geeksforgeeks.org/python-lists](https://www.geeksforgeeks.org/python-lists/)

# Linked Lists

A single node in a linked list has two parts: a reference to the data stored by that node and a pointer to the next node. To re-create a linked list, first I'll need to understand Python pointers. I know pointers don't exist in Python, but I started this project without thinking everything through because I just needed to learn **something**. So let's learn about Python pointers - or the lack thereof.

## Pointers in Python?

### [Stack overflow question](https://stackoverflow.com/questions/3106689/pointers-in-python)

Searching for information about Python pointers led me to this stack overflow question, which I found interesting. While it confirms what I already knew about Python being a pointerless (but not pointless 😆) language, it also points out an interesting situation where the way Python references objects (specifically mutable objects) provides **something reminiscent of pointers**. I think it seems a little inconsistent that this happens. After all, if objA = objB assigned the memory objB references to A, then the original instance should act the same way as ints are also objects. So I asked GPT for some clarification on why there's a difference, and it told me that it's because ints are immutable whereas lists are mutable. Immutable objects are copied by '=', while mutable objects are assigned. To test this a little, I used tuples, a more complex immutable object type. This behavior seems to be consistent. When an object is immutable, operations that change its value actually create a new object with this new value and discard the old object.

---

### [Real Python](https://realpython.com/pointers-in-python/)

Next, I'm checking out this website, which talks a little more about **why** pointers don't exist in Python. It also claims to offer a way to simulate them, and a package   **ctypes** that lets me use Python's inner workings of C to use real pointers.

#### Mutable and immutable objects

Interestingly, the first thing this article talks about is **mutable and immutable objects**. Clearly this is an important distinction, however recognizing whether an object is mutable or not isn't intuative to me. So I'd like to investigate consistent ways to differentiate the two. One option that I [found](https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/) involves simply trying to modify the object in some way. This should give a Type Error. However this feels like a bad idea for a few reasons. First errors may vary between different objects, packages, and code styles. And secondly, this just isn't consistent. While modifying an element of a tuple gives a TypeError as shown, modifying an int, float, or string doesn't despite each being immutable. This is because, as previously described, the objects are simply being discarded and replaced by a new object with the correct value. Finding information on how to idenify whether an arbitrary object is mutable or not has proved mildly challenging. Many guides and forum posts refer to specific object types, and fail to talk about more general cases. After this slight difficulty I checked with GPT looking for advice on what types of things I should be searching for.

#### id()

GPT showed me the id() funciton and how I could use it to determine if an object was stored in the same location at two different points in time. I thought this was quite promising, and decided to look into it further. [W3schools](https://www.w3schools.com/python/ref_func_id.asp) mentions that some objects have constant unique IDs (e.g. integers -5 to 256). While I have a few guesses as to what this may mean, I did some troubleshooting on this to try and things that standout, however I had quite a difficult time as IDs outside of the constant unique IDs behaved very unpredictably, often (but not always) remaining the same when I expected them to change. This is likely just that these IDs are not guaranteed to be the same, but could be.

TODO do a couple examples with mutable objects and show that modifying a mutable object does not change the id.


TODO:

* [ ]  Investigate Python pointers until I find something I think might work for a linked list
* [ ]  Figure out how Python linked lists work, implement some basic functionality, and write tests for them
* [ ]  Design my own linked list objects



future things that look cool

new hobby language pointerless: https://ptls.dev/docs.html
