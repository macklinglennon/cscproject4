#lab4 by Mac Glennon

#ask the user for an algebraic expression

s = "n"
myList = []

while(s != "end"):
    s = str(input("Input an algebraic expression: "))

    if(s == "end"):
        print("session ended")
        break

#find the operator
    
    sgn = s.find('+')
    if sgn == -1:
        sgn = s.find('-')
    if sgn == -1:
        sgn = s.find('*')
    if sgn == -1:
        sgn = s.find('/')
    if sgn == -1 and s != "last":
        print("invalid entry")
    if s == "last":
        print(myList)

    while(sgn != -1): 
        #get numeric values of integers entered
        firstInt = int(s[:sgn])
        operator = str(s[sgn])
        secondInt = int(s[sgn+1:])

        #designate operation for each possible operator
        theSum = firstInt + secondInt
        theQuo = firstInt / secondInt
        theProd = firstInt * secondInt
        theDif = firstInt - secondInt

                          
        #calculate
        if operator == "+":
            calc = (str(firstInt) + " + " + str(secondInt) + " = " + str(theSum))
            print(calc)
            myList.append(calc)
            
        if operator == "-":
            calc = (str(firstInt) + " - " + str(secondInt) + " = " + str(theDif))
            print(calc)
            myList.append(calc)
            
        if operator == "*":
            calc = (str(firstInt) + " * " + str(secondInt) + " = " + str(theProd))
            print(calc)
            myList.append(calc)

        if operator == "/":
            calc = (str(firstInt) + " / " + str(secondInt) + " = " + str(theQuo))
            print(calc)
            myList.append(calc)

            
        sgn = -1


                       
