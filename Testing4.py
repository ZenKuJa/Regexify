class char_set:

    name: str
    chars: str
    short: str

    def __init__(self, name: str, chars: str, short_name: str):
        
        self.name = name
        self.chars = chars
        self.short = short_name
        pass

    def get_short(self) -> str:
        return self.short

    def get_char_set(self) -> str:
        return self.chars

input_str: str = "Hello@welt.de"

lower_letter: char_set = char_set(name="lower_letter", chars= "abcdefghijklmnopqrstuvwxyz", short_name="[a-z]")
upper_letter: char_set = char_set(name= "upper_letter", chars= "ABCDEFGHIJKLMNOPQRSTUVWXYZ", short_name= "[A-Z]")
numbers: char_set = char_set(name= "numbers", chars= "0123456789", short_name="[0-9]")
punctuation: char_set = char_set(name= "punctuation", chars= ".,!?\";:", short_name="[.,!?\";:]")
special_chars: char_set = char_set(name="@/\\*#-_€", chars= "@/\\*#-_€", short_name= "[@/\\*#-_€]")

my_alphabet: list[char_set] = []

my_alphabet.append(lower_letter)
my_alphabet.append(upper_letter)
my_alphabet.append(numbers)
my_alphabet.append(punctuation)
my_alphabet.append(special_chars)

reg_ex: str = ""

group_length: int = 1
for i, c in enumerate(input_str, start=1):
    if c == input_str[i-1]:
        group_length += 1
    else:
        for set in my_alphabet:
            current_chars: str =set.get_char_set()
            if c in current_chars:
                print(c)
                reg_ex = f"{reg_ex}{set.get_short()}{{{group_length}}}"
        group_length = 1     

print(reg_ex)

