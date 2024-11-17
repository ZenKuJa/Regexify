from typing import Union

from CharSet import CharSet
from RegExPart import RegExPart


class RegularExpression:
    reg_ex_structure: list[RegExPart]

    def __init__(self):
        self.reg_ex = ""
        self.reg_ex_structure = []

    def append(self, occurring_strings: list[str], char_set: CharSet, min_amount: int, max_amount: int) -> None:
        new_reg_ex_part: RegExPart = RegExPart(occurring_strings, char_set, min_amount, max_amount)
        self.reg_ex_structure.append(new_reg_ex_part)

    def to_str(self) -> str:
        return_str: str = ""
        str_occurring_chars: str = ""
        str_short: str = ""
        str_min: int = 0
        str_max: int = 0

        for reg_ex_part in self.reg_ex_structure:
            # generate regEx char set
            str_occurring_chars = reg_ex_part.get_occurring_chars()
            str_short = reg_ex_part.get_char_set().get_short()
            str_min = reg_ex_part.get_min_length()
            str_max = reg_ex_part.get_max_length()

            if len(str_occurring_chars) <= 5:
                str_short = ""
                for c in str_occurring_chars:
                    str_short += c
            return_str = f"{return_str}[{str_short}]"

            if str_min < str_max:
                return_str = f"{return_str}{{{str_min},{str_max}}}"
            elif str_min > str_max:
                return_str = f"{return_str}{{{str_max},{str_min}}}"
            elif str_min > 1:
                return_str = f"{return_str}{{{str_max}}}"
            else:
                ...


        return return_str

    def get_reg_ex_parts(self) -> list[RegExPart]:
        return self.reg_ex_structure

    def get_reg_ex_order(self) -> list[CharSet]:
        reg_ex_order: list[CharSet] = []
        for reg_ex_part in self.reg_ex_structure:
            reg_ex_order.append(reg_ex_part.get_char_set())
        return reg_ex_order
