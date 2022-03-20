from numpy import iscomplexobj
import ply.yacc as yacc
import ply.lex as lex
import lexer
from lexer import *
import sys
# from scope import *
from scope import *
from utils import *

tokens=lexer.tokens
tokens.remove('COMMENT')
# tokens.append('MULTP')

precedence = (
    # ('left', 'CONV'),
    ('left', 'LBRACE'),
    ('right', 'ASSIGN', 'DEFINE'),
    ('left','IDENT'),
    ('left','SEMICOLON'),
    ('left','COLON'),
    ('left','INT', 'FLOAT', 'IMAG', 'RUNE', 'STRING'),
    ('left','BREAK'),
    ('left','CONTINUE'),
    ('left','RETURN'),
    ('left', 'COMMA'),
    ('right', 'NOT', 'ADD_ASSIGN', 'SUB_ASSIGN', 'MUL_ASSIGN', 'QUO_ASSIGN', 'REM_ASSIGN', 'AND_ASSIGN', 'OR_ASSIGN', 'XOR_ASSIGN', 'SHL_ASSIGN', 'SHR_ASSIGN', 'AND_NOT_ASSIGN'),
    ('left', 'LOR'),
    ('left', 'LAND'),
    ('left', 'EQL', 'NEQ','LSS','LEQ','GTR','GEQ'),
    ('left', 'ADD', 'SUB','OR','XOR'),
    ('left', 'MUL', 'QUO','REM','AND','AND_NOT','SHL','SHR'),
    ('left', 'LPAREN', 'RPAREN', 'LBRACK', 'RBRACK', 'RBRACE', 'INC', 'DEC', 'PERIOD'),
    ('left', 'UMUL'),
)

non_terminals = {}
ignored_tokens = [';', '{', '}', '(', ')', '[', ']', ',']

# ## Start Semantic Analysis
# context = {}
# def setupContext():
#     context['scopeTab'] = {} # Dictionary for Scope Symbol Tables
#     context['nextScopeId'] = 0 # Id for next scope table
#     context['currentScope'] = context['nextScopeId'] # Setting current scope id to 0
#     context['nextScopeId'] += 1 # Incrementing next scope id
#     context['scopeTab'][context['currentScope']] = scope() # Symbol Table
#     context['scopeStack'] = [0] # Stack for active scopes
#     context['forDepth'] = 0 # Inside 0 for loops at present
#     context['switchDepth'] = 0 # Inside 0 switch statements at present
#     context['structSymbolsList'] = None # List of symbols in current struct

# def endContext():
#     # Dump Symbol Table of each function as CSV

#     # Dump AST of functions in DOT format
#     print(context)

# def beginScope():
#     prevScope = context['currentScope']
#     context['currentScope'] = context['nextScopeId']
#     context['scopeStack'].append(context['currentScope'])
#     context['scopeTab'][context['currentScope']] = scope(prevScope)
#     context['scopeTab'][context['currentScope']].inheritTypes(context['scopeTab'][context['prevScope']])
#     context['nextScopeId'] += 1


# def():
#     context['scopeStack'].pop()
    # context['currentScope'] = context['scopeStack'][-1]

###################################################################################
#####################                                        ######################
######                         STARTING GRAMMAR                            ########
#####################                                        ######################
###################################################################################

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
    
# def p_SourceFile(p):
#     """
#     SourceFile : SetupContext PackageClause SEMICOLON ImportDeclMult TopLevelDeclMult
#     """(p)
#     endContext()

# def p_SetupContext(p):
#     """
#     SetupContext :
#     """    
#     p[0] = []
#     setupContext()

# def p_BeginScope(p):
#     """
#     : 
#     """
#     p[0] = []
#     beginScope()

# def p_EndScope(p):
#     """
#     : 
#     """
#     p[0] = []
#    ()

stm = SymTableMaker()
ast = None
    
def p_SourceFile(p):
    """
    SourceFile : PackageClause SEMICOLON ImportDeclMult TopLevelDeclMult
    """
    global ast
    p[0] = FileNode()
    p[0].addChild(p[1], p[3], p[4])
    ast = p[0]

###################################################################################
### Package related grammar
###################################################################################

def p_PackageClause(p):
    """
    PackageClause : PACKAGE IDENT
    """
    p[0] = LitNode(dataType = 'string', label = p[2])

