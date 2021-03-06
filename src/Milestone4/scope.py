basicTypes = ['int', 'byte', 'int8', 'int16', 'int32', 'int64', 'float32', 'float64', 'uint8', 'uint16', 'uint32', 'uint64', 'string', 'rune', 'bool']
basicTypeSizes = {'int':4, 'float': 4, 'string': 12, 'rune': 2, 'byte': 1, 'int8': 1, 'int16': 2, 'int32': 4, 'int64': 8, 'uint8': 1, 'uint16': 2, 'uint32': 4, 'uint64': 8, 'float32': 4, 'float64': 8, 'bool': 1}
compositeTypes = ['struct', 'array', 'slice', 'map']
from copy import deepcopy
def zeroLit(dataType):
    if dataType == 'int':
        dt = {'name' : 'int', 'baseType' : 'int', 'level' : 0}
        return ExprNode(dt, label='0', operator=None, isConst=True, isAddressable=False, val=0)
        # return LitNode('0', dataType, isConst=True, val=0)
    else:
        raise NotImplementedError

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
        self.negoffset=0

    def insert(self, id, info, isarg=False):
        if not isarg:
            info['offset'] = self.offset
            self.offset += info['dataType']['size']
        else:
            self.negoffset -= info['dataType']['size']
            info['offset'] = self.negoffset

        self.localsymTable[id] = info


    def getinfo(self, id):
        return self.localsymTable.get(id,None)

    def updateAttr(self, id, **kwargs):
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
        self.stack = [0]
        self.id = 0
        self.nextId = 1
        self.currentReturnType = None
        self.forDepth = 0
        self.switchDepth = 0
        self.labels = {}
        self.currentLabel = None
        self.pkgs = {}
        # self.labels: dict[str] -> dict[]
        # self.labels[label] = {
        # 'scopeTab' : _ , 
        # 'mappedName' : _, 
        # 'expecting' : _, 
        # 'lineno' : _
        # 'prevGotos' : [
        #  (scopeTab, lineno), (scopeTab, lineno) ...
        # ]}
        self.nextLabel = 0
        self.addBuiltInFuncs()

    def addFunction(self, label, info):
        self.functions[label] = deepcopy(info)
        self.newScope()
    
    def addType(self, type, typeObj):
        self.symTable[self.id].addType(type, deepcopy(typeObj))

    def newScope(self):
        self.symTable[self.nextId] = scope(self.nextId, parentScope = self.id)
        self.stack.append(self.nextId)
        self.id = self.nextId
        self.nextId += 1
    
    def exitScope(self):
        self.stack.pop()
        self.id = self.stack[-1]
    
    def add(self, ident, info, isarg=False):
        self.symTable[self.id].insert(ident, deepcopy(info), isarg)

    def get(self, ident, scope=None):
        if scope is None:
            if ident in self.functions:
                return deepcopy(self.functions[ident])
            scope = self.getScope(ident)
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
                return self.symTable[j].typeDefs[type]
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
    
    def addBuiltInFuncs(self):
        print("TODO: Add builtin function definitions by parsing or by hard coding")

