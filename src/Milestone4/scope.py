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
    def __init__(self, dataType, operator, isConst = False):
        super().__init__()
        self.children = []
        self.dataType = dataType
        self.operator = operator
        self.isConst = isConst 

class IdentNode(Node):
    def __init__(self, scope, label, dataType = None, val = 0, isConst = False):
        super().__init__()
        self.children = None
        self.scope = scope
        self.dataType = dataType
        self.label = label
        self.val = val
        self.isConst = isConst

class TypeNode(Node):
    def __init__(self, scope, dataType):
        self.label = dataType
        self.children = None
        self.scope = scope

class LitNode(Node):
    def __init__(self, dataType, label):
        super().__init__()
        self.children = None
        self.dataType = dataType
        self.label = label

class FuncDeclNode(Node):
    pass