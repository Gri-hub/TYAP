from DFA.dfa_class import DFA
from DFA.NFA.nfa_class import NFA
from DFA.nfa_to_dfa import nfa_to_dfa
from DFA.NFA.regex_to_nfa import regex_to_nfa
from regex.nodes.regex_node import RegexNode


def build_dfa_from_regex(regex: RegexNode, terminal=None) -> DFA:
    nfa = regex_to_nfa(regex, terminal)
    return build_dfa_from_nfa(nfa)


def build_dfa_from_nfa(nfa: NFA) -> DFA:
    dfa = nfa_to_dfa(nfa)
    dfa.minimize()
    dfa.delete_unreachable()
    dfa.make_determinated()
    return dfa
