import sys
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

def getUserFloat(inputs):
    while True:
        try:
            inp = float(input(inputs).strip())
            if inp > 0:
               return inp
        except:
	        print("you can't convert that string to a float")

def createCaloricBalance():
    print("Hi! This program will calculate your caloric balance for the day!")
    print("Before we can start, I need some information about you. Be honest! :)")
    print("")
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


def eatFoodAction(mycal):
    promt = "Okay! How many calories did you just eat?"
    cals = getUserFloat(promt)
    mycal.eatFood(cals)
    value = mycal.getBalance()
    message = "Sweet! Your caloric balance is now " + str(value)
    print (message)

def quitAction(mycal):
    print ("Bye! See you next time!")
    sys.exit(0)

def applyAction(mycal, string):
    if string == "f":
        return eatFoodAction(mycal)
    elif string == "a":
    	return recordActivityAction(mycal)
    elif string == "q":
    	return quitAction(mycal)
    else:
    	print('Sorry, that option is invalid.')


def main():

    mycal = createCaloricBalance()
    while True:
        value = mycal.getBalance()
        print ("Thanks! Now, throughout the day, tell me each time you eat or move.")
        print ("Your caloric balance is starting at " + str(value) + "(you need to eat something))")
        menu = formatMenu()
        inputs = formatMenuPrompt()
        inputs = inputs.strip()
        for i in menu:
            print (i)
        string = getUserString(inputs)
        applyAction(mycal, string)


if __name__ == '__main__':
    main()
