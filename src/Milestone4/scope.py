basicTypes = ['int', 'float', 'string', 'rune']
basicTypeSizes = {'int':4, 'float': 4, 'string': 4, 'rune': 1}
class ScopeTableError(Exception):
    def __init__(self, message):
        super().__init__(message)

class node:
    def __init__(self, name):
        self.name = name
        self.ast = []
        self.exprList = []
        self.exprTypeList = []
        self.metadata = {}
    
    def __repr__(self):
        return f"Name:{self.name}\nExprList:{self.exprList}\nExprSizeList:{self.exprTypeList}\nMetadata:{self.metadata}\nAST:{self.ast}"

class scope:
    def __init__(self, parentScope=None):
        self.symTable = {}
        self.parentScope = parentScope
        self.avlTypes = basicTypes.copy()
        self.avlTypeSizes = basicTypeSizes.copy()

    def insert(self, id, typeAttr):
        if id not in self.symTable:
            self.symTable[id] = {}
            self.symTable[id]['type'] = typeAttr
        else:
            # Should an error be raised?
            # How to handle shadowing of identifiers with 
            # it being previously declared in parent scope
            raise ScopeTableError("Identifier is being redeclared")

    def updateAttr(self, id, **kwargs):
        if id not in self.symTable:
            raise ScopeTableError("Identifier has not been declared")
        for key, value in kwargs.items():
            self.symTable[id][key] = value

    def setParent(self, parent):
        # Does this store only the reference?
        self.parent = parent
    
    def inheritTypes(self, prevScope):
        for avlType in prevScope.avlTypes:
            if avlType not in self.avlTypes:
                self.avlTypes.append(avlType)
        
        for avlTypeSize in prevScope.avlTypeSizes:
            if avlTypeSize not in self.avlTypeSizes:
                self.avlTypeSizes.append(avlTypeSize)
    
    def __repr__(self):
        return f"SymTable: {self.symTable}\nParentScopeId:{self.parentScope}\nAvlTypes:{self.avlTypes}\n"