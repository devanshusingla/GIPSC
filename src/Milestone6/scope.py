from copy import deepcopy
from distutils.log import Log
from typing import List

basicTypes = ['int', 'byte', 'int8', 'int16', 'int32', 'int64', 'float32', 'float64', 'uint8', 'uint16', 'uint32', 'uint64', 'string', 'rune', 'bool']
basicNumericTypes = ['int', 'byte', 'int8', 'int16', 'int32', 'int64', 'float32', 'float64', 'uint8', 'uint16', 'uint32', 'uint64', 'rune']
basicTypeSizes = {'int':4, 'float': 4, 'string': 12, 'rune': 2, 'byte': 1, 'int8': 1, 'int16': 2, 'int32': 4, 'int64': 8, 'uint8': 1, 'uint16': 2, 'uint32': 4, 'uint64': 8, 'float32': 4, 'float64': 8, 'bool': 1}
compositeTypes = ['struct', 'array', 'slice', 'map']

builtinFunctions = ["__syscall"]

curr_temp = 0
curr_var_temp = 0
    
def new_temp():
    global curr_temp
    temp = curr_temp
    curr_temp += 1
    return "temp_" +str(temp)

def var_new_temp():
    global curr_var_temp
    var_temp = curr_var_temp 
    curr_var_temp += 1
    return "var_temp_" + str(var_temp)

def zeroLit(stm, dataType):
    if dataType in basicTypes:
        dt = LitNode({'name' : dataType, 'baseType' : dataType, 'level' : 0, 'size': basicTypeSizes[dataType]}, label=None, isConst=True, val=None)
        if dataType == "string" or dataType == "Rune":
            dt.label = ""
            dt.val = ""
        elif dataType == "complex128":
            dt.label = "0i"
            dt.val = float(0)
        else:
            dt.label = "0"
            dt.val = 0
        return ExprNode(dt.dataType, label=dt.label, operator=None, isConst=True, isAddressable=False, val=dt.val)
        # return LitNode('0', dataType, isConst=True, val=0)
    else:
        if dataType['name'] == 'struct':
            return CompositeLitNode(stm, dataType, NodeList([zeroLit(stm, dt) for dt in dataType["keyTypes"].values()]))

class ScopeTableError(Exception):
    pass

class DuplicateKeyError(Exception):
    pass

class SwitchCaseError(Exception):
    pass

class LogicalError(Exception):
    pass

class scope:
    def __init__(self, currentScopeId, parentScope=None):
        self.localsymTable = {}
        self.id = currentScopeId
        self.parentScope = parentScope
        self.avlTypes = basicTypes.copy()
        self.typeDefs = {}
        self.offset=0
        self.negoffset=-8
        self.okReturn = False
        self.NotAllChildReturn = False

    def insert(self, id, info, isarg=False):
        if not isarg:
            info['offset'] = self.offset
            self.offset += info['dataType']['size']
        else:
            info['offset'] = self.negoffset
            self.negoffset -= info['dataType']['size']

        self.localsymTable[id] = info


    def getinfo(self, id):
        return self.localsymTable.get(id,None)

    def updateAttr(self, id, kwargs):
        if id not in self.localsymTable:
            raise ScopeTableError("Identifier has not been declared")
        for key, value in kwargs.items():
            self.localsymTable[id][key] = value

    def addType(self, type, typeObj):
        # self.avlTypes.append(type)
        self.typeDefs[type] = typeObj

    def setParent(self, parent):
        # Does this store only the reference?
        self.parent = parent
    
    # def inheritTypes(self, prevScope):
    #     for avlType in prevScope.avlTypes:
    #         if avlType not in self.avlTypes:
    #             self.avlTypes.append(avlType)

