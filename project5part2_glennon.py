#lab4 by Mac Glennon

#define function

def evaluateSimpleExpression(s):


#find the operator
    
    sgn = s.find('+')
    if sgn == -1:
        sgn = s.find('-')
    if sgn == -1:
        sgn = s.find('*')
    if sgn == -1:
        sgn = s.find('/')
   
    
    #get numeric values of integers entered
    firstInt = int(s[:sgn])
    operator = str(s[sgn])
    secondInt = int(s[sgn+1:])

    #designate operation for each possible operator
    theSum = firstInt + secondInt
    theQuo = firstInt / secondInt
    theProd = firstInt * secondInt
    theDif = firstInt - secondInt

                          
    #calculate and return value
    if operator == "+":
        calc = (str(firstInt) + " + " + str(secondInt) + " = " + str(theSum))
        return(calc)
        
            
    if operator == "-":
        calc = (str(firstInt) + " - " + str(secondInt) + " = " + str(theDif))
        return(calc)
        
            
    if operator == "*":
        calc = (str(firstInt) + " * " + str(secondInt) + " = " + str(theProd))
        return(calc)
        

    if operator == "/":
        calc = (str(firstInt) + " / " + str(secondInt) + " = " + str(theQuo))
        return(calc)

#test program

x = str(4+4)
print(evaluateSimpleExpression(x))
        

            
        


                       
