from CharSet import CharSet
from CharSetController import CharSetController
from RegEx import RegularExpression


class RegExGenerator:
    char_controller: CharSetController = None
    def __init__(self):
         self.char_controller = CharSetController()
         pass

    def generate(self, input_str: str) -> RegularExpression:
        reg_ex: RegularExpression = RegularExpression()
        group_length: int = 1
        for i, c in enumerate(input_str):
            current_charset: CharSet = self.char_controller.get_char_set(c)
            if i+1 >= len(input_str):
                prev_charset: CharSet = self.char_controller.get_char_set(input_str[i - 1])
                if current_charset == prev_charset:
                        reg_ex.append(current_charset, c, group_length)
                else:
                    reg_ex.append(current_charset, c, 1)
            else:
                next_charset: CharSet = self.char_controller.get_char_set(input_str[i + 1])
                same_set: bool = False
                if current_charset == next_charset:
                        group_length += 1
                else:
                    reg_ex.append(current_charset, c, group_length)
                    group_length = 1
                    
        return reg_ex