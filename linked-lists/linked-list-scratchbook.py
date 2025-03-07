# Stack overflow question

# pointers could give behavior like this, but python doesn't have a good way to do that
# a = 1
# b = a
# a = 2
# b == 2
# # in actuality, b != 2 :(

# something reminiscent of pointers
# a = [0]
# b = a
# a[0] = 2
# print(f"a[0]: {a[0]}, b[0]: {b[0]}")
# # a == b

a = (1, 0)
b = a
a = (2, 0)
print(f"a[0]: {a[0]}, b[0]: {b[0]}")

###########################################################################

# RealPython.com follow along

