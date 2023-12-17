from DFA.dfa_class import DFA
from DFA.NFA.nfa_class import NFA
from DFA.dfa_node import DFA_Node
from DFA.NFA.nfa_node import NFA_Node


def nfa_to_dfa(nfa: NFA) -> DFA:
    nfa.delete_epsilon_closure()

    dfa_nodes = []
    transitions = dict()

    queue = [frozenset([nfa.root])]
    dfa_nodes.append(frozenset([nfa.root]))
    used = set()
    dfa = DFA()

    while len(queue) > 0:
        curr_state = queue.pop(0)
        letters = get_alphabet(dfa, curr_state)

        for letter in letters:
            next_state = frozenset(get_transition(curr_state, letter))
            if curr_state not in transitions.keys():
                transitions[curr_state] = dict()
            transitions[curr_state][letter] = next_state

            if next_state not in used:
                queue.append(next_state)
                used.add(next_state)
                dfa_nodes.append(next_state)

    equivalent = dict()
    for node in dfa_nodes:
        if nfa.root in node:
            dfa.root = DFA_Node(node)
            equivalent[node] = dfa.root
        else:
            new_node = DFA_Node(node)
            dfa.states.add(new_node)
            equivalent[node] = new_node

        for n in node:
            for t in n.terminal:
                equivalent[node].terminal.add(t)

    for source, letter_transitions in transitions.items():
        for letter, target in letter_transitions.items():
            dfa.add_edge(equivalent[source], equivalent[transitions[source][letter]], letter)

    dfa.delete_unreachable()
    return dfa


def get_transition(source: set[NFA_Node], letter: str) -> set[NFA_Node]:
    move = set()
    for node in source:
        if letter in node.to.keys():
            for neighbour in node.to[letter]:
                move.add(neighbour)

    return move


def get_alphabet(dfa: DFA, curr_state) -> set:
    letters = set()
    for vert in curr_state:
        for letter in vert.to.keys():
            if letter is not None:
                letters.add(letter)
                dfa.alphabet.add(letter)
    return letters