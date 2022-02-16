import ply.yacc as yacc
import ply.lex as lex
import lexer
from lexer import *
import sys

tokens=lexer.tokens
tokens.remove('COMMENT')

precedence = (
    ('right', 'ASSIGN', 'DEFINE', 'NOT'),
    ('left', 'LOR'),
    ('left', 'LAND'),
    ('left', 'EQL', 'NEQ','LSS','LEQ','GTR','GEQ'),
    ('left', 'ADD', 'SUB','OR','XOR'),
    ('left', 'MUL', 'QUO','REM','AND','AND_NOT','SHL','SHR'),
)

## Starting grammar

def p_SourceFile(p):
    """
    SourceFile : PackageStat SEMICOLON ImportDeclMult TopLevelDeclMult
    """

## Package related grammar

def p_PackageStat(p):
    """
    PackageStat : PACKAGE PackageName
    """

def p_PackageName(p):
    """
    PackageName : IDENT
    """

## Import related grammar

def p_ImportDeclMult(p):
    """
    ImportDeclMult : ImportDeclMult ImportDecl SEMICOLON
                   |  
    """

def p_ImportDecl(p):
    """
    ImportDecl : IMPORT ImportSpec
               | IMPORT LPAREN ImportSpecMult RPAREN
    """

def p_ImportMult(p):
    """
    ImportSpecMult : ImportSpecMult ImportSpec SEMICOLON 
               |
    """    

def p_ImportSpec(p):
    """
    ImportSpec : PERIOD ImportPath
              | IDENT ImportPath
              | ImportPath 
    """

def p_ImportPath(p):
    """
    ImportPath : STRING
    """

## Top-Level related grammar

def p_TopLevelDeclMult(p):
    """
    TopLevelDeclMult : TopLevelDeclMult TopLevelDecl SEMICOLON
                     |
    """

def p_TopLevelDecl(p):
    """
    TopLevelDecl : Decl 
                 | FuncDecl
    """

def p_Decl(p):
    """
    Decl : ConstDecl 
         | VarDecl
         | TypeDecl
    """

def p_ConstDecl(p):
    """
    ConstDecl : CONST ConstSpec
              | CONST LPAREN ConstSpecMult RPAREN
    """
    
def p_ConstSpecMult(p):
    """
    ConstSpecMult : ConstSpecMult ConstSpec SEMICOLON
                  | 
    """

def p_ConstSpec(p):
    """
    ConstSpec : IdentifierList Type ASSIGN ExpressionList 
    """

def p_IdentifierList(p):
    """
    IdentifierList : IDENT IdentifierOth
    """

def p_IdentifierOth(p):
    """
    IdentifierOth : IdentifierOth COMMA IDENT 
                  | 
    """
    
#Type

def p_Type(p):
    """
    Type : TypeName 
         | TypeLit
         | LPAREN Type RPAREN
    """

def p_TypeName(p):
    """
    TypeName : IDENT
             | QualifiedIdent
    """
def p_QualifiedIdent(p):
    """
    QualifiedIdent : IDENT PERIOD IDENT
    """

# function type remaining
# Added function type
def p_TypeLit(p):
    """
    TypeLit : ArrayType
            | StructType
            | PointerType
            | SliceType
            | MapType
            | FunctionType
    """

