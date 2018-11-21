import random

class Game:
    def __init__(self):
        self.bet = 0
        self.numberOfPlayers = 0
        self.players = []
        self.playersCards = []
        self.dealerdsCards = []
        self.HEADER  = '\033[95m'
        self.INFO    = '\033[94m'
        self.WARNING = '\033[93m'
        self.SUCCESS = '\033[92m'
        self.DANGER  = '\033[91m'
        self.BOLD    = '\033[1m'
        self.ENDC    = '\033[0m'

    def intro(self):
        print(" test")
        print(self.BOLD + "                     Welcome to" + self.ENDC)
        print(self.INFO + "")
        print("      .------..------..------..------..------.      ")
        print(" .-.  |B.--. ||L.--. ||A.--. ||C.--. ||K.--. |.-.   ")
        print("((5)) | :(): || :/\: || (\/) || :/\: || :/\: ((5))  ")
        print(" '-.-.| ()() || (__) || :\/: || :\/: || :\/: |'-.-. ")
        print("  ((1)) '--'B|| '--'L|| '--'A|| '--'C|| '--'K| ((1))")
        print("   '-'`------'`------'`------'`------'`------'  '-' ")
        print("      .------..------..------..------.              ")
        print(" .-.  |J.--. ||A.--. ||C.--. ||K.--. |.-.           ")
        print("((5)) | :(): || (\/) || :/\: || :/\: ((5))          ")
        print(" '-.-.| ()() || :\/: || :\/: || :\/: |'-.-.         ")
        print("  ((1)) '--'J|| '--'A|| '--'C|| '--'K| ((1))        ")
        print("   '-'`------'`------'`------'`------'  '-'         " + self.ENDC)
        print(self.SUCCESS + "              By Brandon Stewart" + self.ENDC)
        print("")
        return

    #subrutines
    def getUserString(self, prompt):
        inputs = input(prompt)
        inputs = inputs.strip()
        while inputs == "":
            inputs = input(prompt)
            inputs = inputs.strip()
            print ("What? ")
        return inputs

    def getUserFloat(self, inputs):
        while True:
            try:
                inp = float(input(inputs).strip())
                if inp > 0:
                   return inp
            except:
    	        print("You must enter a number")

    #this method will ask each player for there name and if it is a human or computer playing
    def addPlayerNames(self):
        pass


    def addToDealer(self, sute, value):
        self.dealerdsCards.append([ sute, value ])

    def addToPlayer(self, sute, value, playerID):
        self.dealerdsCards.append([ sute, value, playerID ])

    def formatMenu(self):
        list = [ 'What would you like to do?', '[H] Hit', '[S] Stand', '[SP] Split', '[Q] Quit' ]
        return list

    def value(self, value):
        if (value == 12):
            value = "K"
        elif (value == 11):
            value = "Q"
        elif (value == 10):
            value = "J"
        elif (value == 1):
            value = "A"
        return value

    def sute(self, sute):
        if (sute == 0): #Harts
            return ["| (\/) |", "| :\/: |"]
        elif (sute == 1): #Spades
            return ["| :/\: |","| (__) |"]
        elif (sute == 2): #Diamouds
            return ["| :/\: |","| :\/: |"]
        elif (sute == 3): #Clubs
            return ["| :(): |","| ()() |"]

    def card(self, cards):

        #test cards
        #cards = [[1 , 2],[0 , 1],[1 , 5],[1 , 12]]

        #declartion of row verables
        row1 = ""
        row2 = ""
        row3 = ""
        row4 = ""
        row5 = ""
        row6 = ""

        #construction of card rows
        for rows in cards:
            #set color of card to red if harts or diamouds
            color = ""
            if (rows[0] in [0,2]):
                color = self.DANGER

            row1 += (color + ".------. " + str(self.ENDC))
            row2 += (color + "|" + str(self.value(rows[1])) + ".--. | "  + str(self.ENDC))
            row3 += (color + str(self.sute(rows[0])[0]) + " "  + str(self.ENDC))
            row4 += (color + str(self.sute(rows[0])[1]) + " "  + str(self.ENDC))
            row5 += (color + "| '--'" + str(self.value(rows[1])) +"| "  + str(self.ENDC))
            row6 += (color + "`------' " + str(self.ENDC))

        #print the cards
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print(row5)
        print(row6)

        return

    #the askBet method will return ask the player to enter a number
    def askBet(self):
        bet = self.getUserFloat("What is your bet? $")
        if (bet <= 0):
            print("bet must be greater then 0")
        else:
            self.bet = bet
            print("OK your Bet is $" + str(bet) + " Good luck!")

    def deal(self):
        print('What would you like to do?')
        deal = self.getUserString('Deal (d): ')
        while (str(deal) != "d"):
            deal = self.getUserString('Deal (d): ')
            print ("What? ")
        print ("Let's Play ")


    def addToPlayer(self):
        while True:
            try:
                numberOfPlayers = self.getUserFloat("How many players are there? (You can have up to 5): ")
                if (numberOfPlayers <= 5 and numberOfPlayers > 0):
                    self.numberOfPlayers = numberOfPlayers
                    return numberOfPlayers
                else:
                    print('The number you entered must be between 1-5')
            except:
                return "Error"

    def setPlayers(self):
        for i in range(int(self.numberOfPlayers)):
            print ("what is player" + str(i + 1) + "'s name?: ")
        return

    def main(self):
        cards = [[1 , 2],[0 , 1],[1 , 5],[1, 12]]
        self.intro()
        #self.deal()
        self.addToPlayer()
        self.setPlayers()
        #self.card(cards)
        #while True:
    	#	menu = formatMenu()

game = Game()
game.main()
