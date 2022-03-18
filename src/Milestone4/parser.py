import ply.yacc as yacc
import ply.lex as lex
import lexer
from lexer import *
import sys
from scope import *

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

## Start Semantic Analysis
context = {}
def setupContext():
    context['scopeTab'] = {} # Dictionary for Scope Symbol Tables
    context['nextScopeId'] = 0 # Id for next scope table
    context['currentScope'] = context['nextScopeId'] # Setting current scope id to 0
    context['nextScopeId'] += 1 # Incrementing next scope id
    context['scopeTab'][context['currentScope']] = scope() # Symbol Table
    context['scopeStack'] = [0] # Stack for active scopes
    context['forDepth'] = 0 # Inside 0 for loops at present
    context['switchDepth'] = 0 # Inside 0 switch statements at present
    context['structSymbolsList'] = None # List of symbols in current struct
    context['labelCount'] = 0 # Count for label
    context['labelMap'] = {} # Dictionary for custom labels

def endContext():
    # Dump Symbol Table of each function as CSV

    # Dump AST of functions in DOT format
    pprint.pprint(context)

def newLabel():
    context['labelCount'] += 1
    return f"label#{context['labelCount']-1}"

def beginScope():
    prevScope = context['currentScope']
    context['currentScope'] = context['nextScopeId']
    context['scopeStack'].append(context['currentScope'])
    context['scopeTab'][context['currentScope']] = scope(prevScope)
    context['scopeTab'][context['currentScope']].inheritTypes(context['scopeTab'][prevScope])
    context['nextScopeId'] += 1

def endScope():
    context['scopeStack'].pop()
    context['currentScope'] = context['scopeStack'][-1]

def checkExpected():
    # Check whether unresolved expected tokens are present
    # Could we show the user all expected errors together
    # Labels
    for label in context['labelMap']:
        if context['labelMap'][label][0] == 'expected':
            raise ValueError(f"Label {label} not declared anywhere but used at {context['labelMap'][label][1]}")

###################################################################################
#####################                                        ######################
######                         STARTING GRAMMAR                            ########
#####################                                        ######################
###################################################################################

COMPACT = False
def get_value_p(p):
    return []
    value = [str(sys._getframe(1).f_code.co_name)[2:]]
    # value = []
    for i in range(1, len(p)):
        if isinstance(p[i], str):
            if p[i] in ignored_tokens:
                continue
            if p[i] not in non_terminals:
                value.append([p[i]])
        elif len(p[i]) > 0:
            if COMPACT:
                if p[i][0] == value[0]:
                    value.extend(p[i][1:])
                else:
                    value.append(p[i])
            else:
                value.append(p[i])
    if not isinstance(value, str) and COMPACT:
        if len(value) == 2:
            return value[1]
        if len(value) == 1:
            return []
        if len(value) > 2:
            if value[0] == 'Expr':
                value = value[2] + [value[1]] + value[3:]
            elif value[0] == 'UnaryExpr':
                value = value[1] + [value[2]]
                # print(value, value[2] + [value[1]] + value[3:])
    return value

def get_nt_name():
    return str(sys._getframe(1).f_code.co_name)[2:]

def p_SourceFile(p):
    """
    SourceFile : SetupContext PackageClause SEMICOLON ImportDeclMult TopLevelDeclMult
    """
    p[0] = p[5]
    p[0].name = get_nt_name()
    checkExpected()
    endContext()
    print(p[0])

def p_SetupContext(p):
    """
    SetupContext :
    """
    p[0] = []
    setupContext()

def p_EndScope(p):
    """
    EndScope : 
    """
    p[0] = []
    endScope()

###################################################################################
### Package related grammar
###################################################################################

def p_PackageClause(p):
    """
    PackageClause : PACKAGE IDENT
    """
    p[0] = node(get_nt_name())

###################################################################################
### Import related grammar
###################################################################################

def p_ImportDeclMult(p):
    """
    ImportDeclMult : ImportDecl SEMICOLON ImportDeclMult
                   |  
    """
    p[0] = node(get_nt_name())

def p_ImportDecl(p):
    """
    ImportDecl : IMPORT ImportSpec
               | IMPORT LPAREN ImportSpecMult RPAREN
    """
    p[0] = node(get_nt_name())

def p_ImportMult(p):
    """
    ImportSpecMult : ImportSpec SEMICOLON ImportSpecMult  
               |
    """
    p[0] = node(get_nt_name())

