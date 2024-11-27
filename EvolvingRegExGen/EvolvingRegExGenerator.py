import logging
from EvolvingRegExGen.EvolvingCharSet import EvolvingCharSet
from EvolvingRegExGen.EvolvingCharSetController import EvolvingCharSetController
from EvolvingRegExGen.EvolvingRegEx import EvolvingRegularExpression


class EvolvingRegExGenerator:
    char_controller: EvolvingCharSetController
    def __init__(self):
         self.char_controller = EvolvingCharSetController()
         pass

    def generate(self, input_str: str) -> EvolvingRegularExpression:
        """Takes an input string and generates the corresponding RegularExpression object"""
        reg_ex: EvolvingRegularExpression = EvolvingRegularExpression()
        group_length: int = 1
        occurring_chars: str = ""
        for i, c in enumerate(input_str):
            occurring_chars += c
            current_charset: EvolvingCharSet = self.char_controller.get_char_set(c)

            #last char
            if i+1 >= len(input_str):
                prev_charset: EvolvingCharSet = self.char_controller.get_char_set(input_str[i - 1])
                if current_charset == prev_charset:
                    reg_ex.append(current_charset, [occurring_chars], min_amount=group_length, max_amount=group_length)
                else:
                    reg_ex.append(current_charset, [occurring_chars], 1, max_amount=1)
            # next char exists
            else:
                next_charset: EvolvingCharSet = self.char_controller.get_char_set(input_str[i + 1])
                same_set: bool = False
                if current_charset == next_charset:
                        group_length += 1
                else:
                    reg_ex.append(current_charset, [occurring_chars], min_amount=group_length, max_amount=group_length)
                    occurring_chars = ""
                    group_length = 1
        return reg_ex

    def generate_list(self, str_list: list[str]) -> list[EvolvingRegularExpression]:
        """Takes a list of type string and generates the corresponding RegularExpression object for each string.
        Returns a list containing the RegularExpression objects in the same order as the input list."""
        output_list: list[EvolvingRegularExpression] = []
        for _str in str_list:
            output_list.append(self.generate(_str))
        return output_list


    def merge_2_reg_ex(self, reg_ex_1: EvolvingRegularExpression, reg_ex_2: EvolvingRegularExpression) -> EvolvingRegularExpression | None:
        """Takes two RegularExpression objects, combines them and returns a RegularExpression object that describes the given RegularExpressions.
        If they don't follow the same CharSet order, none is returned"""
        new_reg_ex: EvolvingRegularExpression = EvolvingRegularExpression()

        if reg_ex_1.get_reg_ex_order() ==  reg_ex_2.get_reg_ex_order():
            new_reg_ex: EvolvingRegularExpression = EvolvingRegularExpression()
            for re_part_1, re_part_2 in zip(reg_ex_1.get_reg_ex_parts(), reg_ex_2.get_reg_ex_parts()):
                char_set: EvolvingCharSet = re_part_1.get_char_set()
                occurring_strings: list[str] = re_part_1.get_occurring_strings() + (re_part_2.get_occurring_strings())
                min_amount: int = min(re_part_1.get_min_length(), re_part_2.get_min_length())
                max_amount: int = max(re_part_1.get_max_length(), re_part_2.get_max_length())

                new_reg_ex.append(char_set, occurring_strings, min_amount, max_amount)

            return new_reg_ex
        else:
            return None

    def merge_reg_ex_list(self, reg_ex_list: list[EvolvingRegularExpression]) -> EvolvingRegularExpression | None:
        """Takes a list of type RegularExpression and returns a RegularExpression object that describes all contained RegularExpressions.
        If they don't follow the same CharSet order, none is returned."""
        new_reg_ex: EvolvingRegularExpression = reg_ex_list[0]
        for reg_ex in reg_ex_list[1:]:
            output = self.merge_2_reg_ex(new_reg_ex, reg_ex)
            if output is not None:
                new_reg_ex: EvolvingRegularExpression = output
            else:
                return None

        return new_reg_ex