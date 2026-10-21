#if statement
#Check positive number
number = int(input("Enter value: " ))
if  number >  0:
  print('Positive')


#check voting  eligibility
age =  int(input("Enter  your age: "))
if age >= 18:
  print('Eligible for vote')
  

marks = int(input("Enter your  marks: "))
attendence = int(input("Enter your attendence percentage: "))
if marks >=35 and attendence >75:
  print("Eligible for exam")
  

number = int(input("Enter a number: ")) 
if number % 2 == 0:
  print('Even number')
  

#Check whether a person is an adult
age =  int(input("Enter your age: "))
if age > 18:
  print('You are an adult')


age = int(input("Enter age: "))
if age > 18:
  print('Eligible for driving licence')
-------------------------------------------------------------------------------
Enter value: 29
Positive
Enter  your age: 42
Eligible for vote
Enter your  marks: 66
Enter your attendence percentage: 98
Eligible for exam
Enter a number: 80
Even number
Enter your age: 24
You are an adult
Enter age: 20
Eligible for driving licence
