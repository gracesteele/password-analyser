from password import Password

MIN_PASSWORD_LEN = 8

class PasswordChecker:

    def __init__(self, password):
        self.password = Password(password)
        self.password.update_characteristics()
        self.score = 0
        self.excess = 0

    def get_score(self):
        self.calc_complexity()
        return self.score

    def check_repetition(self):
        pass

    def update_excess(self):
        if self.password.get_length() >= MIN_PASSWORD_LEN:
            self.score += 50
            self.excess = self.password.get_length() - MIN_PASSWORD_LEN

    def analyse_password(self):
        if self.password.get_numbers() > 0 and self.password.get_uppers() > 0 and self.password.get_symbols() > 0:
            self.score += 25
        elif self.password.get_numbers() > 0 or self.password.get_uppers() > 0 or self.password.get_symbols() > 0:
            self.score += 15
        
        if self.password.get_password().islower():
            self.score -= 15

        if self.password.get_password().isdigit():
            self.score -= 35

    def calc_complexity(self):
        self.update_excess()
        self.analyse_password()

        self.score += self.excess * 3 + self.password.get_numbers() * 5 + self.password.get_uppers() * 4 + self.password.get_symbols() * 5
