from CharSet import char_set

class regular_expression:
    reg_ex = ""
    length = 0

    def append(self, set: char_set, char: str, amount: int) -> None:
        self.length += 1 
        if amount <= 1:
            self.reg_ex += f"[{char}]"
        else: 
            self.reg_ex += f"{set.get_short()}{{{amount}}}"
    
    def to_str(self) -> str:
        return self.reg_ex