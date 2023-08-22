def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5 #because 1-4 were already handled
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print("Please enter the starting number of your range.")
startingNumber = input()
print("Please enter the ending number of your range.")
endingNumber = input()
prime_list = [] #initializes the list

for i in range(int(startingNumber), int(endingNumber)+1):
  if is_prime(i) == True:
      prime_list.append(i) #saves the prime numbers in the list
print(prime_list)