import ply.yacc as yacc
import lexer
import pprint

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

parser=yacc.yacc()

with open("action.txt", "w") as f:
    for key, val in parser.action.items():
        f.writelines(f'{key} : {val}\n')

with open("goto.txt", "w") as f:
    for key, val in parser.goto.items():
        f.writelines(f'{key} : {val}\n')