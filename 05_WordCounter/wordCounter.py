f = open("text.txt") #open the text file containing the story
text = f.read()
print(text) # printing the story
text= text.lower()
text = text.replace('.', '').replace(',', '')
wordCounter = {}
words = text.split() 
for word in words:
  wordCounter[word] = words.count(word)


groupedWords = {
}
    
for key, value in wordCounter.items():
    if value not in groupedWords:
        groupedWords[value] = []  # Initialize an empty list for the frequency value
    groupedWords[value].append(key)

sortedWords = dict(sorted(groupedWords.items(), reverse = True))
print("These are the most frequent words in the story: ")
for key, value in sortedWords.items():
   if key > 5:
      print("These words occured " + str(key) + " times: " + (', '.join(value)))