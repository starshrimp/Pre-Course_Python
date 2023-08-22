print("Please enter a word.")
word = input()

if word == "".join(reversed(word)): #"".join to convert the reversed iterator into a string 
  print("This is a palindrome.")
else:
  print("This is not a palindrome.")

