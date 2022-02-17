import ply.yacc as yacc
import ply.lex as lex
import lexer
from lexer import *
import sys

tokens=lexer.tokens
tokens.remove('COMMENT')

precedence = (
    ('left', 'IDENT'),
    ('left', 'COMMA' ),
    ('left', 'LBRACK' ),
    ('left', 'RBRACK'),
    ('left', 'LBRACE'),
    ('left', 'RBRACE'),
    ('left', 'PERIOD'),
    ('left', 'SEMICOLON'),
    ('left', 'COLON'),
    ('left', 'INT'),
    ('left', 'FLOAT'),
    ('left', 'STRING'),
    ('left', 'BREAK'),
    ('left', 'CONTINUE'),
    ('left', 'RETURN'),
    ('right', 'ASSIGN', 'DEFINE', 'NOT'),
    ('left','LPAREN'),
    ('left','RPAREN'),
    ('left', 'LOR'),
    ('left', 'LAND'),
    ('left', 'EQL', 'NEQ','LSS','LEQ','GTR','GEQ'),
    ('left', 'ADD', 'SUB','OR','XOR'),
    ('left', 'MUL', 'QUO','REM','AND','AND_NOT','SHL','SHR'),
)

non_terminals = {}

## Starting grammar
def get_value_p(p):
    value = [str(sys._getframe(1).f_code.co_name)[2:]]
    for i in range(1, len(p)):
        if isinstance(p[i], str) and p[i] not in non_terminals:
            value.append([p[i]])
        else:
            value.append(p[i])
    return value
    
def p_SourceFile(p):
    """
    SourceFile : PackageClause SEMICOLON ImportDeclMult TopLevelDeclMult
    """
    p[0] = get_value_p(p)
    

## Package related grammar

def p_PackageClause(p):
    """
    PackageClause : PACKAGE PackageName
    """
    p[0] = get_value_p(p)

def p_PackageName(p):
    """
    PackageName : IDENT
    """
    p[0] = get_value_p(p)

## Import related grammar

def p_ImportDeclMult(p):
    """
    ImportDeclMult : ImportDeclMult ImportDecl SEMICOLON
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

## Top-Level related grammar

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
    """
    p[0] = get_value_p(p)

def p_IdentifierList(p):
    """
    IdentifierList : IDENT IdentifierOth
    """
    p[0] = get_value_p(p)

def p_IdentifierOth(p):
    """
    IdentifierOth : COMMA IDENT IdentifierOth  
                  | 
    """
    p[0] = get_value_p(p)
    
#Type

def p_Type(p):
    """
    Type : TypeName 
         | TypeLit
         | LPAREN Type RPAREN
    """
    p[0] = get_value_p(p)

def p_TypeName(p):
    """
    TypeName : IDENT
             | QualifiedIdent
    """
    p[0] = get_value_p(p)

def p_QualifiedIdent(p):
    """
    QualifiedIdent : IDENT PERIOD IDENT
    """
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

