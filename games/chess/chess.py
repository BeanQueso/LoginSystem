import random
main_letter = input("What is the main letter?: ")
letters = input("Enter each letter: ")
letters = letters.split(' ')

possible_words = []

all_words = []

with open("words.txt", "r") as f:
    f = f.read()

    for i in f:
        all_words.append(i)
        print(f.index(i))
print(all_words)
while len(possible_words) <= 10:
    word = ""
    for i in letters:
        rand_letter = random.choice(letters)
        word+=rand_letter
        

    if main_letter in word and word in all_words:
        possible_words.append(word)

print(possible_words)   