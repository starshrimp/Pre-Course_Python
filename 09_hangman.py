import requests
response = requests.get("https://random-word.ryanrk.com/api/en/word/random")
if response.status_code == 200:
    # The request was successful
    random_word = response.text.strip().upper()  # Extract the word from the response and remove any whitespace
    random_word = random_word.strip('["]').strip('"]') # Remove any spaces from the word
    
else:
    print("Failed to fetch a random word.") 

positions = []
guessed_letters = []
attempts = 7  # Number of allowed wrong attempts
hangman_pictures = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hangman_pictures = hangman_pictures[::-1] # Reverse the list

while True:  
  if not all(letter in guessed_letters for letter in random_word):
    print(f"Your word has {len(random_word)} letters. Guess a letter. Enter quit to quit.")
  elif all(letter in guessed_letters for letter in random_word):
    print("Congratulations! You have won the game!")
    break
  if attempts == 7 and not guessed_letters:
    print(len(random_word)*"_")
  
  user_input=input().upper()
  if not user_input.isalpha():
    print("Please enter a single letter.")
    continue
  displayed_characters = []
  
  if user_input in random_word:
    if user_input in random_word:
        print("Correct!")
        guessed_letters.append(user_input)
        print(" ".join(letter if letter in guessed_letters else "_" for letter in random_word))
        for letter in random_word:
          # Check if the current letter is in the guessed_letters collection
          if letter in guessed_letters:
              # If the letter is guessed, add it to the displayed_characters list
              displayed_characters.append(letter)
          else:
              # If the letter is not guessed, add an underscore to the displayed_characters list
              displayed_characters.append("_")
          
  elif user_input == 'quit':
        print("Exiting the loop...")
        break

  elif user_input == 'solution':
        print(random_word)
        break
  elif attempts == 1:
        print("You have no more attempts left. You lose!")
        print("Random word:", random_word)
        attempts -= 1
        print(hangman_pictures[attempts])
        break
  else:
    print(f"The letter '{user_input}' is not in the string.")
    attempts -= 1
    if attempts == 1:
      print(f"You have {attempts} attempt left.")
    else:
      print(f"You have {attempts} attempts left.")
    print(hangman_pictures[attempts])
    print(" ".join(letter if letter in guessed_letters else "_" for letter in random_word))


      

  

