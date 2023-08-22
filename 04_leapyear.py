print("Please enter a year.")
year = input()

if int(year) % 400 == 0:
    print("This is a leap year.")
elif int(year) % 100 == 0:
   print("This is not a leap year.")
else:
    if int(year) % 4 == 0:
      print("This is a leap year.")
    else:
      print("This is not a leap year.")