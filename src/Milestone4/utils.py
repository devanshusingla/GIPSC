from scope import *

def getBaseType(stm, dt):
    curr = dt
    while (curr not in stm[stm.id].avlTypes) and (curr in stm[stm.id].typeDefs):
        curr = stm[stm.id].typeDefs[curr]
    
    if curr in stm[stm.id].avlTypes:
        return curr 
    else:
        return None

def isBasicNumeric(dt):
    if (len(dt) >= 3 and dt[0:3] == "int")  or (len(dt) >= 5 and dt[0:5] == "float") or (len(dt) >= 8 and dt[0:8] == "complex") or dt== 'byte' or dt == 'rune':
        return True
    return False

def isBasicInteger(dt):
    if (len(dt) >= 3 and dt[0:3] == "int") or dt == "byte" or dt == "rune":
        return True
    return False

def isOrdered(dt):
    if (len(dt) >= 3 and dt[0:3] == "int")  or (len(dt) >= 5 and dt[0:5] == "float") or dt == "string" or dt == 'byte' or dt == 'rune':
        return True
    return False
    
def checkBinOp(stm, dt1, dt2, binop, firstchar):
    dt1 = getBaseType(stm, dt1)
    dt2 = getBaseType(stm, dt2)

    if dt1 == None or dt2 == None:
        return False

    if binop == '+' or binop == '-' or binop == '*' or binop == '/':
        if isBasicNumeric(dt1) and isBasicNumeric(dt2) and dt1 == dt2:
            return True
        elif binop == '+' and dt1 == dt2 and dt1 == "string":
             return True 
        return False 
    
    if binop == '%' or binop == '&' or binop == '|' or binop == '^' | binop == '&^':
        if isBasicInteger(dt1) and isBasicInteger(dt2) and dt1 == dt2:
            return True
        return False 

    if binop == '<<' or binop == '>>':
        if isBasicInteger(dt1) and isBasicInteger(dt2) and firstchar != '-':
            return True 
        return False

    if binop == '&&' or binop == '||':
        if dt1 == 'bool' and dt2 == 'bool':
            return True
        return False
    
    if binop == '==' or binop == '!=':
        if isBasicNumeric(dt1) and isBasicNumeric(dt2) and dt1 == dt2:
            return True
        elif dt1 == dt2 and (dt1 == "string" or dt1== "bool" ):
             return True 
        return False 

    if binop == '<' or binop == '<=' or binop == '>' or binop == '>=':
        if isOrdered(dt1) and isOrdered(dt2) and dt1 == dt2:
            return True
        else:
            return False

def getFinalType(stm, dt1, dt2, binop):
    dt1 = getBaseType(stm, dt1)
    dt2 = getBaseType(stm, dt2)

    if binop == '+' or binop == '-' or binop == '*' or binop == '/':
        if dt1 == 'byte' or dt1 == 'rune':
            return 'int32'
        return dt1
    
    if binop == '%' or binop == '&' or binop == '|' or binop == '^' | binop == '&^':
        if dt1 == 'byte' or dt1 == 'rune':
            return 'int32'
        return dt1

    if binop == '<<' or binop == '>>':
        if dt1 == 'byte':
            return 'uint8'
        if dt1 == 'rune':
            return 'int32'
        return dt1

    if binop == '&&' or binop == '||' or binop == '<' or binop == '<=' or binop == '>' or binop == '>=' or binop == '==' or binop == '!=':
        return 'bool'

def checkUnOp(stm, dt, unOp):
    dt = getBaseType(stm, dt)

    if unOp == '+' or unOp == '-':
        return isBasicNumeric(dt)
        
    if unOp == '!':    
        return dt == "bool"

    if unOp == '^':
        return isBasicInteger(dt)

    # if unOp == '*':
    
    # if unOp == '&':

def getUnaryType(stm, dt, unOp):
    dt = getBaseType(stm, dt)

    if unOp != '*' and unOp != '&':
        if dt == 'byte':
            return 'uint8'
        if dt == 'rune':
            return 'uint32'
        else: 
            return dt
