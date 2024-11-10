class RegExGenerator:
    def get_reg_ex_list_for(self, in_str: str) -> list[str]:
        reg_ex_list: list[str] = []

        for letter in in_str:
            if letter.islower():
                reg_ex_list.append("[a-z]")
            elif letter.isupper():
                reg_ex_list.append("[A-Z]")
            elif letter.isnumeric():
                reg_ex_list.append("[0-9]")
            else:
                reg_ex_list.append("unknown")

        return reg_ex_list


