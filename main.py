#Step 5
import hangman_art
import hangman_words
import random


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-: - Import the logo from hangman_art.py and print it at the start of the game.

print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
  
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #TODO-: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"{guess} is already chosen, please chose different letter")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
      
    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"you guessed {guess}, thats not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose the game.")
      
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win the game")
      
    #TODO-: - Import the stages from hangman_art.py
    print(hangman_art.stages[lives])