###################################################################################
### Import related grammar
###################################################################################

def p_ImportDeclMult(p):
    """
    ImportDeclMult : ImportDecl SEMICOLON ImportDeclMult
                   |  
    """
    if len(p) > 1:
        p[3].addChild(*p[1])
        p[0] = p[3]
    else:
        p[0] = ImportNode()

def p_ImportDecl(p):
    """
    ImportDecl : IMPORT ImportSpec
               | IMPORT LPAREN ImportSpecMult RPAREN
    """
    if len(p) == 3:
        p[0] = [p[2]]
    elif len(p) == 5:
        p[0] = p[3]

def p_ImportMult(p):
    """
    ImportSpecMult : ImportSpec SEMICOLON ImportSpecMult  
               |
    """
    if len(p) == 1:
        p[0] = []
    elif len(p) == 4:
        p[3].append(p[1])
        p[0] = p[3]

def p_ImportSpec(p):
    """
    ImportSpec : PERIOD ImportPath
              | IDENT ImportPath
              | ImportPath 
    """
    if len(p) == 2:
        p[0] = ImportPathNode()
        p[0].addChild(p[1][1:-1], p[1])
    
def p_ImportPath(p):
    """
    ImportPath : STRING
    """
    p[0] = p[1]

###################################################################################
### Top-Level related grammar
###################################################################################

def p_TopLevelDeclMult(p):
    """
    TopLevelDeclMult : TopLevelDecl SEMICOLON TopLevelDeclMult 
                     |
    """
    if len(p)>1:
        p[3].addChild(*p[1])
        p[0] = p[3]

    if len(p)==1:
        p[0] = DeclNode()

def p_TopLevelDecl(p):
    """
    TopLevelDecl : Decl 
                 | FuncDecl
    """
    p[0] = p[1]

def p_Decl(p):
    """
    Decl : ConstDecl 
         | VarDecl
         | TypeDecl
    """
    p[0] = p[1]

###################################################################################
### Constant Declarations
###################################################################################

def p_ConstDecl(p):
    """
    ConstDecl : CONST ConstSpec
              | CONST LPAREN ConstSpecMult RPAREN
    """
    if len(p)==3:
        p[0]= [p[2]]
    
    else:
        p[0]=p[3]

def p_ConstSpecMult(p):
    """
    ConstSpecMult : ConstSpec SEMICOLON ConstSpecMult 
                  | 
    """
    if len(p)>1:
        p[3].addChild(*[p[1]])
        p[0] = p[3]

    else:
        p[0] = [Node()]

def p_ConstSpec(p):
    """
    ConstSpec : IdentifierList Type ASSIGN ExpressionList 
                | IdentifierList IDENT ASSIGN ExpressionList
                | IdentifierList IDENT PERIOD IDENT ASSIGN ExpressionList
    """
    p[0] = Node()
    for i, child in enumerate(p[1].children):
        # Check redeclaration for identifier list
        latest_scope = stm.getScope(child.label)
        if latest_scope == stm.id:
            raise NameError('Redeclaration of identifier: ' + child, p.lineno(1))
        
        # Check for the presence of type
        present = stm.findType(p[2])
        if present != -1:
            # Add to symbol table
            stm.add(child.label, {'type': p[2], 'isConst': True})
            p[1].children[i].dataType = p[2]
        else:
            raise TypeError('Type not declared/found: ' + p[2], p.lineno(1))

    if len(p[1].children) != len(p[len(p)-1].children):
        raise NameError("Assignment is not balanced", p.lineno(1))

    for i, expression in enumerate(p[len(p)-1].children):
        if expression.dataType != p[2]:
            raise ("Mismatch of type for identifier: " + p[1].children[i].label, p.lineno(1))
    
    for i, expression in enumerate(p[len(p)-1].children):
        p[0].children.append(ExprNode())
        p[0].children[i].addChild([p[1].children[i], p[len(p)-1].children[i]])
        p[0].children[i].operator = 'ASSIGN'
        p[0].children[i].dataType = p[2]
        p[1].children[i].isConst = True
    

    
###################################################################################
### Variable Declarations
###################################################################################

def p_VarDecl(p):
    """
    VarDecl : VAR VarSpec
            | VAR LPAREN VarMult RPAREN
    """
    if len(p)==3:
        p[0]= [p[2]]
    
    else:
        p[0]=p[3]

