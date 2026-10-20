#Identity operators
a = [1, 2, 3]
b = a
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is  b)
print(a == b)

x = 10
y = 10
print(x is y)
print(x == y)

a = None
print(a is None)

m = [10, 20,30]
n = [30, 40, 50]
print(m is not n)

#checks whether both variables refer to the same object
#checks whether the values are equal
-------------------------------------------------------------------------------------------
True
False
True
True
True
True
True
