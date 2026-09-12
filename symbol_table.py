class SymbolTable:
    def __init__(self):
        self.symbols = set()

    def check_and_add(self, identifier: str) -> str:
        # Check if identifier is in the symbol table and add it if not.
        if identifier in self.symbols:
            return "already in symbol table"
        else:
            self.symbols.add(identifier)
            return "new identifier"

    def get_all_symbols(self):
        # return all symbols
        return sorted(list(self.symbols))


# Testing
if __name__ == "__main__":
    table = SymbolTable()
    
    test_tokens = ["x", "total", "x", "count", "total", "y"]
    
    for token in test_tokens:
        status = table.check_and_add(token)
        print(f"Token: {token:<8} -> {status}")
        
    print("\nAll Identifiers in Symbol Table:", table.get_all_symbols())