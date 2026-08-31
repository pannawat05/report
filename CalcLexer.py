from sly import Lexer,Parser

class CalcLexer(Lexer):
    tokens = {  PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN }

    literals = { '+', '-', '*', '/' }

    


    @_(r'\+')
    def PLUS(self, t):
        return t

    @_(r'\-')
    def MINUS(self, t):
        return t

    @_(r'\*')
    def TIMES(self, t):
        return t

    @_(r'\/')
    def DIVIDE(self, t):
        return t

    @_(r'\(')
    def LPAREN(self, t):
        return t

    @_(r'\)')
    def RPAREN(self, t):
        return t

    # Ignore whitespace
    @_(r'\s+')
    def whitespace(self, t):
        pass