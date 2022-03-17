basicTypes = ['int', 'float', 'string', 'rune']
basicTypeSizes = {'int':4, 'float': 4, 'string': 4, 'rune': 1}
class ScopeTableError(Exception):
    pass

class node:
    def __init__(self, grammar):
        self.grammar = grammar
        self.exprList = []
        self.exprTypeList = []
        self.metadata = {}

class scope:
    def __init__(self):
        self.symTable = {}
        self.parentScope = None
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