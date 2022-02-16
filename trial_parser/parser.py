import ply.yacc as yacc
import ply.lex as lex
import lexer
from lexer import *
import sys

tokens=lexer.tokens

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
    SourceFile : PackageStat ImportDeclMult TopLevelDeclMult
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
    ConstSpecMult : ConstSpecMult ConstSpec
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

#extra
def p_TypeName(p):
    """
    TypeName : INT
             | FLOAT
             | STRING
             | TYPE IDENT
    """

# function type remaining
def p_TypeLit(p):
    """
    TypeLit : ArrayType
            | StructType
            | PointerType
            | SliceType
            | MapType
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
    FieldDeclMult : FieldDeclMult FieldDecl
                  | 
    """

def p_FieldDecl(p):
    """
    FieldDecl : IdentifierList Type
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

# def p_FunctionLit(p):
#     """
#     FunctionLit : FUNC Signature 
#     """

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
    TypeSpecMult : TypeSpecMult TypeSpec 
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
    VarMult : VarMult VarSpec
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