# string ignore escape sequences but doesnt take any actions!

#######################################
# IMPORTS
#######################################

import re

#######################################
# COUNT VARIABLES
#######################################

line = 1
count = 0
#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'
LETTERS = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
KEYWORDS = ['Move', 'Update', 'Delete', 'Insert', 'FIELD', 'RETURN_STATEMENT', 'JAVADOC', 'MODIFIER', 'BLOCK_COMMENT',
            'LINE_COMMENT', 'IF_STATEMENT', 'BLOCK_COMMENT', 'METHOD', 'SINGLE_TYPE', 'ASSIGNMENT', 'METHOD_INVOCATION']
TYPE = 'QWERTYUIOPASDFGHJKLZXCVBNM'


#######################################
# POSITION
#######################################

class Position:
    def __init__(self, idx, ln, col, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.ftxt)


#######################################
# TOKENS
#######################################

class Token:
    def __init__(self, type, token_string):
        self.type = type
        self.token_string = token_string

    def __repr__(self):
        if self.type == 'KEY':
            return f'{self.token_string}'
        return '.'


#######################################
# LEXER
#######################################

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = Position(-1, 0, -1, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        global line, count
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \n':
                line += 1
                self.advance()
            elif self.current_char in ' \t':
                self.advance()
            elif self.current_char in LETTERS:
                tokens.append(self.token_identifier())
            else:
                self.advance()
        return tokens

    def token_identifier(self):
        global count
        id_str = ''
        pos_start = self.pos.copy()

        while self.current_char is not None and self.current_char in LETTERS + DIGITS + '_'+'.'+'('+')'+':':
            id_str += self.current_char
            self.advance()

        tok_type = 'KEY' if id_str in KEYWORDS else 'NA'
        count += 1
        return id_str

#######################################
# RUN
#######################################

def run(text):
    print("HELLO")
    lexer = Lexer(text)
    tokens = lexer.make_tokens()
    return tokens
