from typing import Union

from CharSet import CharSet

class RegularExpression:
    reg_ex_structure: list[dict[str, Union[CharSet, str, int]]]

    def __init__(self):
        self.reg_ex = ""
        self.reg_ex_structure = []

    def append(self, char_set: CharSet, occurring_chars: str, min_amount: int, max_amount: int) -> None:
        new_reg_ex_part: dict[str, Union[CharSet, str, int]] = {
            "char_set": char_set,
            "occurring_chars": "".join(sorted(set(occurring_chars))),
            "min": min_amount,
            "max": max_amount
        }
        self.reg_ex_structure.append(new_reg_ex_part)
    
    def to_str(self) -> str:
        return_str: str = ""
        str_occurring_chars: str = ""
        str_short: str = ""
        str_min: int = 0
        str_max: int = 0

        for reg_ex_part in self.reg_ex_structure:
            # generate regEx char set
            str_occurring_chars = reg_ex_part["occurring_chars"]
            str_short = reg_ex_part["char_set"].get_short()
            str_min = reg_ex_part["min"]
            str_max = reg_ex_part["max"]

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



            #return_str  = f"{return_str}[{str_short}]{{{str_min},{str_max}}}"

        return return_str

    def get_reg_ex_parts(self) -> list[dict[str, Union[CharSet, str, int]]]:
        return self.reg_ex_structure

    def get_reg_ex_order(self) -> list[CharSet]:
        reg_ex_order: list[CharSet] = []
        for part in self.reg_ex_structure:
            reg_ex_order.append(part["char_set"])

        return reg_ex_order


