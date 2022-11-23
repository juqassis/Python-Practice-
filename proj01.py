import math

print ("welcome to Horizons Car Rentals ") 
print("At the prompts, please enter the following:") 
print("Customer's classification code (a character: BD, D, W)")
print("Number of days the vehicle was rented (int)")
print("Odometer reading at the start of the rental period (int)")
print("Odometer reading at the end of the rental period (int)")




doesUserContinue = input("do you want to continue?: ")
baseCharge = 40.00
while doesUserContinue != "B":
    print("That is not a valid option, please try again")
    doesUserContinue = input("do you want to continue?: ")
    while doesUserContinue == "A":
            customerCode = input("Customer code(BD, D, W): ")
            numDays = int(input("Number of days: "))
            beginningOdometerReading = int(input("Odometer reading at  start: "))
            endingOdometerReading = int(input("reading at the end:"))
            roundedMileage = (endingOdometerReading - beginningOdometerReading) /10
            if customerCode == "BD":
                baseChargeTimesDays = baseCharge * numDays
                newPrice =  baseChargeTimesDays+ (roundedMileage * 0.25)
                print(newPrice)
                doesUserContinue = input("do you want to continue?: ")
            elif customerCode == "D":
                baseCharge = 60.00
                if roundedMileage / numDays > 100:
                    allowedMiles = numDays * 100
                    overageCharge = roundedMileage - allowedMiles
                    totalCharge = baseCharge * numDays + ( overageCharge * 0.25)
                    print(totalCharge)
                else:
                    totalCharge = baseCharge * numDays
                    print("$", totalCharge)


                doesUserContinue = input("do you want to continue?: ")
            elif customerCode == "W":
                print("You selected W")
                #code here 
                doesUserContinue = input("do you want to continue?: ")

            

    