## Symbol Table Maker
class SymTableMaker:
    def __init__(self):
        self.symTable : dict[int, scope] = {}
        self.symTable[0] = scope(0)
        self.functions = {}
        self.stack : List[scope] = [0]
        self.id = 0
        self.nextId = 1
        self.currentReturnType = None
        # self.forDepth = 0
        # self.switchDepth = 0
        self.labels = {}
        # self.labels: dict[str] -> dict[]
        # self.labels[label] = {
        # 'scopeTab' : _ , 
        # 'mappedName' : _, 
        # 'expecting' : _, 
        # 'lineno' : _
        # 'prevGotos' : [
        #  (scopeTab, lineno), (scopeTab, lineno) ...
        # ]}
        self.currentLabel = None
        self.pkgs = {}
        self.nextLabel = 0
        self.forStack = []
        self.switchStack = []
        self.currentSwitchExpPlace = None
        self.nextCase = 0
        self.addBuiltInFuncs()
        self.addTypeCastFunctions()

    def addFunction(self, label, info):
        self.functions[label] = deepcopy(info)
        self.newScope()
        self.functions[label]['scope'] = self.id
    
    def addType(self, type, typeObj):
        self.symTable[self.id].addType(type, deepcopy(typeObj))

    def newScope(self):
        self.symTable[self.nextId] = scope(self.nextId, parentScope = self.id)
        self.stack.append(self.nextId)
        self.id = self.nextId
        self.nextId += 1
    
    def exitScope(self):
        if self.symTable[self.id].okReturn == True:
            if len(self.stack) >= 2:
                self.symTable[self.stack[-2]].okReturn = True
        if self.symTable[self.id].okReturn == False:
            if len(self.stack) >= 2:
                self.symTable[self.stack[-2]].NotAllChildReturn = True
        self.stack.pop()
        self.id = self.stack[-1]
    
    def add(self, ident, info, isarg=False):
        self.symTable[self.id].insert(ident, deepcopy(info), isarg)

    def get(self, ident, scope=None):
        if scope is None:
            if ident in self.functions:
                return deepcopy(self.functions[ident])
            scope = self.getScope(ident)
            if scope == -1:
                raise Exception("Ident not found in symbol table")
            return deepcopy(self.symTable[scope].getinfo(ident))
        else:
            return deepcopy(self.symTable[scope].getinfo(ident))

    def findType(self, type):
        if isinstance(type, dict):
            type = type['name']
        i = len(self.stack) - 1
        while i >= 0:
            j = self.stack[i]
            if type in self.symTable[j].avlTypes:
                return ElementaryType(dataType={'name':type, 'baseType': type, 'level': 0})
            if type in self.symTable[j].typeDefs:
                return deepcopy(self.symTable[j].typeDefs[type])
            else:
                i -= 1
            
        return -1
    
    def getScope(self, ident):
        i = len(self.stack) - 1
        if ident in self.functions:
            return 0
        while i >= 0:
            if ident in self.symTable[self.stack[i]].localsymTable:
                break
            else:
                i -= 1

        if i == -1:
            return i
        else:
            return self.stack[i]
    
    def getCurrentScope(self):
        return self.stack[-1]
    
    def getNewLabel(self):
        self.nextLabel += 1
        return f"label_{self.nextLabel-1}"

    def addTypeCastFunctions(self):
        for type1 in basicNumericTypes:
            dt = {'baseType': type1, 'name': type1, 'level': 0, 'size': basicTypeSizes[type1]}
            info = {"params": [], "return": [dt], "dataType": {'name': 'func', 'baseType': 'func', 'level': 0}}
            self.functions[type1] = deepcopy(info)  

        type1 = 'string'
        dt = {'baseType': type1, 'name': type1, 'level': 0, 'size': basicTypeSizes[type1]}
        info = {"params": [], "return": [dt], "dataType": {'name': 'func', 'baseType': 'func', 'level': 0}}
        self.functions[type1] = deepcopy(info)           
    
    def addBuiltInFuncs(self):
        print("TODO: Add builtin function definitions by parsing or by hard coding")

## AST Abstract Node Class
class Node:
    def __init__(self, label = "Node"):
        self.children = []
        self.label = label
        self.code = []
        self.place = None
        self.isConst = False
        self.isRef = False
        self.isDeRef = False
        self.lvalue = None
    
    def addChild(self, *children):
        if children:
            self.children.extend(children)
            for child in children:
                if child and hasattr(child, "code"):
                    self.code.extend(child.code)

    def __str__(self):
        return self.label 

## AST Node Classes

class FileNode(Node):
    def __init__(self, pkgName, importDecl, globalDecl):
        super().__init__()
        self.addChild(pkgName, importDecl, globalDecl)
    
    def __str__(self):
        return "FILE"

class ImportNode(Node):

    def __init__(self):
        super().__init__()
        
    def __str__(self):
        return "IMPORT"

