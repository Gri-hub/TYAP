from DFA.NFA.node import AutomatonNode


class Automaton:
    def __init__(self, alphabet=None):
        self.root = AutomatonNode()
        self.states = set()
        self.alphabet = alphabet if alphabet is not None else set()

    def combine(self, automatons: list):
        for automaton in automatons:
            for state in automaton.states:
                self.states.add(state)