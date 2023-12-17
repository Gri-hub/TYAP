from DFA.NFA.node import AutomatonNode


class DFA_Node(AutomatonNode):
    def __init__(self, nfa_nodes_set=None):
        super().__init__()

        if nfa_nodes_set is not None:
            for node in nfa_nodes_set:
                for token in node.terminal:
                    self.terminal.add(token)

    def To(self, letter: str) -> AutomatonNode:
        return self.to[letter]

    def accept(self, visitor):
        return self.terminal


