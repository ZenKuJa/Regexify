from EvolvingRegExGen.EvolvingCharSet import EvolvingCharSet
from EvolvingRegExGen.EvolvingRegExPart import EvolvingRegExPart


class EvolvingRegularExpression:
    reg_ex_structure: list[EvolvingRegExPart]
    reg_ex_operators: list[str]

    max_occurring_strings: int = 3
    max_occurring_chars: int = 7

    def __init__(self):
        self.reg_ex = ""
        self.reg_ex_structure = []
        self.reg_ex_operators = [
            ".", "*", "+", "?", "$", "|", "^", "\\", "-", "(", ")", "{", "}", "[", "]"
        ]

    def append(self, char_set: EvolvingCharSet, occurring_strings: list[str], min_amount: int, max_amount: int) -> None:
        new_reg_ex_part: EvolvingRegExPart = EvolvingRegExPart(list(set(occurring_strings)), char_set, min_amount, max_amount)
        self.reg_ex_structure.append(new_reg_ex_part)
    
    def to_str(self) -> str:
        return_str: str = ""
        str_occurring_chars: str = ""
        str_occurring_strings: list[str] = []
        str_short: str = ""
        str_min: int = 0
        str_max: int = 0

        for reg_ex_part in self.reg_ex_structure:
            # generate regEx char set
            str_occurring_chars = reg_ex_part.get_occurring_chars()
            str_occurring_strings = reg_ex_part.get_occurring_strings()
            str_short = reg_ex_part.get_char_set().get_short()
            str_min = reg_ex_part.get_min_length()
            str_max = reg_ex_part.get_max_length()

            if len(str_occurring_strings) == 1:
                str_short = str_occurring_strings[0]

                if str_short in self.reg_ex_operators:
                    return_str += f"+\\{str_short}"
                else:
                    return_str += f"+{str_short}"
                continue

            elif len(str_occurring_strings) <= self.max_occurring_strings:
                str_short = ""
                for i, occurring_string in enumerate(str_occurring_strings):
                    if i < len(str_occurring_strings) - 1:
                        str_short += f"{occurring_string}|"
                    else:
                        str_short += f"{occurring_string}"

                return_str += f"({str_short})"
                continue
            elif len(str_occurring_chars) <= self.max_occurring_chars:
                str_short = ""
                for c in str_occurring_chars:
                    str_short += c
            return_str += f"[{str_short}]"

            if str_min < str_max:
                return_str += f"{{{str_min},{str_max}}}"
            elif str_min > str_max:
                return_str += f"{{{str_max},{str_min}}}"
            elif str_min > 1:
                return_str += f"{{{str_max}}}"
            else:
                ...



            #return_str  = f"{return_str}[{str_short}]{{{str_min},{str_max}}}"

        return f"^{return_str}$"

    def get_reg_ex_parts(self) -> list[EvolvingRegExPart]:
        return self.reg_ex_structure

    def get_reg_ex_order(self) -> list[EvolvingCharSet]:
        reg_ex_order: list[EvolvingCharSet] = []
        for part in self.reg_ex_structure:
            reg_ex_order.append(part.get_char_set())

        return reg_ex_order
