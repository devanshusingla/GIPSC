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
    context['forDepth'] = 0 # Inside 0 for loops at present
    context['switchDepth'] = 0 # Inside 0 switch statements at present

def endContext():
    print(context)

def beginScope():
    print("Beginning Scope")
    pass

def endScope():
    print("Ending Scope")
    pass

###################################################################################
#####################                                        ######################
######                         STARTING GRAMMAR                            ########
#####################                                        ######################
###################################################################################

COMPACT = False
def get_value_p(p):
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
    
def p_SourceFile(p):
    """
    SourceFile : SetupContext PackageClause SEMICOLON ImportDeclMult TopLevelDeclMult
    """
    p[0] = get_value_p(p)
    endContext()

def p_SetupContext(p):
    """
    SetupContext :
    """    
    p[0] = []
    setupContext()

def p_BeginScope(p):
    """
    BeginScope : 
    """
    p[0] = []
    beginScope()

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
    p[0] = get_value_p(p)

###################################################################################
### Import related grammar
###################################################################################

def p_ImportDeclMult(p):
    """
    ImportDeclMult : ImportDecl SEMICOLON ImportDeclMult
                   |  
    """
    p[0] = get_value_p(p)

def p_ImportDecl(p):
    """
    ImportDecl : IMPORT ImportSpec
               | IMPORT LPAREN ImportSpecMult RPAREN
    """
    p[0] = get_value_p(p)

def p_ImportMult(p):
    """
    ImportSpecMult : ImportSpec SEMICOLON ImportSpecMult  
               |
    """
    p[0] = get_value_p(p)

def p_ImportSpec(p):
    """
    ImportSpec : PERIOD ImportPath
              | IDENT ImportPath
              | ImportPath 
    """
    p[0] = get_value_p(p)
    
def p_ImportPath(p):
    """
    ImportPath : STRING
    """
    p[0] = get_value_p(p)

###################################################################################
### Top-Level related grammar
###################################################################################

def p_TopLevelDeclMult(p):
    """
    TopLevelDeclMult : TopLevelDecl SEMICOLON TopLevelDeclMult 
                     |
    """
    p[0] = get_value_p(p)

def p_TopLevelDecl(p):
    """
    TopLevelDecl : Decl 
                 | FuncDecl
    """
    p[0] = get_value_p(p)

def p_Decl(p):
    """
    Decl : ConstDecl 
         | VarDecl
         | TypeDecl
    """
    p[0] = get_value_p(p)

###################################################################################
### Constant Declarations
###################################################################################

def p_ConstDecl(p):
    """
    ConstDecl : CONST ConstSpec
              | CONST LPAREN ConstSpecMult RPAREN
    """
    p[0] = get_value_p(p)

def p_ConstSpecMult(p):
    """
    ConstSpecMult : ConstSpec SEMICOLON ConstSpecMult 
                  | 
    """
    p[0] = get_value_p(p)

def p_ConstSpec(p):
    """
    ConstSpec : IdentifierList Type ASSIGN ExpressionList 
                | IdentifierList IDENT ASSIGN ExpressionList
                | IdentifierList IDENT PERIOD IDENT ASSIGN ExpressionList
    """
    p[0] = get_value_p(p)

###################################################################################
### Variable Declarations
###################################################################################

def p_VarDecl(p):
    """
    VarDecl : VAR VarSpec
            | VAR LPAREN VarMult RPAREN
    """
    p[0] = get_value_p(p)

def p_VarMult(p):
    """
    VarMult : VarSpec SEMICOLON VarMult 
            | 
    """
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

###################################################################################
### Type Declarations
###################################################################################

def p_TypeDecl(p):
    """
    TypeDecl : TYPE TypeSpec
             | TYPE LPAREN TypeSpecMult RPAREN
    """
    p[0] = get_value_p(p)

def p_TypeSpecMult(p):
    """
    TypeSpecMult : TypeSpec SEMICOLON TypeSpecMult 
                 | 
    """
    p[0] = get_value_p(p)

def p_TypeSpec(p):
    """
    TypeSpec : AliasDecl
             | Typedef
    """
    p[0] = get_value_p(p)

