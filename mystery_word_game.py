
import random

words = {
    "elephant": "Animal",
    "rainbow": "Nature",
    "diamond": "Precious stone",
    "astronaut": "Space",
    "chocolate": "Food",
    "telescope": "Science",
    "penguin": "Bird",
    "volcano": "Natural phenomenon",
    "butterfly": "Insect",
    "hospital": "Place",
    "pyramid": "Historical structure",
    "waterfall": "Natural beauty",
    "keyboard": "Technology",
    "sunflower": "Flower",
    "treasure": "Valuable objects",
    "dolphin": "Sea animal",
    "guitar": "Musical instrument",
    "library": "Place for reading",
    "raincoat": "Clothing",
    "planet": "Space object",
    "beebijan": "A person's name"
}

secret_word = random.choice(list(words.keys()))
hint = words[secret_word]

guessed_letters = []
attempts = 6

print("===== MYSTERY WORD CHALLENGE =====")
print("\nGuess the hidden word!")
print("Hint:", hint)

while attempts > 0:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word!")
        print("Your score:", attempts)
        break

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

else:
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)

print("\n===== THANK YOU FOR PLAYING =====")
