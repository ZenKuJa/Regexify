class EvolvingCharSet:
    name: str
    chars: str
    short: str

    def __init__(self, name: str, chars: str, short_name: str):
        self.name = name
        self.chars = chars
        self.short = short_name
        pass

    def get_short(self) -> str:
        """Returns the short form of this set as string"""
        return self.short

    def get_char_set(self) -> str:
        """Returns all chars included by this set as string"""
        return self.chars

    def get_name(self) -> str:
        """Returns the written name of this set as string"""
        return self.name