def p_AliasDecl(p):
    """
    AliasDecl : IDENT ASSIGN Type
                | IDENT ASSIGN IDENT
                | IDENT ASSIGN IDENT PERIOD IDENT
    """
    p[0] = get_value_p(p)

def p_TypeDef(p):
    """
    Typedef : IDENT Type
              | IDENT IDENT
              | IDENT IDENT PERIOD IDENT

    """
    p[0] = get_value_p(p)

###################################################################################
### Identifier List
###################################################################################

def p_IdentifierList(p):
    """
    IdentifierList : IDENT
                   | IDENT COMMA IdentifierList
    """
    p[0] = get_value_p(p)


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
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

###################################################################################
## Selector

def p_Selector(p):
    """
    Selector : PERIOD IDENT
    """
    p[0] = get_value_p(p)

###################################################################################
## Index

def p_Index(p):
    """
    Index : LBRACK Expr RBRACK
    """
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)


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
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

###################################################################################
### Pointer Type
###################################################################################

def p_PointerType(p):
    """
    PointerType : MUL Type %prec UMUL
               | MUL IDENT %prec UMUL
                | MUL IDENT PERIOD IDENT %prec UMUL
    """
    p[0] = get_value_p(p)

###################################################################################
### Slice Type
###################################################################################

def p_SliceType(p):
    """
    SliceType : LBRACK RBRACK ElementType
    """
    p[0] = get_value_p(p)

###################################################################################
### Array Type
###################################################################################

def p_ArrayType(p):
    """
    ArrayType : LBRACK ArrayLength RBRACK ElementType
    """
    p[0] = get_value_p(p)

def p_ArrayLength(p):
    """
    ArrayLength : Expr
    """
    p[0] = get_value_p(p)

def p_ElementType(p):
    """
    ElementType : Type
                | IDENT
                | IDENT PERIOD IDENT
    """
    p[0] = get_value_p(p)

###################################################################################
### Struct Type
###################################################################################

def p_StructType(p):
    """
    StructType : STRUCT LBRACE FieldDeclMult RBRACE 
    """
    p[0] = get_value_p(p)

#extra
def p_FieldDeclMult(p):
    """
    FieldDeclMult : FieldDeclMult FieldDecl SEMICOLON
                  | 
    """
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)
    
def p_Tag(p):
    """
    Tag : STRING
    """
    p[0] = get_value_p(p)

def p_EmbeddedField(p):
    """
    EmbeddedField : MUL IDENT
                  | IDENT
                  | MUL IDENT PERIOD IDENT
                  | IDENT PERIOD IDENT
    """
    p[0] = get_value_p(p)

###################################################################################
### Map Type
###################################################################################

def p_MapType(p):
    """
    MapType : MAP LBRACK KeyType RBRACK ElementType
    """
    p[0] = get_value_p(p)
    
def p_KeyType(p):
    """
    KeyType : Type
            | IDENT
            | IDENT PERIOD IDENT
    """
    p[0] = get_value_p(p)

###################################################################################
### Function Type
###################################################################################

def p_FunctionType(p):
    """
    FunctionType : FUNC Signature 
    """
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

def p_LiteralValue(p):
    """
    LiteralValue : LBRACE ElementList COMMA RBRACE 
                 | LBRACE ElementList RBRACE 
                 | LBRACE RBRACE 
    """
    p[0] = get_value_p(p)

def p_ElementList(p):
    """
    ElementList : KeyedElement 
                | ElementList COMMA KeyedElement 
    """
    p[0] = get_value_p(p)

def p_KeyedElement(p):
    """
    KeyedElement : Element
                 | Key COLON Element
    """
    p[0] = get_value_p(p)

def p_Key(p):
    """
    Key : Expr
        | LiteralValue
    """
    p[0] = get_value_p(p)

def p_Element(p):
    """
    Element : Expr
            | LiteralValue
    """
    p[0] = get_value_p(p)

###################################################################################
### Function Literal
###################################################################################

def p_FunctionLit(p):
    """
    FunctionLit : FUNC Signature FunctionBody
    """
    p[0] = get_value_p(p)

###################################################################################
## Function Declarations

def p_FuncDecl(p):
    """
    FuncDecl : FUNC FunctionName Signature BeginScope FunctionBody EndScope
             | FUNC FunctionName Signature
    """
    p[0] = get_value_p(p)

