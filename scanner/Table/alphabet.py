from enum import Enum

ALPHABET = {
    'STR': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'NUM': '0123456789',
    'L_ROUND_BR': '(',
    'R_ROUND_BR': ')',
    'L_FIGURE_BR': '{',
    'R_FIGURE_BR': '}',
    'QUOTE': '"',
    'SEMICOLON': ';',
    'DOT': '.',
    'PLUS': '+',
    'MINUS': '-',
    'STAR': '*',
    'SLASH': '/',
    'UNDERSCORE': '_',
    'ASSIGN': '=',
    'EQUAL': '==',
}

KEY_WORDS = [
    'if',
    'else',
    'for',
    'while'
]

class TOKENS(Enum):
    L_ROUND_BR = "L_ROUND_BR"
    R_ROUND_BR = "R_ROUND_BR"
    L_FIGURE_BR = "L_FIGURE_BR"
    R_FIGURE_BR = "R_FIGURE_BR"
    QUOTE = "QUOTE"
    SEMICOLON = "SEMICOLON"
    DOT = "DOT"
    UNDERSCORE = "UNDERSCORE"
    VARNAME = "VARNAME"
    STR = "STR"
    NUM = "NUM"
    KEYWORD = "KEYWORD"
    ASSIGN = "ASSIGN"
    EQUAL = "EQUAL"
    PLUS = "PLUS"
    MINUS = "MINUS"
    STAR = "STAR"
    SLASH = "SLASH"

def category_of(letter: str):
    for category, token in ALPHABET.items():
        if letter in token:
            return category
