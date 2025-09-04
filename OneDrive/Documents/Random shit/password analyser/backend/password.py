class Password:
    def __init__(self, password):
        self.password = password
        self.length = len(password)
        self.char_password = list(password)
        self.uppers = 0
        self.numbers = 0
        self.symbols = 0

    def get_password(self):
        return self.password
    
    def get_length(self):
        return self.length
    
    def get_uppers(self):
        return self.uppers
    
    def get_numbers(self):
        return self.numbers

    def get_symbols(self):
        return self.symbols
    
    def update_characteristics(self):
        self.uppers = 0
        self.numbers = 0
        self.symbols = 0

        for char in self.password:
            if char.isupper():
                self.uppers += 1
            if char.isnumeric():
                self.numbers += 1
            if not char.isalnum():
                self.symbols += 1
