from enum import Enum, auto

basicTypes = ['int', 'byte', 'int8', 'int16', 'int32', 'int64', 'float32', 'float64', 'uint8', 'uint16', 'uint32', 'uint64' 'string', 'rune', 'bool']
basicTypeSizes = {'int':4, 'float': 4, 'string': 4, 'rune': 1}

class ScopeTableError(Exception):
    pass

class scope:
    def __init__(self, parentScope=None):
        self.localsymTable = {}
        self.parentScope = parentScope
        self.avlTypes = basicTypes.copy()
        self.typeDefs = {}

    def insert(self, id, info):
        self.localsymTable[id] = info

    def getinfo(self, id):
        return self.localsymTable.get(id,None)

    def updateAttr(self, id, **kwargs):
        if id not in self.localsymTable:
            raise ScopeTableError("Identifier has not been declared")
        for key, value in kwargs.items():
            self.localsymTable[id][key] = value

    def addType(self, type):
        self.avlTypes.append(type)

    def setParent(self, parent):
        # Does this store only the reference?
        self.parent = parent
    
    def inheritTypes(self, prevScope):
        for avlType in prevScope.avlTypes:
            if avlType not in self.avlTypes:
                self.avlTypes.append(avlType)

## Symbol Table Maker
class SymTableMaker:
    def __init__(self):
        self.symTable = {}
        self.symTable[0] = scope()
        self.functions = {}
        self.stack = [0]
        self.id = 0
        self.nextId = 1

    def addFunction(self, label, info):
        self.functions[label] = info
    
    def newScope(self):
        self.symTable[self.nextId] = scope(parentScope = self.id)
        self.stack.append(self.nextId)
        self.id = self.nextId
        self.nextId += 1
    
    def exitScope(self):
        self.stack.pop()
        self.id = self.stack[-1]
    
    def add(self, ident, info):
        self.symTable[self.id].insert(ident, info)

    def get(self, ident, scope=None):
        if scope is None:
            return self.symTable[self.id].getinfo(ident)
        else:
            return self.symTable[scope].getinfo(ident)

    def findType(self, type):
        i = len(self.stack) - 1
        while i >= 0:
            if type in self.symTable[i].avlTypes or type in self.symTable[i].typeDefs:
                break
            else:
                i -= 1
            
        if i == -1:
            return -1 
        else:
            return self.stack[i]
    
    def getScope(self, ident):
        i = len(self.stack) - 1
        while i >= 0:
            if ident in self.symTable[i].localsymTable:
                break
            else:
                i -= 1

        if i == -1:
            return i
        else:
            return self.stack[i]

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
    def __init__(self, alias, path):
        super().__init__()
        self.addChild(alias, path)
    
    def __str__(self):
        return f'PKG'

class DeclNode(Node):
    def __str__(self):
        return "GLOBAL"

class IdentNode(Node):
    def __init__(self, scope, label, dataType = None, val = 0, isConst = False):
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
    def __init__(self, dataType, label):
        super().__init__()
        self.children = None
        self.dataType = dataType
        if self.dataType == "string":
            self.label = label[1:-1]
        else:
            self.label = label
    
    def __str__(self):
        if self.dataType == "string":
            return f'\\\"{self.label}\\\"'
        else:
            return self.label

class OpNode(Node):
    def __init__(self, operator):
        super().__init__()
        self.operator = operator

    def __str__(self):
        return self.operator

class KeyValNode(Node):
    def __init__(self, key, val):
        super().__init__()
        self.children.append(key, val)
    
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
        self.addChild(*params)
    
    def __str__(self):
        return "PARAMS"

class FuncReturnNode(Node):
    def __init__(self, returnNode):
        super().__init__()
        self.returnNode = returnNode
    
    def __str__(self):
        return "RETURN"

class BlockNode(Node):
    def __init__(self, statements):
        super().__init__()
        self.addChild(*statements)
    
    def __str__(self):
        return "{}"

class ExprNode(Node):
    def __init__(self, dataType, label = None, operator = None, isConst = False):
        super().__init__()
        self.children = []
        self.label = label
        self.dataType = dataType
        self.operator = operator
        self.isConst = isConst # For constant folding

    def __str__(self):
        if self.operator is None:
            return self.label 
        else:
            return self.operator

class DotNode(Node):
    def __init__(self, label="Node"):
        super().__init__(label)
    
    def __str__(self):
        return f'DOT'

class IndexNode(Node):
    def __init__(self, arrNode, indexNode, label="Node"):
        super().__init__(label)
        self.addChild(arrNode, indexNode)
    
    def __str__(self):
        return f'[]'

class SliceNode(Node):
    def __init__(self, arrNode, lIndexNode, rIndexNode, maxIndexNode, label="Node"):
        super().__init__(label)
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

### TYPE Class
class Type:
    def __init__(self):
        self.children = []
    
    def addChild(self, *children):
        if children:
            self.children.extend(children)

class ElementaryType(Type):
    def __init__(self, type):
        super().__init__()
        self.type = type
        self.children = None
    
    def __str__(self):
        return self.type

class PointerType(Type):
    def __init__(self, type):
        super().__init__()
        self.type = type
        self.children = type.children
    
    def __str__(self):
        return f'*{self.type}'

class ParenType(Type):
    def __init__(self, type):
        super().__init__()
        self.type = type
        self.children = type.children
    
    def __str__(self):
        return f'({self.type})'

class BrackType(Type):
    def __init__(self, type, length=None):
        super().__init__()
        self.addChild(length, type)
    
    def __str__(self):
        return f'[]'

class MapType(Type):
    def __init__(self, keyType, valueType):
        super().__init__()
        self.children = [keyType, valueType]
    
    def __str__(self):
        return f'MAP'

class StructType(Type):
    def __init__(self, elList):
        super().__init__()
        self.addChild(elList)
    
    def __str__(self):
        return f'STRUCT'

class StructFieldType(Type):
    def __init__(self, key, type, tag):
        super().__init__()
        self.addChild(key, type, tag)
    
    def __str__(self):
        return f':'

class FuncType(Type):
    def __init__(self, paramsType, returnType):
        super().init()
        self.addChild(returnType, *paramsType)
    
    def __str__(self):
        return f'FUNC'

class ParamType(Type):
    def __init__(self, key, type):
        super().__init__()
        self.addChild(key, type)
    
    def __str__(self):
        return f'='