import ply.yacc as yacc
import ply.lex as lex
import lexer
from lexer import *
import sys

tokens=lexer.tokens

precedence = (
    ('right', 'ASSIGN', 'DEFINE', 'NOT')
    ('left', 'LOR'),
    ('left', 'LAND'),
    ('left', 'EQL', 'NEQ','LSS','LEQ','GTR','GEQ'),
    ('left', 'ADD', 'SUB','OR','XOR'),
    ('left', 'MUL', 'QUO','REM','AND','AND_NOT','SHL','SHR'),
)

## Starting grammar

def p_SourceFile(p):
    """
    SourceFile : PackageStat ImportDeclMult TopLevDeclMult
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
    ImportDeclMult : ImportDeclMult ImportDecl
                   |  
    """

def p_ImportDecl(p):
    """
    ImportDecl : IMPORT ImportOne
               | IMPORT LPAREN ImportMult RPAREN
    """


def p_ImportMult(p):
    """
    ImportMult : ImportMult ImportOne 
               |
    """    

def p_ImportOne(p):
    """
    ImportOne : PERIOD ImportPath
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
    TopLevelDeclMult : TopLevelDeclMult TopLevelDecl
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
    ConstSpecMult : ConstSpecMult ConstSpec
                  | 
    """

def p_ConstSpec(p):
    """
    ConstSpec : IdetifierList Type ASSIGN ExpressionList 
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
    TypeName : INT
             | FLOAT
             | STRING
             | BOOL
             | TYPE IDENT
    """

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
    StructType : STRUCT LBRACE FieldDeclMult RBACE 
    """

def p_FieldDeclMult(p):
    """
    FieldDeclMult : FieldDeclMult FieldDecl
                  | 
    """

def FieldDecl(p):
    """
    FieldDecl : IdentifierList Type
    """

# pointer type
def p_PointerType(p):
    """
    PointerType : MUL BaseType
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
    AddOP : ADD 
          | SUB
          | OR
          | XOR
    """

def p_MulOp(p):
    """
    MulOp : 
    """
    

def p_ExprOth(p):
    """
    ExprOth : ExprOth COMMA Expr
            | 
    """

def p_ExprMult(p):
    """
    ExprMult : ExprMult 
    """

def p_VarDecl(p):
    """
    VarDecl : 
    """

def p_FuncDecl(p):
    """
    FuncDecl : 
    """


def p_error(p):
    print("Print Syntax Error", p)

## Build lexer
lexer = lex.lex()

parser=yacc.yacc()

with open("action.txt", "w") as f:
    for key, val in parser.action.items():
        f.writelines(f'{key} : {val}\n')

with open("goto.txt", "w") as f:
    for key, val in parser.goto.items():
        f.writelines(f'{key} : {val}\n')

## Trying to handle input

with open(sys.argv[1], 'r') as f:
    input_str = f.read()

out = parser.parse(input_str, lexer = lexer)
# print(out)