class ImportPathNode(Node):
    def __init__(self, alias, path, astNode):
        super().__init__()
        if alias is not None:
            self.addChild(alias)
        self.addChild(path, astNode)
    
    def __str__(self):
        return f'PKG'

class DeclNode(Node):
    def __str__(self):
        return "GLOBAL"

class IdentNode(Node):
    def __init__(self, scope, label, dataType = {}, val = 0, isConst = False):
        super().__init__()
        self.children = None
        self.scope = scope
        self.dataType = dataType
        self.label = label
        self.val = val
        self.isConst = isConst
    
    def __str__(self):
        return f'{self.label}'

class LitNode(Node):
    def __init__(self, label, dataType = None, isConst = False, val=None):
        super().__init__()
        self.children = None
        self.dataType = dataType
        self.isConst = isConst
        self.val = val
        if self.dataType == "string":
            self.label = label[1:-1]
        else:
            self.label = label
    
    def __str__(self):
        if self.isConst:
            return str(self.val)
        if isinstance(self.dataType, str) and self.dataType == "string":
            return f'\\\"{self.label}\\\"'
        elif 'name' in self.dataType and self.dataType['name'] == 'string':
            return f'\\\"{self.label}\\\"'
        else:
            return str(self.label)

import utils
class CompositeLitNode(Node):
    def  __init__(self, stm, compositeLitType, elList):
        super().__init__()
        self.dataType = compositeLitType
        self.children = []
        if not isinstance(elList, list):
            raise NameError("Expected List of values")

        # Initialising var_temp variable in 3ac code
        self.place = var_new_temp()
        addr = new_temp()

        if self.dataType['name'] == 'struct':
            hasKey = False
            hasNotKey = False
            for el in elList:
                if isinstance(el, KeyValNode):
                    hasKey = True
                else:
                    hasNotKey = True
            
            if hasKey and hasNotKey:
                raise NameError("all elements should have key or not have key")
            
            self.code.append(f"new {self.place} {self.dataType['size']}")
            if hasKey:
                kv = {}
                for el in elList:
                    if el.key in kv:
                        raise NameError("field key repeated")
                    if el.key not in self.dataType['keyTypes']:
                        raise NameError("Unknown field key")
                    kv[el.key] = el.val
                
                for key, t in self.dataType['keyTypes'].items():
                    if key in kv:
                        val = kv[key]
                    else:
                        val = zeroLit(stm,t)

                    if isinstance(val, ExprNode):
                        self.addChild(StructFieldNode(key, val))
                        self.code.append(f'{addr} = {self.place}.addr + {self.dataType["offset"][key]}')
                        self.code.append(f'* {addr} = {val.place}')
                    else:
                        raise SyntaxError("Not changing literals to expressions properly")
            
            else:
                if len(elList) != len(self.dataType['keyTypes']):
                    raise NameError("Unequal arguments for structure")

                for (key, t), val in zip(self.dataType['keyTypes'].items(), elList):
                    if not utils.isTypeCastable(stm, t, val.dataType):
                        raise TypeError(f"Type of {key} of struct: {t['name']} doesn't match with type of {val.label} : {val.dataType['name']}")
                    
                    if isinstance(val, ExprNode):
                        self.addChild(StructFieldNode(key, val))
                        self.code.append(f'{addr} = {self.place}.addr + {self.dataType["offset"][key]}')
                        self.code.append(f'* {addr} = {val.place}')
                    else:
                        raise SyntaxError("Not changing literals to expressions properly")

        elif self.dataType['name'] == 'array':
            if len(elList) > int(self.dataType['length']):
                raise "Too many arguments"
            vis = [False]*self.dataType['length']
            children = [None]*self.dataType['length']
            prevKey = -1
            for el in elList:
                if isinstance(el, KeyValNode):
                    if not isinstance(el.key, int):
                        raise NameError("index should be of type int for arrays")
                    prevKey = el.key
                else:
                    prevKey += 1

                if prevKey >= self.dataType['length']:
                    raise "index overflow"
                if vis[prevKey]:
                    raise NameError("Duplicate index in array")
                vis[prevKey] = True
                children[prevKey] = el

            if isinstance(self.dataType["baseType"], str):
                elSize = basicTypeSizes[self.dataType["baseType"]]
            else:
                elSize = self.dataType["baseType"]["size"]
            self.code.append(f"new {self.place} {elSize*self.dataType['length']}")
            self.code.append(f'{addr} = {self.place}.addr')
            for i in range(self.dataType['length']):
                if not vis[i]:
                    self.addChild(zeroLit(stm,self.dataType['baseType']))
                    self.code.append(f'* {addr} = 0')
                else:
                    if isinstance(children[i], NodeList):
                        if isinstance(self.dataType['baseType'], str):
                            raise NameError("Normal literal should not be of type NodeList")
                        else:
                            children[i] = CompositeLitNode(stm, self.dataType['baseType'], children[i])
                    
                    self.addChild(children[i])
                    self.code.append(f'* {addr} = {children[i].place}')
                
                self.code.append(f'{addr} = {addr} + {elSize}')

        elif self.dataType['name'] == 'slice':
            vis = []
            children = []
            prevKey = -1
            for el in elList:
                if isinstance(el, KeyValNode):
                    if not isinstance(el.key, int):
                        raise NameError("index should be of type int for arrays")
                    prevKey = el.key
                else:
                    prevKey += 1
                
                if prevKey >= len(children)-1:
                    children.extend([None]*(prevKey+1-len(children)))
                    vis.extend([False]*(prevKey+1-len(vis)))

                if vis[prevKey]:
                    raise NameError("Duplicate index in array")
                vis[prevKey] = True
                if isinstance(el, ExprNode):
                    children[prevKey] = el
                elif self.dataType['baseType'] in compositeTypes:
                    children[prevKey] = CompositeLitNode(self.dataType['baseType'], el)
                else:
                    children[prevKey] = LitNode(el, self.dataType['baseType'])

            self.dataType['length'] = len(children)
            self.dataType['capacity'] = self.dataType['length']

            if isinstance(self.dataType["baseType"], str):
                elSize = basicTypeSizes[self.dataType["baseType"]]
            else:
                elSize = self.dataType["baseType"]["size"]
            self.code.append(f"new {self.place} {elSize*self.dataType['length']}")
            self.code.append(f'{addr} = {self.place}.addr')
            for i in range(self.dataType['length']):
                if not vis[i]:
                    self.addChild(zeroLit(stm,self.dataType['baseType']))
                    self.code.append(f'* {addr} = 0')
                else:
                    if isinstance(children[i], NodeList):
                        if isinstance(self.dataType['baseType'], str):
                            raise NameError("Normal literal should not be of type NodeList")
                        else:
                            children[i] = CompositeLitNode(stm, self.dataType['baseType'], children[i])
                    
                    self.addChild(children[i])
                    self.code.append(f'* {addr} = {children[i].place}')
                
                self.code.append(f'{addr} = {addr} + {elSize}')

        # TODO add map comoposite
        elif self.dataType['name'] == 'map':
            # print("TODO: Map not implemented in CompositeLitNode")
            # Working with elList
            keys = []

            for element in elList:
                if not isinstance(element, KeyValNode):
                    raise TypeError("All the elements should be of key : val type")
                key = element.key
                val = element.val

                ## TODO: Check type for key
                keytype = element.keytype 

                if not utils.isTypeCastable(stm, keytype, self.dataType['KeyType']):
                    raise TypeError("Key not typecastable to map's key dataType")

                if key in keys:
                    raise DuplicateKeyError("Key " + key + "already assigned")
                else:
                    keys.append(key)

                if not utils.isTypeCastable(stm, self.dataType['ValueType'], val.dataType):
                    raise TypeError("Value cannot be typecasted to required datatype for key: " + key)

                self.addChild(element)    

    def __str__(self):
        if self.dataType['name'] == 'array':
            return f'ARRAY[{self.dataType["length"]}]'
        elif self.dataType['name'] == 'slice':
            return f'SLICE[{self.dataType["length"]}:{self.dataType["capacity"]}]'
        elif self.dataType['name'] == 'map':
            key = self.dataType['KeyType']['name']
            val = self.dataType['ValueType']['name']
            return f'MAP[{key}:{val}]'
        else:
            return f'{self.dataType["name"]}'

