from enum import Enum, auto

basicTypes = ['int', 'byte', 'int8', 'int16', 'int32', 'int64', 'float32', 'float64', 'uint8', 'uint16', 'uint32', 'uint64' 'string', 'rune', 'bool']
basicTypeSizes = {'int':4, 'float': 4, 'string': 4, 'rune': 1}

class ScopeTableError(Exception):
    pass

# class node:
#     def __init__(self, grammar):
#         self.grammar = grammar
#         self.exprList = []
#         self.exprTypeList = []
#         self.metadata = {}

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
    def __init__(self):
        self.children = []
    
    def addChild(self, *children):
        for child in children:
            self.children.append(child)

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

### TYPE Nodes
class TypeNode(Node):
    pass

class ElementaryTypeNode(TypeNode):
    def __init__(self, type):
        super().__init__()
        self.type = type
        self.children = None
    
    def __str__(self):
        super().__init__()
        return self.type

class PointerTypeNode(TypeNode):
    def __init__(self, typeNode):
        super().__init__()
        self.typeNode = typeNode
        self.children = typeNode.children
    
    def __str__(self):
        return f'*{self.typeNode}'

class ParenTypeNode(TypeNode):
    def __init__(self, typeNode):
        super().__init__()
        self.typeNode = typeNode
        self.children = typeNode.children
    
    def __str__(self):
        return f'({self.typeNode})'

class BrackTypeNode(TypeNode):
    def __init__(self, typeNode, length=None):
        super().__init__()
        self.addChild(length, typeNode)
    
    def __str__(self):
        return f'[]'

class MapTypeNode(TypeNode):
    def __init__(self, keyTypeNode, valueTypeNode):
        super().__init__()
        self.children = [keyTypeNode, valueTypeNode]
    
    def __str__(self):
        return f'MAP'

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
    def __init__(self, *params):
        super().__init__()
        self.addChild(params)
    
    def __str__(self):
        return "PARAMS"

class FuncReturnNode(Node):
    def __init__(self, returnNode):
        super().__init__()
        self.returnNode = returnNode
    
    def __str__(self):
        return "RETURN"

class FuncBodyNode(Node):
    def __init__(self, statements):
        super().__init__()
        self.addChild(statements)
    
    def __str__(self):
        return "BODY"

class ExprNode(Node):
    def __init__(self, dataType, label = None, operator = None, isConst = False):
        super().__init__()
        self.children = []
        self.label = label
        self.dataType = dataType
        self.operator = operator
        self.isConst = isConst # For constant folding