print ("welcome to Horizons Car Rentals ") 
print("At the prompts, please enter the following:") 
print("Customer's classification code (a character: BD, D, W)")
print("Number of days the vehicle was rented (int)")
print("Odometer reading at the start of the rental period (int)")
print("Odometer reading at the end of the rental period (int)")




doesUserContinue = input("do you want to continue?: ")
baseCharge = 40.00

while doesUserContinue == "A":
        customerCode = input("Customer code(BD, D, W): ")
        numDays = int(input("Number of days: "))
        beginningOdometerReading = float(input("Odometer reading at  start: "))
        endingOdometerReading = float(input("reading at the end:"))
        
        if customerCode == "BD":
            beginningOdometerReadingRounded = round(beginningOdometerReading, 1)
            endingOdometerReadingRounded = round(endingOdometerReading,1)
            baseChargeTimesDays = baseCharge * numDays
            newPrice =  baseChargeTimesDays+ (endingOdometerReading - beginningOdometerReading * 0.25)
            print(newPrice)
            doesUserContinue = input("do you want to continue?: ")
        elif customerCode == "D":
            print("You selected D")
            doesUserContinue = input("do you want to continue?: ")
        elif customerCode == "W":
            print("You selected W")
            doesUserContinue = input("do you want to continue?: ")

            

    


