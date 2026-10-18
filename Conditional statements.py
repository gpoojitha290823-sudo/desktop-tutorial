#Conditional operators
num = int(input("Enter a number: "))
result = 'positive' if(num>0) else 'negative'
print(result)

#Check driving licence eligibility
age = int(input("Enter your age: "))
eligibility = 'Eligible for driving licence' if(age>=18) else 'Not eligible for licence'
print(eligibility)

#Chexk whether two numbers are equal or different
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))
res = 'Equal' if(x==y) else 'Different'
print(res)

#Check whether the username matches
username = input("Enter your name: ")
result = 'Username matched' if(username=='pooja') else'Username not matched'
print(result)
--------------------------------------------------------------------------------------------------
Enter a number: 42
positive
Enter your age: 18
Eligible for driving licence
Enter x value: 29
Enter y value: 29
Equal
Enter your name: pooja
Username matched
