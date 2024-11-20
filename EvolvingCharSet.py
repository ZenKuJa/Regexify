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
        return self.short

    def get_char_set(self) -> str:
        return self.chars

    def get_name(self) -> str:
        return self.name
