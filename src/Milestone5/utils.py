from tokenize import Name
from scope import *
import os

# COMPACT = False
# def get_value_p(p):
#     value = [str(sys._getframe(1).f_code.co_name)[2:]]
#     # value = []
#     for i in range(1, len(p)):
#         if isinstance(p[i], str):
#             if p[i] in ignored_tokens:
#                 continue
#             if p[i] not in non_terminals:
#                 value.append([p[i]])
#         elif len(p[i]) > 0:
#             if COMPACT:
#                 if p[i][0] == value[0]:
#                     value.extend(p[i][1:])
#                 else:
#                     value.append(p[i])
#             else:
#                 value.append(p[i])
#     if not isinstance(value, str) and COMPACT:
#         if len(value) == 2:
#             return value[1]
#         if len(value) == 1:
#             return []
#         if len(value) > 2:
#             if value[0] == 'Expr':
#                 value = value[2] + [value[1]] + value[3:]
#             elif value[0] == 'UnaryExpr':
#                 value = value[1] + [value[2]]
#                 # print(value, value[2] + [value[1]] + value[3:])
#     return value

LIBPATH = os.path.dirname(os.path.realpath(__file__)) + "/lib"

def getPath(filename, target_folder):
    for root, dirs, files in os.walk(LIBPATH):
        if filename in files:
            return os.path.join(root, filename)

    for root, dirs, files in os.walk(target_folder):
        if filename in files:
            return os.path.join(root, filename)
    
    raise NameError(f"Invalid import: {filename}")

def getBaseType(stm, dt):
    curr = dt
    
    if isinstance(curr, str) and curr in stm.symTable[stm.id].typeDefs:
        return stm.symTable[stm.id].typeDefs[curr]
    else:
        return dt

def isBasicNumeric(stm, dt):

    dt = getBaseType(stm, dt)

    if not isinstance(dt, str):
        if 'baseType' in dt:
            if 'level' in dt and dt['level'] != 0:
                return False 
            dt = dt['baseType']
        else:
            return False 

    if (len(dt) >= 4 and dt[0:4] == "uint") or (len(dt) >= 3 and dt[0:3] == "int")  or (len(dt) >= 5 and dt[0:5] == "float") or (len(dt) >= 8 and dt[0:8] == "complex") or dt== 'byte' or dt == 'rune':
        return True
    return False

def isBasicInteger(stm, dt):

    dt = getBaseType(stm, dt)

    if not isinstance(dt, str):
        if 'baseType' in dt:
            if 'level' in dt and dt['level'] != 0:
                return False 
            dt = dt['baseType']
        else:
            return False 

    if (len(dt) >= 4 and dt[0:4] == "uint") or (len(dt) >= 3 and dt[0:3] == "int") or dt == "byte" or dt == "rune":
        return True
    return False

def isOrdered(stm, dt):

    dt = getBaseType(stm, dt)

    if not isinstance(dt, str):
        if 'baseType' in dt:
            if 'level' in dt and dt['level'] != 0:
                return False 
            dt = dt['baseType']
        else:
            return False 

    if (len(dt) >= 4 and dt[0:4] == "uint") or (len(dt) >= 3 and dt[0:3] == "int")  or (len(dt) >= 5 and dt[0:5] == "float") or dt == "string" or dt == 'byte' or dt == 'rune':
        return True
    return False
    
def checkBinOp(stm, dt1, dt2, binop, firstchar):
    
    dt1 = getBaseType(stm, dt1)
    dt2 = getBaseType(stm, dt2)

    if dt1['level'] > 0 or dt2['level'] > 0:
        if binop != '==' and binop != '!=':
            return False
        if dt1['level'] != dt2['level']:
            return False

    if not isinstance(dt1, str):
        if 'baseType' in dt1:
            dt1 = dt1['baseType']
        else:
            return False

    if not isinstance(dt2, str):
        if 'baseType' in dt2:
            dt2 = dt2['baseType']
        else:
            return False

    if dt1 == None or dt2 == None or dt1 not in stm.symTable[stm.id].avlTypes or dt2 not in stm.symTable[stm.id].avlTypes:
        return False

    if binop == '+' or binop == '-' or binop == '*' or binop == '/':
        if isBasicNumeric(stm, dt1) and isBasicNumeric(stm, dt2) and dt1 == dt2:
            return True
        elif binop == '+' and dt1 == dt2 and dt1 == "string":
             return True 
        return False 
    
    if binop == '%' or binop == '&' or binop == '|' or binop == '^' or binop == '&^':
        if isBasicInteger(stm, dt1) and isBasicInteger(stm, dt2) and dt1 == dt2:
            return True
        return False 

    if binop == '<<' or binop == '>>':
        if isBasicInteger(stm, dt1) and isBasicInteger(stm, dt2) and firstchar != '-':
            return True 
        return False

    if binop == '&&' or binop == '||':
        if dt1 == 'bool' and dt2 == 'bool':
            return True
        return False
    
    if binop == '==' or binop == '!=':
        if isBasicNumeric(stm, dt1) and isBasicNumeric(stm, dt2) and dt1 == dt2:
            return True
        elif dt1 == dt2 and (dt1 == "string" or dt1== "bool" ):
             return True 
        return False 

    if binop == '<' or binop == '<=' or binop == '>' or binop == '>=':
        if isOrdered(stm, dt1) and isOrdered(stm, dt2) and dt1 == dt2:
            return True
        else:
            return False

