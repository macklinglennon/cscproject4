#lab2 by Mac Glennon

#define function

def simpleExpressionIsValid(s):


#find the operator
    
    sgn = s.find('+')
    if sgn == -1:
        sgn = s.find('-')
    if sgn == -1:
        sgn = s.find('*')
    if sgn == -1:
        sgn = s.find('/')
    if sgn == -1:
        return False
    else:
        return True

#if legitimate mathematical operator is not used between variables, then
#function will return the value False
                       
