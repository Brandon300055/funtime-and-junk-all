class Player:
    def __init__(self, name):
        self.name = name
        self.letters = []
        return

    def getName(self):
        return self.name

    def getLetters(self):
        return self.letters

    def drawLetter(self):
        letters = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        randomNum = random.randint(0, (len(letters)-1))
        self.letters.append(letters[randomNum])
        return letters[randomNum]
        
    def printLetters(self):
        string = ""
        for i in range(len(self.letters)):
            string += self.letters[i] + " "
        return string.strip()

    def checkWord(self, word):
        letters = self.letters[::]
        for i in range(len(word)):
            if word[i] in letters:
                letters.remove(word[i])
            else:
                return False
        self.letters = letters
        return True