#array type
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
    """
    p[0] = get_value_p(p)

#struct type
def p_StructType(p):
    """
    StructType : STRUCT LBRACE FieldDeclMult RBRACE 
    """
    p[0] = get_value_p(p)

#extra
def p_FieldDeclMult(p):
    """
    FieldDeclMult : FieldDecl SEMICOLON FieldDeclMult 
                  | 
    """
    p[0] = get_value_p(p)

def p_FieldDecl(p):
    """
    FieldDecl : IdentifierList Type
              | EmbeddedField
              | IdentifierList Type Tag
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
    EmbeddedField : MUL TypeName
                  | TypeName
    """
    p[0] = get_value_p(p)

# pointer type

def p_PointerType(p):
    """
    PointerType : MUL BaseType
    """
    p[0] = get_value_p(p)
    
def p_BaseType(p):
    """
    BaseType : Type
    """
    p[0] = get_value_p(p)

#slice type
def p_SliceType(p):
    """
    SliceType : LBRACK RBRACK ElementType
    """
    p[0] = get_value_p(p)

#map type
def p_MapType(p):
    """
    MapType : MAP LBRACK KeyType RBRACK ElementType
    """
    p[0] = get_value_p(p)
    
def p_KeyType(p):
    """
    KeyType : Type
    """
    p[0] = get_value_p(p)

# Function Type
def p_FunctionType(p):
    """
    FunctionType : FUNC Signature 
    """
    p[0] = get_value_p(p)

## Expression related grammar

def p_ExpressionList(p):
    """
    ExpressionList : Expr ExprOth
    """
    p[0] = get_value_p(p)

def p_Expr(p):
    """
    Expr : UnaryExpr 
         | Expr BinOp Expr 
    """
    p[0] = get_value_p(p)

def p_UnaryExpr(p):
    """
    UnaryExpr : PrimaryExpr 
              | UnaryOp UnaryExpr
    """
    p[0] = get_value_p(p)

def p_BinOp(p):
    """
    BinOp : LOR 
          | LAND
          | RelOp
          | AddOp
          | MulOp
    """
    p[0] = get_value_p(p)

def p_RelOp(p):
    """
    RelOp : EQL 
          | NEQ
          | LSS
          | LEQ
          | GTR
          | GEQ
    """
    p[0] = get_value_p(p)

def p_AddOp(p):
    """
    AddOp : ADD 
          | SUB
          | OR
          | XOR
    """
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)
    
def p_UnaryOp(p):
    """
    UnaryOp : ADD
            | SUB
            | NOT
            | XOR
            | MUL
            | AND
    """
    p[0] = get_value_p(p)

def p_ExprOth(p):
    """
    ExprOth : COMMA Expr ExprOth 
            | 
    """
    p[0] = get_value_p(p)

## Operands and Literals

def p_Operand(p):
    """
    Operand : Lit 
            | OperandName
            | LPAREN Expr RPAREN
    """
    p[0] = get_value_p(p)

def p_Lit(p):
    """
    Lit : BasicLit
        | CompositeLit
        | FunctionLit
    """
    p[0] = get_value_p(p)
    
def p_BasicLit(p):
    """
    BasicLit : INT
             | FLOAT
             | IMAG
             | RUNE
             | STRING
    """
    p[0] = get_value_p(p)

def p_CompositeLit(p):
    """
    CompositeLit : StructType LiteralValue
                 | ArrayType LiteralValue
                 | SliceType LiteralValue
                 | MapType LiteralValue
                 | TypeName LiteralValue
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
                | COMMA KeyedElement ElementList 
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
    Key : IDENT
        | Expr
        | LiteralValue
    """
    p[0] = get_value_p(p)

def p_Element(p):
    """
    Element : Expr
            | LiteralValue
    """
    p[0] = get_value_p(p)

def p_OperandName(p):
    """
    OperandName : IDENT
    """
    p[0] = get_value_p(p)

def p_FunctionLit(p):
    """
    FunctionLit : FUNC Signature FunctionBody
    """
    p[0] = get_value_p(p)

## Primary Expressions

def p_PrimaryExpr(p):
    """
    PrimaryExpr : Operand
                | Conversion
                | PrimaryExpr Selector
                | PrimaryExpr Slice
                | PrimaryExpr Arguments
    """
    p[0] = get_value_p(p)

def p_Conversion(p):
    """
    Conversion : Type LPAREN Expr RPAREN
               | Type LPAREN Expr COMMA RPAREN
    """
    p[0] = get_value_p(p)

def p_Selector(p):
    """
    Selector : PERIOD IDENT
    """
    p[0] = get_value_p(p)

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
    p[0] = get_value_p(p)

## Type declarations

def p_TypeDecl(p):
    """
    TypeDecl : TYPE TypeSpec
             | TYPE LPAREN TypeSpecMult RPAREN
    """
    p[0] = get_value_p(p)

#typespecmult
def p_TypeSpecMult(p):
    """
    TypeSpecMult : TypeSpec SEMICOLON TypeSpecMult 
                 | 
    """
    p[0] = get_value_p(p)

#typespec
def p_TypeSpec(p):
    """
    TypeSpec : AliasDecl
             | Typedef
    """
    p[0] = get_value_p(p)

#aliasdecl
def p_AliasDecl(p):
    """
    AliasDecl : IDENT ASSIGN Type
    """
    p[0] = get_value_p(p)

#typedef
def p_TypeDef(p):
    """
    Typedef : IDENT Type
    """
    p[0] = get_value_p(p)

## Variable declarations

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
            | IdentifierList ASSIGN ExpressionList
            | IdentifierList Type
    """
    p[0] = get_value_p(p)

