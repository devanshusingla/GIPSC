from enum import Enum, auto

# basicTypes = ['int', 'float', 'string', 'rune']
# basicTypeSizes = {'int':4, 'float': 4, 'string': 4, 'rune': 1}
# class ScopeTableError(Exception):
#     pass

# class node:
#     def __init__(self, grammar):
#         self.grammar = grammar
#         self.exprList = []
#         self.exprTypeList = []
#         self.metadata = {}

# class scope:
#     def __init__(self, parentScope=None):
#         self.symTable = {}
#         self.parentScope = parentScope
#         self.avlTypes = basicTypes.copy()
#         self.avlTypeSizes = basicTypeSizes.copy()

#     def insert(self, id, typeAttr):
#         if id not in self.symTable:
#             self.symTable[id] = {}
#             self.symTable[id]['type'] = typeAttr
#         else:
#             # Should an error be raised?
#             # How to handle shadowing of identifiers with 
#             # it being previously declared in parent scope
#             raise ScopeTableError("Identifier is being redeclared")

#     def updateAttr(self, id, **kwargs):
#         if id not in self.symTable:
#             raise ScopeTableError("Identifier has not been declared")
#         for key, value in kwargs.items():
#             self.symTable[id][key] = value

#     def setParent(self, parent):
#         # Does this store only the reference?
#         self.parent = parent
    
#     def inheritTypes(self, prevScope):
#         for avlType in prevScope.avlTypes:
#             if avlType not in self.avlTypes:
#                 self.avlTypes.append(avlType)
        
#         for avlTypeSize in prevScope.avlTypeSizes:
#             if avlTypeSize not in self.avlTypeSizes:
#                 self.avlTypeSizes.append(avlTypeSize)

class DataType(Enum):
    STR = auto()

## Symbol Table Maker
class SymTableMaker:
    def __init__(self):
        self.symTable = {0: {}}
        self.stack = [0]
        self.id = 0
        self.nextId = 1
    
    def newScope(self):
        self.symTable[self.nextId] = {}
        self.stack.append(self.nextId)
        self.id = self.nextId
        self.nextId += 1
    
    def exitScope(self):
        self.stack.pop()
        self.id = self.stack[-1]
    
    def add(self, ident, info):
        self.symTable[self.id][ident] = info
    
    def scope(self, ident):
        i = len(self.stack) - 1
        while self.stack[i] != 0:
            if ident in self.stack[i]:
                break
            else:
                i -= 1
        
        return self.stack[i]

## AST Abstract Node Class
class Node:
    def __init__(self):
        self.child = []
    
    def addChild(self, *children):
        for child in children:
            self.child.append(child)

## AST Node Classes
class FileNode(Node):
    def addChild(self, pkgName, importDecl, globalDecl):
        self.child.append(pkgName)
        self.child.append(importDecl)
        self.child.append(globalDecl)

class ImportNode(Node):
    pass

class ImportPathNode(Node):
    def addChild(self, alias, path):
        self.child.append(alias)
        self.child.append(path)

class IdentNode(Node):
    def __init__(self, scope, dataType, val):
        super().__init__()
        self.child = None
        self.scope = scope
        self.dataType = dataType
        self.val = val

class LitNode(Node):
    def __init__(self, dataType, val):
        super().__init__()
        self.child = None
        self.dataType = dataType
        self.val = val