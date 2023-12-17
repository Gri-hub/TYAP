from scanner.Table.alphabet import ALPHABET, category_of, KEY_WORDS, TOKENS
from scanner.lexem_class import Lexem
from scanner.Table.table_class import Table
import re


class Scaner:
    def __init__(self, table: Table, key_words=None):
        self.table = table
        self.key_words = key_words if key_words is not None else []
        self.lexems = []

    def move_in_table(self, block):
        if len(block) > 255:
            raise Exception("Only strings could be longer than 255 characters")

        curr_state = self.table.start
        value = ""
        curr_token = None

        for i in range(len(block)):
            letter = block[i]
            if category_of(letter) not in self.table[curr_state].keys() or self.table[curr_state][category_of(letter)] == self.table.error:
                if value == "":
                    raise Exception(f"Language doesn't support {block}")
                self.lexems.append(Lexem(curr_token[0], value))
                return block[i:]
            else:
                curr_state = self.table[curr_state][category_of(letter)]
                value += letter
                curr_token = list(curr_state.terminal)

        if len(value) < len(block):
            raise Exception(f"{block} is not recognised as valid token")

        if len(curr_token) != 1:
            print(curr_token)
            raise Exception(f"Scaner cannot find lexem for {block}")
        else:
            curr_token = curr_token[0]
        self.lexems.append(Lexem(curr_token, value))

    def scan_block(self, block: str):
        if block[0] == '0':
            raise Exception('Cant start with 0')

        elif block[0] == ' ':
            pass
        elif block[0] in ALPHABET['NUM']:
            num = 0
            for i in range(len(block)):
                if block[i] in ALPHABET['NUM']:
                    num = num * 10 + int(block[i])
                else:
                    self.lexems.append(Lexem(TOKENS.NUM.name, num))
                    return block[i:]
            next_word = self.lexems.append(Lexem(TOKENS.NUM.name, num))

            if next_word is not None:
                self.scan_block(next_word)

        elif block[0] == ALPHABET['QUOTE']:
            if block[-1] != ALPHABET['QUOTE']:
                raise Exception("No closing quote found")
            self.lexems.append(Lexem(TOKENS.STR.name, block[1:-1]))

        elif block in ['true', 'false']:
            self.read_bool(block)

        elif block in self.key_words:
            self.lexems.append(Lexem(TOKENS.KEYWORD.name, block))

        else:
            next_word = self.move_in_table(block)
            if next_word is not None:
                self.scan_block(next_word)

    def scan(self, text: str):
        block = re.split('(\".*?\")|\s+', text)
        block = [w for w in block if w is not None and w != '']

        i = 0
        while i < len(block):
            self.scan_block(block[i])
            i += 1

        lexems = self.lexems
        self.lexems = []
        return lexems
