#Check whether a number positive, negative or zero
num = int(input("Enter a number: "))
if num  > 0:
  print('positive')
elif num  < 0:
  print('negative')
else:
  print('zero') 


#check student grade
marks = int(input("Enter your marks: "))
if marks >= 90:
  print('A grade')
elif marks >= 75:
  print('B grade')
elif marks >= 50:
  print('C grade')
elif marks >= 35:
  print('D grade')
else:
  print('zero')


#check even or odd or zero
num = int(input("Enter a number: "))
if num == 0:
  print('zero')
elif num % 2 == 0:
  print('even number')
else:
  print('odd number')
----------------------------------------------------
Enter a number: -48
negative
Enter your marks: 56
C grade
Enter a number: 75
odd number
