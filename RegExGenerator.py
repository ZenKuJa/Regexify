from typing import Union

from CharSet import CharSet
from CharSetController import CharSetController
from RegEx import RegularExpression


class RegExGenerator:
    char_controller: CharSetController
    def __init__(self):
         self.char_controller = CharSetController()
         pass

    def generate(self, input_str: str) -> RegularExpression:
        reg_ex: RegularExpression = RegularExpression()
        group_length: int = 1
        occurring_chars: str = ""
        for i, c in enumerate(input_str):
            occurring_chars += c
            current_charset: CharSet = self.char_controller.get_char_set(c)

            #last char
            if i+1 >= len(input_str):
                prev_charset: CharSet = self.char_controller.get_char_set(input_str[i - 1])
                if current_charset == prev_charset:
                    reg_ex.append(current_charset, [occurring_chars], min_amount=group_length, max_amount=group_length)
                else:
                    reg_ex.append(current_charset, [occurring_chars], 1, max_amount=1)
            # next char exists
            else:
                next_charset: CharSet = self.char_controller.get_char_set(input_str[i + 1])
                same_set: bool = False
                if current_charset == next_charset:
                        group_length += 1
                else:
                    reg_ex.append(current_charset, [occurring_chars], min_amount=group_length, max_amount=group_length)
                    occurring_chars = ""
                    group_length = 1
        return reg_ex

    def generate_list(self, str_list: list[str]) -> list[RegularExpression]:
        output_list: list[RegularExpression] = []
        for _str in str_list:
            output_list.append(self.generate(_str))
        return output_list



    def merge_2_reg_ex(self, reg_ex_1: RegularExpression, reg_ex_2: RegularExpression) -> RegularExpression | None:
        new_reg_ex: RegularExpression = RegularExpression()

        if reg_ex_1.get_reg_ex_order() ==  reg_ex_2.get_reg_ex_order():
            new_reg_ex: RegularExpression = RegularExpression()
            for re_part_1, re_part_2 in zip(reg_ex_1.get_reg_ex_parts(), reg_ex_2.get_reg_ex_parts()):
                char_set: CharSet = re_part_1.get_char_set()
                occurring_strings: list[str] = re_part_1.get_occurring_strings() + (re_part_2.get_occurring_strings())
                min_amount: int = min(re_part_1.get_min_length(), re_part_2.get_min_length())
                max_amount: int = max(re_part_1.get_max_length(), re_part_2.get_max_length())

                new_reg_ex.append(char_set, occurring_strings, min_amount, max_amount)

            return new_reg_ex
        else:
            print("regular expressions follow a different structure")
            return None

    def merge_reg_ex_list(self, reg_ex_list: list[RegularExpression]) -> RegularExpression | None:
        new_reg_ex: RegularExpression = reg_ex_list[0]
        for reg_ex in reg_ex_list[1:]:
            output = self.merge_2_reg_ex(new_reg_ex, reg_ex)
            if output is not None:
                new_reg_ex: RegularExpression = output
            else:
                return None

        return new_reg_ex