import ply.lex as lex
import ply.yacc as yacc
import sys

# --- Lexing rules ---
# NOTE: Replace these with your own

# Token list:

tokens = ['LSQBRACKET',
          'RSQBRACKET',
          'COMMA',
          'LPARENTHESE',
          'RPARENTHESE',
          'LBRACE',
          'RBRACE',
          'COLON',
          'STRING',
          'NUMBER',
          'TRUE',
          'FALSE',
          'DOT',
          'NULL'
          ]

# Specification of each token:
t_ignore = " \t\n"   # These things are ignored


t_LPARENTHESE = r'\('
t_RPARENTHESE = r'\)'


def t_LSQBRACKET(t):
    r'\['
    return t

def t_RSQBRACKET(t):
    r'\]'
    return t

def t_LBRACE(t):
    r'\{'
    return t

def t_RBRACE(t):
    r'\}'
    return t

def t_COLON(t):
    r'\:'
    return t

def t_COMMA(t):
    r','
    return t

def t_NUMBER(t):
    r'-?(0|([1-9]\d*))(\.\d+)?([e|E]([+|-]?)\d+)?'
    return t

def t_STRING(t):
    r'\" ([^\"\\]|\\["bfnrt\\/]|\\u[0-9a-fA-F]{4} )* \"'
    return t

def t_DOT(t):
    r'\.'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_NULL(t):
    r'null'
    return t

# Performing action (in this case, error)

def t_error(t):
    t.lexer.skip(1)

# --- End lexing rules


# Leave this here; this generates a lexer from the above rules
lexer = lex.lex()


#code for testing lexer#
# lexer.input(r'[0.]')
#
#
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)


# --- Parsing rules ---
# NOTE: Replace these with your own
def p_JSON(p):
    '''
    JSON : object
         | array
    '''

def p_object(p):
    '''object : LBRACE members RBRACE'''


def p_members(p):
    '''members : pair COMMA members
               | pair
               | empty'''


def p_pair(p):
    '''pair : STRING COLON value'''


def p_array(p):
    '''array : LSQBRACKET valuelist RSQBRACKET'''


def p_valuelist(p):
    '''valuelist : valuelist COMMA value
	             | value
	             | empty'''


def p_value(p):
    '''value : NUMBER
             | STRING
             | array
             | object
             | TRUE
             | FALSE
             | NULL'''


def p_empty(p):
    '''empty : '''
#
# Error rule
def p_error(p):
    #print("p_error in parser: Syntax error in input!")
    raise SyntaxError

# --- End parsing rules ---


# Leave this here; this generates a parser from the above rules

parser = yacc.yacc()


#####main function: need to call from cmd#####
try:
    file = open(sys.argv[1]).read()
    parser.parse(file)
    print("Success: parsed file")
except SyntaxError:
    print("SYNTAX Error: file is not properly formatted JSON")
except EOFError:
    print('EOF End of file error is raised')
except TypeError:
    print("TYPE Error: file is not properly formatted JSON")
except:
    print("ALL Error: file is not properly formatted JSON")

sys.exit(0)