def p_VarMult(p):
    """
    VarMult : VarSpec SEMICOLON VarMult 
            | 
    """
    if len(p) > 1:
        p[3].append(p[1])
        p[0] = p[3]
    else:
        p[0] = [Node()] 

def p_VarSpec(p):
    """
    VarSpec : IdentifierList Type ASSIGN ExpressionList
            | IdentifierList IDENT ASSIGN ExpressionList
            | IdentifierList IDENT PERIOD IDENT ASSIGN ExpressionList
            | IdentifierList ASSIGN ExpressionList
            | IdentifierList Type
            | IdentifierList IDENT
            | IdentifierList IDENT PERIOD IDENT
    """
    p[0] = Node()

    for i, child in enumerate(p[1].children):
        # Check redeclaration for identifier list
        latest_scope = stm.getScope(child.label)
        if latest_scope == stm.id:
            raise NameError('Redeclaration of identifier: ' + child, p.lineno(1))
        
        present = stm.findType(p[2])
        if present != -1:
            # Add to symbol table
            stm.add(child.label, {'type': p[2], 'isConst' : False})
            p[1].children[i].dataType = p[2]
        else: 
            raise TypeError('Type not declared/found: ' + p[2], p.lineno(1))

    # if assignment is also done
    if p[-1].children != None and isinstance(p[-1].children[0], ExprNode):
        if len(p[1].children) != len(p[-1].children):
            raise NameError("Assignment is not balanced", p.lineno(1))

        for i, expression in enumerate(p[-1].children):
            if expression.dataType != p[2]:
                raise ("Mismatch of type for identifier: " + p[1].children[i].label, p.lineno(1))

        for i, expression in enumerate(p[-1].children):
            p[0].children.append(ExprNode())
            p[0].children[i].addChild([p[1].children[i], p[-1].children[i]])
            p[0].children[i].operator = 'ASSIGN'
            p[0].children[i].dataType = p[2]


###################################################################################
### Type Declarations
###################################################################################

def p_TypeDecl(p):
    """
    TypeDecl : TYPE TypeSpec
             | TYPE LPAREN TypeSpecMult RPAREN
    """
    if len(p) == 3:
        p[0] = [p[2]]
    else:
        p[0] = p[3]

def p_TypeSpecMult(p):
    """
    TypeSpecMult : TypeSpec SEMICOLON TypeSpecMult 
                 | 
    """
    if len(p) > 1:
        p[3].append(p[1])
        p[0] = p[3]

    else:
        p[0] = [Node()]

    
def p_TypeSpec(p):
    """
    TypeSpec : AliasDecl
             | Typedef
    """
    p[0] = p[1]

def p_AliasDecl(p):
    """
    AliasDecl : IDENT ASSIGN Type
                | IDENT ASSIGN IDENT
                | IDENT ASSIGN IDENT PERIOD IDENT
    """ 
    p[0] = Node()
    if p[1].label in stm[stm.id].typeDefs:
        raise ("Redeclaration of Alias " + p[1].label, p.lineno(1))
        
    else:
       stm[stm.id].typeDefs[p[1].label] = p[-1].label

def p_TypeDef(p):
    """
    Typedef : IDENT Type
              | IDENT IDENT
              | IDENT IDENT PERIOD IDENT

    """
    p[0] = Node()
    if p[1].label in stm[stm.id].typeDefs:
        raise ("Redeclaration of Alias " + p[1].label, p.lineno(1))
    present = stm.findType(p[-1])
    if present != -1:
       stm[stm.id].typeDefs[p[1].label] = p[-1].label
    else:
        raise TypeError('Base type not found ' + p[-1], p.lineno(1))


###################################################################################
### Identifier List
###################################################################################

def p_IdentifierList(p):
    """
    IdentifierList : IDENT
                   | IDENT COMMA IdentifierList
    """

    if len(p) == 2:
        p[0] = Node()
        p[0].addChild(*[IdentNode(label = p[1], scope = stm.id)])

    else:
        p[3].addChild(*[IdentNode(label = p[1], scope = stm.id)])
        p[0] = p[3]


###################################################################################
#####################                                        ######################
######                           EXPRESSIONS                               ########
#####################                                        ######################
###################################################################################

