from CharSet import CharSet

class RegularExpression:
    reg_ex = ""
    length = 0

    def append(self, char_set: CharSet, char: str, amount: int) -> None:
        self.length += 1 
        if amount <= 1:
            self.reg_ex += f"[{char}]"
        else: 
            self.reg_ex += f"{char_set.get_short()}{{{amount}}}"
    
    def to_str(self) -> str:
        return self.reg_ex