def p_ImportSpec(p):
    """
    ImportSpec : PERIOD ImportPath
              | IDENT ImportPath
              | ImportPath 
    """
    p[0] = node(get_nt_name())
    
def p_ImportPath(p):
    """
    ImportPath : STRING
    """
    p[0] = node(get_nt_name())

###################################################################################
### Top-Level related grammar
###################################################################################

def p_TopLevelDeclMult(p):
    """
    TopLevelDeclMult : TopLevelDecl SEMICOLON TopLevelDeclMult 
                     |
    """
    p[0] = node(get_nt_name())
    if len(p) > 2:
        p[0].ast += p[1].ast + p[3].ast

def p_TopLevelDecl(p):
    """
    TopLevelDecl : Decl 
                 | FuncDecl
    """
    p[0] = p[1]
    p[0].name = get_nt_name()

def p_Decl(p):
    """
    Decl : ConstDecl 
         | VarDecl
         | TypeDecl
    """
    p[0] = p[1]
    p[0].name = get_nt_name()

###################################################################################
### Constant Declarations
###################################################################################

def p_ConstDecl(p):
    """
    ConstDecl : CONST ConstSpec
              | CONST LPAREN ConstSpecMult RPAREN
    """
    p[0] = node(get_nt_name())

def p_ConstSpecMult(p):
    """
    ConstSpecMult : ConstSpec SEMICOLON ConstSpecMult 
                  | 
    """
    p[0] = node(get_nt_name())

def p_ConstSpec(p):
    """
    ConstSpec : IdentifierList Type ASSIGN ExpressionList 
                | IdentifierList IDENT ASSIGN ExpressionList
                | IdentifierList IDENT PERIOD IDENT ASSIGN ExpressionList
    """
    p[0] = node(get_nt_name())

###################################################################################
### Variable Declarations
###################################################################################

def p_VarDecl(p):
    """
    VarDecl : VAR VarSpec
            | VAR LPAREN VarMult RPAREN
    """
    p[0] = node(get_nt_name())

def p_VarMult(p):
    """
    VarMult : VarSpec SEMICOLON VarMult 
            | 
    """
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())

###################################################################################
### Type Declarations
###################################################################################

def p_TypeDecl(p):
    """
    TypeDecl : TYPE TypeSpec
             | TYPE LPAREN TypeSpecMult RPAREN
    """
    p[0] = node(get_nt_name())

def p_TypeSpecMult(p):
    """
    TypeSpecMult : TypeSpec SEMICOLON TypeSpecMult 
                 | 
    """
    p[0] = node(get_nt_name())

def p_TypeSpec(p):
    """
    TypeSpec : AliasDecl
             | Typedef
    """
    p[0] = node(get_nt_name())

def p_AliasDecl(p):
    """
    AliasDecl : IDENT ASSIGN Type
                | IDENT ASSIGN IDENT
                | IDENT ASSIGN IDENT PERIOD IDENT
    """
    p[0] = node(get_nt_name())

def p_TypeDef(p):
    """
    Typedef : IDENT Type
              | IDENT IDENT
              | IDENT IDENT PERIOD IDENT

    """
    p[0] = node(get_nt_name())

###################################################################################
### Identifier List
###################################################################################

def p_IdentifierList(p):
    """
    IdentifierList : IDENT
                   | IDENT COMMA IdentifierList
    """
    p[0] = node(get_nt_name())


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
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())

###################################################################################
## Selector

def p_Selector(p):
    """
    Selector : PERIOD IDENT
    """
    p[0] = node(get_nt_name())

###################################################################################
## Index

def p_Index(p):
    """
    Index : LBRACK Expr RBRACK
    """
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())


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
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())

###################################################################################
### Pointer Type
###################################################################################

def p_PointerType(p):
    """
    PointerType : MUL Type %prec UMUL
               | MUL IDENT %prec UMUL
                | MUL IDENT PERIOD IDENT %prec UMUL
    """
    p[0] = node(get_nt_name())

###################################################################################
### Slice Type
###################################################################################

def p_SliceType(p):
    """
    SliceType : LBRACK RBRACK ElementType
    """
    p[0] = node(get_nt_name())

###################################################################################
### Array Type
###################################################################################

def p_ArrayType(p):
    """
    ArrayType : LBRACK ArrayLength RBRACK ElementType
    """
    p[0] = node(get_nt_name())

