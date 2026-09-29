#Square of a number

num = int(input("Enter a number: "))
print("square", num*num)

#cube of a number
num = int(input("Enter a number: "))
print("cube", num*num*num)

#Largest of two numbers
x = int(input("Enter a first number: "))
y = int(input("Enter a second number"))

if x > y:
  print("Largest", x)
else:
  print("Largest", y)

#Positive or Negative
num = int(input("Enter a number: "))
if num >= 0:
  print("Positive")
else:
  print("Negative")
-------------------------------------------------------------------------------------
Enter a number: 29
square 841
Enter a number: 66
cube 287496
Enter a first number: 936697
Enter a second number947864
Largest 947864
Enter a number: 10
Positive