def p_ExpressionList(p):
    """
    ExpressionList : Expr
                   | ExpressionList COMMA Expr
    """
    p[0] = Node()
    
    if len(p) == 2:
        p[0].addChild(*[p[1]])
        
    else:
        p[1].children.append(p[3])
        p[0] = p[1]
    
def p_Expr(p):
    """
    Expr : UnaryExpr 
         | Expr LOR  Expr
         | Expr LAND Expr
         | Expr EQL  Expr
         | Expr NEQ Expr
         | Expr LSS Expr
         | Expr LEQ Expr
         | Expr GTR Expr
         | Expr GEQ Expr
         | Expr ADD  Expr
         | Expr SUB Expr
         | Expr OR Expr
         | Expr XOR Expr
         | Expr MUL Expr
         | Expr QUO Expr
         | Expr REM Expr
         | Expr SHL Expr
         | Expr SHR Expr
         | Expr AND Expr
         | Expr AND_NOT Expr
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        dt1 = p[1].dataType
        dt2 = p[3].dataType

        if not checkBinOp(stm, dt1, dt2, p[2], p[3][-1]):
            raise TypeError("Incompatible operand types", p.lineno(1))

        p[0] = ExprNode(operator = p[2])
        p[0].addChild(*[p[1], p[3]])

        dt = getFinalType(dt1, dt2, p[2])
        p[0].dataType = dt

def p_UnaryExpr(p):
    """
    UnaryExpr : PrimaryExpr 
            | ADD UnaryExpr
            | SUB UnaryExpr
            | NOT UnaryExpr
            | XOR UnaryExpr
            | MUL UnaryExpr
            | AND UnaryExpr
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        if not checkUnOp(stm, p[1], p[2].dataType):
            raise TypeError("Incompatible operand for Unary Expression", p.lineno(1))
        
        p[0] = ExprNode()
        p[0].addChild(*[p[2]])
        p[0].dataType = getUnaryType(p[2].dataType, p[1])

###################################################################################
### Primary Expression
###################################################################################

def p_PrimaryExpr(p):
    """
    PrimaryExpr :  Lit
                | IDENT
                | IDENT PERIOD IDENT
                | LPAREN Expr RPAREN
                | PrimaryExpr Selector
                | PrimaryExpr Index
                | PrimaryExpr Slice
                | PrimaryExpr Arguments
    """

    ## PrimaryExpr -> Lit
    if len(p) == 2 and isinstance(p[1], LitNode):
        p[0] = ExprNode(dataType = p[1].dataType)
        p[0].chilren = p[1].children

    ## Primary Expr -> Ident
    elif (len(p) == 2):

        # Check declaration
        latest_scope = stm.getScope(p[1])
        
        if latest_scope == -1:
            ## To be checked for global declarations (TODO)
            print("Expecting global declaration for " + p[1], p.lineno(1))
            
        dt = stm.get(p[1])['type']
        p[0] = ExprNode(dataType=dt, label = p[1])
    
    ## Primary Expr -> LPAREN Expr RPAREN
    elif len(p) == 4 and isinstance(p[2], ExprNode):
        p[0] = p[2]

    ## PrimaryExpr -> PrimaryExpr Selector
    

###################################################################################
## Selector

def p_Selector(p):
    """
    Selector : PERIOD IDENT
    """

###################################################################################
## Index

def p_Index(p):
    """
    Index : LBRACK Expr RBRACK
    """

###################################################################################
## Slice

def p_Slice(p):
    """
    Slice : LBRACK Expr COLON Expr RBRACK
          | LBRACK COLON Expr RBRACK
          | LBRACK Expr COLON RBRACK
          | LBRACK COLON RBRACK
          | LBRACK COLON Expr COLON Expr RBRACK
          | LBRACK Expr COLON Expr COLON Expr RBRACK
    """

###################################################################################
## Arguments

def p_Arguments(p):
    """
    Arguments : LPAREN RPAREN
              | LPAREN ExpressionList RPAREN
              | LPAREN ExpressionList COMMA RPAREN
              | LPAREN TypeT RPAREN
              | LPAREN TypeT COMMA RPAREN
              | LPAREN TypeT COMMA ExpressionList RPAREN 
              | LPAREN TypeT COMMA ExpressionList COMMA RPAREN 
              | LPAREN IDENT RPAREN
              | LPAREN IDENT COMMA RPAREN
              | LPAREN IDENT COMMA ExpressionList RPAREN 
              | LPAREN IDENT COMMA ExpressionList COMMA RPAREN 
              | LPAREN IDENT PERIOD IDENT RPAREN
              | LPAREN IDENT PERIOD IDENT COMMA RPAREN
              | LPAREN IDENT PERIOD IDENT COMMA ExpressionList RPAREN 
              | LPAREN IDENT PERIOD IDENT COMMA ExpressionList COMMA RPAREN   
    """


