from CharSet import char_set
from CharSetController import char_set_controller
from RegEx import regular_expression


class regular_expression_generator:
    char_controller: char_set_controller = None
    def __init__(self):
         self.char_controller = char_set_controller()
         pass

    def generate(self, input_str: str) -> regular_expression:
        reg_ex: regular_expression = regular_expression()
        group_length: int = 1
        for i, c in enumerate(input_str):
            current_charset: char_set = self.char_controller.get_char_set(c)
            if i+1 >= len(input_str):
                prev_charset: char_set = self.char_controller.get_char_set(input_str[i-1])
                if current_charset == prev_charset:
                        reg_ex.append(current_charset, c, group_length)
                else:
                    reg_ex.append(current_charset, c, 1)
            else:
                next_charset: char_set = self.char_controller.get_char_set(input_str[i+1])
                same_set: bool = False
                if current_charset == next_charset:
                        group_length += 1
                else:
                    reg_ex.append(current_charset, c, group_length)
                    group_length = 1
                    
        return reg_ex

