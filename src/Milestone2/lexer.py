import sys, os
PLY_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "ply"))
sys.path.append(PLY_PATH)
import lex

if (len(sys.argv)==1):
    print("Please provide test file path")

"""
    Most of the tokens are taken from 
    the original go token file at 
    https://go.dev/src/go/token/token.go
"""

## Reserved tokens
reserved = {
    'break' : 'BREAK',
    'type' : 'TYPE',
    'fallthrough' : 'FALLTHROUGH',
    'import' : 'IMPORT',
    'default' : 'DEFAULT',
    'struct' : 'STRUCT',
    'if' : 'IF',
    'return' : 'RETURN',
    'func' : 'FUNC',
    'else' : 'ELSE',
    'range' : 'RANGE',
    'var' : 'VAR',
    'case' : 'CASE',
    'switch' : 'SWITCH',
    'continue': 'CONTINUE',
    'goto' :  'GOTO',
    'map' : 'MAP',
    'const' : 'CONST',
    'for' : 'FOR'
}

## Tokens other than reserved
tokens = [
    'COMMENT',
    'IDENT', 'INT', 'FLOAT', 'IMAG', 'RUNE', 'STRING',
    'ADD', 'SUB', 'MUL', 'QUO', 'REM',
    'AND', 'OR', 'XOR', 'SHL', 'SHR', 'AND_NOT',
    'ADD_ASSIGN', 'SUB_ASSIGN', 'MUL_ASSIGN', 'QUO_ASSIGN', 'REM_ASSIGN',
    'AND_ASSIGN', 'OR_ASSIGN', 'XOR_ASSIGN', 'SHL_ASSIGN', 'SHR_ASSIGN', 'AND_NOT_ASSIGN',
    'LAND', 'LOR', 'ARROW', 'INC', 'DEC',
    'EQL', 'LSS', 'GTR', 'ASSIGN', 'NOT',
    'NEQ', 'LEQ', 'GEQ', 'DEFINE',
    'LPAREN', 'LBRACK', 'LBRACE', 'COMMA', 'PERIOD',
    'RPAREN', 'RBRACK', 'RBRACE', 'SEMICOLON', 'COLON'
] + list(reserved.values())

## Simple regex statements

t_ignore  = ' \t\n'
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_QUO = r'/'
t_REM = r'%'

t_AND = r'&'
t_OR = r'\|'
t_XOR = r'\^'
t_SHL = r'<<'
t_SHR  = r'>>'
t_AND_NOT = r'&\^'

t_ADD_ASSIGN = r'\+='
t_SUB_ASSIGN =  r'-='
t_MUL_ASSIGN = r'\*='
t_QUO_ASSIGN  = r'/='
t_REM_ASSIGN = r'%='

t_AND_ASSIGN = r'&='
t_OR_ASSIGN = r'\|='
t_XOR_ASSIGN = r'\^='
t_SHL_ASSIGN =  r'<<='
t_SHR_ASSIGN = r'>>='
t_AND_NOT_ASSIGN = r'&\^='

t_LAND = r'&&'
t_LOR = r'\|\|'
# t_ARROW = r'<-'
t_INC = r'\+\+'
t_DEC = r'--'

t_EQL = r'=='
t_LSS = r'<'
t_GTR = r'>'
t_ASSIGN = r'='
t_NOT = '!'

t_NEQ = r'!='
t_LEQ = r'<='
t_GEQ = r'>='
t_DEFINE = r':='

t_LPAREN = r'\('
t_LBRACK = r'\['
t_LBRACE = r'\{'
t_COMMA = r','
t_PERIOD = r'\.'

t_RPAREN = r'\)'
t_RBRACK = r'\]'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COLON = r':'


## Adding some other regex rules in the order they should 
## be checked (Hopefully :))

#change rune and decide order
t_RUNE = r'\'.|\n\''

#need to print comments as tokens?
def t_COMMENT(t):
    r'//.* | /\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_STRING(t):
    r'\"(.|\n)*?\"|\`(.|\n)*?\`'
    t.lexer.lineno += t.value.count('\n')
    return t

def t_IDENT(t):
    r'[A-Za-z_][A-Za-z_0-9]*'
    if t.value in list(reserved.keys()):
        t.type = reserved[t.value]
    return t

def t_IMAG(t):
    r'([0-9]+(\.?)[0-9]*(((e|E)(\+|-)?[0-9]+)?)|([0-9]*(\.?)[0-9]+(((e|E)(\+|-)?[0-9]+)?)))i'
    return t 

def t_FLOAT(t):
    r'[0-9]+\.[0-9]*(((e/E)(\+|-)?[0-9]+)?)|[0-9]*\.[0-9]+(((e/E)(\+|-)?[0-9]+)?)|[0-9]+(((e/E)(\+|-)?[0-9]+))'
    return t 

def t_INT(t):
    r'0(x|X)[0-9a-fA-F]+|[0-7]+|[1-9][0-9]*'
    return t

# def t_NEWLINE(t):
#     r'\n+'
#     t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print("Not valid taken: '%s'" % t.value[0])
    t.lexer.skip(1)

## Importing from a test file
data_file = open(sys.argv[1]) 
data = ""

for line in data_file:
    data += line

#test
lexer = lex.lex()
lexer.input(data)

# for key, value in lexer.__dict__.items():
#     print(key,' : ',value)

while 1:
    tok = lex.token()
    if not tok: 
        break
    print(tok)
