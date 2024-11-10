class MyRegEx:

    str_up_to_date: bool = False
    reg_ex_str: str = ""
    reg_ex_list: list[str] = []

    def generate_reg_ex_str(self) -> str:
        new_reg_ex_str: str = ""
        reg_ex_list: list[str] = self.reg_ex_list

        prev_expression: str = None
        expression_amount: int = 0
        finished: bool = False

        for expression in reg_ex_list:
            finished = False
            if prev_expression == None:
                prev_expression = expression
                expression_amount += 1
            elif prev_expression == expression:
                expression_amount += 1
            else:
                new_reg_ex_str = f"{new_reg_ex_str}{prev_expression}{{{expression_amount}}}"
                prev_expression = expression
                expression_amount = 1
                prev_expression = None
                finished = True

        if finished: 
            return new_reg_ex_str
        else:
            new_reg_ex_str = f"{new_reg_ex_str}{prev_expression}{{{expression_amount}}}"
            return new_reg_ex_str

    def get_reg_ex_string(self) -> str:
        if self.str_up_to_date:
            return self.reg_ex_str
        else:
            self.reg_ex_str = ""
            self.reg_ex_str = self.generate_reg_ex_str()
            self.str_up_to_date = True
            return self.reg_ex_str
    
    def set_reg_ex_list(self, reg_ex_list: list[str]) -> None:
        self.str_up_to_date = False
        self.reg_ex_list = reg_ex_list
    
    def append_reg_ex_list(self, new_expression_part: str) -> None:
        self.str_up_to_date = False
        self.reg_ex_list.append(new_expression_part)

    