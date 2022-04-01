import random


word_bank = ["Sohoe", "Shrimp", "Fawn", "Rishika", "Nishi", "Shug", "Amoghesia"]
hangman_word = random.choice(word_bank) #choses a random word from the word bank
word_letters = list(hangman_word .upper()) #sets the word into a list of letters
dashed_list = "_" * len(hangman_word)
guessed_letters = []
correct_letters = []
valid_guess = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
life = 6



print("Welcome to hangman!")
print("This is your word" + dashed_list)


while (life > -1) and (len(correct_letters) < len(word_letters)):
    user_guess = str(input("Enter your guess: ").upper())

    if user_guess not in valid_guess:
        print("Not a valid guess.")
        continue

    if user_guess in guessed_letters:
        print("You already guessed that letter")
        continue

    guessed_letters.append(user_guess)
        
    if user_guess in word_letters:
        for x in word_letters:
            if x == user_guess:
                correct_letters.append(user_guess)
        print("You guessed correctly")

    else:
        life = life - 1
        print("You guessed it wrong. " + "You have " + str(life) + " hearts remaining")
    
    for i in range(len(word_letters)):
        if word_letters[i] in correct_letters:
            dashed_list = dashed_list[:i] + word_letters[i] + dashed_list[i+1:]

    print("This is how the word looks like now: " + dashed_list)
    print("---------------------------------------------------------------------------------------------------")

    if (len(correct_letters) == len(word_letters)) and (life > 0):
        print("Yay you guessed the word correctly!")

    if (life <= 0):
        print("You lost")
        print("The word was" + str(hangman_word))
        