class StructFieldNode(Node):
    def __init__(self, key, val):
        super().__init__()
        self.key = key
        self.type = val
        self.dataType = val.dataType
        self.addChild(key, val)

    def __str__(self):
        return ":"

class OpNode(Node):
    def __init__(self, operator):
        super().__init__()
        self.operator = operator

    def __str__(self):
        return self.operator

class KeyValNode(Node):
    def __init__(self, key, val):
        super().__init__()
        self.key = key.label
        self.keytype = key.dataType
        self.val = val
        self.addChild(key)
        self.addChild(val)
    
    def __str__(self):
        return f':'

class FuncNode(Node):
    def __init__(self, nameNode, paramNode, returnNode, bodyNode):
        super().__init__()
        self.addChild(nameNode, paramNode, returnNode, bodyNode)
    
    def __str__(self):
        return "FUNC"

class FuncParamNode(Node):
    def __init__(self, params):
        super().__init__()
        self.dataType = []
        self.addChild(*params)
        # for param in params:
        #     self.dataType.append(param.dataType)
    
    def addChild(self, *children):
        super().addChild(*children)
        for child in children:
            self.dataType.append(child.dataType)

    def __str__(self):
        return "PARAMS"

class FuncReturnNode(Node):
    def __init__(self, params):
        super().__init__()
        self.dataType = []
        self.addChild(*params)
    
    def addChild(self, *children):
        super().addChild(*children)
        for child in children:
            if isinstance(child.dataType, list):
                self.dataType.extend(child.dataType)
            else:
                self.dataType.append(child.dataType)

    def __str__(self):
        return "RETURN-TYPE"