###################################################################################
#####################                                        ######################
######                             TYPES                                   ########
#####################                                        ######################
###################################################################################

def p_Type(p):
    """
    Type : TypeT
         | PointerType
         | LPAREN PointerType RPAREN
    """

def p_TypeT(p):
    """
    TypeT : ArrayType
          | StructType
          | SliceType
          | MapType
          | FunctionType
          | LPAREN TypeT RPAREN
          | LPAREN IDENT RPAREN
          | LPAREN IDENT PERIOD IDENT RPAREN
    """

###################################################################################
### Pointer Type
###################################################################################

def p_PointerType(p):
    """
    PointerType : MUL Type %prec UMUL
               | MUL IDENT %prec UMUL
                | MUL IDENT PERIOD IDENT %prec UMUL
    """

###################################################################################
### Slice Type
###################################################################################

def p_SliceType(p):
    """
    SliceType : LBRACK RBRACK ElementType
    """

###################################################################################
### Array Type
###################################################################################

def p_ArrayType(p):
    """
    ArrayType : LBRACK ArrayLength RBRACK ElementType
    """

def p_ArrayLength(p):
    """
    ArrayLength : Expr
    """

def p_ElementType(p):
    """
    ElementType : Type
                | IDENT
                | IDENT PERIOD IDENT
    """

###################################################################################
### Struct Type
###################################################################################

def p_StructType(p):
    """
    StructType : STRUCT BeginStruct LBRACE FieldDeclMult RBRACE EndStruct 
    """

def p_BeginStruct(p):
    """
    BeginStruct : 
    """
    context['structSymbolsList'] = []

def p_EndStruct(p):
    """
    EndStruct : 
    """
    context['structSymbolsList'] = None

#extra
def p_FieldDeclMult(p):
    """
    FieldDeclMult : FieldDeclMult FieldDecl SEMICOLON
                  | 
    """

def p_FieldDecl(p):
    """
    FieldDecl : IdentifierList Type 
              | IdentifierList IDENT
              | IdentifierList IDENT PERIOD IDENT
              | EmbeddedField
              | IdentifierList Type Tag
              | IdentifierList IDENT Tag
              | IdentifierList IDENT PERIOD IDENT Tag
              | EmbeddedField Tag
    """
    
def p_Tag(p):
    """
    Tag : STRING
    """

def p_EmbeddedField(p):
    """
    EmbeddedField : MUL IDENT
                  | IDENT
                  | MUL IDENT PERIOD IDENT
                  | IDENT PERIOD IDENT
    """

###################################################################################
### Map Type
###################################################################################

def p_MapType(p):
    """
    MapType : MAP LBRACK KeyType RBRACK ElementType
    """
    
def p_KeyType(p):
    """
    KeyType : Type
            | IDENT
            | IDENT PERIOD IDENT
    """

###################################################################################
### Function Type
###################################################################################

def p_FunctionType(p):
    """
    FunctionType : FUNC Signature 
    """

###################################################################################
#####################                                        ######################
######                             LITERALS                                ########
#####################                                        ######################
###################################################################################

def p_Lit(p):
    """
    Lit : BasicLit
        | CompositeLit
        | FunctionLit
    """

###################################################################################
### Basic Literal
###################################################################################
    
def p_BasicLit(p):
    """
    BasicLit : INT
             | FLOAT
             | IMAG
             | RUNE
             | STRING
             | BOOL
    """

###################################################################################
### Composite Literal
###################################################################################

def p_CompositeLit(p):
    """
    CompositeLit : StructType Arguments
                 | ArrayType LiteralValue
                 | SliceType LiteralValue
                 | MapType LiteralValue
                 | IDENT LiteralValue
                 | IDENT PERIOD IDENT LiteralValue
    """

def p_LiteralValue(p):
    """
    LiteralValue : LBRACE ElementList COMMA RBRACE 
                 | LBRACE ElementList RBRACE 
                 | LBRACE RBRACE 
    """