def p_ShortVarDecl(p):
    """
    ShortVarDecl : IdentifierList DEFINE ExpressionList
    """
    p[0] = get_value_p(p)

## Function Declarations

def p_FuncDecl(p):
    """
    FuncDecl : FUNC FunctionName Signature FunctionBody
             | FUNC FunctionName Signature
    """
    p[0] = get_value_p(p)

def p_FunctionName(p):
    """
    FunctionName : IDENT
    """
    p[0] = get_value_p(p)

def p_FunctionBody(p):
    """
    FunctionBody : Block
    """
    p[0] = get_value_p(p)

def p_Signature(p):
    """
    Signature : Parameters Result
              | Parameters
    """
    p[0] = get_value_p(p)

def p_Parameters(p):
    """
    Parameters : LPAREN RPAREN
               | LPAREN ParameterList RPAREN
               | LPAREN ParameterList COMMA RPAREN
    """
    p[0] = get_value_p(p)
    
def p_ParameterList(p):
    """
    ParameterList : COMMA ParameterDecl ParameterList 
                  | ParameterDecl
    """
    p[0] = get_value_p(p)

def p_ParameterDecl(p):
    """
    ParameterDecl : Type
                  | IdentifierList Type
    """
    p[0] = get_value_p(p)

def p_Result(p):
    """
    Result : Parameters 
           | Type
    """
    p[0] = get_value_p(p)