class BlockNode(Node):
    def __init__(self, statements):
        super().__init__()
        self.addChild(statements)
    
    def __str__(self):
        return "{}"

class ExprNode(Node):
    def __init__(self, dataType, label = None, operator = None, isConst = False, isAddressable = False, val = None, pkg=None):
        super().__init__()
        self.children = []
        self.label = label
        self.dataType = dataType
        self.operator = operator
        self.isConst = isConst # For constant folding
        self.val = val # For saving the value returned by constant folding
        self.isAddressable = isAddressable
        self.pkg = pkg

    def __str__(self):
        if self.pkg is not None:
            return '.'
        if self.isConst:
            if 'name' in self.dataType and self.dataType['name'] == 'string':
                return f'\\\"{self.label[1:-1]}\\\"'
            return str(self.val)
        if self.operator is None:
            if 'name' in self.dataType and self.dataType['name'] == 'string':
                return f'\\\"{self.label}\\\"'
            return self.label
        else:
            return self.operator

class NodeListNode(Node):
    def __init__(self, children):
        super().__init__()
        self.addChild(*children)

    def __str__(self):
        return "LIST"
    

class DotNode(Node):
    def __init__(self, selectorNode):
        super().__init__()
        self.addChild(selectorNode)
    
    def __str__(self):
        return f'DOT'

class IndexNode(Node):
    def __init__(self, arrNode, indexNode, dataType = None, label="Node"):
        super().__init__(label)
        self.addChild(arrNode, indexNode)
        self.dataType = dataType
    def __str__(self):
        return f'[]'

class SliceNode(Node):
    def __init__(self, arrNode, lIndexNode, rIndexNode, maxIndexNode, label="Node"):
        super().__init__(label)
        self.lIndexNode = lIndexNode
        self.rIndexNode = rIndexNode
        self.maxIndexNode = maxIndexNode
        self.addChild(arrNode, lIndexNode, rIndexNode, maxIndexNode)
    
    def __str__(self):
        return f'[:]'

class FuncCallNode(Node):
    def __init__(self, funcNode, paramsNode):
        super().__init__()
        self.addChild(funcNode, *paramsNode)
    
    def __str__(self):
        return f'func()'

class BuiltinFuncNode(FuncCallNode):
    # INFO: If you add other builtins remember to add dataType which is return type, code and place fields.
    
    def __init__(self, name, args):
        temp = []
        for expr in args:
            if isinstance(expr, list):
                temp.extend(expr)
            else:
                temp.append(expr)

        args = temp
        super().__init__(name, args)
        self.isAddressable = False

        self.dataType = {}
        self.place = "builtin"
        code = []
        if name.label == "__syscall":
            if args[0].val is None or not isinstance(args[0].val, int):
                raise Exception("First argument to syscall must be constant")

            self.place = f"__syscall_{args[0].val}"
            for arg in args[1:]:
                self.code.append(f"params {arg.place}")
            code.append(f'call #syscall_{args[0].val}')
            
            if args[0].val == 11:
                if len(args) != 2:
                    raise Exception("Incorrect number of arguments")
            else:
                raise Exception("Syscall not implemented for the given number")

        self.code.extend(code)
    
    
    def __str__(self):
        return f'BUILTIN'
        