## AST Abstract Node Class
class Node:
    def __init__(self, label = "Node"):
        self.children = []
        self.label = label
    
    def addChild(self, *children):
        if children:
            self.children.extend(children)

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
        self.dataType = compositeLitType.dataType
        self.children = []
        if not isinstance(elList, list):
            raise NameError("Expected List of values")
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
                        val = zeroLit(t)
                    if isinstance(val, ExprNode):
                        self.children.append(StructFieldNode(key, val))
                    elif t.name in compositeTypes:
                        self.children.append(StructFieldNode(key, CompositeLitNode(t, val)))
                    else:
                        self.children.append(StructFieldNode(key, LitNode(val, t)))
            
            else:
                if len(elList) != len(self.dataType['keyTypes']):
                    raise NameError("Unequal arguments for structure")
                for (key, t), val in zip(self.dataType['keyTypes'].items(), elList):
                    if not utils.isTypeCastable(stm, t, val.dataType):
                        raise TypeError(f"Type of {key} of struct: {t['name']} doesn't match with type of {val.label} : {val.dataType['name']}")
                    if isinstance(val, ExprNode):
                        self.children.append(StructFieldNode(key, val))
                    elif t.name in compositeTypes:
                        self.children.append(StructFieldNode(key, CompositeLitNode(t, val)))
                    else:
                        self.children.append(StructFieldNode(key, LitNode(val, t)))

        elif self.dataType['name'] == 'array':
            if len(elList) > int(self.dataType['length']):
                raise "Too many arguments"
            vis = [False]*self.dataType['length']
            self.children = [None]*self.dataType['length']
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
                self.children[prevKey] = el
                # if self.dataType['baseType'] in compositeTypes:
                #     self.children[prevKey] = CompositeLitNode(self.dataType['baseType'], el)
                # else:
                #     self.children[prevKey] = LitNode(el, self.dataType['baseType'])

            for i in range(self.dataType['length']):
                if not vis[i]:
                    self.children[i] = zeroLit(self.dataType['baseType'])

        elif self.dataType['name'] == 'slice':
            self.vis = []
            self.children = []
            prevKey = -1
            for el in elList:
                if isinstance(el, KeyValNode):
                    if not isinstance(el.key, int):
                        raise NameError("index should be of type int for arrays")
                    prevKey = el.key
                else:
                    prevKey += 1
                
                if prevKey >= len(self.children)-1:
                    self.children.extend([None]*(prevKey+1-len(self.children)))
                    self.vis.extend([False]*(prevKey+1-len(self.vis)))

                if self.vis[prevKey]:
                    raise NameError("Duplicate index in array")
                self.vis[prevKey] = True
                if isinstance(el, ExprNode):
                    self.children[prevKey] = el
                elif self.dataType['baseType'] in compositeTypes:
                    self.children[prevKey] = CompositeLitNode(self.dataType['baseType'], el)
                else:
                    self.children[prevKey] = LitNode(el, self.dataType['baseType'])

            for i in range(len(self.children)):
                if not self.vis[i]:
                    self.children[i] = zeroLit(self.dataType['baseType'])
            self.dataType['length'] = len(self.children)
            self.dataType['capacity'] = self.dataType['length']

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


                self.children.append(element)    

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
        self.children.append(key)
        self.children.append(val)
    
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
        self.addChild(*statements)
    
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
        self.addChild(smtNode, varNode, *casesNode)
    
    def __str__(self):
        return "SWITCH"

class CasesNode(Node):
    def __init__(self, caseValsNode, instrNode):
        super().__init__()
        self.instrNode = instrNode
        self.addChild(*caseValsNode, *instrNode)
    
    def __str__(self):
        return "CASES"

class CaseNode(Node):
    def __init__(self, caseValNode):
        super().__init__()
        self.addChild(caseValNode)

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
    
    def __str__(self):
        return "RANGE"

### TYPE Class
class Type:
    def __init__(self, dataType = {}):
        self.children = []
        self.dataType = dataType
    
    def addChild(self, *children):
        if children:
            self.children.extend(children)

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
        self.dataType = dataType
        self.dataType["size"] = 4
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
        self.dataType = {'name': "struct", 'keyTypes': {}, 'level' : 0}
        for field in fieldList:
            if field.dataType['key'] in self.dataType['keyTypes']:
                raise NameError("Can not have same key names in two fields of structure")
            else:
                self.dataType['keyTypes'][field.dataType['key']] = field.dataType['dataType']
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
    def __init__(self, dataType=[]):
        super().__init__(dataType)
    
    def addChild(self, type):
        self.dataType.append(type.dataType)
        self.children.append(type)

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

## Wrapper class
class Wrapper:
    def __init__(self, val):
        self.val = val