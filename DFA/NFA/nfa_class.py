from DFA.NFA.nfa_node import NFA_Node
from DFA.NFA.automaton_class import Automaton


class NFA(Automaton):
    def __init__(self):
        super().__init__()
        self.root = NFA_Node()
        self.sink = NFA_Node()
        self.states.add(self.root)
        self.states.add(self.sink)

    def add_edge(self, source: NFA_Node, target: NFA_Node, letter: str):
        self.states.add(source)
        self.states.add(target)
        self.alphabet.add(letter)

        if letter not in source.to.keys():
            source.to[letter] = set()
        source.to[letter].add(target)

    def delete_unreachable(self):
        queue = [self.root]
        used = {self.root}

        while len(queue) > 0:
            curr = queue.pop(0)

            for letter, neighbours in curr.to.items():
                for state in neighbours - used:
                    queue.append(state)
                    used.add(state)

        for state in self.states - used:
            self.states.remove(state)

    def eps_closure(self) -> list:
        transitions = []
        for state in self.states:
            for neighbour in state.by_eps:
                transitions.append([state, neighbour])
        return transitions

    def delete_epsilon_closure(self):
        while len(self.eps_closure()) > 0:
            transitions = self.eps_closure()
            for source, target in transitions:
                for t in target.terminal:
                    source.terminal.add(t)
                source.by_eps.remove(target)

                for to in target.by_eps:
                    source.by_eps.add(to)
                for letter, states in target.to.items():
                    for s in states:
                        self.add_edge(source, s, letter)

        self.delete_unreachable()

    def print(self):
        print("-----------------------------------------------------------------------------------")
        print("number of states:", len(self.states))
        for state in self.states:
            print("state number:", state)
            if state == self.root:
                print("start state")
            if state == self.sink:
                print("trash state")
            for letter, to in sorted(state.to.items()):
                print(f"by letter {letter} to: {[str(el) for el in to]}")
            print("epsilon closure:", [str(el) for el in state.by_eps])
            print()