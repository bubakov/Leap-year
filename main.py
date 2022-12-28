# loop 
while True:
# user input into int
  year = int(input("Which year do you want to check? "))

# leap year is divisible by 4 and not by 100
  if year % 4 == 0:
    # if it is divisible by 100, it has to be divisible by 400
      if year % 100 != 0 :
          print("Leap year.")
      elif year % 400 == 0:
          print("Leap year.")
  # if above conditions are not true, it is not a leap year
  else:
    print("Not leap year.")