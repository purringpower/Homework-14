class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_letters(self):
        print(self.letters)

    def letters_num(self):
        letters_num = len(self.letters.split(' '))


class EngAlphabet(Alphabet):
    def __init__(self):
        Alphabet.__init__(self,
                          lang='En',
                          letters='a b c d e f g h i g k l m n o p q r s t y v w z w z')

    def is_en_letter(self, letter):
        if letter.lower() in self.letters:
            return True
        return False

    def letters_num(self):
        letters_num = len(self.letters.split(' '))
        print(letters_num)

    @staticmethod
    def example():
        print("Hello world!")


eng_alphabet = EngAlphabet()
eng_alphabet.print_letters()
eng_alphabet.letters_num()
print(eng_alphabet.is_en_letter('F'))
eng_alphabet.example()
