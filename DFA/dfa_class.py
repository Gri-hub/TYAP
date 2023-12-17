from DFA.NFA.automaton_class import Automaton
from DFA.dfa_node import DFA_Node


class DFA(Automaton):
    def __init__(self):
        super().__init__()
        self.root = DFA_Node()
        self.trap = DFA_Node()
        self.states.add(self.root)
        self.states.add(self.trap)

    def add_edge(self, source: DFA_Node, target: DFA_Node, letter: str):
        self.states.add(source)
        self.states.add(target)
        self.alphabet.add(letter)

        source.to[letter] = target

    def delete_unreachable(self):
        queue = [self.root]
        used = {self.root}

        while len(queue) > 0:
            curr = queue.pop(0)

            for letter, state in curr.to.items():
                if state not in used:
                    queue.append(state)
                    used.add(state)

        for state in self.states - used:
            self.states.remove(state)

    def make_determinated(self):
        for letter in self.alphabet:
            self.add_edge(self.trap, self.trap, letter)
        for state in self.states:
            for letter in self.alphabet:
                if letter not in state.to.keys():
                    if letter is not None:
                        self.add_edge(state, self.trap, letter)

    def merge_states(self, states_to_merge: set):
        new_state = DFA_Node()
        self.states.add(new_state)
        if self.root in states_to_merge:
            self.root = new_state

        for dfa_state in self.states:
            for key, value in dfa_state.to.items():
                if value in states_to_merge:
                    dfa_state.to[key] = new_state

        for state in states_to_merge:
            for key, value in state.to.items():
                if value in states_to_merge:
                    new_state.to[key] = new_state
                else:
                    new_state.to[key] = value

            for t in state.terminal:
                new_state.terminal.add(t)

            if state in self.states:
                self.states.remove(state)

    def minimize(self):
        equivalents = dict()
        for state1 in self.states:
            for state2 in self.states:
                if state1.to == state2.to and state1 != state2 and state1.terminal == state2.terminal:
                    if id(state1) in equivalents.keys():
                        equivalents[id(state1)].add(state2)
                    if id(state2) in equivalents.keys():
                        equivalents[id(state2)].add(state1)
                    else:
                        equivalents[id(state1)] = {state1, state2}

        for key, states in equivalents.items():
            self.merge_states(states)

    def print(self):
        print("-----------------------------------------------------------------------------------")
        print("number of states:", len(self.states))
        for state in self.states:
            print("state number:", state)
            if state == self.root:
                print("start state")
            if state == self.trap:
                print("trash state")
            for letter, to in sorted(state.to.items()):
                print(f"by letter {letter} to: {str(to)}", end="\n")
            print("\n")
