from scanner.Table.alphabet import category_of
from scanner.Table.build_scaner_dfa import build_scaner_dfa


class Table:
    def __init__(self) -> None:
        self.dfa = build_scaner_dfa()
        self.table = {}
        self.error = self.dfa.trap
        self.start = None
        self.error = None
        self.complete_table()

    def complete_table(self):
        for state in self.dfa.states:
            if state == self.dfa.root:
                self.start = state
            elif state == self.dfa.trap:
                self.error = self.dfa.trap

            self.table[state] = {}
            for letter in self.dfa.alphabet:
                self.table[state][category_of(letter)] = state.To(letter)

    def __getitem__(self, state):
        return self.table[state]
