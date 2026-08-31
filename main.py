from CalcLexer import CalcLexer
from IdentiInt import MiniLexer
lexer = CalcLexer()
minilexer = MiniLexer()

while True:
    # text = input('calc > ')

    # if text:
    #     tokens = lexer.tokenize(text)

    #     for token in tokens:
    #         print(token)

    text = input('mini > ')
    if text:
        tokens = minilexer.tokenize(text)
        for token in tokens:
             print(f"Type: {token.type:<10} Value: {token.value}")
