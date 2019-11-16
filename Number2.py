print ("USE LOWERCASE LETTERS")
secretWord = input("Secret Word: ")
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
length_word = len(secretWord); lettersGuessed = []; guessWord =[]

def secret():
    for character in secretWord:
        guessWord.append("_")        
    print ("The word has ", length_word, "letters")
    print (' '.join(guessWord))
    
def getGuessedWord():    
    turns = 1    
    while turns < 6:        
        guess = input("Type a letter: ")
        if guess not in alphabet:
            print ("Wrong guess. Try Again")
        elif guess in lettersGuessed:
            print("Letter already chosen. Please try again")
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print ("Correct! Try again \n")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guessWord[x] = guess
                        print(' '.join(guessWord))                
        if '_' not in guessWord:
                        print("Congrats!")
                        break
secret(); getGuessedWord()
