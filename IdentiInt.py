import sys
from sly import Lexer

class MiniLexer(Lexer):
    tokens = {INT, ID, IF, THEN, ELSE, ENDIF, WHILE, DO, ENDWHILE, PRINT, NEWLINE, READ}
    
    keywords = {'if', 'then', 'else', 'endif','while', 'do', 'endwhile', 'print', 'newline', 'read'}
    
    @_(r'\d+')
    def INT(self, t):
        t.value = int(t.value)
        return t
    
    @_(r'[a-zA-Z][a-zA-Z0-9]*')
    def ID(self, t):
        if t.value in self.keywords:
            t.type = t.value.upper()
        return t
    
    ignore = ' \t'
    
    def error(self, t):
        print(f"Lexical error: unexpected character '{t.value[0]}'")
        sys.exit(1)
        
# if __name__ == '__main__':
#     lexer = MiniLexer()
#     text = "score 123 student123 if If 0"
    
#     print("------ Lexical Analysis ---")
#     for tok in lexer.tokenize(text):
#         print(f"Type: {tok.type:<10} Value: {tok.value}")