def p_ArrayLength(p):
    """
    ArrayLength : Expr
    """
    p[0] = node(get_nt_name())

def p_ElementType(p):
    """
    ElementType : Type
                | IDENT
                | IDENT PERIOD IDENT
    """
    p[0] = node(get_nt_name())

###################################################################################
### Struct Type
###################################################################################

def p_StructType(p):
    """
    StructType : STRUCT BeginStruct LBRACE FieldDeclMult RBRACE EndStruct 
    """
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())
    
def p_Tag(p):
    """
    Tag : STRING
    """
    p[0] = node(get_nt_name())

def p_EmbeddedField(p):
    """
    EmbeddedField : MUL IDENT
                  | IDENT
                  | MUL IDENT PERIOD IDENT
                  | IDENT PERIOD IDENT
    """
    p[0] = node(get_nt_name())

###################################################################################
### Map Type
###################################################################################

def p_MapType(p):
    """
    MapType : MAP LBRACK KeyType RBRACK ElementType
    """
    p[0] = node(get_nt_name())
    
def p_KeyType(p):
    """
    KeyType : Type
            | IDENT
            | IDENT PERIOD IDENT
    """
    p[0] = node(get_nt_name())

###################################################################################
### Function Type
###################################################################################

def p_FunctionType(p):
    """
    FunctionType : FUNC Signature 
    """
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())

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
    """
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())

def p_LiteralValue(p):
    """
    LiteralValue : LBRACE ElementList COMMA RBRACE 
                 | LBRACE ElementList RBRACE 
                 | LBRACE RBRACE 
    """
    p[0] = node(get_nt_name())

def p_ElementList(p):
    """
    ElementList : KeyedElement 
                | ElementList COMMA KeyedElement 
    """
    p[0] = node(get_nt_name())

def p_KeyedElement(p):
    """
    KeyedElement : Element
                 | Key COLON Element
    """
    p[0] = node(get_nt_name())

def p_Key(p):
    """
    Key : Expr
        | LiteralValue
    """
    p[0] = node(get_nt_name())

def p_Element(p):
    """
    Element : Expr
            | LiteralValue
    """
    p[0] = node(get_nt_name())

###################################################################################
### Function Literal
###################################################################################

def p_FunctionLit(p):
    """
    FunctionLit : FUNC Signature FunctionBody
    """
    p[0] = node(get_nt_name())

###################################################################################
## Function Declarations

def p_FuncDecl(p):
    """
    FuncDecl : FUNC FunctionName BeginScope Signature FunctionBody EndScope
             | FUNC FunctionName BeginScope Signature EndScope
    """
    p[0] = node(get_nt_name())
    # Add function name and signatures later
    if len(p) == 6:
        p[0].ast = p[5].ast

###################################################################################
## Function Name

def p_FunctionName(p):
    """
    FunctionName : IDENT
    """
    p[0] = p[1]

###################################################################################
## Function Body

def p_FunctionBody(p):
    """
    FunctionBody : Block
    """
    p[0] = p[1]
    p[0].name = get_nt_name()

###################################################################################
## Function Signature

def p_Signature(p):
    """
    Signature : Parameters Result
              | Parameters
    """
    p[0] = node(get_nt_name())

###################################################################################
## Function Parameters

def p_Parameters(p):
    """
    Parameters : LPAREN RPAREN
               | LPAREN ParameterList RPAREN
               | LPAREN ParameterList COMMA RPAREN
    """
    p[0] = node(get_nt_name())
    
def p_ParameterList(p):
    """
    ParameterList : ParameterDecl
                  | ParameterList COMMA IDENT
                  | ParameterList COMMA IDENT PERIOD IDENT
                  | ParameterList COMMA Type
                  | ParameterList COMMA ParameterDecl 
    """
    p[0] = node(get_nt_name())

def p_ParameterDecl(p):
    """
    ParameterDecl : IdentifierList Type
                  | IdentifierList IDENT
                  | IdentifierList IDENT PERIOD IDENT
    """
    p[0] = node(get_nt_name())

###################################################################################
## Return Type

def p_Result(p):
    """
    Result : Parameters 
           | Type
           | IDENT
           | IDENT PERIOD IDENT
    """
    p[0] = node(get_nt_name())


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
    p[0] = node(get_nt_name())
    if len(p) == 4:
        p[0].ast = p[1].ast + p[3].ast

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
              | BeginScope Block EndScope
              | IfStmt
              | SwitchStmt
              | ForStmt
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]
    p[0].name = get_nt_name()

###################################################################################
### Labeled Statements
###################################################################################

def p_LabeledStmt(p):
    """
    LabeledStmt : Label COLON Statement
    """
    p[0] = node(get_nt_name())
    if p[1] in context['labelMap']:
        raise ValueError(f"Label {p[1]} redeclared at line {p.lexer.lineno}.\nIt was previously declared at line {context['labelMap'][p[1]][1]}\n")
    else:
        context['labelMap'][p[1]] = (newLabel(), p.lexer.lineno)
    p[0].ast = ['LABEL', [p[1], p[3].ast]]

def p_Label(p):
    """
    Label : IDENT
    """
    p[0] = p[1]

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
    p[0] = p[1]
    p[0].name = get_nt_name()

###################################################################################
### Empty Statements

def p_EmptyStmt(p):
    """
    EmptyStmt : 
    """
    p[0] = node(get_nt_name())

###################################################################################
### Expression Statements

def p_ExpressionStmt(p):
    """
    ExpressionStmt : Expr
    """
    # p[0] = p[1]
    p[0] = node(get_nt_name())

###################################################################################
### Increment/Decrement Statements

def p_IncDecStmt(p):
    """
    IncDecStmt :  Expr INC
                 | Expr DEC
    """
    # To be analysed later
    p[0] = node(get_nt_name())

###################################################################################
### Assignment Statements

def p_Assignment(p):
    """
    Assignment : ExpressionList assign_op ExpressionList
    """
    # To be analysed later
    p[0] = node(get_nt_name())

def p_assign_op(p):
    """
    assign_op : add_op_assign 
              | mul_op_assign
              | ASSIGN
    """
    p[0] = node(get_nt_name())
    p[0].exprTypeList.append(p[1])
    p[0].metadata['op'] = p[1]

def p_add_op_assign(p):
    """
    add_op_assign : ADD_ASSIGN
                    | SUB_ASSIGN
                    | OR_ASSIGN
                    | XOR_ASSIGN
    """
    p[0] = p[1]

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
    p[0] = p[1]

###################################################################################
### Short Variable Declaration

def p_ShortVarDecl(p):
    """
    ShortVarDecl : IdentifierList DEFINE ExpressionList
    """
    p[0] = node(get_nt_name())

###################################################################################
### Goto Statements
###################################################################################

def p_GotoStmt(p):
    """
    GotoStmt :  GOTO Label
    """
    p[0] = node(get_nt_name())
    if p[1] in context['labelMap']:
        # Label seen before somewhere
        if context['labelMap'][p[1]][0] == 'expected':
            # It was used before; not declared :(
            pass
        else:
            # It was declared before :)
            pass
    else:
        # Label not seen before
        context['labelMap'][p[1]] = ('expected', p.lexer.lineno)
    p[0].ast = ['GOTO', [p[2]]]

###################################################################################
### Return Statements
###################################################################################

def p_ReturnStmt(p):
    """
    ReturnStmt : RETURN ExpressionList
                | RETURN
    """
    p[0] = node(get_nt_name())

###################################################################################
### Break Statements
###################################################################################

def p_BreakStmt(p):
    """
    BreakStmt : BREAK Label
                | BREAK
    """
    p[0] = node(get_nt_name())

###################################################################################
### Continue Statements
###################################################################################

def p_ContinueStmt(p):
    """
    ContinueStmt :  CONTINUE Label
                    | CONTINUE
    """
    p[0] = node(get_nt_name())

###################################################################################
### Fallthrough Statements
###################################################################################

def p_FallthroughStmt(p):
    """
    FallthroughStmt : FALLTHROUGH
    """
    p[0] = node(get_nt_name())

###################################################################################
### Block Statements
###################################################################################

def p_Block(p):
    """
    Block : LBRACE StatementList RBRACE
    """
    p[0] = p[2]
    p[0].name = get_nt_name()

###################################################################################
### If Else Statements
###################################################################################

def p_IfStmt(p):
    """
    IfStmt : IF Expr BeginScope Block EndScope else_stmt
           | IF BeginScope SimpleStmt EndScope SEMICOLON Expr else_stmt
    """
    p[0] = node(get_nt_name())

def p_else_stmt(p):
    """
    else_stmt : ELSE IfStmt
                | ELSE BeginScope Block EndScope
                |
    """
    p[0] = node(get_nt_name())

###################################################################################
### Switch Statements
###################################################################################

def p_SwitchStmt(p):
    """
    SwitchStmt :  ExprSwitchStmt
                 | TypeSwitchStmt
    """
    p[0] = node(get_nt_name())

###################################################################################
### Expression Switch Statements

def p_ExprSwitchStmt(p):
    """
    ExprSwitchStmt : SWITCH BeginScope SimpleStmt EndScope SEMICOLON BeginScope Expr EndScope LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
                     | SWITCH Expr LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
                     | SWITCH BeginScope SimpleStmt EndScope SEMICOLON LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
                     | SWITCH LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
    """
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())

def p_ExprCaseClause(p):
    """
    ExprCaseClause : BeginScope ExprSwitchCase COLON StatementList EndScope
    """
    p[0] = node(get_nt_name())

def p_ExprSwitchCase(p):
    """
    ExprSwitchCase : CASE ExpressionList
                     | DEFAULT
    """
    p[0] = node(get_nt_name())

###################################################################################
### Type Switch Statements

def p_TypeSwitchStmt(p):
    """
    TypeSwitchStmt : SWITCH SimpleStmt SEMICOLON TypeSwitchGuard LBRACE TypeCaseClauseMult RBRACE
                     | SWITCH TypeSwitchGuard LBRACE TypeCaseClauseMult RBRACE
    """
    p[0] = node(get_nt_name())

def p_TypeSwitchGuard(p):
    """
    TypeSwitchGuard : IDENT DEFINE PrimaryExpr PERIOD LPAREN TYPE RPAREN
                      | PrimaryExpr PERIOD LPAREN TYPE RPAREN
    """
    p[0] = node(get_nt_name())

def p_TypeCaseClauseMult(p):
    """
    TypeCaseClauseMult : TypeCaseClause TypeCaseClauseMult 
                        |
    """
    p[0] = node(get_nt_name())

def p_TypeCaseClause(p):
    """
    TypeCaseClause : CASE BeginScope TypeList EndScope COLON BeginScope StatementList EndScope
                     | DEFAULT COLON BeginScope StatementList EndScope
    """
    p[0] = node(get_nt_name())

def p_TypeList(p):
    """
    TypeList : Type
                | IDENT 
                | IDENT PERIOD IDENT
                | Type COMMA TypeList
                | IDENT COMMA TypeList
                | IDENT PERIOD IDENT COMMA TypeList
    """
    p[0] = node(get_nt_name())

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
    p[0] = node(get_nt_name())

def p_BeginFor(p):
    """
    BeginFor : 
    """
    p[0] = []
    beginScope()
    context['forDepth'] += 1
    # Add two labels to be used
    # for code generation

def p_EndFor(p):
    """
    EndFor : 
    """
    p[0] = []
    context['forDepth'] -= 1
    endScope()

def p_Condition(p):
    """
    Condition : Expr
    """
    p[0] = node(get_nt_name())

###################################################################################
### For Clause

def p_ForClause(p):
    """
    ForClause : InitStmt SEMICOLON Condition SEMICOLON PostStmt
                | InitStmt SEMICOLON SEMICOLON PostStmt
    """
    p[0] = node(get_nt_name())

def p_InitStmt(p):
    """
    InitStmt :   SimpleStmt
    """
    p[0] = p[1]
    p[0].name = get_nt_name()

def p_PostStmt(p):
    """
    PostStmt :   SimpleStmt
    """
    p[0] = p[1]
    p[0].name = get_nt_name()

###################################################################################
### Range Clause

def p_RangeClause(p):
    """
    RangeClause : RangeList RANGE Expr
    """
    p[0] = node(get_nt_name())

def p_RangeList(p):
    """
    RangeList : ExpressionList ASSIGN 
                | IdentifierList DEFINE
                | 
    """
    p[0] = node(get_nt_name())

def p_BeginScope(p):
    """
    BeginScope : 
    """
    p[0] = []
    beginScope()


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

parser, grammar = yacc.yacc(debug=True)

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
    out = parser.parse(f.read(), lexer = lexer, debug=True)
    if out is None:
        f.close()
        sys.exit(1)
    output_file = sys.argv[1][:-2] + "output"
    with open(output_file, 'w') as fout:
        pprint.pprint(out, width=10, stream=fout)