def p_ElementList(p):
    """
    ElementList : KeyedElement 
                | ElementList COMMA KeyedElement 
    """

def p_KeyedElement(p):
    """
    KeyedElement : Element
                 | Key COLON Element
    """

def p_Key(p):
    """
    Key : Expr
        | LiteralValue
    """

def p_Element(p):
    """
    Element : Expr
            | LiteralValue
    """

###################################################################################
### Function Literal
###################################################################################

def p_FunctionLit(p):
    """
    FunctionLit : FUNC Signature FunctionBody
    """

###################################################################################
## Function Declarations

def p_FuncDecl(p):
    """
    FuncDecl : FUNC FunctionName BeginFunc Signature FunctionBody EndFunc
             | FUNC FunctionName Signature
    """
    
    ## Add entry in stm
    info = {'params' : [], 'result': []}
    for i in range(len(p[3].children)):
        if isinstance(p[3].children[i], ResultNode):
            info['result'].append(p[3].children[i].dataType)
        else:
            info['params'].append([p[3].children[i].label, p[3].children[i].dataType]) 

    stm.addFunction(p[2].label, info)

    ## Make node
    p[0] = FuncDeclNode()
    for i in range(len(p)):
        if i == 0:
            continue
        else:
            p[0].children.append(p[i])

def p_BeginFunc(p):
    """
    BeginFunc : 
    """
    stm.newScope()

def p_EndFunc(p):
    """
    EndFunc : 
    """
    stm.exitScope()

###################################################################################
## Function Name
def p_FunctionName(p):
    """
    FunctionName : IDENT
    """
    ##  Check redeclaration
    if p[2].label in stm.functions:
        raise ("Redeclaration of function " + p[2].label, p.lineno(1))
    
    ## Add func type to symbol table
    stm[stm.id].addType("func")

    info = {}
    stm.addFunction(p[1], info)

    p[0] = IdentNode(scope = stm.id, label = p[1], dataType = "func")

###################################################################################
## Function Body

def p_FunctionBody(p):
    """
    FunctionBody : Block
    """
    p[0] = p[1]

###################################################################################
## Function Signature

def p_Signature(p):
    """
    Signature : Parameters Result
              | Parameters
    """
    p[0] = Node()
    p[0].children.append(p[1])
    if len(p) > 2:
        p[0].children.append(p[2])

###################################################################################
## Function Parameters

def p_Parameters(p):
    """
    Parameters : LPAREN RPAREN
               | LPAREN ParameterList RPAREN
               | LPAREN ParameterList COMMA RPAREN
    """
    p[0] = Node()
    
    if len(p) > 3:
        p[0].addChild(*p[2])

def p_ParameterList(p):
    """
    ParameterList : ParameterDecl
                  | ParameterList COMMA IDENT
                  | ParameterList COMMA IDENT PERIOD IDENT
                  | ParameterList COMMA Type
                  | ParameterList COMMA ParameterDecl 
    """
    if len(p)==2 :
        p[0] = p[1]

    elif len(p) == 4 and isinstance(p[3], ParamNode):
        p[1].children.append(p[3])
        p[0] = p[1]

    elif len(p) == 4 and isinstance(p[3], str):
        p[1].children.append(ParamNode(datatype = p[3]))
        p[0] = p[1]    
        ## Add types to symbol table
        stm[stm.id].addType(p[3])

def p_ParameterDecl(p):
    """
    ParameterDecl : IdentifierList Type
                  | IdentifierList IDENT
                  | IdentifierList IDENT PERIOD IDENT
    """
    p[0] = Node()
    
    if len(p) == 3 and isinstance(p[2], str):
        stm[stm.id].addType(p[2])

        for i, child in enumerate(p[1].children):
            p[0].chidren.append(ParamNode(label = child.label, dataType = p[2]))

###################################################################################
## Return Type

def p_Result(p):
    """
    Result : Parameters 
           | Type
           | IDENT
           | IDENT PERIOD IDENT
    """
    p[0] = ResultNode()
    if len(p) == 1 and isinstance(p[1], str):
        p[0].children.append(IdentNode(dataType = p[1]))
    
    elif len(p) == 1:
        p[0] = p[1]

###################################################################################
#####################                                        ######################
######                           STATEMENTS                                ########
#####################                                        ######################
###################################################################################

