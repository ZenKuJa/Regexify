from CheckRegEx import CheckRegEx

class CheckRegExController:
    regExChecker: CheckRegEx

    def __init__(self):
        self.regExChecker = CheckRegEx()

    def get_matching_strings(self, reg_ex:str, string_list:list[str]) -> list[str]:
        return self.get_matching_strings(reg_ex= reg_ex, string_list=string_list)

    def check_for_match(self, reg_ex:str, string_list:list[str]) -> bool:
        return self.regExChecker.check_for_match(reg_ex= reg_ex, string_list=string_list)
