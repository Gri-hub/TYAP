from scanner.scaner_class import Scaner
from scanner.lexem_class import print_lexems
from scanner.Table.table_class import Table


def test_scaner():
    table = Table()
    scaner = Scaner(table)

    ############# simple test ################
    print('---------------------------------------------------------')
    lexems = scaner.scan('1224235 "hello world!"')
    print_lexems(lexems)

    ################### codestyle test #######################
    print('---------------------------------------------------------')
    lexems = scaner.scan('a = 20; b= "hello world!"; if c == 16 { a= 6;} else {2+2;}')
    print_lexems(lexems)

    ################ == not interpreted as = and = ################
    print('---------------------------------------------------------')
    lexems = scaner.scan('a = 2')
    print_lexems(lexems)
    lexems = scaner.scan('a == 20')
    print_lexems(lexems)

    ################### subwords #####################
    print('---------------------------------------------------------')
    lexems = scaner.scan('aif = 20; ifandelse = 10')
    print_lexems(lexems)

