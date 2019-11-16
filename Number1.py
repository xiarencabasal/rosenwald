secretWord = str(input("Enter Word: "))
lettersGuessed = input("Guess a Letter: ")

def isWordGuessed (secretWord, lettersGuessed):
        for s in secretWord:
            x = s in lettersGuessed
            if x == ("False"):
                break
            return x
print (isWordGuessed(secretWord, lettersGuessed))