#array type
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
    """

#struct type
def p_StructType(p):
    """
    StructType : STRUCT LBRACE FieldDeclMult RBRACE 
    """

#extra
def p_FieldDeclMult(p):
    """
    FieldDeclMult : FieldDeclMult FieldDecl SEMICOLON
                  | 
    """

def p_FieldDecl(p):
    """
    FieldDecl : IdentifierList Type
              | EmbeddedField
              | IdentifierList Type Tag
              | EmbeddedField Tag
    """
def p_Tag(p):
    """
    Tag : STRING
    """

def p_EmbeddedField(p):
    """
    EmbeddedField : MUL TypeName
                  | TypeName
    """

# pointer type

def p_PointerType(p):
    """
    PointerType : MUL BaseType
    """
    
def p_BaseType(p):
    """
    BaseType : Type
    """

#slice type
def p_SliceType(p):
    """
    SliceType : LBRACK RBRACK ElementType
    """

#map type
def p_MapType(p):
    """
    MapType : MAP LBRACK KeyType RBRACK ElementType
    """
    
def p_KeyType(p):
    """
    KeyType : Type
    """

# Function Type
def p_FunctionType(p):
    """
    FunctionType : FUNC Signature 
    """

## Expression related grammar

def p_ExpressionList(p):
    """
    ExpressionList : Expr ExprOth
    """

def p_Expr(p):
    """
    Expr : UnaryExpr 
         | Expr BinOp Expr 
    """

def p_UnaryExpr(p):
    """
    UnaryExpr : PrimaryExpr 
              | UnaryOp UnaryExpr
    """

def p_BinOp(p):
    """
    BinOp : LOR 
          | LAND
          | RelOp
          | AddOp
          | MulOp
    """

def p_RelOp(p):
    """
    RelOp : EQL 
          | NEQ
          | LSS
          | LEQ
          | GTR
          | GEQ
    """

def p_AddOp(p):
    """
    AddOp : ADD 
          | SUB
          | OR
          | XOR
    """

def p_MulOp(p):
    """
    MulOp : MUL
          | QUO
          | REM
          | SHL
          | SHR
          | AND
          | AND_NOT
    """
    
def p_UnaryOp(p):
    """
    UnaryOp : ADD
            | SUB
            | NOT
            | XOR
            | MUL
            | AND
    """

def p_ExprOth(p):
    """
    ExprOth : ExprOth COMMA Expr
            | 
    """

## Operands and Literals

def p_Operand(p):
    """
    Operand : Lit 
            | OperandName
            | LPAREN Expr RPAREN
    """

def p_Lit(p):
    """
    Lit : BasicLit
        | CompositeLit
        | FunctionLit
    """    
    
def p_BasicLit(p):
    """
    BasicLit : INT
             | FLOAT
             | IMAG
             | RUNE
             | STRING
    """

def p_CompositeLit(p):
    """
    CompositeLit : StructType LiteralValue
                 | ArrayType LiteralValue
                 | SliceType LiteralValue
                 | MapType LiteralValue
                 | TypeName LiteralValue
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
    Key : IDENT
        | Expr
        | LiteralValue
    """

def p_Element(p):
    """
    Element : Expr
            | LiteralValue
    """

def p_OperandName(p):
    """
    OperandName : IDENT
    """

def p_FunctionLit(p):
    """
    FunctionLit : FUNC Signature FunctionBody
    """

## Primary Expressions

def p_PrimaryExpr(p):
    """
    PrimaryExpr : Operand
                | Conversion
                | PrimaryExpr Selector
                | PrimaryExpr Slice
                | PrimaryExpr Arguments
    """

def p_Conversion(p):
    """
    Conversion : Type LPAREN Expr RPAREN
               | Type LPAREN Expr COMMA RPAREN
    """

def p_Selector(p):
    """
    Selector : PERIOD IDENT
    """

def p_Slice(p):
    """
    Slice : LBRACK Expr COLON Expr RBRACK
          | LBRACK COLON Expr RBRACK
          | LBRACK Expr COLON RBRACK
          | LBRACK COLON RBRACK
          | LBRACK COLON Expr COLON Expr RBRACK
          | LBRACK Expr COLON Expr COLON Expr RBRACK
    """

def p_Arguments(p):
    """
    Arguments : LPAREN RPAREN
              | LPAREN ExpressionList RPAREN
              | LPAREN ExpressionList COMMA RPAREN
              | LPAREN Type RPAREN
              | LPAREN Type COMMA RPAREN
              | LPAREN Type COMMA ExpressionList RPAREN 
              | LPAREN Type COMMA ExpressionList COMMA RPAREN   
    """

## Type declarations

def p_TypeDecl(p):
    """
    TypeDecl : TYPE TypeSpec
             | TYPE LPAREN TypeSpecMult RPAREN
    """

#typespecmult
def p_TypeSpecMult(p):
    """
    TypeSpecMult : TypeSpecMult TypeSpec SEMICOLON
                 | 
    """

#typespec
def p_TypeSpec(p):
    """
    TypeSpec : AliasDecl
             | Typedef
    """

#aliasdecl
def p_AliasDecl(p):
    """
    AliasDecl : IDENT ASSIGN Type
    """
    
#typedef
def p_TypeDef(p):
    """
    Typedef : IDENT Type
    """

## Variable declarations

def p_VarDecl(p):
    """
    VarDecl : VAR VarSpec
            | VAR LPAREN VarMult RPAREN
    """

def p_VarMult(p):
    """
    VarMult : VarMult VarSpec SEMICOLON
            | 
    """

def p_VarSpec(p):
    """
    VarSpec : IdentifierList Type ASSIGN ExpressionList
            | IdentifierList ASSIGN ExpressionList
            | IdentifierList Type
    """

def p_ShortVarDecl(p):
    """
    ShortVarDecl : IdentifierList DEFINE ExpressionList
    """

## Function Declarations

def p_FuncDecl(p):
    """
    FuncDecl : FUNC FunctionName Signature FunctionBody
             | FUNC FunctionName Signature
    """

def p_FunctionName(p):
    """
    FunctionName : IDENT
    """    

def p_FunctionBody(p):
    """
    FunctionBody : Block
    """

def p_Signature(p):
    """
    Signature : Parameters Result
              | Parameters
    """

def p_Parameters(p):
    """
    Parameters : LPAREN RPAREN
               | LPAREN ParameterList RPAREN
               | LPAREN ParameterList COMMA RPAREN
    """
    
def p_ParameterList(p):
    """
    ParameterList : ParameterList COMMA ParameterDecl
                  | ParameterDecl
    """

def p_ParameterDecl(p):
    """
    ParameterDecl : Type
                  | IdentifierList Type
    """

def p_Result(p):
    """
    Result : Parameters 
           | Type
    """

## Statements ---------------------------------------

def p_StatementList(p):
    """
    StatementList : StatementList Statement SEMICOLON 
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