def getFinalType(stm, dt1, dt2, binop):
    dt1_copy = dt1.copy()
    
    dt1 = getBaseType(stm, dt1)
    dt2 = getBaseType(stm, dt2)

    if not isinstance(dt1, str):
        if 'baseType' in dt1:
            dt1 = dt1['baseType']
    
    if not isinstance(dt2, str):
        if 'baseType' in dt2:
            dt2 = dt2['baseType']

    if binop == '+' or binop == '-' or binop == '*' or binop == '/':
        if dt1 == 'byte' or dt1 == 'rune':
            return {'name': 'int32', 'baseType' : 'int32', 'level' : 0}
        return dt1_copy
    
    if binop == '%' or binop == '&' or binop == '|' or binop == '^' or binop == '&^':
        if dt1 == 'byte' or dt1 == 'rune':
            return {'name': 'int32', 'baseType' : 'int32', 'level' : 0}
        return dt1_copy

    if binop == '<<' or binop == '>>':
        if dt1 == 'byte':
            return {'name': 'uint8', 'baseType' : 'uint8', 'level' : 0}
        if dt1 == 'rune':
            return {'name': 'int32', 'baseType' : 'int32', 'level' : 0}
        return dt1_copy

    if binop == '&&' or binop == '||' or binop == '<' or binop == '<=' or binop == '>' or binop == '>=' or binop == '==' or binop == '!=':
        return {'name': 'bool', 'baseType' : 'bool', 'level' : 0}

def checkUnOp(stm, dt, unOp, flag):
    dt = getBaseType(stm, dt)

    if unOp == '*':
        if isinstance(dt, str):
            return False
        
        if 'name' not in dt:
            return False

        if dt['name']== 'pointer' or dt['name']=='array' or dt['name'] =='slice':
            return True
        else:
            return False

    if unOp == '&':
        if flag:
            return True
        else:
            return False

    if not isinstance(dt, str):
        if 'baseType' in dt:
            dt = dt['baseType']
        else:
            return False

    if dt == None or dt not in stm.symTable[stm.id].avlTypes:
        return False

    if unOp == '+' or unOp == '-':
        return isBasicNumeric(stm, dt)
        
    if unOp == '!':    
        return dt == "bool"

    if unOp == '^':
        return isBasicInteger(stm, dt)


def getUnaryType(stm, dt, unOp):
    dt_copy = dt.copy()
    dt = getBaseType(stm, dt)

    if unOp == '*':
        dt_copy['level'] -= 1
        if dt_copy['level'] == 0:
            dt_copy['name'] = dt_copy['baseType']
        return dt_copy

    if unOp == '&':
        if isinstance(dt_copy, str):
            return {'baseType': dt, 'level': 1, 'name': 'pointer'}
        dt_copy['level'] += 1
        if dt_copy['level'] == 1:
            dt_copy['name'] = 'pointer'
        return dt_copy

    if not isinstance(dt, str):
        if 'baseType' in dt:
            dt = dt['baseType']

    if unOp != '*' and unOp != '&':
        if dt == 'byte':
            return {'name': 'uint8', 'baseType': 'uint8', 'level': 0}
        if dt == 'rune':
            return {'name': 'uint32', 'baseType': 'uint32', 'level': 0}
        else: 
            return dt_copy

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
    if (dt1 == dt2):
        return True
    if 'name' in dt1 and 'name' in dt2 and dt1['name']!=dt2['name']:
        return False

    if 'name' not in dt1 or 'name'not in dt2:
        return False

    while 'name' in dt1 and (dt1['name'] == 'array' or dt1['name'] == 'slice' or dt1['name'] == 'pointer' or dt1['name'] in basicTypes):
        if 'name' in dt2 and dt1['name']!= dt2['name']:
            return False
        elif 'name' not in dt2:
            return False 

        l1 = dt1['level']
        l2 = dt2['level']
        dt1 = dt1['baseType']
        dt2 = dt2['baseType']

    if isinstance(dt1, str) and isinstance(dt2, str):
        dt1 = getBaseType(stm, dt1)
        dt2 = getBaseType(stm, dt2)

        if dt1 == dt2 and l1 == l2:
            return True
        if isBasicInteger(stm, dt1) and isBasicInteger(stm, dt2) and l1 == l2:
            return True
        
        ## Float to int typecasting
        # if (len(dt1) >= 3 and dt1[0:3] == "int") and (len(dt2) >= 5 and dt2[0:5] == "float"):
        #     return True
        return False

    if isinstance(dt1, str) or isinstance(dt2, str):
        return False
    
    if 'name' in dt1 and 'name' in dt2 and dt1['name'] != dt2['name']:
        return False

    if 'name' in dt1 and dt1['name'] == 'struct':
        for i in dt1:
            tmp = dt1[i]
            if tmp == 'name':
                continue 
            else:
                if i in dt2:
                    if not isTypeCastable(stm, dt1[i], dt2[i]):
                        return False 
                else:
                    return False 
        return True 

    if dt1['name'] == 'map':
        return isTypeCastable(stm, dt1['KeyType'], dt2['KeyType']) and isTypeCastable(stm, dt1['ValueType'], dt2['ValueType'])