def p_StatementList(p):
    """
    StatementList : Statement SEMICOLON StatementList  
                  | 
    """

def p_Statement(p):
    """
    Statement : Decl
              | LabeledStmt
              | SimpleStmt
              | GotoStmt
              | ReturnStmt
              | BreakStmt
              | ContinueStmt
              | FallthroughStmt
              | Block
              | IfStmt
              | SwitchStmt
              | ForStmt
    """

###################################################################################
### Labeled Statements
###################################################################################

def p_LabeledStmt(p):
    """
    LabeledStmt : Label COLON Statement
    """

def p_Label(p):
    """
    Label : IDENT
    """

###################################################################################
### Simple Statements
###################################################################################

def p_SimpleStmt(p):
    """
    SimpleStmt :  EmptyStmt
                | ExpressionStmt
                | IncDecStmt
                | Assignment
                | ShortVarDecl
    """

###################################################################################
### Empty Statements

def p_EmptyStmt(p):
    """
    EmptyStmt : 
    """

###################################################################################
### Expression Statements

def p_ExpressionStmt(p):
    """
    ExpressionStmt : Expr
    """

###################################################################################
### Increment/Decrement Statements

def p_IncDecStmt(p):
    """
    IncDecStmt :  Expr INC
                 | Expr DEC
    """

###################################################################################
### Assignment Statements

def p_Assignment(p):
    """
    Assignment : ExpressionList assign_op ExpressionList
    """

def p_assign_op(p):
    """
    assign_op : add_op_assign 
              | mul_op_assign
              | ASSIGN
    """

def p_add_op_assign(p):
    """
    add_op_assign : ADD_ASSIGN
                    | SUB_ASSIGN
                    | OR_ASSIGN
                    | XOR_ASSIGN
    """

def p_mul_op_assign(p):
    """
    mul_op_assign : MUL_ASSIGN
                    | QUO_ASSIGN
                    | REM_ASSIGN
                    | AND_ASSIGN
                    | SHL_ASSIGN
                    | SHR_ASSIGN
                    | AND_NOT_ASSIGN
    """

###################################################################################
### Short Variable Declaration

def p_ShortVarDecl(p):
    """
    ShortVarDecl : IdentifierList DEFINE ExpressionList
    """

###################################################################################
### Goto Statements
###################################################################################

def p_GotoStmt(p):
    """
    GotoStmt :  GOTO Label
    """

###################################################################################
### Return Statements
###################################################################################

def p_ReturnStmt(p):
    """
    ReturnStmt : RETURN ExpressionList
                | RETURN
    """

###################################################################################
### Break Statements
###################################################################################

def p_BreakStmt(p):
    """
    BreakStmt : BREAK Label
                | BREAK
    """

###################################################################################
### Continue Statements
###################################################################################

def p_ContinueStmt(p):
    """
    ContinueStmt :  CONTINUE Label
                    | CONTINUE
    """

###################################################################################
### Fallthrough Statements
###################################################################################

def p_FallthroughStmt(p):
    """
    FallthroughStmt : FALLTHROUGH
    """

###################################################################################
### Block Statements
###################################################################################

def p_Block(p):
    """
    Block : LBRACE StatementList RBRACE
    """

###################################################################################
### If Else Statements
###################################################################################

def p_IfStmt(p):
    """
    IfStmt : IF Expr Block else_stmt
           | IF SimpleStmt SEMICOLON Expr else_stmt
    """

def p_else_stmt(p):
    """
    else_stmt : ELSE IfStmt
                | ELSE Block
                |
    """

###################################################################################
### Switch Statements
###################################################################################

def p_SwitchStmt(p):
    """
    SwitchStmt :  ExprSwitchStmt
                 | TypeSwitchStmt
    """

###################################################################################
### Expression Switch Statements

def p_ExprSwitchStmt(p):
    """
    ExprSwitchStmt : SWITCH SimpleStmt SEMICOLON Expr LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
                     | SWITCH Expr LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
                     | SWITCH SimpleStmt SEMICOLON LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
                     | SWITCH LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
    """

def p_BeginSwitch(p):
    """
    BeginSwitch : 
    """
    context['switchDepth'] += 1

def p_EndSwitch(p):
    """
    EndSwitch : 
    """
    context['switchDepth'] -= 1

def p_ExprCaseClauseMult(p):
    """
    ExprCaseClauseMult : ExprCaseClause ExprCaseClauseMult 
                         |
    """

