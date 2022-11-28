import math 

#prompt user to process triangle 
processTriangle = input("Do you want to process a triangle?: ")
numTriangles = 0 


#iterate if above processTriangle = "y" or "Y" 
while processTriangle == "Y" or processTriangle == "y":
    #input length for each side 
    sideLengthThree = float(input("Enter the Lengh of side AB: "))
    sideOneLength = float(input("Enter the Length of side BC:"))
    sideLengthTwo = float(input("Enter the Length of side CA: "))

    #check if we form a valid triangle
    if sideLengthThree + sideOneLength > sideLengthTwo:
        numTriangles +=1 
        print("Valid Triangle")
        print("Triangle sides: ")
        validTriangle = True
        #print all triangle sides 
        print("\tLength of side AB: ", sideLengthThree)
        print("\tLength of side BC: ", sideOneLength)
        print("\tLength of side CA: ", sideLengthTwo)
        #calculate the angles in radians 
        angleOneCalc = math.acos((sideLengthTwo ** 2 + sideLengthThree ** 2 - sideOneLength ** 2)/(2 * sideLengthTwo * sideLengthThree))
        angleTwoCalc = math.acos((sideOneLength **2 + sideLengthThree ** 2 - sideLengthTwo **2) / (2 * sideOneLength * sideLengthThree))
        angleThreeCalc = math.acos((sideOneLength ** 2 + sideLengthTwo ** 2 - sideLengthThree **2) /(2 * sideOneLength * sideLengthTwo)) 
        ##

        # convert radians to degress and print results 
        sideOneToDegrees = angleOneCalc *180/ math.pi
        sideTwoToDegrees = angleTwoCalc * 180 / math.pi
        sideThreeToDegrees = angleThreeCalc * 180 / math.pi
        
      

       
        #calculate perimiter and area 
        perimiter= sideOneLength + sideLengthTwo + sideLengthThree
        calculateSemiPerimiter = .5 * (sideOneLength + sideLengthTwo + sideLengthThree) 
        calcuateArea = math.sqrt((calculateSemiPerimiter * (calculateSemiPerimiter - sideOneLength) *(calculateSemiPerimiter - sideLengthTwo) * (calculateSemiPerimiter - sideLengthThree)))
       
       #print interior angles 
        print("Degree measure of Interior Angles: ")
        print("\tAngle A: ", round(sideOneToDegrees, 1))
        print("\tAngle B: ", round(sideTwoToDegrees, 1))
        print("\tAngle C: ", round(sideThreeToDegrees, 1))
        
        #print radian angles 
        print("Radian Measure of interior angles: ")
        print("\tRadian measure of Angle A:", round(angleOneCalc, 1))
        print("\tRadian measure of angle B: ", round(angleTwoCalc, 1))
        print("\tRadian measure of angle C: ", round(angleThreeCalc, 1))

        

        #print perimiter and area 
        print("Perimeter and Area: ")
        print("\tPerimeter of Triangle: ", round(perimiter, 1))
        print("\tArea: ", round(calcuateArea, 1))

        print("Types of Triangles: ")
        #checks to see which types of triangles apply if we formed a valid one from initial input 
        if validTriangle == True:
            if sideOneLength and sideLengthTwo == sideLengthThree:
                equilateralTriangle = True 
                print("\tequalateral Triangle")
            if sideOneLength == sideLengthTwo or sideLengthTwo == sideLengthThree or sideOneLength == sideLengthThree: 
                isoslesTraingle = True 
                print("\tIsosoles triangle")
            if sideOneLength != sideLengthTwo and sideLengthTwo != sideLengthThree and sideOneLength != sideLengthThree: 
                scaleneTriangle = True
                print("\tScalene triangle")
            if sideOneToDegrees == 90.0 or sideTwoToDegrees == 90.0 or sideThreeToDegrees == 90:
                print("\tRight Triangle")
            if sideOneToDegrees > 90.0 or sideTwoToDegrees > 90.0 or sideThreeToDegrees > 90:
                print("\tobtuse triangle")
            if sideOneToDegrees != 90.0 and sideTwoToDegrees != 90.0 and sideThreeToDegrees != 90.0:
                print("\toblique triangle")
            
        processTriangle = input("Do you want to process a triangle?:  ")
         
        #check if the length of the first two sides are less than the third, if so, this is an invalid triangle 
    elif sideLengthThree + sideOneLength < sideLengthTwo:
        print("That is not a valid Triangle: ") 
        processTriangle = input("Do you want to process a triangle?: ")
    elif sideLengthThree + sideOneLength == sideLengthTwo:
        print("degenerate Triangle ")
        processTriangle = input("Do you want to process a triangle?: ")
        


print("numer of valid Triangles:" , numTriangles)    

