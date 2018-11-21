import caloric_balance
def formatMenu():
    return ['What would you like to do?', '[f] Record Food Consumption', '[a] Record Physical Activity', '[q] Quit']
def formatMenuPrompt():
    return 'Enter an option: '
def formatActivityMenu():
    return ['Choose an activity to record', '[j] Jump rope', '[r] Running', '[s] Sitting', '[w] Walking']

def getUserString(prompt):
    inputs = input(prompt)
    inputs = inputs.strip()
    while inputs == "":
        inputs = input(prompt)
        inputs = inputs.strip()
    return inputs

def getUserFloat(prompt):
    asdf = 0
    while asdf <= 0:
        try:
            asdf = float(input(prompt))
        except:
            print("That does not work")
    return asdf

def createCaloricBalance():
    gender = getUserString("What is your gender (f or m)?")
    age = getUserFloat("What is your age?")
    height = getUserFloat("What is your height in inches? ")
    weight = getUserFloat("What is your weight in pounds?")

    mycal = caloric_balance.CaloricBalance(gender, age, height, weight)

    return mycal

def recordActivityAction(mycal):
    menu=formatActivityMenu()
    for line in menu:
        print(line)

    inputs2 = "a"
    inputs2 = getUserString(formatMenuPrompt())
    if inputs2 != "j" and inputs2 != "r" and inputs2 != "s" and inputs2 != "w":
        print("Sorry, that option is invalid")
        return

    if inputs2 == "j":
        num = .074
    elif inputs2 == "r":
        num = .115
    elif inputs2 == "s":
        num = .058
    elif inputs2 == "w":
        num = .065

    mins = getUserFloat("For how many minutes did you perform this activity?")
    mycal.recordActivity(num, mins)
    print("Awesome! Your caloric balance is now " + str(mycal.getBalance()))

def eatFoodAction():
    pass
def quitAction():
    pass
def applyAction(mycal, string):
    CaloricBalance
    pass
def main():
    pass

if __name__ == '__main__':
    main()
