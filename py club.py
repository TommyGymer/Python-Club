# Getting started
## Basic functions
# print()

# input()

# ### Use of the basic functions
# print(input(": "))

# ## Variables
# a = 5
# b = "string"
# c = False

# print(a)
# d = input(f"{b}: ")

# ## Branching
# if c:
#     print(d)
# else:
#     print(b)

# ## Reassignment
# c = True

# if c:
#     print(d)
# else:
#     print(b)

# ## Looping
# for i in range(0, 10):
#     print(a)

# j = 0
# while j < 10:
#     print(b)
#     j += 1

# ### Inline loop
# a = [i for i in range(0, 10)]
# print(a)

# print(chr(65))

a = "stringz"

for i in a:
    n = ord(i)
    n += 1
    if n >= 123:
        n -= 26
    print(chr(n))

#file reading and writing