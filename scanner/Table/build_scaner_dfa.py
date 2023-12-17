from DFA.dfa_class import DFA
from regex.nodes.binary_node import BinaryNode, RegexOperations
from regex.nodes.leaf_node import LeafNode
from DFA.NFA.regex_to_nfa import regex_to_nfa
from DFA.NFA.regex_blocks import union
from DFA.build_dfa import build_dfa_from_nfa
from scanner.Table.alphabet import ALPHABET


def build_regex_of_var_name() -> BinaryNode:
    letters = LeafNode()
    for letter in ALPHABET['STR']:
        letters = BinaryNode(letters, LeafNode(letter), RegexOperations.UNITE)
    regex = BinaryNode(letters, None, RegexOperations.CLOSURE)
    regex = BinaryNode(letters, regex, RegexOperations.CONCAT)
    return regex


TOKENS_TO_REGEX = {
    'VARNAME': build_regex_of_var_name(),
    'L_ROUND_BR': LeafNode(ALPHABET['L_ROUND_BR']),
    'R_ROUND_BR': LeafNode(ALPHABET['R_ROUND_BR']),
    'L_FIGURE_BR': LeafNode(ALPHABET['L_FIGURE_BR']),
    'R_FIGURE_BR': LeafNode(ALPHABET['R_FIGURE_BR']),
    'QUOTE': LeafNode(ALPHABET['QUOTE']),
    'SEMICOLON': LeafNode(ALPHABET['SEMICOLON']),
    'DOT': LeafNode(ALPHABET['DOT']),
    'EQUAL': BinaryNode(LeafNode(ALPHABET['ASSIGN']), LeafNode(ALPHABET['ASSIGN']), RegexOperations.CONCAT),
    'ASSIGN': LeafNode(ALPHABET['ASSIGN']),
    'PLUS': LeafNode(ALPHABET['PLUS']),
    'MINUS': LeafNode(ALPHABET['MINUS']),
    'STAR': LeafNode(ALPHABET['STAR']),
    'SLASH': LeafNode(ALPHABET['SLASH']),
    'NUM': None,
    'STR': None,
    'KEYWORD': None
}


def build_scaner_dfa() -> DFA:
    automatons = []
    for token, reg in TOKENS_TO_REGEX.items():
        if reg is not None:
            nfa = regex_to_nfa(reg)
            nfa.sink.make_terminal(token)
            automatons.append(nfa)

    final_nfa = union(automatons)
    final_dfa = build_dfa_from_nfa(final_nfa)
    return final_dfa