###################################################################################
## Function Name

def p_FunctionName(p):
    """
    FunctionName : IDENT
    """
    p[0] = get_value_p(p)

###################################################################################
## Function Body

def p_FunctionBody(p):
    """
    FunctionBody : Block
    """
    p[0] = get_value_p(p)

###################################################################################
## Function Signature

def p_Signature(p):
    """
    Signature : Parameters Result
              | Parameters
    """
    p[0] = get_value_p(p)

###################################################################################
## Function Parameters

def p_Parameters(p):
    """
    Parameters : LPAREN RPAREN
               | LPAREN ParameterList RPAREN
               | LPAREN ParameterList COMMA RPAREN
    """
    p[0] = get_value_p(p)
    
def p_ParameterList(p):
    """
    ParameterList : ParameterDecl
                  | ParameterList COMMA IDENT
                  | ParameterList COMMA IDENT PERIOD IDENT
                  | ParameterList COMMA Type
                  | ParameterList COMMA ParameterDecl 
    """
    p[0] = get_value_p(p)

def p_ParameterDecl(p):
    """
    ParameterDecl : IdentifierList Type
                  | IdentifierList IDENT
                  | IdentifierList IDENT PERIOD IDENT
    """
    p[0] = get_value_p(p)

###################################################################################
## Return Type

def p_Result(p):
    """
    Result : Parameters 
           | Type
           | IDENT
           | IDENT PERIOD IDENT
    """
    p[0] = get_value_p(p)


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
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

###################################################################################
### Labeled Statements
###################################################################################

def p_LabeledStmt(p):
    """
    LabeledStmt : Label COLON Statement
    """
    p[0] = get_value_p(p)

def p_Label(p):
    """
    Label : IDENT
    """
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

###################################################################################
### Empty Statements

def p_EmptyStmt(p):
    """
    EmptyStmt : 
    """
    p[0] = get_value_p(p)

###################################################################################
### Expression Statements

def p_ExpressionStmt(p):
    """
    ExpressionStmt : Expr
    """
    p[0] = get_value_p(p)

###################################################################################
### Increment/Decrement Statements

def p_IncDecStmt(p):
    """
    IncDecStmt :  Expr INC
                 | Expr DEC
    """
    p[0] = get_value_p(p)

###################################################################################
### Assignment Statements

def p_Assignment(p):
    """
    Assignment : ExpressionList assign_op ExpressionList
    """
    p[0] = get_value_p(p)

def p_assign_op(p):
    """
    assign_op : add_op_assign 
              | mul_op_assign
              | ASSIGN
    """
    p[0] = get_value_p(p)

def p_add_op_assign(p):
    """
    add_op_assign : ADD_ASSIGN
                    | SUB_ASSIGN
                    | OR_ASSIGN
                    | XOR_ASSIGN
    """
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

###################################################################################
### Short Variable Declaration

def p_ShortVarDecl(p):
    """
    ShortVarDecl : IdentifierList DEFINE ExpressionList
    """
    p[0] = get_value_p(p)

###################################################################################
### Goto Statements
###################################################################################

def p_GotoStmt(p):
    """
    GotoStmt :  GOTO Label
    """
    p[0] = get_value_p(p)

###################################################################################
### Return Statements
###################################################################################

def p_ReturnStmt(p):
    """
    ReturnStmt : RETURN ExpressionList
                | RETURN
    """
    p[0] = get_value_p(p)

###################################################################################
### Break Statements
###################################################################################

def p_BreakStmt(p):
    """
    BreakStmt : BREAK Label
                | BREAK
    """
    p[0] = get_value_p(p)

###################################################################################
### Continue Statements
###################################################################################

def p_ContinueStmt(p):
    """
    ContinueStmt :  CONTINUE Label
                    | CONTINUE
    """
    p[0] = get_value_p(p)

###################################################################################
### Fallthrough Statements
###################################################################################

def p_FallthroughStmt(p):
    """
    FallthroughStmt : FALLTHROUGH
    """
    p[0] = get_value_p(p)

###################################################################################
### Block Statements
###################################################################################

def p_Block(p):
    """
    Block : LBRACE StatementList RBRACE
    """
    p[0] = get_value_p(p)

