from sly import Lexer
import sys

class CommentHandling(Lexer):

	@_(r'//.*', r'/\*[\s\S]*?\*/')
	def comment_handler(self, t):
		self.lineno += t.value.count('\n')

	def error(self, t):
		print(f"Syntax/Lexical Error: Illegal character '{t.value[0]}' at line {self.lineno}")
		sys.exit(1)