def p_ExprCaseClause(p):
    """
    ExprCaseClause : ExprSwitchCase COLON StatementList
    """

def p_ExprSwitchCase(p):
    """
    ExprSwitchCase : CASE ExpressionList
                     | DEFAULT
    """

###################################################################################
### Type Switch Statements

def p_TypeSwitchStmt(p):
    """
    TypeSwitchStmt : SWITCH SimpleStmt SEMICOLON TypeSwitchGuard LBRACE TypeCaseClauseMult RBRACE
                     | SWITCH TypeSwitchGuard LBRACE TypeCaseClauseMult RBRACE
    """

def p_TypeSwitchGuard(p):
    """
    TypeSwitchGuard : IDENT DEFINE PrimaryExpr PERIOD LPAREN TYPE RPAREN
                      | PrimaryExpr PERIOD LPAREN TYPE RPAREN
    """

def p_TypeCaseClauseMult(p):
    """
    TypeCaseClauseMult : TypeCaseClause TypeCaseClauseMult 
                        |
    """

def p_TypeCaseClause(p):
    """
    TypeCaseClause : CASE TypeList COLON StatementList
                     | DEFAULT COLON StatementList
    """

def p_TypeList(p):
    """
    TypeList : Type
                | IDENT 
                | IDENT PERIOD IDENT
                | Type COMMA TypeList
                | IDENT COMMA TypeList
                | IDENT PERIOD IDENT COMMA TypeList
    """

###################################################################################
### For Statements
###################################################################################

def p_ForStmt(p):
    """
    ForStmt : FOR BeginFor Condition Block EndFor
            | FOR BeginFor ForClause Block EndFor
            | FOR BeginFor RangeClause Block EndFor
            | FOR BeginFor Block EndFor
    """

def p_BeginFor(p):
    """
    BeginFor : 
    """
    # print("For Begins")
    # beginScope()
    # context['forDepth'] += 1
    # Add two labels to be used
    # for code generation

def p_EndFor(p):
    """
    EndFor : 
    """
    # print("For Ends")
#     context['forDepth'] -= 1
#    ()

def p_Condition(p):
    """
    Condition : Expr
    """

###################################################################################
### For Clause

def p_ForClause(p):
    """
    ForClause : InitStmt SEMICOLON Condition SEMICOLON PostStmt
                | InitStmt SEMICOLON SEMICOLON PostStmt
    """

def p_InitStmt(p):
    """
    InitStmt :   SimpleStmt
    """

def p_PostStmt(p):
    """
    PostStmt :   SimpleStmt
    """

###################################################################################
### Range Clause

def p_RangeClause(p):
    """
    RangeClause : RangeList RANGE Expr
    """

def p_RangeList(p):
    """
    RangeList : ExpressionList ASSIGN 
                | IdentifierList DEFINE
                | 
    """


###################################################################################
#####################                                        ######################
######                             ERROR                                   ########
#####################                                        ######################
###################################################################################

def p_error(p):
    print("Syntax Error: ", p)


###################################################################################
#####################                                        ######################
######                           BUILD LEXER                               ########
#####################                                        ######################
###################################################################################

lexer = lex.lex()

parser, grammar = yacc.yacc()

path_to_root = os.environ.get('PATH_TO_ROOT')
milestone = os.environ.get('MILESTONE')
if path_to_root is not None:
    with open(path_to_root + "/src/Milestone" + str(milestone) + "/action.txt", "w") as f:
        for key, val in parser.action.items():
            f.writelines(f'{key} : {val}\n')

    with open(path_to_root + "/src/Milestone" + str(milestone) + "/goto.txt", "w") as f:
        for key, val in parser.goto.items():
            f.writelines(f'{key} : {val}\n')

non_terminals = grammar.Nonterminals

## Trying to handle input
with open(sys.argv[1], 'r') as f:
    import pprint
    out = parser.parse(f.read(), lexer = lexer)
    if out is None:
        f.close()
        sys.exit(1)
    output_file = sys.argv[1][:-2] + "output"
    with open(output_file, 'w') as fout:
        pprint.pprint(out, width=10, stream=fout)

def dfs(ast):
    print(f'{ast}')
    if hasattr(ast, 'children') and ast.children is not None:
        for c in ast.children:
            dfs(c)

dfs(ast)