import re


class CheckRegEx:

    def get_matching_string_list(self, reg_ex: str, string_list:list[str]) -> list[str]:
        matched_strings: list[str] = list(str)

        for word in string_list:
            if re.match(pattern=reg_ex, string=word):
                matched_strings.append(word)

        return matched_strings

    def check_for_match(self, reg_ex: str, string_list:list[str]) -> bool:
        return_bool: bool = True

        for word in string_list:
            if not re.match(pattern=reg_ex, string=word):
                return_bool = False

        return return_bool