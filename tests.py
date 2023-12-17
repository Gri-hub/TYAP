from DFA.build_dfa import \
    build_dfa_from_regex
from DFA.NFA.regex_to_nfa import regex_to_nfa
from regex.nodes.binary_node import BinaryNode, RegexOperations
from regex.nodes.leaf_node import LeafNode


def test_regex_to_mdfa():
    ############# TEST 1 #############
    a = LeafNode('a')
    b = LeafNode('b')
    c = LeafNode('c')
    ab = BinaryNode(a, b, RegexOperations.UNITE)
    abc = BinaryNode(ab, c, RegexOperations.UNITE)
    ac = BinaryNode(a, c, RegexOperations.CONCAT)
    ab_cl = BinaryNode(ab, None, RegexOperations.CLOSURE)

    nfa = regex_to_nfa(ab_cl, "ab_cl")
    print(f"NFA for {ab_cl}")
    nfa.print()
    print("\n")

    ############# TEST 2 #############
    dfa = build_dfa_from_regex(ab_cl, str(ab_cl))
    print(f"DFA for {ab_cl}")
    dfa.print()

    ############# TEST 3 #############
    ac_cl = BinaryNode(ac, None, RegexOperations.CLOSURE)
    ab_cl_plus_ac_cl = BinaryNode(ab_cl, ac_cl, RegexOperations.UNITE)
    ab_cl_plus_ac_cl_cl = BinaryNode(ab_cl_plus_ac_cl, None, RegexOperations.CLOSURE)

    print(f"DFA for {ab_cl_plus_ac_cl_cl}")
    dfa = build_dfa_from_regex(ab_cl_plus_ac_cl_cl, str(ab_cl_plus_ac_cl_cl))
    dfa.print()
