import ply.yacc as yacc
import ply.lex as lex
import lexer
from lexer import *
import sys

tokens=lexer.tokens

def p_varE(p):
    """
    varE : varE ADD varT 
         | varT
    """

def p_varT(p):
    """
    varT : varT MUL varF
         | varF
    """

def p_varF(p):
    """
    varF : LPAREN varE RPAREN 
         | IDENT
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