###################################################################################
### If Else Statements
###################################################################################

def p_IfStmt(p):
    """
    IfStmt : IF Expr BeginScope Block EndScope else_stmt
           | IF BeginScope SimpleStmt EndScope SEMICOLON Expr else_stmt
    """
    p[0] = get_value_p(p)

def p_else_stmt(p):
    """
    else_stmt : ELSE IfStmt
                | ELSE BeginScope Block EndScope
                |
    """
    p[0] = get_value_p(p)

###################################################################################
### Switch Statements
###################################################################################

def p_SwitchStmt(p):
    """
    SwitchStmt :  ExprSwitchStmt
                 | TypeSwitchStmt
    """
    p[0] = get_value_p(p)

###################################################################################
### Expression Switch Statements

def p_ExprSwitchStmt(p):
    """
    ExprSwitchStmt : SWITCH BeginScope SimpleStmt EndScope SEMICOLON BeginScope Expr EndScope LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
                     | SWITCH Expr LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
                     | SWITCH BeginScope SimpleStmt EndScope SEMICOLON LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
                     | SWITCH LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
    """
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

def p_ExprCaseClause(p):
    """
    ExprCaseClause : BeginScope ExprSwitchCase COLON StatementList EndScope
    """
    p[0] = get_value_p(p)

def p_ExprSwitchCase(p):
    """
    ExprSwitchCase : CASE ExpressionList
                     | DEFAULT
    """
    p[0] = get_value_p(p)

###################################################################################
### Type Switch Statements

def p_TypeSwitchStmt(p):
    """
    TypeSwitchStmt : SWITCH SimpleStmt SEMICOLON TypeSwitchGuard LBRACE TypeCaseClauseMult RBRACE
                     | SWITCH TypeSwitchGuard LBRACE TypeCaseClauseMult RBRACE
    """
    p[0] = get_value_p(p)

def p_TypeSwitchGuard(p):
    """
    TypeSwitchGuard : IDENT DEFINE PrimaryExpr PERIOD LPAREN TYPE RPAREN
                      | PrimaryExpr PERIOD LPAREN TYPE RPAREN
    """
    p[0] = get_value_p(p)

def p_TypeCaseClauseMult(p):
    """
    TypeCaseClauseMult : TypeCaseClause TypeCaseClauseMult 
                        |
    """
    p[0] = get_value_p(p)

def p_TypeCaseClause(p):
    """
    TypeCaseClause : CASE BeginScope TypeList EndScope COLON BeginScope StatementList EndScope
                     | DEFAULT COLON BeginScope StatementList EndScope
    """
    p[0] = get_value_p(p)

def p_TypeList(p):
    """
    TypeList : Type
                | IDENT 
                | IDENT PERIOD IDENT
                | Type COMMA TypeList
                | IDENT COMMA TypeList
                | IDENT PERIOD IDENT COMMA TypeList
    """
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

def p_BeginFor(p):
    """
    BeginFor : 
    """
    print("For Begins")
    beginScope()
    context['forDepth'] += 1
    # Add two labels to be used
    # for code generation

def p_EndFor(p):
    """
    EndFor : 
    """
    print("For Ends")
    context['forDepth'] -= 1
    endScope()

def p_Condition(p):
    """
    Condition : Expr
    """
    p[0] = get_value_p(p)

###################################################################################
### For Clause

def p_ForClause(p):
    """
    ForClause : InitStmt SEMICOLON Condition SEMICOLON PostStmt
                | InitStmt SEMICOLON SEMICOLON PostStmt
    """
    p[0] = get_value_p(p)

def p_InitStmt(p):
    """
    InitStmt :   SimpleStmt
    """
    p[0] = get_value_p(p)

def p_PostStmt(p):
    """
    PostStmt :   SimpleStmt
    """
    p[0] = get_value_p(p)

###################################################################################
### Range Clause

def p_RangeClause(p):
    """
    RangeClause : RangeList RANGE Expr
    """
    p[0] = get_value_p(p)

def p_RangeList(p):
    """
    RangeList : ExpressionList ASSIGN 
                | IdentifierList DEFINE
                | 
    """
    p[0] = get_value_p(p)


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