class LabelNode(Node):
    def __init__(self, labelNode, statementNode):
        super().__init__()
        self.addChild(labelNode, statementNode)
    
    def __str__(self):
        return f'LABEL'
    
class LabelStatementNode(Node):
    def __init__(self, statementNode, lineno):
        super().__init__()
        self.statementNode = statementNode
        self.statementLabel = lineno
        self.addChild(statementNode)

    def __str__(self):
        return f'LINE:{self.statementLabel}'

class GotoNode(Node):
    def __init__(self, labelNode):
        super().__init__()
        self.addChild(labelNode)
    
    def __str__(self):
        return "GOTO"

class ReturnNode(Node):
    def __init__(self, valsNode):
        super().__init__()
        self.addChild(*valsNode)
    
    def __str__(self):
        return "RETURN"

class BreakNode(Node):
    def __init__(self, labelNode=None):
        super().__init__()
        if labelNode:
            self.addChild(labelNode)
    
    def __str__(self):
        return "BREAK"

class ContinueNode(Node):
    def __init__(self, labelNode=None):
        super().__init__()
        if labelNode:
            self.addChild(labelNode)
    
    def __str__(self):
        return "CONTINUE"

class FallthroughNode(Node):
    def __str__(self):
        return "FALLTHROUGH"

class EmptyNode(Node):
    def __str__(self):
        return ""

class IncNode(Node):
    def __init__(self, exprNode):
        super().__init__()
        self.addChild(exprNode)
    
    def __str__(self):
        return f'++'

class DecNode(Node):
    def __init__(self, exprNode):
        super().__init__()
        self.addChild(exprNode)
    
    def __str__(self):
        return f'--'

class IfNode(Node):
    def __init__(self, initNode, condNode, thenNode, elseNode):
        super().__init__()
        self.addChild(initNode, condNode, thenNode, elseNode)

    def __str__(self):
        return f'IF'

class ThenNode(Node):
    def __init__(self, blockNode):
        super().__init__()
        self.addChild(blockNode)
    
    def __str__(self):
        return f'THEN'

class ElseNode(Node):
    def __init__(self, blockNode):
        super().__init__()
        self.addChild(blockNode)
    
    def __str__(self):
        return f'ELSE'

class SwitchNode(Node):
    def __init__(self, smtNode, varNode, casesNode):
        super().__init__()
        self.addChild(smtNode, varNode, casesNode)
    
    def __str__(self):
        return "SWITCH"

class CasesNode(Node):
    def __init__(self, caseValsNode, instrNode):
        super().__init__()
        self.instrNode = instrNode
        self.addChild(caseValsNode, instrNode)
    
    def __str__(self):
        return "CASES"

class CaseNode(Node):
    def __init__(self, caseValNode):
        super().__init__()
        self.addChild(caseValNode)
        self.dataType = None

    def __str__(self):
        return "CASE"

class DefaultNode(Node):
    def __str__(self):
        return "DEFAULT"    

class ForNode(Node):
    def __init__(self, clauseNode, instrNode):
        super().__init__()
        self.addChild(clauseNode, instrNode)
    
    def __str__(self):
        return "FOR"

class ForClauseNode(Node):
    def __init__(self, initNode, condNode, updNode):
        super().__init__()
        self.addChild(initNode, condNode, updNode)
    
    def __str__(self):
        return "CLAUSE"

class ForRangeNode(Node):
    def __init__(self, paramsNode, iterableNode):
        super().__init__(self)
        self.addChild(*paramsNode, iterableNode)
        self.vartemp = None
    
    def __str__(self):
        return "RANGE"

### TYPE Class
class Type:
    def __init__(self, dataType = {}):
        self.code = []
        self.children = []
        self.dataType = dataType
    
    def addChild(self, *children):
        if children:
            self.children.extend(children)
            for child in children:
                if child and hasattr(child, "code"):
                    self.code.extend(child.code)

