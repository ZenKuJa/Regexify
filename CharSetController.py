
from CharSet import char_set

class char_set_controller:
    lower_letter: char_set = char_set(name="lower_letter", chars= "abcdefghijklmnopqrstuvwxyz", short_name="[a-z]")
    upper_letter: char_set = char_set(name= "upper_letter", chars= "ABCDEFGHIJKLMNOPQRSTUVWXYZ", short_name= "[A-Z]")
    numbers: char_set = char_set(name= "numbers", chars= "0123456789", short_name="[0-9]")
    punctuation: char_set = char_set(name= "punctuation", chars= "., !?\";:", short_name="[., !?\";:]")
    special_chars: char_set = char_set(name="@/\\*#-_€", chars= "@/\\*#-_€", short_name= "[@/\\*#-_€]")

    my_alphabet: list[char_set] = []

    my_alphabet.append(lower_letter)
    my_alphabet.append(upper_letter)
    my_alphabet.append(numbers)
    my_alphabet.append(punctuation)
    my_alphabet.append(special_chars)

    

    def get_char_set(self, char: str) -> char_set:
        found: bool = False
        for set in self.my_alphabet:
            if char in set.get_char_set():
                found = True
                return set
        if not found:
            return None