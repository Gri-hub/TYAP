class Lexem:
    def __init__(self, token, value=None) -> None:
        self.token = token
        self.value = value

    def __str__(self):
        return f"{self.token}({self.value})"

def print_lexems(lexems: list):
    for lexem in lexems:
        print(lexem, end="\n" if lexem.value in [";", "{", "}"] else " ")
        if lexem.value == "{":
            print("", end="\t")
    print("\n")