## Labeled Statements-----------------------------------
def p_LabeledStmt(p):
    """
    LabeledStmt : Label COLON Statement
    """

def p_Label(p):
    """
    Label : IDENT
    """
## -----------------------------------------------------

## Simple Statements -----------------------------------
def p_SimpleStmt(p):
    """
    SimpleStmt :  EmptyStmt
                | ExpressionStmt
                | IncDecStmt
                | Assignment
                | ShortVarDecl
    """

def p_EmptyStmt(p):
    """
    EmptyStmt : 
    """

def p_ExpressionStmt(p):
    """
    ExpressionStmt : Expr
    """

def p_IncDecStmt(p):
    """
    IncDecStmt :  Expr INC
                | Expr DEC
    """

## Assignment Statements --------------------------
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
## ------------------------------------------------
## ------------------------------------------------

def p_ReturnStmt(p):
    """
    ReturnStmt : RETURN ExpressionList
                | RETURN
    """

def p_BreakStmt(p):
    """
    BreakStmt : BREAK Label
                | BREAK
    """

def p_ContinueStmt(p):
    """
    ContinueStmt :  CONTINUE Label
                    | CONTINUE
    """

def p_GotoStmt(p):
    """
    GotoStmt :  GOTO Label
    """

def p_FallthroughStmt(p):
    """
    FallthroughStmt : FALLTHROUGH
    """

def p_Block(p):
    """
    Block : LBRACE StatementList RBRACE
    """

