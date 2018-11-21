def kitten():
    while True:
        a = int(input('what is your favoret number '))
        d = {3, 'meow'}
        if a in d:
            print("Thats right that is " + str(a) + " Is a very niffty number!")
        else:
            print( str(a) + " is not a very good number")

kitten()
