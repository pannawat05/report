from sly import Lexer,Parser

class CalcLexer(Lexer):
    tokens = {  PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, GT, LT, GTE, LTE, EQ, INC, DEC,ASSIGN }

    literals = { '+', '-', '*', '/','>','<','>=','<=','==','++', '--','(',')','=' }

    


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

    @_(r'\>')
    def GT(self, t):
        return t

    @_(r'\<')
    def LT(self, t):
        return t

    @_(r'\>=')
    def GTE(self, t):
        return t

    @_(r'\<=')
    def LTE(self, t):
        return t

    @_(r'\==')
    def EQ(self, t):
        return t

    @_(r'\+\+')
    def INC(self, t):
        return t

    @_(r'\--')
    def DEC(self, t):
        return t