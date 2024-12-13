from EvolvingRegExGen.EvolvingCharSet import EvolvingCharSet


class EvolvingRegExPart:

    occurring_strings: list[str]
    char_set: EvolvingCharSet
    min_length: int
    max_length: int

    def __init__(self, occurring_strings: list[str], char_set: EvolvingCharSet, min_length: int, max_length: int) -> None:
        self.occurring_strings = occurring_strings
        self.char_set = char_set
        self.min_length = min_length
        self.max_length = max_length

    def set_occurring_strings(self, occurring_strings: list[str]) -> None:
        """Sets the occurring_strings list of this RegExPart."""
        self.occurring_strings = occurring_strings

    def set_char_set(self, char_set: EvolvingCharSet) -> None:
        """Sets the char_set of this RegExPart."""
        self.char_set = char_set

    def set_min_length(self, min_length: int) -> None:
        """Sets the min_length of this RegExPart."""
        self.min_length = min_length

    def set_max_length(self, max_length: int) -> None:
        """Sets the max_length of this RegExPart."""
        self.max_length = max_length

    def get_occurring_strings(self) -> list[str]:
        """Returns the occurring strings of this RegExPart."""
        return self.occurring_strings

    def get_occurring_chars(self) -> str:
        """Returns the occurring chars of this RegExPart."""
        occurring_chars = "".join(sorted(set(self.occurring_strings)))
        return occurring_chars

    def get_char_set(self) -> EvolvingCharSet:
        """Returns the char_set of this RegExPart."""
        return self.char_set

    def get_min_length(self) -> int:
        """Returns the min_length of this RegExPart."""
        return self.min_length

    def get_max_length(self) -> int:
        """Returns the max_length of this RegExPart."""
        return self.max_length
