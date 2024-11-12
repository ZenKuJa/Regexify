
from CharSet import CharSet

class CharSetController:
    lower_letter: CharSet = CharSet(name="lower_letter", chars="abcdefghijklmnopqrstuvwxyz", short_name="[a-z]")
    upper_letter: CharSet = CharSet(name="upper_letter", chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ", short_name="[A-Z]")
    numbers: CharSet = CharSet(name="numbers", chars="0123456789", short_name="[0-9]")
    punctuation: CharSet = CharSet(name="punctuation", chars="., !?\";:", short_name="[., !?\";:]")
    special_chars: CharSet = CharSet(name="@/\\*#-_€", chars="@/\\*#-_€", short_name="[@/\\*#-_€]")

    my_alphabet: list[CharSet] = [lower_letter, upper_letter, numbers, punctuation, special_chars]

    def get_char_set(self, char: str) -> CharSet | None:
        found: bool = False
        for char_set in self.my_alphabet:
            if char in char_set.get_char_set():
                found = True
                return char_set
        if not found:
            return None