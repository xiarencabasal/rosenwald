import random
choices = ['a','c','d','e','g','h','i','l','n','s','t','u','v']
word = ['iceland']
secretWord = random.choice(word); length_word = len(secretWord); lettersGuessed =[]; guessWord =[]

def start():
    print ("Welcome to Hangaroo!Lets' play! ")
    print ("Use only the given letters below")
    print ("Use only lowercase my dearest player")
start()

def secret():
    for character in secretWord:
        guessWord.append("_")
        
    print ("The word you have to guess is a place with ", length_word, "characters")
    print (' '.join(guessWord))
    print ("After 5 wrong letters guessed, You lose!") 
        
def guessing():
    turns = 0
    while turns < 5:
        print ("\n", ' '.join(choices))
        guess = input("Letter: \n").lower()
        
        if guess not in choices:
            print ("Wrong guess, Try harder...")
            turns +=1
            print("Number of wrong guesses: ", turns)
        elif guess in lettersGuessed:
            print("Already Used Letter, Try harder player..")
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print ("Nice Guess player!")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guessWord[x] = guess
                        print(' '.join(guessWord))
                choices.remove(guess)
            else:
                print("Wrong guess, try harder...")
                choices.remove(guess)
                turns += 1
                print("Numeber of wrong guesses: ", turns)
                if turns == 4:
                    print("You used all guesses")
                    print("The word is:", secretWord)
                    print("Thanks for trying! Better luck next time")
        if '_' not in guessWord:
                        print("Yey! You guessed the word right! Congrats player!")
                        break              
secret()
guessing()