def checkTypePresence(stm, dt):
    while not isinstance(dt, str) and ('name' in dt) and (dt['name'] == 'array' or dt['name'] == 'slice' or dt['name'] == 'pointer'):
        dt = dt['baseType']

    if isinstance(dt, str):
        return stm.findType(dt)

    elif 'name' in dt and dt['name'] == 'struct':
        for i in dt['keyTypes']:
            tmp = dt['keyTypes'][i]
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

def Not(operand, dataType: str):
    if dataType.startswith('float'):
        operand = int(operand)
    known_bits = dataType[-2:].isnumeric()
    bits = (1<<32) - 1
    if known_bits:
        bits = (1<<(int(dataType[-2]))) - 1
    if dataType.startswith('float'):
        return float(bits^operand)
    else:
        return bits^operand

def Operate(operator, operand1, operand2, lineno, dt2):
    # Operator is a string while operands are values
    # TODO : Check for overflow issues
    # Do type checks
    if operand1 == None:
        if operator == '^':
            return Not(operand2, dt2)
        else:
            operand1 = 0
    if operator == '+':
        return operand1 + operand2  
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2  
    elif operator == '/':
        if operand2 == 0:
            raise LogicalError(f"{lineno}: Trying to divide by 0.")
        return operand1 // operand2
    elif operator == '||':
        return 'true' if operand1 == 'true' or operand2 == 'true' else 'false'  
    elif operator == '&&':
        return 'true' if operand1 == 'true' and operand2 == 'true' else 'false'
    elif operator == '==':
        return operand1 == operand2  
    elif operator == '!=':
        return operand1 != operand2
    elif operator == '<':
        return 'true' if operand1 < operand2 else 'false'  
    elif operator == '<=':
        return 'true' if operand1 < operand2 else 'false'
    elif operator == '>':
        return 'true' if operand1 < operand2 else 'false' 
    elif operator == '>=':
        return 'true' if operand1 < operand2 else 'false'
    elif operator == '|':
        return operand1 | operand2  
    elif operator == '^':
        return operand1 ^ operand2
    elif operator == '%':
        if operand2 <= 0:
            raise LogicalError(f"{lineno}: Trying to get remainder with non-positive divisor.")
        return operand1 % operand2  
    elif operator == '<<':
        return operand1 << operand2
    elif operator == '>>':
        return operand1 >> operand2  
    elif operator == '&':
        return operand1 & operand2
    elif operator == '&^':
        return operand1 & Not(operand2, dt2)
    elif operator == '!':
        return 'false' if operand2 == 'true' else 'true'
    
# def getComplex(val):
#     if '+' not in val:
#         if 'i' not in val:
#             return (float(val), 0.0)
#         else:
#             return (0.0, float(val.strip('i')))
#     else:
#         parts = float.split('+')
#         return (float(parts[0]), float(parts[1].strip('i')))

def checkAncestor(stm : SymTableMaker, lid, gid, noSkipVar=False):
    flag = False
    # Check if scope id of goto scope symbol table is 
    # an ancestor of label scope symbol table
    while True:
        if lid == gid:
            if noSkipVar:
                if len(stm.symTable[lid].localsymTable) > len(stm.symTable[gid].localsymTable):
                    return False
                if len(stm.symTable[lid].avlTypes) < len(stm.symTable[gid].avlTypes):
                    return False
                if len(stm.symTable[lid].typeDefs) < len(stm.symTable[gid].typeDefs):
                    return False
            flag = True
            break
        if lid == 0:
            break
        else:
            lid = stm.symTable[lid].parentScope
    if not flag:
        return False
    else:
        return True    

def isValidGoto(stm : SymTableMaker, labelST : scope, gotoST : scope, checkNoSkipVar=False):
    if checkNoSkipVar:
        return checkAncestor(stm, gotoST.id, labelST.id, checkNoSkipVar)
        # if  < len(labelST.localsymTable):
        #     return False
        # if len(gotoST.avlTypes) < len(labelST.avlTypes):
        #     return False
        # if len(gotoST.typeDefs) < len(labelST.typeDefs):
        #     return False
        # return True
    else:
        return checkAncestor(stm, labelST.id, gotoST.id)
            
def constructDataType(baseType):
    return {
        'name' : baseType,
        'baseType' : baseType,
        'level': 0 
    }