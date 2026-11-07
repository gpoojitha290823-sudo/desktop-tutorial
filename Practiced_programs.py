#write a program to check whether a given character is an alphabet or not
#write a program to check whether a number is even or odd. If it is even, print "Even number"; otherwise, print "odd number"
#write a program to calculate a student's grade based on marks
#write a program to print the multiplication table of a number entered by the user



chr = input("enter chr: ")

if chr >= 'a' and chr <= 'z' or chr >= 'A' and chr <= 'Z':
  print(chr,"is alphabet")
else:
  print(chr,"is not alphabet")

for i in range(1,51):
  if i % 2 == 0:
    print(i)

num = int(input("Enter a number: "))

if num % 2 == 0:
  print("Even number")
else:
  print("Odd number")

marks = 25

if marks >= 90:
  print("Grade A")
elif marks >= 89:
  print("Grade B")
elif marks >= 79:
  print("Grade C")
elif marks >= 49:
  print("Grade D")
else:
  print("Fail")

num = int(input("Enter a number: "))

for i in range(1,11):
  print(num,'x',i,'=',num*i)
----------------------------------------------------------------------
enter chr: p
p is alphabet
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
Enter a number: 23
Odd number
Fail
Enter a number: 12
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120