class ElementaryType(Type):
    def __init__(self, dataType = {}):
        super().__init__()
        self.dataType = dataType
        self.dataType["size"] = basicTypeSizes[dataType['name']]
        self.children = None
    
    def __str__(self):
        return self.dataType['baseType']

class PointerType(Type):
    def __init__(self, dataType = {}):
        super().__init__()    
        self.dataType = {'name': 'pointer', 'size': 4, 'level': 1, 'baseType': dataType}
        if not isinstance(dataType, str):
            self.dataType['level'] += dataType['level']
        self.children = None
    
    def __str__(self):
        x = self.dataType['baseType'] 
        return f'*{x}'

class ParenType(Type):
    def __init__(self, dataType = {}):
        super().__init__()
        self.dataType = dataType
        self.children = None
    
    def __str__(self):
        x = self.dataType['baseType'] 
        return f'({x})'

class BrackType(Type):
    def __init__(self, elementType = {}, length=None):
        super().__init__()
        # Not storing the node about constant length of array type further
        self.length = None
        self.dataType = {
            'baseType' : elementType,
            'size' : 12,
            'level': elementType['level']+1,
            'name' : 'slice' if length is None else 'array'
        }
        if length:
            self.dataType['length'] = length.val
            self.length = length.val
        self.addChild(elementType, length)
    
    def __str__(self):
        return f'[]'

class MapType(Type):
    def __init__(self, keyType, valueType):
        super().__init__()
        self.dataType = {
            'name': 'map',
            'KeyType': keyType.dataType,
            'ValueType': valueType.dataType,
            'size': 12
        }

        self.children = [keyType, valueType]
    
    def __str__(self):
        return f'MAP'

class StructType(Type):
    def __init__(self, fieldList):
        super().__init__()
        size=0
        self.dataType = {'name': "struct", 'keyTypes': {}, 'level' : 0, 'offset': {}}
        for field in fieldList:
            if field.dataType['key'] in self.dataType['keyTypes']:
                raise NameError("Can not have same key names in two fields of structure")
            else:
                self.dataType['keyTypes'][field.dataType['key']] = field.dataType['dataType']
                self.dataType['offset'][field.dataType['key']] = size
                size += field.dataType['size']
        
        self.dataType['size'] = size

        self.addChild(*fieldList)
    
    def __str__(self):
        return f'STRUCT'

class StructFieldType(Type):
    def __init__(self, key, type):
        super().__init__()
        self.dataType = {'name': "field", 'key': key.label, 'dataType': type.dataType, 'size': type.dataType['size']}
        self.addChild(key, type)
    
    def __str__(self):
        return f':'

# class FuncType(Type):
#     def __init__(self, paramsType, returnType):
#         super().init()
#         self.addChild(returnType, *paramsType)
    
#     def __str__(self):
#         return f'FUNC'

class FuncParamType(Type):
    def __init__(self):
        super().__init__()
        self.dataType = []
        self.children = []
    
    def addChild(self, type):
        self.dataType.append(type.dataType)
        self.children.append(type)
        for child in self.children:
                if child and hasattr(child, "code"):
                    self.code.extend(child.code)

    def __str__(self):
        return '()'

# class ParamType(Type):
#     def __init__(self, key, dataType = {}):
#         super().__init__()
#         self.addChild(key, dataType)
    
#     def __str__(self):
#         return f'='

## Exceptions
class ValueNotUsedError(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return repr(self.message) 

class LogicalError(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return repr(self.message)

class NodeList(list):
    def __init__(self, *args):
        self.code = []
        if len(args) > 0:
            super(NodeList, self).__init__(args[0])
            for elem in args[0]:
                if elem and hasattr(elem, "code"):
                    self.code.extend(elem.code)
        else:
            super(NodeList, self).__init__()

    def append(self, x):
        super().append(x)
        if x and hasattr(x, "code"):
            self.code.extend(x.code)
    
    def extend(self, x):
        super().extend(x)
        if x:
            for child in x:
                if child and hasattr(child, "code"):
                    self.code.extend(child.code)

    def __dict__(self):
        return {'children' : super().__dict__, 'code': self.code}

## Wrapper class
class Wrapper:
    def __init__(self, val):
        self.val = val