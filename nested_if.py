#nested if 
#Age classification
age = int(input("Enter your age: "))

if age >= 18:
    if age >= 22:
         print('You are 22 or older')
    else:
         print("You are an adult but under 22")
else:
  print('Yor are a minor')


#Even or odd
num = int(input("Enter a number: "))

if num > 0:
  if num % 2 == 0:
    print('Even')
  else:
    print('Odd')
else:
  print('Not positive')

#Age check
age = int(input("Enter your age: "))

if age >= 13:
   if age >= 18:
     print("Adult")
   else:
     print('Teenager')
else:
  print("Child")


#Number comparison
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

if a > b:
  if a % 2 == 0:
    print("First")
  else:
    print("Second")
else:
  print("Third")
---------------------------------------------------
Enter your age: 21
You are an adult but under 22
Enter a number: -4
Not positive
Enter your age: 25
Adult
Enter a value: 56
Enter b value: 50
First
