from multiprocessing import Condition
from typing import List
from copy import deepcopy
import ply.yacc as yacc
import ply.lex as lex
import lexer
from lexer import *
import sys
import pprint
from scope import *
from utils import *
import os, csv

tokens=lexer.tokens
tokens.remove('COMMENT')
precedence = (
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

##################################################################################
####################                                        ######################
#####                         STARTING GRAMMAR                            ########
####################                                        ######################
##################################################################################

info_tables = {}
stm = SymTableMaker()
target_folder = ''
curr_func_id = 'global'

_symbol = '_'
stm.add(_symbol, {'dataType': {'name': '_', 'baseType': '_', 'level': 0, 'size': 4}})

def p_SourceFile(p):
    """
    SourceFile : PackageClause SEMICOLON ImportDeclMult TopLevelDeclMult
    """
    # Check if any label has expecting key set
    for label in stm.labels:
        if stm.labels[label]['expecting'] == True:
            assert(len(stm.labels[label]['prevGotos']) > 0)
            goto = stm.labels[label]['prevGotos'][0]
            raise LogicalError(f"{goto[1]}: Goto declared without declaring any label {label}.")
    p[4].addChild(p[3][1]) 
    # p[4].code = ["// Source Code Top Level Declaration"] + p[4].code
    p[0] = FileNode(p[1], p[3][0], p[4])

###################################################################################
### Package related grammar
###################################################################################

def p_PackageClause(p):
    """
    PackageClause : PACKAGE IDENT
    """
    p[0] = LitNode(dataType = 'string', label = f'"{p[2]}"')
    p[0].code.append(f"package {p[2]}")

###################################################################################
### Import related grammar
###################################################################################

def p_ImportDeclMult(p):
    """
    ImportDeclMult : ImportDeclMult ImportDecl SEMICOLON
                   |  
    """
    if len(p) > 1:
        p[1][0].addChild(*p[2][0])
        p[1][1].extend(p[2][1])
        p[0] = p[1]
    else:
        p[0] = (ImportNode(), NodeList([]))

def p_ImportDecl(p):
    """
    ImportDecl : IMPORT ImportSpec
               | IMPORT LPAREN ImportSpecMult RPAREN
    """
    if len(p) == 3:
        p[0] = p[2]
    elif len(p) == 5:
        p[0] = p[3]

def p_ImportMult(p):
    """
    ImportSpecMult : ImportSpec SEMICOLON ImportSpecMult  
               |
    """
    if len(p) == 1:
        p[0] = (NodeList([]), NodeList([]))
    elif len(p) == 4:
        p[3][0].extend(p[1][0])
        p[3][1].extend(p[1][1])
        p[0] = p[3]

def p_ImportSpec(p):
    """
    ImportSpec : PERIOD ImportPath
              | IDENT ImportPath
              | ImportPath 
    """

    global stm, target_folder
    if p[1] != '.':
        alias = IdentNode(0, p[1][1:-1])
    else:
        alias = IdentNode(0, p[2][1:-1])
    if len(p) == 2:
        pathname = getPath(p[1][1:-1]+'.go', target_folder)
        path = LitNode(dataType = "string", label = p[1])
    else:
        pathname = getPath(p[2][1:-1]+'.go', target_folder)
        path = LitNode(dataType = "string", label = p[2])

    if alias.label in stm.pkgs:
        raise NameError(f"{p.lexer.lineno}: Cyclic import not supported")
    
    tmp_target_folder = target_folder
    if p[1] != '.':
        temp_stm = stm
        stm = SymTableMaker()
        stm.add(_symbol, {'dataType': {'name': '_', 'baseType': '_', 'level': 0, 'size': 0}})
        astNode, _ = buildAndCompile(pathname)
        temp_stm.pkgs[alias.label] = stm
        stm = temp_stm
        ipnode = ImportPathNode(alias, path, astNode)
        ipnode.code.append(f"import {p[len(p)-1]}")
        p[0] = (NodeList([ipnode]), NodeList([]))
    else:
        astNode, _ = buildAndCompile(pathname)
        stm.pkgs[alias.label] = None
        p[0] = (NodeList(astNode.children[1].children), NodeList(astNode.children[2].children))
    
    target_folder = tmp_target_folder

def p_ImportPath(p):
    """
    ImportPath : STRING
    """
    p[0] = p[1]

###################################################################################
### Top-Level related grammar
###################################################################################

def p_TopLevelDeclMult(p):
    """
    TopLevelDeclMult : TopLevelDecl SEMICOLON TopLevelDeclMult 
                     |
    """
    if len(p)>1:
        p[0] = DeclNode()
        p[0].addChild(p[1])
        # if isinstance(p[1], list):
        #     p[0].addChild(p[1])
        # else:
            

        p[0].addChild(*p[3].children)

    if len(p)==1:
        p[0] = DeclNode()

def p_TopLevelDecl(p):
    """
    TopLevelDecl : Decl 
                 | FuncDecl
    """
    if p[1] is not None:
        p[0] = p[1]
    else:
        p[0] = NodeList([])

def p_Decl(p):
    """
    Decl : ConstDecl 
         | VarDecl
         | TypeDecl
    """
    if p[1] is not None:
        p[0] = p[1]

###################################################################################
### Constant Declarations
###################################################################################

def p_ConstDecl(p):
    """
    ConstDecl : CONST ConstSpec
              | CONST LPAREN ConstSpecMult RPAREN
    """
    if len(p)==3:
        p[0] = p[2]            
    else:
        p[0] = p[3]
        

def p_ConstSpecMult(p):
    """
    ConstSpecMult : ConstSpec SEMICOLON ConstSpecMult 
                  | ConstSpec
    """
    if len(p) == 4:
        p[3].extend(p[1])
        p[0] = p[3]
    else:
        p[0] = NodeList([])

def p_ConstSpec(p):
    """
    ConstSpec : IdentifierList Type ASSIGN ExpressionList 
              | IdentifierList IDENT ASSIGN ExpressionList
              | IdentifierList ASSIGN ExpressionList
    """
    p[0] = NodeList([])
    length = len(p)-1

    count_0 = 0
    count_1 = 0

    expression_datatypes = []

    for i in range(len(p[length])):
        if isinstance(p[length][i], FuncCallNode):
            func_name = p[length][i].children[0].label
            dt_return = stm.functions[func_name]["return"]
            expression_datatypes.extend(dt_return)
            if len(dt_return) == 0:
                raise TypeError(f"{p.lexer.lineno}: Function does not return anything!")
            elif len(dt_return) == 1:
                count_0+=1
            else:
                count_1+=1
        else:
            expression_datatypes.append(p[length][i].dataType)
    
    if count_1 > 0:
        raise TypeError(f"{p.lexer.lineno}: Functions with multi-valued return type can't be allowed in single-value context!.")

    if len(p[1]) != len(expression_datatypes):
        raise NameError(f"{p.lexer.lineno}: Assignment is not balanced")
    
    dt = {}

    if len(p) > 4:
        if isinstance(p[2], str):
            p[2] = stm.findType(p[2])
    
        dt = p[2].dataType

        for i, expression in enumerate(expression_datatypes):
            if not isTypeCastable(stm, dt, expression):
                raise TypeError(f"{p.lexer.lineno}: Mismatch of type for identifier: " + p[1][i].label)

    if count_1 > 0:
        expr = ExprNode(dataType = dt, label = "ASSIGN", operator = "=")
        i = 0
        for child in p[1]:
            expr.addChild(child)
            i+=1
        expr.addChild(p[length][0])
        p[0].append(expr)
    else:
        i = 0
        for (ident, val) in zip(p[1], p[len(p)-1]):
            expr = ExprNode(dataType=p[2], label="ASSIGN", operator="=")
            expr.addChild(ident, val)

            i+= 1
            p[0].append(expr)

    not_base_type = False

    if not isinstance(p[2], str):
        not_base_type = True

    extended_list = []

    for expr in p[length]:
        if isinstance(expr, list):
            extended_list.extend(expr)
        else:
            extended_list.append(expr)

    for i, ident in enumerate(p[1]):

        # Check redeclaration for identifier list
        latest_scope = stm.getScope(ident.label)
        if latest_scope == stm.id or ident.label in stm.functions:
            raise NameError(f'{p.lexer.lineno}: Redeclaration of identifier: ' + ident)
        
        if len(p) > 4:
            if not not_base_type:
                dt = {'baseType' : p[2], 'name': p[2], 'level': 0}
                dt['size'] = basicTypeSizes[dt['name']]
            else:
                dt = p[2].dataType

            if not_base_type:
                present = checkTypePresence(stm, dt) 
            else:
                present = stm.findType(stm, dt)

            if present == -1:
                raise TypeError(f'{p.lexer.lineno}: Type not declared/found: ' + dt)
            else:
                val = extended_list[i].label
                # Add to symbol table
                size = 0
                if dt['name'].startswith('int'):
                    val = int(extended_list[i].val)
                elif dt['name'].startswith('float'):
                    val = float(extended_list[i].val)
                ## Write conditions for rune and other types
                stm.add(ident.label, {'dataType': dt, 'isConst' : True, 'val': val})
                p[1][i].dataType = dt
        else:
            val = extended_list[i].label
            dt = extended_list[i].dataType
            # Add to symbol table
            if dt['name'].startswith('int'):
                val = int(extended_list[i].label)
            elif dt['name'].startswith('float'):    
                val = float(extended_list[i].label)
            ## Write conditions for rune and other types
            stm.add(ident.label, {'dataType': dt, 'isConst' : True, 'val': val})
            p[1][i].dataType = dt
 
    # for expr in p[length]:
    #     p[0].code.extend(expr.code)

    if count_1 == 0:
        for i in range(len(p[1])):
            p[0].code.append(f"{stm.id}_{p[1][i].label} = {p[length][i].place}")
            stm.symTable[stm.id].updateAttr(p[1][i].label, {'tmp': f"{stm.id}_{p[1][i].label}"})

    else:
        for i in range(len(p[1])):
            p[0].code.append(f"{stm.id}_{p[1][i].label} = {p[length][0].place[i]}")
            stm.symTable[stm.id].updateAttr(p[1][i].label, {'tmp': f"{stm.id}_{p[1][i].label}"})


###################################################################################
### Variable Declarations
###################################################################################

def p_VarDecl(p):
    """
    VarDecl : VAR VarSpec
            | VAR LPAREN VarMult RPAREN
    """
    if len(p)==3:
        p[0] = p[2]
    
    else:
        p[0] = p[3]

def p_VarMult(p):
    """
    VarMult : VarSpec SEMICOLON VarMult 
            | VarSpec
    """
    if len(p) > 1:
        p[3].extend(p[1])
        p[0] = p[3]
    else:
        p[0] = NodeList([Node()]) 

def p_VarSpec(p):
    """
    VarSpec : IdentifierList Type ASSIGN ExpressionList
            | IdentifierList IDENT ASSIGN ExpressionList
            | IdentifierList ASSIGN ExpressionList
            | IdentifierList Type
            | IdentifierList IDENT
    """
    p[0] = NodeList([])
    length = len(p)-1
    if len(p) >= 4:
        count_0 = 0
        count_1 = 0

        expression_datatypes = []

        for i in range(len(p[length])):
            if isinstance(p[length][i], FuncCallNode):
                func_name = p[length][i].children[0].label
                dt_return = stm.functions[func_name]["return"]
                expression_datatypes.extend(dt_return)
                if len(dt_return) == 0:
                    raise TypeError(f"{p.lexer.lineno}: Function does not return anything!")
                elif len(dt_return) == 1:
                    count_0+=1
                else:
                    count_1+=1
            else:
                expression_datatypes.append(p[length][i].dataType)
        if count_1 > 0:
            if len(p[length]) > 1:
                raise TypeError(f"{p.lexer.lineno}: Function with more than one return values should be assigned alone!")
        if len(p[1]) != len(expression_datatypes):
            raise NameError(f"{p.lexer.lineno}: Assignment is not balanced")
        
        dt = {}

        if len(p) > 4:
            if isinstance(p[2], str):
                p[2] = stm.findType(p[2])

            if isinstance(p[2], str):
                dt = {'baseType' : p[2], 'name': p[2], 'level': 0}
                dt['size'] = basicTypeSizes[p[2]]
            else:
                dt = p[2].dataType
            for i, expression in enumerate(expression_datatypes):
                if not isTypeCastable(stm, dt, expression):
                    raise TypeError(f"{p.lexer.lineno}: Mismatch of type for identifier: " + p[1][i].label)

        if count_1 > 0:
            expr = ExprNode(dataType = dt, label = "ASSIGN", operator = "=")
            for child in p[1]:
                expr.addChild(child)
            expr.addChild(p[length][0])
            p[0].append(expr)
        else:
            for (ident, val) in zip(p[1], p[len(p)-1]):
                expr = ExprNode(dataType=dt, label="ASSIGN", operator="=")
                expr.addChild(ident, val)
                p[0].append(expr)

        not_base_type = False

        if not isinstance(p[2], str):
            not_base_type = True

        extended_list = []

        for expr in p[length]:
            if isinstance(expr, list):
                extended_list.extend(expr)
            else:
                extended_list.append(expr)

        for i, ident in enumerate(p[1]):

            # Check redeclaration for identifier list
            latest_scope = stm.getScope(ident.label)
            if latest_scope == stm.id or ident.label in stm.functions:
                raise NameError(f'{p.lexer.lineno}: Redeclaration of identifier: ' + ident.label)
            
            if len(p) > 4:
                if not not_base_type:
                    dt = {'baseType' : p[2], 'name': p[2], 'level': 0}
                    dt['size'] = basicTypeSizes[p[2]]
                else:
                    dt = p[2].dataType

                if not_base_type:
                    present = checkTypePresence(stm, dt) 
                else:
                    present = stm.findType(stm, dt)

                if present == -1:
                    raise TypeError(f'{p.lexer.lineno}: Type not declared/found: ' + dt['name'])
                else:
                    # Add to symbol table

                    stm.add(ident.label, {'dataType': dt, 'isConst' : False})
                    p[1][i].dataType = dt    
            else:
                dt = extended_list[i].dataType
                # Add to symbol table
                stm.add(ident.label, {'dataType': dt, 'isConst' : False})
                p[1][i].dataType = dt

        # for expr in p[length]:
        #     p[0].code.extend(expr.code)
        if count_1 == 0:
            for i in range(len(p[1])):
                p[0].code.append(f"{stm.id}_{p[1][i].label} = {p[length][i].place}")
                stm.symTable[stm.id].updateAttr(p[1][i].label, {'tmp': f"{stm.id}_{p[1][i].label}"})

        else:
            for i in range(len(p[1])):
                p[0].code.append(f"{stm.id}_{p[1][i].label} = {p[length][0].place[i]}")
                stm.symTable[stm.id].updateAttr(p[1][i].label, {'tmp': f"{stm.id}_{p[1][i].label}"})
    else:
        not_base_type = False

        if not isinstance(p[2], str):
            not_base_type = True

        for i, ident in enumerate(p[1]):

            # Check redeclaration for identifier list
            latest_scope = stm.getScope(ident.label)
            if latest_scope == stm.id or ident.label in stm.functions:
                raise NameError(f'{p.lexer.lineno}: Redeclaration of identifier: ' + ident)

            if not not_base_type:
                dt = {'baseType' : p[2], 'name': p[2], 'level': 0}
                dt['size'] = basicTypeSizes[p[2]]
            else:
                dt = p[2].dataType

            if not_base_type:
                present = checkTypePresence(stm, dt) 
            else:
                present = stm.findType(dt)

            if present == -1:
                raise TypeError(f'{p.lexer.lineno}: Type not declared/found: ' + dt)
            else:
                # Add to symbol table
                stm.add(ident.label, {'dataType': dt, 'isConst' : False})
                p[1][i].dataType = dt

        for i in range(len(p[1])):
            stm.symTable[stm.id].updateAttr(p[1][i].label, {'tmp': f"{stm.id}_{p[1][i].label}"})

###################################################################################
### Type Declarations
###################################################################################

def p_TypeDecl(p):
    """
    TypeDecl : TYPE TypeSpec
             | TYPE LPAREN TypeSpecMult RPAREN
    """

def p_TypeSpecMult(p):
    """
    TypeSpecMult : TypeSpec SEMICOLON TypeSpecMult 
                 | 
    """

    
def p_TypeSpec(p):
    """
    TypeSpec : AliasDecl
             | Typedef
    """

def p_AliasDecl(p):
    """
    AliasDecl : IDENT ASSIGN Type
                | IDENT ASSIGN IDENT
    """ 
    
    dt = {}
    if isinstance(p[3], str):
        dt['name'] = p[3]
        dt['baseType'] = p[3]
        dt['level'] = 0
    else:
        dt = p[3].dataType

    if checkTypePresence(stm, dt) == -1:
        raise TypeError(f"{p.lexer.lineno}: baseType " + dt + " not declared yet")

    if p[1] in stm.symTable[stm.id].typeDefs:
        raise TypeError(f"{p.lexer.lineno}: Redeclaration of Alias " + p[1])
        
    elif isinstance(p[3], str) and p[3] in stm.symTable[stm.id].avlTypes:
        stm.symTable[stm.id].typeDefs[p[1]] = p[3]
    
    elif isinstance(p[3], str):
        stm.symTable[stm.id].typeDefs[p[1]] = stm.symTable[stm.id].typeDefs[p[3]]

    else:
        stm.symTable[stm.id].typeDefs[p[1]] = dt

def p_TypeDef(p):
    """
    Typedef : IDENT Type
              | IDENT IDENT

    """
    if isinstance(p[2], str):
        p[2] = stm.findType(p[2])
    dt = p[2].dataType

    if checkTypePresence(stm, dt) == -1:
        raise TypeError(f"{p.lexer.lineno}: baseType " + dt + " not declared yet")

    if p[1] in stm.symTable[stm.id].typeDefs:
        raise TypeError(f"{p.lexer.lineno}: Redeclaration of type " + p[1])
        
    elif isinstance(p[2], str) and p[2] in stm.symTable[stm.id].avlTypes:
        stm.symTable[stm.id].typeDefs[p[1]] = {'baseType': p[2], 'name': p[2], 'level' : 0, 'size': basicTypeSizes[p[2]]}
    
    elif isinstance(p[2], str):
        stm.symTable[stm.id].typeDefs[p[1]] = stm.symTable[stm.id].typeDefs[p[2]]

    else:
        p[2].dataType['baseType'] = p[1]
        stm.symTable[stm.id].typeDefs[p[1]] = p[2]

###################################################################################
### Identifier List
###################################################################################

def p_IdentifierList(p):
    """
    IdentifierList : IDENT
                   | IDENT COMMA IdentifierList
    """
    
    p[0] = NodeList([IdentNode(label = p[1], scope = stm.id)])

    if len(p) > 2:
        p[0].extend(p[3])


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
    if len(p) == 2:
        p[0] = NodeList([])
        p[0].append(p[1])
    else:
        p[1].append(p[3])
        p[0] = p[1]
    
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
    if len(p) == 2:
        p[0] = p[1]
    else:
        dt1 = p[1].dataType
        dt2 = p[3].dataType

        firstChar = None
        if hasattr(p[3], 'label') and  isinstance(p[3].label, List):
            firstChar = p[3].label[0]

        if not checkBinOp(stm, dt1, dt2, p[2], firstChar):
            raise TypeError(f"{p.lexer.lineno}: Incompatible operand types")

        dt = getFinalType(stm, dt1, dt2, p[2])

        isConst = False
        val = None
        if isinstance(p[1], ExprNode) and isinstance(p[3], ExprNode) and p[1].isConst and p[3].isConst:
            isConst = True
            val = Operate(p[2], p[1].val, p[3].val, p.lexer.lineno, p[3].dataType['name'])

        p[0] = ExprNode(operator = p[2], dataType = dt, isConst = isConst, val=val, label = val)
        p[0].addChild(p[1], p[3])
        if((p[1].place)[0] == '*' and (p[3].place)[0] == '*') :
            point = new_temp()
            p[0].code.append(f"{point} = {p[1].place}")
            p[1].place = point
        temp_var = new_temp()

        p[0].code.append(f"{temp_var} = {p[1].place} {p[2]}({dt['name']}) {p[3].place}")
        p[0].place = temp_var


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
    if len(p) == 2:
        p[0] = p[1]
    else:
        flag = False
        if not isinstance(p[2], str) and hasattr(p[2], 'isAddressable'):
            flag = p[2].isAddressable 
        if not checkUnOp(stm, p[2].dataType, p[1], flag):
            raise TypeError(f"{p.lexer.lineno}: Incompatible operand for Unary Expression")
        val = None
        isConst = p[2].isConst
        if isConst:
            if p[1] == '*' or p[1] == '&':
                # Referencing or dereferencing a constant in compile time is not possible
                raise LogicalError(f"{p.lexer.lineno}: Constants can't be referenced or dereferenced.")
                isConst = False
                val = None
            else:
                val = Operate(p[1], None, p[2].val, p.lexer.lineno, p[2].dataType['name'])
        if p[1] == '&' and p[2].isRef == True:
            raise LogicalError(f"{p.lexer.lineno}: Can't reference a variable more than once.")
        isAddressable = flag and (p[1] == '*')
        p[0] = ExprNode(dataType = getUnaryType(stm, p[2].dataType, p[1]), operator=p[1], isAddressable = isAddressable, isConst=isConst, val=val)
        p[0].addChild(p[2])
        temp_var = new_temp()
        if p[1] == '*':
            p[0].isDeRef = True
            p[0].lvalue = p[2].place
        elif p[1] == '&':
            p[0].isRef = True
        if p[1] == '-':
            p[0].code.append(f"{temp_var} = {p[1]}({p[2].dataType['name']}) {p[2].place}")
        else:
            p[0].code.append(f"{temp_var} = {p[1]} {p[2].place}")
        p[0].place = temp_var

###################################################################################
### Primary Expression
###################################################################################


def p_PrimaryExpr(p):
    """
    PrimaryExpr :  Lit
                | IDENT
                | LPAREN Expr RPAREN
                | PrimaryExpr Selector
                | PrimaryExpr Index
                | PrimaryExpr Slice
                | PrimaryExpr Arguments
    """
    
    ## PrimaryExpr -> Lit
    if len(p) == 2 and (isinstance(p[1], LitNode) or isinstance(p[1], CompositeLitNode)):
        if isinstance(p[1], LitNode):
            p[0] = ExprNode(p[1].dataType, p[1].label, None, p[1].isConst, False, p[1].val)
            p[0].place = p[1].place
            if p[1].children:
                for child in p[1].children:
                    p[0].addChild(child)
            else:
                p[0].code = p[1].code
        else:
            # Ig Composite Literal is only used for assignment
            p[0] = p[1]

    ## PrimaryExpr -> Ident
    elif (len(p) == 2):
        identType = getBaseType(stm, p[1])
        place = None
            
        if p[1] in stm.pkgs and stm.pkgs[p[1]] != None:
            p[0] = IdentNode(0, p[1], dataType={'name': 'package'})
            # The name of package doesn't have any place value
            p[0].place = None
            return

        ## TODO : What is the need for this?        
        if p[1] in stm.symTable[0].typeDefs:
            # Type Declaration Found
            # Assuming Constructor Initialisation
            dt = stm.symTable[0].typeDefs[p[1]]
            p[0] = ExprNode(dataType=dt, label=p[1], isAddressable=False, isConst=False, val=None)
            # Types need not have place values; they only has role in semantics
            # may consider writing type conversion functions if supporting type conversion. 
            # p[0].place = stm.get(p[1]).get('tmp', None)
            p[0].place = None
            return

        # If typecast function
        if p[1] in utils.basicTypes and isBasicNumeric(stm, {'baseType': p[1], 'level': 0}):
            p[0] = ExprNode(dataType = {'baseType': 'typeCastFunc'}, label = p[1], isAddressable = True, isConst = False)
            pass

        # Check declaration
        latest_scope = ((stm.getScope(p[1]) != -1) or (p[1] in stm.functions)) 

        if latest_scope == 0:
            ## To be checked for global declarations (TODO)
            print("Expecting global declaration for ",p[1])

        stm_entry = stm.get(p[1])
        dt = stm_entry['dataType']
        p[0] = ExprNode(dataType=dt, label = p[1], isAddressable=True, isConst=stm_entry.get('isConst', False), val=stm_entry.get('val', None))
        if stm_entry.get('isArg', None):
            p[0].place = f'arg_[{stm_entry["paramOf"]}_{stm_entry["offset"]}]'
        else:
            p[0].place = stm_entry.get('tmp', None)

    ## PrimaryExpr -> LPAREN Expr RPAREN
    elif len(p) == 4:
        p[0] = p[2]

    else:
        code = []
        place = None
        dt = None
        ## PrimaryExpr -> PrimaryExpr Selector
        if isinstance(p[2], DotNode):
            if isinstance(p[1], IdentNode) and 'name' in p[1].dataType and p[1].dataType['name'] == 'package':
                pkg_stm = stm.pkgs[p[1].label]
                stm_entry = pkg_stm.get(p[2].children[0])
                if stm_entry is None:
                    raise NameError(f"{p.lexer.lineno}: No such variable or function in package {p[1].label}")
                p[0] = ExprNode(dataType=stm_entry['dataType'], label=p[2].children[0], isAddressable=True, isConst=stm_entry.get('isConst', False), val=stm_entry.get('val', None), pkg=p[1].label)
                p[0].addChild(p[1],p[2].children[0])
                if 'tmp' in stm_entry:
                    # Imported Variable
                    p[0].place = stm_entry['tmp']
                else:
                    pass                
                return
            if 'name' not in p[1].dataType or p[1].dataType['name']  != 'struct':
                raise TypeError(f"{p.lexer.lineno}: Expecting struct type but found different one")
            
            field = p[2].children[0]


            if field not in p[1].dataType['keyTypes']:
                raise NameError(f"{p.lexer.lineno}: No such field found in " + p[1].label)
            struct_off = p[1].dataType['offset'][field]

            p[2].addChild(p[1])
            dt = p[1].dataType['keyTypes'][field]
            
            temp = new_temp()
            code.append(f"{temp} = {p[1].place} + {struct_off}")
            place = f"* {temp}"

        ## PrimaryExpr -> PrimaryExpr Index
        elif isinstance(p[2], IndexNode):
            if 'name' not in p[1].dataType or (p[1].dataType['name'] != 'array' and p[1].dataType['name']!= 'map' and p[1].dataType['name'] != 'slice') :
                raise TypeError(f"{p.lexer.lineno}: Expecting array or map type but found different one")

            if p[1].dataType['name'] == 'array' or p[1].dataType['name'] == 'slice':
                if isinstance(p[2].dataType, str):
                    if not isBasicInteger(stm, p[2].dataType):
                        raise TypeError(f"{p.lexer.lineno}: Index cannot be of type " + p[2].dataType)
                else:
                    if isinstance(p[2].dataType['baseType'], str) and p[2].dataType['level'] == 0:
                        if not isBasicInteger(stm, p[2].dataType['baseType']):
                            raise TypeError(f"{p.lexer.lineno}: Index cannot be of type " + p[2].dataType)
                    else:
                        raise TypeError(f"{p.lexer.lineno}: Index type incorrect")

                dt = deepcopy(p[1].dataType['baseType'])
                if dt['level']==0:
                    dt = stm.findType(dt['baseType']).dataType

                temp1 = new_temp()
                elem_size = dt['size']
                code.extend(p[1].code)
                # code.extend(p[2].code)
                code.append(f"{temp1} = {p[2].place} * {elem_size}")
                temp2 = new_temp()
                code.append(f"{temp2} = {p[1].place}.addr + {temp1}")
                # temp3 = new_temp()        
                # code.append(f"{temp3} = *{temp2}")
                place = f"* {temp2}"       

            ## TODO : Discuss Layout for MapType
            if p[1].dataType['name'] == 'map':
                if not isTypeCastable(stm, p[2].dataType, p[1].dataType['KeyType']):
                    raise TypeError(f"{p.lexer.lineno}: Incorrect type for map " + p.lexer.lineno)

                # found = False
                # idx = 0
                # for key in stm.get(p[1].label)['val'].keys:
                #     if p[2] == key:
                #         found = True 
                #         break 
                #     idx += 1

                # keySize = p[1].dataType['KeyType']['size']
                # valSize = p[1].dataType['ValueType']['size']

                # temp1 = new_temp()
                # code.append(f"{temp1} = {keySize} * {idx}")
                # temp2 = new_temp()
                # code.append(f"{temp2} = {valSize} * {idx}")
                # temp3 = new_temp()
                # code.append(f"{temp3} = {temp1} + {temp2}")
                # temp4 = new_temp()
                # code.append(f"{temp4} = {p[1]} + {temp3}")
                # temp5 = new_temp()
                # code.append(f"{temp5} = *({temp4} + {keySize})")
                dt = p[1].dataType['ValueType']

            p[2].children[0] = p[1]                                                      

        ## PrimaryExpr -> PrimaryExpr Slice
        elif isinstance(p[2], SliceNode):
            if 'name' not in p[1].dataType or (p[1].dataType['name'] != 'slice' and p[1].dataType['name'] != 'array'):
                raise TypeError(f"{p.lexer.lineno}: Expecting a slice type but found different one")

            if  p[2].lIndexNode != None: 
                if not isBasicInteger(stm, p[2].lIndexNode.dataType['baseType']):
                    raise TypeError(f"{p.lexer.lineno}: Index cannot be of type " + p[2].dataType)
            
            if  p[2].rIndexNode != None: 
                if not isBasicInteger(stm, p[2].rIndexNode.dataType['baseType']):
                    raise TypeError(f"{p.lexer.lineno}: Index cannot be of type " + p[2].dataType)

            else:
                if isinstance(p[2].lIndexNode.dataType, str):
                    if not isBasicInteger(stm, p[2].lIndexNode.dataType):
                        raise TypeError(f"{p.lexer.lineno}: Index cannot be of type " + p[2].lIndexNode.dataType)
                else:
                    if isinstance(p[2].lIndexNode.dataType['baseType'], str) and p[2].lIndexNode.dataType['level'] == 0:
                        if not isBasicInteger(stm, p[2].lIndexNode.dataType):
                            raise TypeError(f"{p.lexer.lineno}: Index cannot be of type " + p[2].lIndexNode.dataType)
                    else:
                        raise TypeError(f"{p.lexer.lineno}: Index type incorrect")
                
                if isinstance(p[2].rIndexNode.dataType, str):
                    if not isBasicInteger(stm, p[2].rIndexNode.dataType):
                        raise TypeError(f"{p.lexer.lineno}: Index cannot be of type " + p[2].rIndexNode.dataType)
                else:
                    if isinstance(p[2].rIndexNode.dataType['baseType'], str) and p[2].rIndexNode.dataType['level'] == 0:
                        if not isBasicInteger(stm, p[2].rIndexNode.dataType):
                            raise TypeError(f"{p.lexer.lineno}: Index cannot be of type " + p[2].rIndexNode.dataType)
                    else:
                        raise TypeError(f"{p.lexer.lineno}: Index type incorrect")
 
            dt = deepcopy(p[1].dataType['baseType'])

            if dt['level']==0:
                dt = {'name': dt['baseType'], 'baseType': dt['baseType'], 'level': 0}
                dt['size'] = basicTypeSizes[dt['name']]

            temp1 = new_temp()
            elem_size = dt['size']
            code.append(f"{temp1} = {p[2].lIndexNode.place} * {elem_size}")
            temp2 = new_temp()
            code.append(f"{temp2} = {p[2].rIndexNode.place} - {p[2].lIndexNode.place}")
            temp3 = new_temp()
            code.append(f"{temp3} = {p[1].place}.capacity - {p[2].lIndexNode.place}")
            temp4 = var_new_temp()
            code.append(f"{temp4}.addr = {p[1].place}.addr + {temp1}")
            code.append(f"{temp4}.length = {temp2}")
            code.append(f"{temp4}.capacity = {temp3}")

            dt = p[1].dataType.copy()
            p[2].children[0] = p[1]

        ## PrimaryExpr -> PrimaryExpr Arguments
        elif isinstance(p[2], List):
            if hasattr(p[1], "pkg") and p[1].pkg is not None:
                new_stm = stm.pkgs[p[1].pkg]
            else:
                new_stm = stm

            if p[1].label in basicTypes and (isBasicNumeric(stm, {'baseType': p[1].label, 'level': 0}) or p[1].label == 'string'):
                if len(p[2]) > 1:
                    raise LogicalError(f"{p.lexer.lineno:} Only one expression can be typecasted at a time!")
                
                dt = p[2][0].dataType
                if isinstance(p[2][0].dataType, list) and len(p[2][0].dataType) > 1:
                    raise LogicalError(f"{p.lexer.lineno:} Only one expression can be typecasted at a time!")
                elif isinstance(p[2][0].dataType, list):
                    dt = p[2][0].dataType[0]
                
                if not isBasicNumeric(stm, dt):
                    raise TypeError(f"{p.lexer.lineno:} Only Basic Numeric Types can be typecasted with each other!")
                else:
                    if p[2][0].isConst:
                        p[0] = p[2][0]
                        p[0].isAddressable = False
                        p[0].isConst = p[2][0].isConst
                        place = new_temp()
                        try:
                            p[0].val = typecast(p[2][0].val, p[1].label)
                            code.append(f"{place} = {p[0].val}")
                        except Exception as e:
                            raise TypeError(f"{p.lexer.lineno}: Couldn't typecase constant in compile time.")
                    else:
                        p[0] = FuncCallNode(p[1], p[2])
                        p[0].isAddressable = False
                        p[0].isConst = p[2][0].isConst
                        place = f"retval_typecast_{dt['baseType']}_to_{p[1].label}_0"
                        code.append(f"params {p[2][0].place}")
                        code.append(f"call typecast_{dt['baseType']}_to_{p[1].label}")
                    p[0].dataType = {'baseType': p[1].label, 'name': p[1].label, 'level': 0, 'size': utils.basicTypeSizes[p[1].label]}
                    p[0].code.extend(code)
                    p[0].place = place            
                return

            dt = new_stm.findType(p[1].label)

            if dt != -1:
                if not isinstance(dt, StructType):
                    raise TypeError(f'Not of type struct')
                
                p[2] = CompositeLitNode(new_stm, dt.dataType, p[2])
                p[0] = p[2]
                p[0].dataType = dt.dataType
                p[0].isAddressable = False
                return
            else:
        
                if p[1].label not in new_stm.functions:
                    raise NameError(f"{p.lexer.lineno}: No such function declared ")

                info = new_stm.functions[p[1].label]
                paramList = info['params']
                dt = None
                if info['return'] != None:
                    dt = info['return']

                temp = []
                for expr in p[2]:
                    if isinstance(expr, list):
                        temp.extend(expr)
                    else:
                        temp.append(expr)

                p[2] = temp
                if len(paramList) != len(p[2]):
                    raise NameError(f"{p.lexer.lineno}: Different number of arguments in function call: " + p[1].label + "\n Expected " + str(len(paramList)) + " number of arguments but got " + str(len(p[2])))

                for i, argument in enumerate(p[2]):
                    dt1 = argument.dataType
                    dt2 = paramList[i]

                    if not isTypeCastable(new_stm, dt1, dt2):
                        raise TypeError(f"{p.lexer.lineno}: Type mismatch on argument number: {i} - {argument}")

                    code.append(f"params {argument.place}")
                code.append(f"call {p[1].label}")
                p[2] = FuncCallNode(p[1], p[2])
                if len(info['return']) > 1:
                    place = [f"retval_{p[1].label}_{i}" for i in range(len(info['return']))]
                else:
                    place = f"retval_{p[1].label}_0"
        p[0] = p[2]                       

        p[0].isAddressable = True
        p[0].dataType = dt
        p[0].code.extend(code)
        p[0].place = place
        if isinstance(p[2], list):
            p[0].isAddressable = False


###################################################################################
## Selector

def p_Selector(p):
    """
    Selector : PERIOD IDENT
    """
    p[0] = DotNode(p[2])

###################################################################################
## Index

def p_Index(p):
    """
    Index : LBRACK Expr RBRACK
    """
    p[0] = IndexNode(None, p[2], dataType = p[2].dataType)
    p[0].place = p[2].place

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
    lIndexNode = None
    rIndexNode = None
    maxIndexNode = None
    if len(p) == 5:
        if(p[2] == ":"):
            rIndexNode = p[3]
        else:
            lIndexNode = p[2]
    elif len(p) == 6:
        lIndexNode = p[2]
        rIndexNode = p[4]
    elif len(p) == 7:
        rIndexNode = p[3]
        maxIndexNode = p[5]
    elif len(p) == 8:
        lIndexNode = p[2]
        rIndexNode = p[4]
        maxIndexNode = p[6]
    
    p[0] = SliceNode(None, lIndexNode, rIndexNode, maxIndexNode)

###################################################################################
## Arguments

def p_Arguments(p):
    """
    Arguments : LPAREN RPAREN
              | LPAREN ExpressionList RPAREN
              | LPAREN ExpressionList COMMA RPAREN
    """
    p[0] = NodeList([])
    if len(p) == 4:
        if isinstance(p[2], list):
            p[0] = p[2]
        else:
            p[0] = NodeList([p[2]])
    elif len(p) == 5:
        if isinstance(p[2], list):
            p[0] = p[2]
        else:
            p[0] = NodeList([p[2]])

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
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ParenType(p[2], dataType = p[2].dataType)

def p_TypeT(p):
    """
    TypeT : ArrayType
          | StructType
          | SliceType
          | MapType
          | LPAREN TypeT RPAREN
          | LPAREN IDENT RPAREN
    """
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        dt = None
        if isinstance(p[2], str):
            p[0] = stm.findType(p[2])
        else:
            p[0] = p[2]


###################################################################################
### Pointer Type
###################################################################################

def p_PointerType(p):
    """
    PointerType : MUL Type %prec UMUL
               | MUL IDENT %prec UMUL
    """
    if isinstance(p[2], str):
        p[2] = stm.findType(p[2])
        if p[2] == -1:
            raise TypeError(f"{p.lexer.lineno}: No such type")

    p[0] = PointerType(p[2].dataType)

###################################################################################
### Slice Type
###################################################################################

def p_SliceType(p):
    """
    SliceType : LBRACK RBRACK ElementType
    """
    p[0] = BrackType(p[3].dataType)
        
    # p[0].dataType['baseType'] = p[3].dataType['baseType']
    # p[0].dataType['level'] = p[3].dataType['level'] + 1
    # p[0].dataType['name'] = 'slice'

###################################################################################
### Array Type
###################################################################################

def p_ArrayType(p):
    """
    ArrayType : LBRACK ArrayLength RBRACK ElementType
    """
    if stm.id == 0:
        if not p[2].isConst:
            raise LogicalError(f"{p.lexer.lineno}: Array length must be a constant in global scope.")
    p[0] = BrackType(p[4].dataType, p[2])

    # if 'baseType' in p[4].dataType:
    #     p[0].dataType['baseType'] = p[4].dataType['baseType']
    # else:
    #     p[0].dataType['baseType'] = p[4].dataType['name']
    # p[0].dataType['level'] = p[4].dataType['level'] + 1
    
    # p[0].dataType['name'] = 'array'

def p_ArrayLength(p):
    """
    ArrayLength : Expr
    """
    if p[1].dataType['name'] != 'int':
        raise TypeError(f"{p.lexer.lineno}: ArrayLength must be of Integer Type")
    # Golang requires that array size be constant representable
    # const int x = 2
    # var a [x+x]int = [x+x]int{2, 3} works
    # var int x = 2
    # var a [x+x]int = [x+x]int{2, 3} doesn't work
    if p[1].isConst != True:
        raise TypeError(f"{p.lexer.lineno}: ArrayLength is not a constant.")

    p[0] = p[1]

def p_ElementType(p):
    """
    ElementType : Type
                | IDENT
    """    
    if isinstance(p[1], str):
        p[0] = stm.findType(p[1]) 
    else:
        p[0] = p[1]

###################################################################################
### Struct Type
###################################################################################

def p_StructType(p):
    """
    StructType : STRUCT BeginStruct LBRACE FieldDeclMult RBRACE EndStruct 
    """
    p[0] = StructType(p[4])

def p_BeginStruct(p):
    """
    BeginStruct : 
    """

def p_EndStruct(p):
    """
    EndStruct : 
    """

#extra
def p_FieldDeclMult(p):
    """
    FieldDeclMult : FieldDeclMult FieldDecl SEMICOLON
                  | 
    """
    if len(p) == 1:
        p[0] = NodeList([])
    else:
        p[1].extend(p[2])
        p[0] = p[1]


def p_FieldDecl(p):
    """
    FieldDecl : IdentifierList Type 
              | IdentifierList IDENT
              | EmbeddedField
    """
    if len(p) == 2:
        p[0] = NodeList([StructFieldType(p[1], p[1])])

    elif len(p) == 3:
        p[0] = NodeList([])
        if isinstance(p[2], str):
            p[2] = stm.findType(p[2])
        for key in p[1]:
            p[0].append(StructFieldType(key, p[2]))
    
def p_EmbeddedField(p):
    """
    EmbeddedField : MUL IDENT
                  | IDENT
    """
    if len(p) == 2:
        t = stm.findType(p[1])
        t.label = p[1]
        p[0] = t
    else:
        t = stm.findType(p[2])
        t.label = p[2]
        p[2] = t
        p[0] = PointerType(p[2])
        p[0].dataType['baseType'] = p[2]
        p[0].dataType['level'] = 1
    p[0].dataType['name'] = 'embedded'

###################################################################################
### Map Type
###################################################################################

def p_MapType(p):
    """
    MapType : MAP LBRACK KeyType RBRACK ElementType
    """
    p[0] = MapType(p[3], p[5])

    if p[3].dataType['name'] == 'map' or p[3].dataType['name'] == 'func' or p[3].dataType['name'] == 'slice' or p[3].dataType['name'] == 'array':
        raise TypeError(f"{p.lexer.lineno} Invalid map key type")

def p_KeyType(p):
    """
    KeyType : Type
            | IDENT
    """
    if isinstance(p[1], str):
        p[0] = stm.findType(p[1])
    else:
        p[0] = p[1]

    # p[0].dataType['name'] = 'key'


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
    p[0] = p[1]

###################################################################################
### Basic Literal
###################################################################################
    
def p_BasicLit(p):
    """
    BasicLit : IntLit
             | FloatLit
             | ImagLit
             | RuneLit
             | StringLit
             | BoolLit
    """
    p[0] = p[1]

def p_IntLit(p):
    """
    IntLit : INT
    """
    if check_int(p[1]):
        p[0] = LitNode(dataType = {'name': 'int', 'baseType': 'int', 'level': 0, 'size': 4}, label = p[1], isConst=True, val=int(p[1]))
    else:
        raise (f"{p.lexer.lineno}: Integer Overflow detected")
    # print(p[1])
    temp = new_temp()
    p[0].code.append(f"{temp} = {p[1]}")
    p[0].place = temp 

def p_FloatLit(p):
    """
    FloatLit : FLOAT
    """
    p[0] = LitNode(dataType = {'name': 'float64', 'baseType': 'float64', 'level': 0, 'size': 8}, label = p[1], isConst=True, val=float(p[1]))
    temp = new_temp()
    p[0].code.append(f"{temp} = {p[1]}")
    p[0].place = temp 
    
def p_ImagLit(p):
    """
    ImagLit : IMAG
    """
    p[0] = LitNode(dataType = {'name': 'complex128', 'baseType': 'complex128', 'level': 0, 'size': 8}, label = p[1], isConst=True, val=float(p[1].strip('i')))
    temp = new_temp()
    p[0].code.append(f"{temp} = {p[1]}")
    p[0].place = temp 

def p_RuneLit(p):
    """
    RuneLit : RUNE
    """
    p[0] = LitNode(dataType = {'name': 'rune', 'baseType': 'rune', 'level': 0, 'size': 2}, label = p[1], isConst=True, val=p[1])
    temp = new_temp()
    p[0].code.append(f"{temp} = {p[1]}")
    p[0].place = temp 

def p_StringLit(p):
    """
    StringLit : STRING
    """
    p[0] = LitNode(dataType = {'name': 'string', 'baseType': 'string', 'level': 0, 'size': 12}, label = p[1], isConst=True, val=p[1])
    temp = new_temp()
    p[0].code.append(f"{temp} = {p[1]}")
    p[0].place = temp 

def p_BoolLit(p):
    """
    BoolLit : BOOL
    """
    p[0] = LitNode(dataType = {'name': 'bool', 'baseType': 'bool', 'level': 0, 'size': 1}, label = p[1], isConst=True, val = p[1])
    temp = new_temp()
    p[0].code.append(f"{temp} = {p[1]}")
    p[0].place = temp 

###################################################################################
### Composite Literal
###################################################################################

## Need to implement checks
# TODO: Remove arguments
def p_CompositeLit(p):
    """
    CompositeLit : StructType LiteralValue
                 | ArrayType LiteralValue
                 | SliceType LiteralValue
                 | MapType LiteralValue
                 | IDENT LiteralValue
    """
    if isinstance(p[1], str):
        p[1] = stm.findType(p[1])

    p[0] = CompositeLitNode(stm, p[1].dataType, p[2])

def p_LiteralValue(p):
    """
    LiteralValue : LBRACE ElementList COMMA RBRACE 
                 | LBRACE ElementList RBRACE 
                 | LBRACE RBRACE 
    """
    if len(p) > 3:
        p[0] = p[2]
    else:
        p[0] = NodeList([])

def p_ElementList(p):
    """
    ElementList : KeyedElement 
                | ElementList COMMA KeyedElement 
    """
    if len(p) == 2:
        p[0] = NodeList([p[1]])
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_KeyedElement(p):
    """
    KeyedElement : Element
                 | Key COLON Element
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = KeyValNode(p[1], p[3])

def p_Key(p):
    """
    Key : Expr
        | LiteralValue
    """
    
    p[0] = p[1]

def p_Element(p):
    """
    Element : Expr
            | LiteralValue
    """
    p[0] = p[1]

###################################################################################
### Function Literal
###################################################################################

def p_FunctionLit(p):
    """
    FunctionLit : FUNC Signature FunctionBody
    """
    p[0] = FuncNode(None, p[2][0], p[2][1], p[3])

###################################################################################
## Function Declarations

def p_FuncDecl(p):
    """
    FuncDecl : FuncSig FunctionBody
             | FuncSig
    """
    ## Make node
    if len(p) == 2:
        p[0] = FuncNode(p[1][0], p[1][1][0], p[1][1][1], None)
    else:
        p[0] = FuncNode(p[1][0], p[1][1][0], p[1][1][1], p[2])
    p[0].code.append(f"Func END\n")


    global curr_func_id
    stm.currentReturnType = None
    for symbol in stm.symTable[stm.id].localsymTable:
        if symbol not in info_tables[curr_func_id]:
            info_tables[curr_func_id][symbol] = {}
            
        if stm.id not in info_tables[curr_func_id][symbol]:
            info_tables[curr_func_id][symbol][stm.id] = {}
        info_tables[curr_func_id][symbol][stm.id] = stm.symTable[stm.id].localsymTable[symbol]
    curr_func_id = 'global'
    # Analyze whether return statements are present
    if len(p[1][1][1].dataType) > 0 and not stm.symTable[stm.id].okReturn:
        raise LogicalError(f"{p.lexer.lineno}: Function having non-void return type doesn't return anything.")
    stm.exitScope()

def p_FuncSig(p):
    """
    FuncSig : FUNC FunctionName Signature
    """
    global curr_func_id
    if p[3][1] == None:
        if p[3][0] == None:
            stm.addFunction(p[2].label, {"params": [] , "return": [], "dataType": {'name': 'func', 'baseType': 'func', 'level': 0}})
        else:
            stm.addFunction(p[2].label, {"params": p[3][0].dataType, "return": [], "dataType": {'name': 'func', 'baseType': 'func', 'level': 0}})
            for i, param in enumerate(p[3][0].children):
                stm.add(param.label, {"dataType": param.dataType, "val": param.val, "isConst": param.isConst, "isArg": True, 'paramOf': p[2].label}, True)
                p[3][0].children[i].scope = stm.id

    else:
        if p[3][0] == None:
            stm.addFunction(p[2].label, {"params": [] , "return": p[3][1].dataType, "dataType": {'name': 'func', 'baseType': 'func', 'level': 0}})
        else:
            stm.addFunction(p[2].label, {"params": p[3][0].dataType, "return": p[3][1].dataType, "dataType": {'name': 'func', 'baseType': 'func', 'level': 0}})
            for i, param in enumerate(p[3][0].children):
                stm.add(param.label, {"dataType": param.dataType, "val": param.val, "isConst": param.isConst, "isArg": True, 'paramOf': p[2].label}, True)
                p[3][0].children[i].scope = stm.id
    stm.currentReturnType = deepcopy(p[3][1])
    # print("M: ", len(stm.currentReturnType.dataType), p.lexer.lineno)

    curr_func_id = p[2].label
    info_tables[curr_func_id] = {}

    p[0] = NodeList([p[2], p[3]])

###################################################################################
## Function Name
def p_FunctionName(p):
    """
    FunctionName : IDENT
    """
    ##  Check redeclaration
    if p[1] in stm.functions or stm.getScope(p[1]) >= 0 :
        raise (f"{p.lexer.lineno}: Redeclaration of function " + p[1])

    p[0] = IdentNode(scope = stm.id, label = p[1], dataType = "func")

    p[0].code.append(f"\nFunc {p[1]}")

###################################################################################
## Function Body

def p_FunctionBody(p):
    """
    FunctionBody : BlockStart Block BlockEnd
    """
    p[0] = p[2]

###################################################################################
## Function Signature

def p_Signature(p):
    """
    Signature : Parameters Result
              | Parameters
    """
    if len(p) == 3:
        p[0] = NodeList([p[1], p[2]])
    else:
        p[0] = NodeList([p[1], FuncReturnNode([])])

###################################################################################
## Function Parameters

def p_Parameters(p):
    """
    Parameters : LPAREN RPAREN
               | LPAREN ParameterList RPAREN
               | LPAREN ParameterList COMMA RPAREN
    """
    if len(p) == 3:
        p[0] = FuncParamNode([])
    else:
        p[0] = p[2]
    

def p_ParameterList(p):
    """
    ParameterList : ParameterDecl
                  | ParameterList COMMA ParameterDecl
    """
    if len(p)==2 :
        p[0] = FuncParamNode(p[1])

    elif len(p) == 4:
        p[1].addChild(*p[3])
        p[0] = p[1]

def p_ParameterDecl(p):
    """
    ParameterDecl : IdentifierList Type
                  | IdentifierList IDENT
    """
    p[0] = p[1]
    if isinstance(p[2], str):
        p[2] = stm.findType(p[2])
    for i in range(len(p[0])):
        p[0][i].dataType = p[2].dataType

###################################################################################
## Return Type

def p_Result(p):
    """
    Result : LPAREN ParametersType RPAREN
           | LPAREN RPAREN
           | IDENT
           | Type
    """
    if len(p) > 3:
        if isinstance(p[2], str):
            p[2] = stm.findType(p[2])
        if isinstance(p[2], Type):
            p[2] = [p[2]]
            # print("K: ", p[2])
        p[0] = FuncReturnNode(p[2])
    elif len(p) == 3:
        p[0] = FuncReturnNode([])
    else:
        if isinstance(p[1], str):
            p[1] = stm.findType(p[1])
        if isinstance(p[1], Type):
            p[1] = [p[1]]
        # print("G: ", p[1])
        p[0] = FuncReturnNode(p[1])

def p_ParametersType(p):
    """
    ParametersType : IDENT
                   | Type
                   | ParametersType COMMA IDENT
                   | ParametersType COMMA Type
    """
    if len(p) == 2:
        if isinstance(p[1], str):
            p[0] = FuncParamType()
            # print("F: ", p[0].__dict__)
            p[0].addChild(stm.findType(p[1]))
        else:
            p[0] = FuncParamType()
            # print("G: ", p[0].__dict__)
            p[0].addChild(p[1])
    else:
        if isinstance(p[3], str):
            p[1].addChild(stm.findType(p[3]))
        else:
            p[1].addChild(p[3])
        p[0] = p[1]
    # print("R: ",len(p[0].dataType))

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
    if len(p) == 4:
        assert(isinstance(p[3], NodeList))
        p[0] = NodeList([p[1]])
        p[0].extend(p[3])
    else:
        p[0] = NodeList([])

def p_Statement(p):
    """
    Statement : Decl
              | SimpleStmt
              | BreakStmt
              | ContinueStmt
              | FallthroughStmt
              | BlockStart Block BlockEnd
              | GotoStmt
              | LabeledStmt
              | IfStmt
              | SwitchStmt
              | ForStmt
              | ReturnStmt
    """
    p[0] = p[1]

###################################################################################
### Labeled Statements
###################################################################################

def p_LabeledStmt(p):
    """
    LabeledStmt : Label COLON Statement
    """
    stm.labels[p[1]]['statementType'] = type(p[3])
    p[0] = LabelNode(p[1], LabelStatementNode(p[3], p.lexer.lineno))
    stm.currentLabel = None
    p[0].code = [f"{stm.labels[p[1]]['mappedName']}:"] + p[0].code

def p_JumpLabel(p):
    """
    JumpLabel : IDENT
    """
    p[0] = p[1]

def p_Label(p):
    """
    Label : IDENT
    """
    labelScopeTab = deepcopy(stm.symTable[stm.getCurrentScope()])
    if p[1] not in stm.labels:
        # Create a new label and need not set expecting to true; set it to false
        stm.labels[p[1]] = {
            'scopeTab': labelScopeTab,
            'mappedName' : stm.getNewLabel(),
            'expecting' : False ,
            'lineno' : p.lexer.lineno,
            'statementType' : None,
            'prevGotos': []
        }
    else: 
        if stm.labels[p[1]]['expecting'] == False:
            # Redeclaration of label - Error
            raise LogicalError(f"{p.lexer.lineno}: Label declared earlier at {stm.labels[p[1]]['lineno']}.")
        else:
            # Expecting = True; 
            # Analyse previous gotos (if any), and set expecting to False
            for goto in stm.labels[p[1]]['prevGotos']:
                gotoScopeTab, gotoLineno = goto
                if not isValidGoto(stm, labelScopeTab, gotoScopeTab, checkNoSkipVar=True):
                    raise LogicalError(f"{p.lexer.lineno}: Invalid placement of Goto at {gotoLineno} - Goto statement outside of a Block can't jump inside a Block and variable declarations can't be skipped.")
            stm.labels[p[1]]['scopeTab'] = labelScopeTab
            stm.labels[p[1]]['expecting'] = False
            stm.labels[p[1]]['scopeTab'] = labelScopeTab
            stm.labels[p[1]]['lineno'] = p.lexer.lineno
    stm.currentLabel = p[1]
    p[0] = p[1]

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
    p[0] = p[1]

###################################################################################
### Empty Statements

def p_EmptyStmt(p):
    """
    EmptyStmt : 
    """
    p[0] = EmptyNode()

###################################################################################
### Expression Statements

def p_ExpressionStmt(p):
    """
    ExpressionStmt : Expr
    """
    # Check if builtin function definitions are added in STM
    builtInFuncsToAvoid = [
        'append',
        'cap',
        'complex',
        'imag',
        'len',
        'make',
        'new',
        'real'
    ]
    if hasattr(stm, 'builtInFuncs') and isinstance(p[1], FuncCallNode):
        funcName =  p[1].children[0].children[0]
        if funcName in builtInFuncsToAvoid and funcName not in stm.functions:
            funcReturnType = stm.builtInFuncs[funcName]['return']
            raise ValueNotUsedError(f"{p.lexer.lineno}: Value of type {funcReturnType} is not used.")
    p[0] = p[1]

###################################################################################
### Increment/Decrement Statements

def p_IncDecStmt(p):
    """
    IncDecStmt :  Expr INC
                 | Expr DEC
    """
    if p[1].isAddressable == False:
        raise LogicalError(f"{p.lexer.lineno}: Expression is not addressable.")
    if not isBasicNumeric(stm, p[1].dataType):
        raise LogicalError(f"{p.lexer.lineno}: Non-numeric type can't be incremented or decremented.")
    if p[2] == '++':
        p[0] = IncNode(p[1])
        p[0].code.append(f"{p[1].place} = {p[1].place} + 1")
    else:
        p[0] = DecNode(p[1])
        p[0].code.append(f"{p[1].place} = {p[1].place} - 1")

###################################################################################
### Assignment Statements

def p_Assignment(p):
    """
    Assignment : ExpressionList assign_op ExpressionList
    """
    if len(p[1]) != len(p[3]):
        if len(p[3]) == 1 and isinstance(p[3][0], FuncCallNode):
            pass 
        else:
            raise LogicalError(f"{p.lexer.lineno}: Imbalanced assignment with {len(p[1])} identifiers and {len(p[3])} expressions.")
    p[0] = NodeList([])
    expression_dt = []
    for i in range(len(p[3])):
        expr = p[3][i]
        if isinstance(expr.dataType, list):
            expression_dt.extend(expr.dataType)
        else:
            expression_dt.append(expr.dataType)
    for i, (key, val) in enumerate(zip(p[1], p[3])):
        if key.label != _symbol:
            if hasattr(key, 'isConst') and key.isConst == True:
                raise TypeError(f"{p.lexer.lineno}: LHS contains constant! Cannot assign")
            if key.dataType != expression_dt[i]:
                raise TypeError(f"{p.lexer.lineno}: Type of {key.label} : {key.dataType} and {val.label} : {expression_dt[i]} doesn't match.")
            if key.isRef == True:
                raise LogicalError(f"{p.lexer.lineno}: LHS Expression can't assign to an reference.")
            if key.isDeRef == True:
                if key.dataType['level'] < 0:
                    raise LogicalError(f"{p.lexer.lineno}: LHS expression can't be derefenced further")
                key.place = f'*{key.lvalue}'
        exprNode = ExprNode(None, operator=p[2])
        exprNode.addChild(key, val)
        p[0].append(exprNode)
    for i, (key, val) in enumerate(zip(p[1], p[3])):
        if p[2] == '=':
            p[0].code.append(f"{key.place} = {val.place}")
        else:
            p[0].code.append(f"{key.place} = {key.place} {p[2][0]}({expression_dt[i]['name']}) {val.place}")
def p_assign_op(p):
    """
    assign_op : add_op_assign 
              | mul_op_assign
              | ASSIGN
    """
    p[0] = p[1]

def p_add_op_assign(p):
    """
    add_op_assign : ADD_ASSIGN
                    | SUB_ASSIGN
                    | OR_ASSIGN
                    | XOR_ASSIGN
    """
    p[0] = p[1]

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
    p[0] = p[1]

###################################################################################
### Short Variable Declaration

def p_ShortVarDecl(p):
    """
    ShortVarDecl : IdentifierList DEFINE ExpressionList
    """
    length = len(p) - 1

    count_0 = 0
    count_1 = 0

    expression_datatypes = []

    for i in range(len(p[length])):
        if isinstance(p[length][i], FuncCallNode):
            func_name = p[length][i].children[0].label
            dt_return = stm.functions[func_name]["return"]
            expression_datatypes.extend(dt_return)
            if len(dt_return) == 0:
                raise TypeError(f"{p.lexer.lineno}: Function does not return anything!")
            elif len(dt_return) == 1:
                count_0+=1
            else:
                count_1+=1
        else:
            expression_datatypes.append(p[length][i].dataType)
    
    if count_1 > 0:
        if len(p[length]) > 1:
            raise TypeError(f"{p.lexer.lineno}: Function with more than one return values should be assigned alone!")

    if len(p[1]) != len(expression_datatypes):
        raise NameError(f"{p.lexer.lineno}: Assignment is not balanced")
    
    dt = {}

    if len(p[1]) != len(expression_datatypes):
        raise LogicalError(f"{p.lexer.lineno}: Imbalanced declaration with {len(p[1])} identifiers and {len(expression_datatypes)} expressions.")
    p[0] = NodeList([])
    for key, val in zip(p[1], p[3]):
        exprNode = ExprNode(None, label="DEFINE", operator="=")
        exprNode.addChild(key, val)
        p[0].append(exprNode)
    return_values = []
    for expr in p[length]:
        exprDt = expr.dataType
        if isinstance(exprDt, list):
            return_values.extend(exprDt)
        else:
            return_values.append(exprDt)
    assert(len(return_values) == len(p[1]))
    for i, ident in enumerate(p[1]):

        # Check redeclaration for identifier list
        latest_scope = stm.getScope(ident.label)
        if latest_scope == stm.id or ident.label in stm.functions:
            raise NameError(f'{p.lexer.lineno}: Redeclaration of identifier: ' + ident.label)
        
        # Add to symbol table
        dt = return_values[i]
        stm.add(ident.label, {'dataType': dt, 'isConst' : False})
        p[1][i].dataType = dt


    if count_1 == 0:
        for i in range(len(p[1])):
            p[0].code.append(f"{stm.id}_{p[1][i].label} = {p[length][i].place}")
            stm.symTable[stm.id].updateAttr(p[1][i].label, {'tmp': f"{stm.id}_{p[1][i].label}"})

    else:
        for i in range(len(p[1])):
            p[0].code.append(f"{stm.id}_{p[1][i].label} = {p[length][0].place[i]}")
            stm.symTable[stm.id].updateAttr(p[1][i].label, {'tmp': f"{stm.id}_{p[1][i].label}"})

###################################################################################
### Goto Statements
###################################################################################

def p_GotoStmt(p):
    """
    GotoStmt :  GOTO JumpLabel
    """
    gotoScopeTab = deepcopy(stm.symTable[stm.getCurrentScope()])
    if p[2] in stm.labels:
        # Label has been seen before
        if stm.labels[p[2]]['expecting']:
            # Currently not seen the labeled statement
            # Label has been created earlier by previous goto
            stm.labels[p[2]]['prevGotos'].append(
                (gotoScopeTab, p.lexer.lineno)
            )
        else:
            # Label already declared before (backward jump)
            # Check parent condition
            if not isValidGoto(stm, stm.labels[p[2]]['scopeTab'], gotoScopeTab):
                raise LogicalError(f"{p.lexer.lineno}: Invalid placement of goto wrt label at {stm.labels[p[2]]['lineno']} - Goto statement outside of a Block can't jump inside a block.")
            # No need to append gotos as semantic analysis is complete
    else:
        # Label not declared before; expecting label; (forward jump)
        # Semantic analysis to be done when corresponding Label is parsed
        # at the labeled stmt non-terminal

        # Will shallow copy work or do we need deepcopy?
        # Label is created for the first time from goto
        stm.labels[p[2]] = {
            'scopeTab': None,
            'mappedName' : stm.getNewLabel(),
            'expecting' : True ,
            'lineno' : None,
            'statementType' : None,
            'prevGotos': [
                (gotoScopeTab, p.lexer.lineno)
            ]
        }
            
    p[0] = GotoNode(p[2])
    p[0].code.append(f"goto {stm.labels[p[2]]['mappedName']}")

###################################################################################
### Return Statements
###################################################################################

def p_ReturnStmt(p):
    """
    ReturnStmt : RETURN ExpressionList
                | RETURN
    """
    # This case should never arise
    if stm.currentReturnType is None:
        raise LogicalError(f"{p.lexer.lineno}: Return statement outside of a function.")
    if len(p) == 2:
        if stm.currentReturnType:
            raise LogicalError(f"{p.lexer.lineno}: Current function doesn't return nothing.")
        p[0] = ReturnNode([])
        p[0].code.append("return")
    else:
        returnvalues = []
        for expr in p[2]:
            if isinstance(expr.dataType, list):
                returnvalues.extend(expr.dataType)
            else:
                returnvalues.append(expr.dataType)
        # print(len(stm.currentReturnType.dataType), len(returnvalues))
        if len(stm.currentReturnType.dataType) != len(returnvalues):
            raise LogicalError(f"{p.lexer.lineno}: Different number of return values.")
        for returnDataType, ExprNodedt in zip(stm.currentReturnType.dataType, returnvalues):
            if returnDataType != ExprNodedt:
                raise LogicalError(f"{p.lexer.lineno}: Return type of current function :{returnDataType} and the return statement {ExprNodedt} doesn't match.")
        p[0] = ReturnNode(p[2])
        for expr in p[2]:
            p[0].code.append(f"retparams {expr.place}")
        p[0].code.append("return")
    stm.symTable[stm.id].okReturn = True

###################################################################################
### Break Statements
###################################################################################

def p_BreakStmt(p):
    """
    BreakStmt : BREAK 
              | BREAK JumpLabel
    """
    if len(stm.forStack) == 0 and len(stm.switchStack) == 0:
        raise LogicalError(f"{p.lexer.lineno}: Break can only be used inside for loops and switch statements.")
    if len(p) == 2:
        p[0] = BreakNode()
        if len(stm.forStack) == 0:
            p[0].code.append(f"goto end_switch_{stm.switchStack[-1]}")
        elif len(stm.switchStack) == 0:
            p[0].code.append(f"goto end_for_{stm.forStack[-1]}")
        elif stm.forStack[-1] < stm.switchStack[-1]:
            p[0].code.append(f"goto end_switch_{stm.switchStack[-1]}")
        else:
            p[0].code.append(f"goto end_for_{stm.forStack[-1]}")
    else:
        if p[2] not in stm.labels:
            raise LogicalError(f"{p.lexer.lineno}: Label for the break statement must have been declared beforehand.")
        if not stm.labels[p[2]]['statementType'] or stm.labels[p[2]]['statementType'] not in ['FOR', 'SWITCH']:
            raise LogicalError(f"{p.lexer.lineno}: Label used with break statement must be used on a for loop statement or switch node statement.")
        p[0] = BreakNode(p[2])
        lineno = stm.labels[p[2]]['lineno']
        if lineno in stm.forStack:
            p[0].code.append(f"goto end_for_{stm.labels[p[2]]['lineno']}")
        else:
            p[0].code.append(f"goto end_switch_{stm.labels[p[2]]['lineno']}")

###################################################################################
### Continue Statements
###################################################################################

def p_ContinueStmt(p):
    """
    ContinueStmt :  CONTINUE
                 |  CONTINUE JumpLabel
    """
    if len(stm.forStack) == 0:
        raise LogicalError(f"{p.lexer.lineno}: Continue can only be called inside a for loop.")
    if len(p) == 2:
        p[0] = ContinueNode()
        p[0].append.code(f"goto start_for_{stm.forStack[-1]}")
    else:
        if p[2] not in stm.labels:
            raise LogicalError(f"{p.lexer.lineno}: Label for the continue statement must have been declared beforehand.")
        if not stm.labels[p[2]]['statementType'] or stm.labels[p[2]]['statementType'] not in ['FOR']:
            raise LogicalError(f"{p.lexer.lineno}: Label used with continue statement must be used on a for loop statement.")
        p[0] = ContinueNode(p[2])
        p[0].code.append(f"goto begin_for_{stm.labels[p[2]]['lineno']}")

###################################################################################
### Fallthrough Statements
###################################################################################

def p_FallthroughStmt(p):
    """
    FallthroughStmt : FALLTHROUGH
    """
    p[0] = FallthroughNode()
    # Code to implemented later


###################################################################################
### Block Statements
###################################################################################

def p_Block(p):
    """
    Block : LBRACE StatementList RBRACE
    """
    p[0] = BlockNode(p[2])

def p_BlockStart(p):
    """
    BlockStart : 
    """
    stm.newScope()
    p[0] = []

def p_BlockEnd(p):
    """
    BlockEnd : 
    """
    stm.exitScope()
    p[0] = []

###################################################################################
### If Else Statements
###################################################################################

def p_IfStmt(p):
    """
    IfStmt : IF BeginIf Expr BlockStart Block BlockEnd else_stmt EndIf
           | IF BeginIf SimpleStmt SEMICOLON Expr BlockStart Block BlockEnd else_stmt EndIf
    """
    if p[len(p) - 2] and stm.symTable[stm.id].NotAllChildReturn == False:
        stm.symTable[stm.id].okReturn = True
    else:
        stm.symTable[stm.id].okReturn = False
    stm.symTable[stm.id].NotAllChildReturn = True
    stm.exitScope()

    if len(p) == 9:
        if p[3].dataType['baseType'] != 'bool' or p[3].dataType['level'] != 0:
            raise TypeError(f'{p.lexer.lineno}: Expression inside if-statement must be of bool type!') 
        else:
            p[5].code.append(f"goto end_{p.lexer.lineno}")
            p[5].code.append(f"else_{p.lexer.lineno}:")
            p[3].code.append(f"if not {p[3].place} then goto else_{p.lexer.lineno}")
            p[0] = IfNode(None, p[3], ThenNode(p[5]), p[7])
            p[0].code.append(f"end_{p.lexer.lineno}:")
    else:
        if p[5].dataType['baseType'] != 'bool' or p[5].dataType['level'] != 0:
            raise TypeError(f'{p.lexer.lineno}: Expression inside if-statement must be of bool type!') 
        p[0] = IfNode(*p[3], p[5], ThenNode(p[7]), p[9])

def p_BeginIf(p):
    """
    BeginIf : 
    """
    stm.newScope()

def p_EndIf(p):
    """
    EndIf :
    """
    global curr_func_id
    for symbol in stm.symTable[stm.id].localsymTable:
        if symbol not in info_tables[curr_func_id]:
            info_tables[curr_func_id][symbol] = {}

        if stm.id not in info_tables[curr_func_id][symbol]:
            info_tables[curr_func_id][symbol][stm.id] = {}
        
        info_tables[curr_func_id][symbol][stm.id] = stm.symTable[stm.id].localsymTable[symbol]

def p_else_stmt(p):
    """
    else_stmt : ELSE IfStmt
                | ELSE BlockStart Block BlockEnd
                |
    """
    if len(p) > 1:
        p[0] = ElseNode(p[2])

###################################################################################
### Switch Statements
###################################################################################

def p_SwitchStmt(p):
    """
    SwitchStmt :  ExprSwitchStmt
    """
    p[0] = p[1]

###################################################################################
### Expression Switch Statements

def p_ExprSwitchStmt(p):
    """
    ExprSwitchStmt : SWITCH BeginSwitch SimpleStmt SEMICOLON Expr LBRACE ExprCaseClauseMult EndSwitch RBRACE
                     | SWITCH Expr LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
                     | SWITCH BeginSwitch SimpleStmt SEMICOLON LBRACE ExprCaseClauseMult EndSwitch RBRACE
                     | SWITCH LBRACE BeginSwitch ExprCaseClauseMult EndSwitch RBRACE
    """
    smtNode = None
    varNode = None
    casesNode = []
    if len(p) == 7:

        ## Check if a case has been repeated
        lst = []
        for case in p[4]:
            if isinstance(case.children[0][0], CaseNode):
                if case.children[0][0].children[0].label in lst:
                    raise DuplicateKeyError("Case statement for " + case.children[0][0].children[0].label + " has been already written!")
                else:
                    lst.append(case.children[0][0].children[0].label) 
        casesNode = p[4]
        for statement in casesNode[-1].instrNode:
            if isinstance(statement, FallthroughNode):
                raise LogicalError(f"{p.lexer.lineno}: Fallthrough statement can't be used in the last case of the switch statement.")
    elif len(p) == 8:
        
        ## Check if dataType is supported
        if p[2].dataType['level'] != 0 or not isOrdered(stm, p[2].dataType['name']):
            raise TypeError(f"{p.lexer.lineno}: Unsupported type in switch condition!")

        ## Check if a case has been repeated
        lst = []
        for case in p[5]:
            if isinstance(case.children[0][0], CaseNode):
                if case.children[0][0].children[0].label in lst:
                    raise DuplicateKeyError("Case statement for " + case.children[0][0].children[0].label + " has been already written!")
                else:
                    lst.append(case.children[0][0].children[0].label) 
        varNode = p[2]
        casesNode = p[5]
        for statement in casesNode[-1].instrNode:
            if isinstance(statement, FallthroughNode):
                raise LogicalError(f"{p.lexer.lineno}: Fallthrough statement can't be used in the last case of the switch statement.")
    elif len(p) == 9:
        ## Check if a case has been repeated
        lst = []
        for case in p[6]:
            if isinstance(case.children[0][0], CaseNode):
                if case.children[0][0].children[0].label in lst:
                    raise DuplicateKeyError("Case statement for " + case.children[0][0].children[0].label + " has been already written!")
                else:
                    lst.append(case.children[0][0].children[0].label) 

        smtNode = p[2]
        casesNode = p[6]
        for statement in casesNode[-1].instrNode:
            if isinstance(statement, FallthroughNode):
                raise LogicalError(f"{p.lexer.lineno}: Fallthrough statement can't be used in the last case of the switch statement.")
    else:
        if p[2].dataType['level'] != 0 or not isOrdered(stm, p[2].dataType['name']):
            raise TypeError(f"{p.lexer.lineno}: Unsupported type in switch condition!")

        ## Check if a case has been repeated
        lst = []
        for case in p[7]:
            if isinstance(case.children[0][0], CaseNode):
                if case.children[0][0].children[0].label in lst:
                    raise DuplicateKeyError("Case statement for " + case.children[0][0].children[0].label + " has been already written!")
                else:
                    lst.append(case.children[0][0].children[0].label) 
        smtNode = p[2]
        varNode = p[4]
        casesNode = p[7]
        for statement in casesNode[-1].instrNode:
            if isinstance(statement, FallthroughNode):
                raise LogicalError(f"{p.lexer.lineno}: Fallthrough statement can't be used in the last case of the switch statement.")
    
    varNode.code.append(f"{stm.currentSwitchExpPlace} = {varNode.place}")
    p[0] = SwitchNode(smtNode, varNode, casesNode)
    p[0].code.append(f"end_switch_{stm.switchStack[-1]}:")
    stm.switchStack.pop()
    stm.exitScope()
    stm.currentSwitchExpPlace = None
    stm.nextCase = 0

def p_BeginSwitch(p):
    """
    BeginSwitch : 
    """
    if stm.currentLabel and stm.labels[stm.currentLabel]['lineno'] == p.lexer.lineno:
        stm.labels[stm.currentLabel] = 'SWITCH'
        stm.currentLabel = None
    stm.newScope()
    stm.switchStack.append(p.lexer.lineno)
    stm.currentSwitchExpPlace = new_temp()

def p_EndSwitch(p):
    """
    EndSwitch : 
    """
    global curr_func_id
    for symbol in stm.symTable[stm.id].localsymTable:
        if symbol not in info_tables[curr_func_id]:
            info_tables[curr_func_id][symbol] = {}

        if stm.id not in info_tables[curr_func_id][symbol]:
            info_tables[curr_func_id][symbol][stm.id] = {}
        
        info_tables[curr_func_id][symbol][stm.id] = stm.symTable[stm.id].localsymTable[symbol]

def p_ExprCaseClauseMult(p):
    """
    ExprCaseClauseMult : ExprCaseClauseMult ExprCaseClause 
                         |
    """
    if len(p) == 1:
        p[0] = NodeList([])
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_ExprCaseClause(p):
    """
    ExprCaseClause : ExprSwitchCase COLON StatementList
    """
    if isinstance(p[1][0], CasesNode):
        cond_res = new_temp()
        code = []
        code.append(f"{cond_res} = {stm.currentSwitchExpPlace} ==({p[1][0].dataType['name']}) {p[1][0].place}")
        code.append(f"if not {cond_res} then goto case_{stm.nextCase}_{stm.switchStack[-1]}")
        p[1].code.extend(code)
    else:
        # Default Node case
        pass
    p[3].code.append(f"goto end_switch_{stm.switchStack[-1]}")
    p[3].code.append(f"label case_{stm.nextCase}_{stm.switchStack[-1]}:")
    p[0] = CasesNode(p[1], p[3])
    # print(p[0].code)
    
def p_ExprSwitchCase(p):
    """
    ExprSwitchCase : CASE ExpressionList
                     | DEFAULT
    """
    if len(p) == 3:
        stm.nextCase += 1
        p[0] = NodeList([])
        if len(p[2]) > 1:
            raise SwitchCaseError("Complex expressions not allowed inside switch statement!")
        for expr in p[2]:
            caseNode = CaseNode(expr)
            caseNode.place = expr.place
            caseNode.dataType = expr.dataType
            
            p[0].append(caseNode)
    else:
        p[0] = NodeList([DefaultNode()])

###################################################################################
### For Statements
###################################################################################

def p_ForStmt(p):
    """
    ForStmt : FOR BeginFor Condition BlockStart Block BlockEnd EndFor
            | FOR BeginFor ForClause BlockStart Block BlockEnd EndFor
            | FOR BeginFor RangeClause BlockStart Block BlockEnd EndFor
            | FOR BeginFor BlockStart Block BlockEnd EndFor
    """
    if len(p) == 7:
        p[0] = ForNode(None, p[4])
        p[0].code = [f"begin_for_{stm.forStack[-1]}:"] + p[0].code + [f"goto begin_for_{stm.forStack[-1]}", f"end_for_{stm.forStack[-1]}:"]
    else:
        if isinstance(p[3], ForClauseNode) and p[3].children[0] is None and p[3].children[2] is None:
            p[3].code = [f"begin_for_{stm.forStack[-1]}:"] + p[3].children[1].code + [f"if not {p[3].children[1].place} then goto end_for_{stm.forStack[-1]}"]
            p[5].code.append(f"goto begin_for_{stm.forStack[-1]}")
            p[5].code.append(f"end_for_{stm.forStack[-1]}:")
        elif isinstance(p[3], ForClauseNode):
            # initc = p[3][0]
            # condc = p[3][1]
            # postc = p[3][2]
            temp = p[3].children[0].code + [f"begin_for_{stm.forStack[-1]}:"] + p[3].children[1].code
            p[3].code = temp + [f"if not {p[3].children[1].place} goto end_for_{stm.forStack[-1]}"]
            p[5].code.extend(p[3].children[2].code)
            p[5].code.append(f"goto begin_for_{stm.forStack[-1]}")
            p[5].code.append(f"end_for_{stm.forStack[-1]}:")
        else:
            if p[3].children[2].dataType['name'] == 'map':
                pass
            else:
                code = []
                idx = p[3].children[0].place
                code.append(f"{idx} = {idx} + 1")
                elemptr = p[3].vartemp
                elem = p[3].children[1].place
                size = p[3].children[1].dataType['size']
                code.append(f"{elemptr}.pointer = {elemptr}.pointer + {size}")
                code.append(f"{elem} = *{elemptr}")
                code.append(f"goto begin_for_{stm.forStack[-1]}")
                code.append(f"end_for_{stm.forStack[-1]}")
                p[5].code.extend(code)
        p[0] = ForNode(p[3], p[5])
    
    stm.forStack.pop()
    stm.exitScope()

def p_BeginFor(p):
    """
    BeginFor : 
    """
    if stm.currentLabel and stm.labels[stm.currentLabel]['lineno'] == p.lexer.lineno:
        stm.labels[stm.currentLabel]['statementType'] = 'FOR'
        stm.currentLabel = None
    stm.newScope()
    stm.forStack.append(p.lexer.lineno)

def p_EndFor(p):
    """
    EndFor : 
    """
    global curr_func_id
    for symbol in stm.symTable[stm.id].localsymTable:
        if symbol not in info_tables[curr_func_id]:
            info_tables[curr_func_id][symbol] = {}

        if stm.id not in info_tables[curr_func_id][symbol]:
            info_tables[curr_func_id][symbol][stm.id] = {}
        
        info_tables[curr_func_id][symbol][stm.id] = stm.symTable[stm.id].localsymTable[symbol]
    
def p_Condition(p):
    """
    Condition : Expr
    """
    p[0] = ForClauseNode(None, p[1], None)
    p[0].place = p[1].place

###################################################################################
### For Clause

def p_ForClause(p):
    """
    ForClause : InitStmt SEMICOLON Condition SEMICOLON PostStmt
                | InitStmt SEMICOLON SEMICOLON PostStmt
    """
    if len(p) == 6:
        p[0] = ForClauseNode(p[1], p[3].children[1], p[5])
    else:
        dt = {
            'name' : 'bool',
            'baseType': 'bool',
            'level' : 0,
            'size' : 1
        }
        trueNode = ExprNode(dt, label='true', operator=None, isConst=True, isAddressable=False, val='true')
        trueNode.place = new_temp()
        trueNode.code.append(f"{trueNode.place} = true")
        # Absence of condition is equivalent to a FOR true statement
        p[0] = ForClauseNode(p[1], trueNode, p[4])

def p_InitStmt(p):
    """
    InitStmt :   SimpleStmt
    """
    p[0] = p[1]

def p_PostStmt(p):
    """
    PostStmt :   SimpleStmt
    """
    if isinstance(p[1], ExprNode) and p[1].label == 'DEFINE':
        raise LogicalError("Short Variable Declaration not allowed in post statement of for loop.")
    p[0] = p[1]

###################################################################################
### Range Clause

def p_RangeClause(p):
    """
    RangeClause : RangeList RANGE Expr
    """
    rangeExprType = []
    if p[3].dataType['name'] in ['array', 'slice']:
        rangeExprType.append(constructDataType('int')) 
        core_type = p[3].dataType['baseType']
        if not isinstance(core_type, dict):
            core_type = constructDataType(core_type)
        rangeExprType.append(
            core_type
        )
    elif p[3].dataType['name'] in ['string']:
        rangeExprType.append(constructDataType('int')) 
        rangeExprType.append(constructDataType('rune'))
    elif p[3].dataType['name'] in ['map']:
        key_type = p[3].dataType['KeyType']
        if not isinstance(key_type, dict):
            key_type = constructDataType(key_type)
        value_type = p[3].dataType['ValueType']
        if not isinstance(value_type, dict):
            value_type = constructDataType(value_type)
        rangeExprType.append(
            key_type
        )
        rangeExprType.append(
            value_type
        )
    else:
        raise TypeError(f"{p.lexer.lineno}: Core Type of range clause must be array, pointer to an array, slice or map")
    if len(p[1]) == 2:
        if p[1][0].label == p[1][1].label and p[1][0].label != '_':
            raise LogicalError(f"{p.lexer.lineno}: Range clauses has multiple identifiers with same name.")
    for idx, var in enumerate(p[1]):
        if isinstance(var, IdentNode):
            # ShortVarDecl
            # If shortvaldecl statement, insert into stm
            var.dataType = deepcopy(rangeExprType[idx])
            stm.add(var.label, {'dataType' : rangeExprType[idx], 'isConst' : False})
        elif isinstance(var, ExprNode):
            # Assignment
            # If assignment statement check for types
            if var.label != '_':
                lastDeclaredEntry = stm.get(var.label)
                if lastDeclaredEntry != -1:
                    if lastDeclaredEntry['dataType'] != rangeExprType[idx]:
                        raise TypeError(f"{p.lexer.lineno}: Type of {var.label} does't match with {rangeExprType[idx]['name']}.")
            else:
                var.dataType = deepcopy(rangeExprType[idx])
                stm.add(var.label, {'dataType' : rangeExprType[idx], 'isConst' : False})

    p[0] = ForRangeNode(p[1], p[3])

    code = []
    idx = new_temp()
    elemptr = var_new_temp()
    elem = new_temp()
    p[1][0].place = idx
    scopeid = stm.getScope(p[1][0].label)
    stm.symTable[scopeid].localsymTable[p[1][0].label]['tmp'] = idx
    p[1][1].place = elem
    scopeid = stm.getScope(p[1][1].label)
    stm.symTable[scopeid].localsymTable[p[1][1].label]['tmp'] = elem
    code.append(f"{idx} = 0")
    code.append(f"{elemptr}.pointer = {p[3].place}.pointer")
    code.append(f"{elem} = *{elemptr}.pointer")
    code.append(f"begin_for_{stm.forStack[-1]}:")
    cond_res = new_temp()
    code.append(f"{cond_res} = {idx} <(int) {elemptr}.length")
    code.append(f"if not {cond_res} goto end_for_{stm.forStack[-1]}")
    p[0].code = code
    p[0].vartemp = elemptr

def p_RangeList(p):
    """
    RangeList : ExpressionList ASSIGN 
                | IdentifierList DEFINE
                | 
    """
    if len(p) == 1:
        p[0] = NodeList([])
    else:
        if p[2] == '=':
            for expr in p[1]:
                if expr.isAddressable is False:
                    raise TypeError(f"{p.lexer.lineno}: Operands in expression list must be addressable or map index expressions.")
        if len(p[1]) > 2:
            raise LogicalError(f"{p.lexer.lineno}: Atmost two iteration values may be provided to the range expression.")
        p[0] = p[1]


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

def genAutomaton(parser):
    path_to_root = os.environ.get('PATH_TO_ROOT')
    milestone = os.environ.get('MILESTONE')
    if path_to_root is not None:
        with open(path_to_root + "/src/Milestone" + str(milestone) + "/action.txt", "w") as f:
            for key, val in parser.action.items():
                f.writelines(f'{key} : {val}\n')

        with open(path_to_root + "/src/Milestone" + str(milestone) + "/goto.txt", "w") as f:
            for key, val in parser.goto.items():
                f.writelines(f'{key} : {val}\n')

def parse(parser, lexer, source_code):
    # Trying to handle input
    return parser.parse(source_code, lexer = lexer)

def writeOutput(parser_out, output_file):
    if parser_out is None:
        raise ValueError("Invalid output from parser.")
    with open(output_file, 'w') as fout:
        pprint.pprint(parser_out, width=10, stream=fout)


def df(root, level):
    print('    '*level + str(root) +  " - " +  str(type(root)))
    if hasattr(root, 'children') and root.children:
        for child in root.children:
            df(child, level+1)

def create_sym_tables(path_to_folder):
    if not os.path.exists(path_to_folder):
        os.mkdir(path_to_folder)

    for key in info_tables:
        filename = os.path.join(path_to_folder, key) + ".csv"
        info = info_tables[key]
        dict = []
        i = 0
        for item in info:
            dict.append({})
            dict[i]['ident'] = item
            dict[i]['scope'] = list(info[item].keys())[0]
            dict[i]['info'] = info[item][dict[i]['scope']]
            i += 1

        fields = ['ident', 'scope', 'info']

        with open(filename, "w") as f:
            writer = csv.DictWriter(f, fieldnames = fields)

            writer.writeheader()

            writer.writerows(dict)
    
def buildAndCompile(input_file):
    global target_folder

    target_folder = os.path.dirname(os.path.join(os.getcwd(),input_file))
    source_code = None
    path_to_source_code = input_file
    output_file = path_to_source_code[:-2] + "output"
    with open(path_to_source_code, 'r') as f:
        source_code = f.read()
    lexer = lex.lex()
    parser, _ = yacc.yacc()
    genAutomaton(parser)
    parser_out = parse(parser, lexer, source_code)
    # df(parser_out, 0)
    writeOutput(parser_out, output_file)
    create_sym_tables(os.path.join(os.getcwd(), path_to_source_code[:-2]) + "symTables")
    print("Writing 3AC")
    return parser_out, stm

if __name__ == '__main__':
    buildAndCompile(sys.argv[1])
    
