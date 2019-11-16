choices = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lettersGuessed = list(input("Choose only from the given letters "))
def getAvailableLetters(lettersGuessed):
    ab = []
    for x in choices:
        ab = ["" if x in lettersGuessed else x for x in choicecs
    print (''.join(ab))
    return x
getAvailableLetters(lettersGuessed)