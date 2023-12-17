from DFA.NFA.nfa_class import NFA
from DFA.NFA.regex_blocks import closure_automaton, concatenate, union
from regex.nodes.binary_node import BinaryNode, RegexOperations
from regex.nodes.leaf_node import LeafNode
from regex.nodes.regex_node import RegexNode


def leaf_to_nfa(regex: LeafNode) -> NFA:
    nfa = NFA()
    nfa.add_edge(nfa.root, nfa.sink, regex.letter)
    return nfa


def binary_to_nfa(regex: BinaryNode) -> NFA:
    automatons = regexps_to_automatons([regex.exp1, regex.exp2])

    if regex.operation == RegexOperations.CLOSURE:
        return closure_automaton(automatons[0])

    elif regex.operation == RegexOperations.UNITE:
        return union(automatons)

    elif regex.operation == RegexOperations.CONCAT:
        return concatenate(automatons)


def regexps_to_automatons(regexps: list[RegexNode]) -> list[NFA]:
    ans = []
    for reg in regexps:
        if reg is not None:
            nfa = regex_to_nfa(reg)
            ans.append(nfa)
    return ans


def regex_to_nfa(regex: RegexNode, terminal=None):
    if isinstance(regex, LeafNode):
        nfa = leaf_to_nfa(regex)
    else:
        nfa = binary_to_nfa(regex)
    if terminal is not None:
        nfa.sink.make_terminal(terminal)
    return nfa
