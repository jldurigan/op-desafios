import re

regex = re.compile(r'^[A-Z ]{1,16}$')

expressao = input('digite uma expressão de até 16 caracteres. obs: só serão aceitas letras, sem acentuação ou pontuação\n')
expressao = expressao.upper()

if not regex.fullmatch(expressao):
    print("Expressão inválida")
else:
    print("Expressão válida")