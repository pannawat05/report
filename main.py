from CalcLexer import CalcLexer as operlexcer
from IdentiInt import MiniLexer as letterlexcer

lexer = operlexcer()
minilexer = letterlexcer()


while True:
    text = input('text > ')

    if not text:
        continue

    # แยก input เป็นส่วน ๆ ด้วย space
    parts = text.split()

    for part in parts:

        # ถ้าเป็น operator
        if part in ['+', '-', '*', '/', '=', '>', '<', '>=', '<=', '==', '!=', '++', '--', '(', ')']:
            tokens = lexer.tokenize(part)

            for token in tokens:
                print(f"Type: {token.type:<10} Value: {token.value}")

        # ถ้าเป็นตัวอักษรหรือตัวเลข
        else:
            token1 = minilexer.tokenize(part)

            for token in token1:
                print(f"Type: {token.type:<10} Value: {token.value}")