## Statements ---------------------------------------

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
              | Block
              | IfStmt
              | SwitchStmt
              | ForStmt
    """
    p[0] = get_value_p(p)

## Labeled Statements-----------------------------------
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
    p[0] = get_value_p(p)

def p_EmptyStmt(p):
    """
    EmptyStmt : 
    """
    p[0] = get_value_p(p)

def p_ExpressionStmt(p):
    """
    ExpressionStmt : Expr
    """
    p[0] = get_value_p(p)

def p_IncDecStmt(p):
    """
    IncDecStmt :  Expr INC
                | Expr DEC
    """
    p[0] = get_value_p(p)

## Assignment Statements --------------------------
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

## ------------------------------------------------
## ------------------------------------------------

def p_ReturnStmt(p):
    """
    ReturnStmt : RETURN ExpressionList
                | RETURN
    """
    p[0] = get_value_p(p)

def p_BreakStmt(p):
    """
    BreakStmt : BREAK Label
                | BREAK
    """
    p[0] = get_value_p(p)

def p_ContinueStmt(p):
    """
    ContinueStmt :  CONTINUE Label
                    | CONTINUE
    """
    p[0] = get_value_p(p)

def p_GotoStmt(p):
    """
    GotoStmt :  GOTO Label
    """
    p[0] = get_value_p(p)

def p_FallthroughStmt(p):
    """
    FallthroughStmt : FALLTHROUGH
    """
    p[0] = get_value_p(p)

def p_Block(p):
    """
    Block : LBRACE StatementList RBRACE
    """
    p[0] = get_value_p(p)

## If Else Block -----------------------------------
def p_IfStmt(p):
    """
    IfStmt : IF SimpleStmtOpt Expr Block else_stmt
    """
    p[0] = get_value_p(p)

def p_else_stmt(p):
    """
    else_stmt : ELSE IfStmt
                | ELSE Block
                |
    """
    p[0] = get_value_p(p)

def p_SimpleStmtOpt(p):
    """
    SimpleStmtOpt : SimpleStmt SEMICOLON 
                    |
    """
    p[0] = get_value_p(p)

## --------------------------------------------------


## Switch Stmt --------------------------------------
def p_SwitchStmt(p):
    """
    SwitchStmt :  ExprSwitchStmt
                 | TypeSwitchStmt
    """
    p[0] = get_value_p(p)

## ExprSwitchStmt -----------------------------------
def p_ExprSwitchStmt(p):
    """
    ExprSwitchStmt : SWITCH SimpleStmtOpt ExprOpt LBRACE ExprCaseClauseMult RBRACE
    """
    p[0] = get_value_p(p)

def p_ExprOpt(p):
    """
    ExprOpt : Expr
              |
    """
    p[0] = get_value_p(p)

def p_ExprCaseClauseMult(p):
    """
    ExprCaseClauseMult : ExprCaseClause ExprCaseClauseMult 
                         |
    """
    p[0] = get_value_p(p)

def p_ExprCaseClause(p):
    """
    ExprCaseClause : ExprSwitchCase COLON StatementList
    """
    p[0] = get_value_p(p)

def p_ExprSwitchCase(p):
    """
    ExprSwitchCase : CASE ExpressionList
                     | DEFAULT
    """
    p[0] = get_value_p(p)
## -------------------------------------------------

## TypeSwitchStmt ----------------------------------
def p_TypeSwitchStmt(p):
    """
    TypeSwitchStmt : SWITCH SimpleStmtOpt TypeSwitchGuard LBRACE TypeCaseClauseMult RBRACE
    """
    p[0] = get_value_p(p)

def p_TypeSwitchGuard(p):
    """
    TypeSwitchGuard : ShortVarDeclOpt PrimaryExpr PERIOD LPAREN TYPE RPAREN
    """
    p[0] = get_value_p(p)

def p_ShortVarDeclOpt(p):
    """
    ShortVarDeclOpt :   IDENT DEFINE
                        |
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
    TypeCaseClause : TypeSwitchCase COLON StatementList
    """
    p[0] = get_value_p(p)

def p_TypeSwitchCase(p):
    """
    TypeSwitchCase : CASE TypeList 
                     | DEFAULT
    """
    p[0] = get_value_p(p)

def p_TypeList(p):
    """
    TypeList : Type TypeOth
    """
    p[0] = get_value_p(p)

def p_TypeOth(p):
    """
    TypeOth :  COMMA Type TypeOth
                |
    """
    p[0] = get_value_p(p)

## -------------------------------------------------


## --------------------------------------------------



## For Stmt -----------------------------------------
def p_ForStmt(p):
    """
    ForStmt : FOR Condition Block
            | FOR ForClause Block
            | FOR RangeClause Block
    """
    p[0] = get_value_p(p)

def p_Condition(p):
    """
    Condition : Expr
    """
    p[0] = get_value_p(p)

## For Clause -------------------------------------
def p_ForClause(p):
    """
    ForClause : InitStmt SEMICOLON ConditionOpt SEMICOLON PostStmt
    """
    p[0] = get_value_p(p)

def p_InitStmt(p):
    """
    InitStmt :   SimpleStmt
    """
    p[0] = get_value_p(p)

def p_ConditionOpt(p):
    """
    ConditionOpt :   Condition
                    |
    """
    p[0] = get_value_p(p)

def p_PostStmt(p):
    """
    PostStmt :   SimpleStmt
    """
    p[0] = get_value_p(p)

## --------------------------------------------------

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

## --------------------------------------------------
## --------------------------------------------------

def p_error(p):
    print("Syntax Error: ", p)

## Build lexer
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
