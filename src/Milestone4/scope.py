from enum import Enum, auto

basicTypes = ['int', 'float', 'string', 'rune']
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

    def insert(self, id, typeAttr):
        self.localsymTable[id] = {}
        self.localsymTable[id]['type'] = typeAttr

    def updateAttr(self, id, **kwargs):
        if id not in self.localsymTable:
            raise ScopeTableError("Identifier has not been declared")
        for key, value in kwargs.items():
            self.localsymTable[id][key] = value

    def setParent(self, parent):
        # Does this store only the reference?
        self.parent = parent
    
    def inheritTypes(self, prevScope):
        for avlType in prevScope.avlTypes:
            if avlType not in self.avlTypes:
                self.avlTypes.append(avlType)

class DataType(Enum):
    STR = auto()
    INT = auto()
    FLOAT = auto()
    RUNE = auto()

## Symbol Table Maker
class SymTableMaker:
    def __init__(self):
        self.symTable = {}
        self.symTable[0] = scope()
        self.stack = [0]
        self.id = 0
        self.nextId = 1
    
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
    
    def getScope(self, ident):
        i = len(self.stack) - 1
        while self.stack[i] != 0:
            if ident in self.stack[i].localsymTable:
                break
            else:
                i -= 1
        
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
    def addChild(self, pkgName, importDecl, globalDecl):
        self.children.append(pkgName)
        self.children.append(importDecl)
        self.children.append(globalDecl)

class ImportNode(Node):
    pass

class DeclNode(Node):
    pass

class ImportPathNode(Node):
    def addChild(self, alias, path):
        self.children.append(alias)
        self.children.append(path)

class ExprNode(Node):
    def __init__(self, dataType, operator):
        super().__init__()
        self.children = []
        self.dataType = dataType
        self.operator = operator

class IdentNode(Node):
    def __init__(self, scope, dataType, val):
        super().__init__()
        self.children = None
        self.scope = scope
        self.dataType = dataType
        self.val = val

class TypeNode(Node):
    def __init__(self, scope, dataType):
        self.val = dataType
        self.children = None
        self.scope = scope

class LitNode(Node):
    def __init__(self, dataType, val):
        super().__init__()
        self.children = None
        self.dataType = dataType
        self.val = val

class FuncDeclNode(Node):
    pass