class CaloricBalance:
    def __init__(self, gender, age, height, weight):
        self.weight = weight
        self.balance = -self.getBMR(gender, age, height, weight)
        return

    def getBMR(self, gender, age, height, weight):
        if gender == "m":
            BMR = (66 + (12.7 * height) + (6.23 * weight) - (6.8 * age))
        elif gender == "f":
            BMR = (655 + (4.7 * height) + (4.35 * weight) - (4.7 * age))
        else:
            BMR = 0.0
        return BMR


    def getBalance(self):
        return self.balance

    def recordActivity(self, caloric_burn_per_pound_per_minute, minutes):
        total = (minutes * (caloric_burn_per_pound_per_minute * self.weight))
        self.balance =  self.balance - total

    def eatFood(self, calories):
        self.balance =  self.balance + calories
        return
    
    
