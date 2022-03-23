from scope import *

def getBaseType(stm, dt):
    curr = dt
    
    if curr in stm.symTable[stm.id].typeDefs:
        return stm.symTable[stm.id].typeDefs[curr]
    else:
        return dt

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

    if 'baseType' in dt1:
        dt1 = dt1['baseType']
    else:
        return False
    if 'baseType' in dt2:
        dt2 = dt2['baseType']
    else:
        return False

    if dt1 == None or dt2 == None or dt1 not in stm[stm.id].avlTypes or dt2 not in stm[stm.id].avlTypes:
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

## Returns if n is in range of integers
def check_int(n):
    sz = len(n)
    if len(n) <= 18:
        return True 
    elif len(n) > 19:
        return False
    elif int(n) < 2**64:
        return True 
    return False

def isConvertibletoInt(f):
    sz = len(f)
    present = False 
    for i in range(sz):
        if f[i] == '.':
            present = True 

    if not present:
        return False 
    else:
        i = sz - 1
        while f[i] != '.':
            if f[i] != '0':
                return False 
            i -= 1
        return True
    
def isTypeCastable(stm, dt1, dt2):
    if dt1['name']!=dt2['name']:
        return False

    while 'name' in dt1 and (dt1['name'] == 'array' or dt1['name'] == 'slice' or dt1['name'] == 'pointer' or dt1['name'] == 'elementary'):
        if dt1['name']!= dt2['name']:
            return False

        dt1 = dt1['baseType']
        dt2 = dt2['baseType']

    if isinstance(dt1, str) and isinstance(dt2, str):
        dt1 = getBaseType(stm, dt1)
        dt2 = getBaseType(stm, dt2)

        if dt1 == dt2:
            return True
        if isBasicInteger(dt1) and isBasicInteger(dt2):
            return True
        if (len(dt1) >= 3 and dt1[0:3] == "int") and (len(dt2) >= 5 and dt2[0:5] == "float"):
            return True
        return False

    if isinstance(dt1, str) or isinstance(dt2, str):
        return False
    
    if 'name' in dt1 and dt1['name'] != dt2['name']:
        return False

    if 'name' in dt1 and dt1['name'] == 'struct':
        for i in dt1:
            tmp = dt1[i]
            if tmp == 'name':
                continue 
            else:
                if i in dt2:
                    if not isTypeCastable(dt1[i], dt2[i]):
                        return False 
                else:
                    return False 
        return True 

    if dt1['name'] == 'map':
        return isTypeCastable(dt1['KeyType'], dt2['KeyType']) and isTypeCastable(dt1['ValueType'], dt2['ValueType'])

def checkTypePresence(stm, dt):
    while ('name' in dt) and (dt['name'] == 'array' or dt['name'] == 'slice' or dt['name'] == 'pointer' or dt['name'] == 'elementary'):
        dt = dt['baseType']

    if isinstance(dt, str):
        return stm.findType(dt)

    elif 'name' in dt and dt['name'] == 'struct':
        for i in dt:
            tmp = dt[i]
            if tmp == 'name':
                continue
            else:
                flag = checkTypePresence(stm, tmp)
                if flag == -1:
                    return -1
        return 1
                        
    elif 'name' in dt and dt['name'] == 'map':
        flag = checkTypePresence(stm, dt['KeyType'])
        if flag == -1:
            return -1
        else:
            flag = checkTypePresence(stm, dt['ValueType'])
            if flag == -1:
                return -1
        return 1
