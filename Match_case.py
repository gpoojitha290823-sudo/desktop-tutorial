#Matching a number
a = int(input("Enter a number: "))

match a:
  case 1:
    print('You selected 1')
  case 2:
    print('You selected 2')
  case 3:
    print('You selected 3')
  case _:
    print('Invalid number')

#Matching traffic signal
signal_colour = input("Enter traffic signal colour: ")

match signal_colour:
  case 'red':
    print("stop")
  case 'yellow':
    print("wait for a while")
  case 'green':
    print("go")
  case _:
    print("Invalid signal colour")


#Matching a day
day = int(input("Enter a day (1-7): "))

match day:
  case 1:
    print('Monday')
  case 2:
    print('Tuesday')
  case 3:
    print('Wednesday')
  case 4:
    print('Thursday')
  case 5:
    print('Friday')
  case 6: 
    print('Saturday')
  case 7:
    print('Sunday')
  case _:
    print('Invalid day')
    
