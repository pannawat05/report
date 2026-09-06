import sys
from pathlib import Path
from CalcLexer import CalcLexer
from IdentiInt import MiniLexer

# python main.py รันทุกไฟล์ใน folder 
# python main.py test1.txt test2.txt รันทุก file เแฑาะที่เป็น args  

def process_file(file_path, lexer):
    print(f"\n==================================================")
    print(f"  Processing File: {file_path}")
    print(f"==================================================")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        print(f"--- Input Content ---")
        print(content.strip())
        print(f"---------------------\n")

        # ส่งข้อความเข้า Lexer
        tokens = lexer.tokenize(content)

        print(f"--- Tokenized Output ---")
        print(f"{'TYPE':<15} | {'VALUE'}")
        print("-" * 35)

        for token in tokens:
            print(f"{token.type:<15} | {token.value}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Lexical Error / Exception: {e}")


def main():
    minilexer = MiniLexer()
    args = sys.argv[1:]

    if args:
        print("Mode: Processing specified files from command line")
        test_files = [Path(f) for f in args]
    else:
        print("Mode: Scanning all .txt files in current directory")
        test_files = list(Path(".").glob("*.txt"))

    if not test_files:
        print("No input files to process.")
        return

    for file_path in test_files:
        process_file(file_path, minilexer)

if __name__ == "__main__":
    main()