from sly import Lexer
import sys

class CommentHandling(Lexer):
	tokens = set()
	ignore = ' \t\n'

	@_(r'//.*', r'/\*[\s\S]*?\*/')
	def comment_handler(self, t):
		self.lineno += t.value.count('\n')

	def error(self, t):
		print(f"Syntax/Lexical Error: Illegal character '{t.value[0]}' at line {self.lineno}")
		sys.exit(1)


from pathlib import Path
def main():
	args = sys.argv[1:]

	# อ่านไฟล์หากระบุ Argument หรือใช้ ข้อความทดสอบ หากไม่ได้ระบุไฟล์
	if args:
		filepath = Path(args[0])
		if not filepath.is_file():
			print(f"Error: ไม่พบไฟล์ '{filepath}'")
			sys.exit(1)
		code = filepath.read_text(encoding='utf-8')
	else:
		print("[Notice] ไม่ได้ระบุไฟล์ -> ใช้ข้อความทดสอบอัตโนมัติ\n")
		code = """
		// 1. Single-line comment
		/* 2. Block comment
		   แบบหลายบรรทัด */
		# 3. Another single-line comment
		x = 10  // Assign 10 to x
		y = 20
		"""

	# รัน Lexer
	lexer = CommentHandling()
	tokens = list(lexer.tokenize(code))

	print("=== ผลการตัด Token (ข้าม Comment) ===")
	for tok in tokens:
		print(f"Line {tok.lineno} | Type: {tok.type:<10} | Value: {tok.value}")
	
	print(f"\nประมวลผลสำเร็จ: พบทั้งหมด {len(tokens)} Tokens")

main()