## If Else Block -----------------------------------
def p_IfStmt(p):
    """
    IfStmt : IF SimpleStmtOpt Expr Block else_stmt
    """

def p_else_stmt(p):
    """
    else_stmt : ELSE IfStmt
                | ELSE Block
                |
    """

def p_SimpleStmtOpt(p):
    """
    SimpleStmtOpt : SimpleStmt SEMICOLON 
                    |
    """
## --------------------------------------------------


## Switch Stmt --------------------------------------
def p_SwitchStmt(p):
    """
    SwitchStmt :  ExprSwitchStmt
                 | TypeSwitchStmt
    """

## ExprSwitchStmt -----------------------------------
def p_ExprSwitchStmt(p):
    """
    ExprSwitchStmt : SWITCH SimpleStmtOpt ExprOpt LBRACE ExprCaseClauseMult RBRACE
    """

def p_ExprOpt(p):
    """
    ExprOpt : Expr
              |
    """

def p_ExprCaseClauseMult(p):
    """
    ExprCaseClauseMult : ExprCaseClauseMult ExprCaseClause
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
## -------------------------------------------------

## TypeSwitchStmt ----------------------------------
def p_TypeSwitchStmt(p):
    """
    TypeSwitchStmt : SWITCH SimpleStmtOpt TypeSwitchGuard LBRACE TypeCaseClauseMult RBRACE
    """

def p_TypeSwitchGuard(p):
    """
    TypeSwitchGuard : ShortVarDeclOpt PrimaryExpr PERIOD LPAREN TYPE RPAREN
    """

def p_ShortVarDeclOpt(p):
    """
    ShortVarDeclOpt :   IDENT DEFINE
                        |
    """
def p_TypeCaseClauseMult(p):
    """
    TypeCaseClauseMult : TypeCaseClauseMult TypeCaseClause
                        |
    """

def p_TypeCaseClause(p):
    """
    TypeCaseClause : TypeSwitchCase COLON StatementList
    """

def p_TypeSwitchCase(p):
    """
    TypeSwitchCase : CASE TypeList 
                     | DEFAULT
    """

def p_TypeList(p):
    """
    TypeList : Type TypeOth
    """

def p_TypeOth(p):
    """
    TypeOth :  COMMA Type TypeOth
                |
    """
## -------------------------------------------------


## --------------------------------------------------



## For Stmt -----------------------------------------
def p_ForStmt(p):
    """
    ForStmt : FOR Condition Block
            | FOR ForClause Block
            | FOR RangeClause Block
    """

def p_Condition(p):
    """
    Condition : Expr
    """

## For Clause -------------------------------------
def p_ForClause(p):
    """
    ForClause : InitStmt SEMICOLON ConditionOpt SEMICOLON PostStmt
    """

def p_InitStmt(p):
    """
    InitStmt :   SimpleStmt
    """

def p_ConditionOpt(p):
    """
    ConditionOpt :   Condition
                    |
    """

def p_PostStmt(p):
    """
    PostStmt :   SimpleStmt
    """
## --------------------------------------------------

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

## --------------------------------------------------
## --------------------------------------------------

def p_error(p):
    print("Print Syntax Error", p)

## Build lexer
lexer = lex.lex()

parser=yacc.yacc(debug=False)

path_to_root = os.environ['PATH_TO_ROOT']
milestone = os.environ['MILESTONE']
with open(path_to_root + "/src/Milestone" + str(milestone) + "/action.txt", "w") as f:
    for key, val in parser.action.items():
        f.writelines(f'{key} : {val}\n')

with open(path_to_root + "/src/Milestone" + str(milestone) + "/goto.txt", "w") as f:
    for key, val in parser.goto.items():
        f.writelines(f'{key} : {val}\n')

## Trying to handle input

with open(sys.argv[1], 'r') as f:
    input_str = f.read()
out = parser.parse(input_str, lexer = lexer)
print(out)