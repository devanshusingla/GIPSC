import sys
sys.path.append('../')
import ply.lex as lex

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
    'switch' : 'SWICTH',
    'continue': 'CONTINUE',
    'goto' :  'GOTO',
    'map' : 'MAP',
    'const' : 'CONST',
    'for' : 'FOR'
}

## Tokens other than reserved
tokens = [
    'COMMENT',
    'IDENT', 'INT', 'FLOAT', 'IMAG', 'CHAR', 'STRING',
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

t_ignore  = ' \t'
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

#test
data = "\t+"
lex.lex()
lex.input(data)
while 1:
    tok = lex.token()
    if not tok: 
        break
    print(tok)











