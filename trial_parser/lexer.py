import sys, os
PLY_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "ply"))
sys.path.append(PLY_PATH)
from ply.lex import TOKEN

"""
    Most of the tokens are taken from 
    the original go token file at 
    https://go.dev/src/go/token/token.go
"""



## Tokens other than reserved
tokens = [
    'IDENT',
    'ADD', 'MUL',
    'LPAREN', 
    'RPAREN',
] 
## Simple regex statements

t_ignore  = ' \t\n'
t_ADD = r'\+'
t_MUL = r'\*'
t_IDENT = r'[0-9]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_error(t):
    print("Not valid token: '%s'" % t.value[0])
    t.lexer.skip(1)

#test
if __name__ == '__main__':
    if (len(sys.argv)==1):
        print("Please provide test file path")

    import ply.lex as lex

    ## Importing from a test file
    data_file = open(sys.argv[1]) 
    data = ""

    for line in data_file:
        data += line
    lexer = lex.lex()
    lexer.input(data)

    print(f"Token\t\tLine#\tColumn#\tLexeme")
    while 1:
        tok = lex.token()
        if not tok: 
            break
        print(f"{tok.type:<10}\t{tok.lineno:^7}\t{tok.lexcol:^7}\t{tok.value!r}")