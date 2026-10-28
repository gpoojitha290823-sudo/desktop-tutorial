#Age checker
age = int(input("Enter your age: "))

result = 'Adult' if age >= 18 else 'Minor'
print(result)

#check even or odd
num = int(input("Enter a numer: "))
res = 'Even' if num % 2 == 0 else 'Odd'
print(res)

#check pass or fail
marks = 36
result_2 = "Pass" if marks >= 35 else "Fail"
print(result_2)

num = -12
print("Positive" if num > 0 else "Negative")
-----------------------------------------------------
Enter your age: 24
Adult
Enter a numer: 29
Odd
Pass
Negative
