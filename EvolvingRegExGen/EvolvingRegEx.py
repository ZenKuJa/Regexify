from EvolvingRegExGen.EvolvingCharSet import EvolvingCharSet
from EvolvingRegExGen.EvolvingRegExPart import EvolvingRegExPart


class EvolvingRegularExpression:
    reg_ex_structure: list[EvolvingRegExPart]
    reg_ex_operators: list[str]

    reg_ex_str: str

    max_occurring_strings: int = 3
    max_occurring_chars: int = 7

    def __init__(self):
        self.reg_ex_str = ""
        self.reg_ex_structure = []
        self.reg_ex_operators = [
            ".", "*", "+", "?", "$", "|", "^", "\\", "-", "(", ")", "{", "}", "[", "]"
        ]

    def append(self, char_set: EvolvingCharSet, occurring_strings: list[str], min_amount: int, max_amount: int) -> None:
        """Add a new RegExPart to the RegEx structure."""
        self.reg_ex_str = ""
        new_reg_ex_part: EvolvingRegExPart = EvolvingRegExPart(list(set(occurring_strings)), char_set, min_amount, max_amount)
        self.reg_ex_structure.append(new_reg_ex_part)
    
    def to_str(self) -> str:
        """Returns the RegularExpression as a string."""
        if self.reg_ex_str == "":
            print("generated new return string")
            str_occurring_chars: str = ""
            str_occurring_strings: list[str] = []
            str_short: str = ""
            str_min: int = 0
            str_max: int = 0

            #Iterates over every RegExPart of this RegularExpression
            for reg_ex_part in self.reg_ex_structure:

                #Read all needed data from the RegExParts for
                str_occurring_chars = reg_ex_part.get_occurring_chars()
                str_occurring_strings = reg_ex_part.get_occurring_strings()
                str_short = reg_ex_part.get_char_set().get_short()
                str_min = reg_ex_part.get_min_length()
                str_max = reg_ex_part.get_max_length()

                #Check if only one string occurs at the current position
                if len(str_occurring_strings) == 1:
                    str_short = str_occurring_strings[0]

                    #If the string is one of the Regular Expression formatting characters
                    #a backslash is added as an escape character
                    if str_short in self.reg_ex_operators:
                        self.reg_ex_str += f"+\\{str_short}"

                    #If the string is not part of the formatting characters, it is added
                    #to the final reg_ex_str without any brackets
                    else:
                        self.reg_ex_str += f"+{str_short}"

                    #Escapes the current for-iteration to skip the addition of {min, max} brackets
                    continue

                # if less strings than the defined max occur, they are appended to each
                #other with a | between them
                elif len(str_occurring_strings) <= self.max_occurring_strings:
                    str_short = ""

                    #this for-loop loops over all occurring_strings in this RegExPart
                    for i, occurring_string in enumerate(str_occurring_strings):

                        #if a string exists after the current one, it is appended with a |
                        if i < len(str_occurring_strings) - 1:
                            str_short += f"{occurring_string}|"

                        #if no next string exists, it is just appended blank
                        else:
                            str_short += f"{occurring_string}"

                    self.reg_ex_str += f"({str_short})"

                    # Escapes the current for-iteration to skip the addition of {min, max} brackets
                    continue

                #Check less strings occur at the current position than the defined maximum
                elif len(str_occurring_chars) <= self.max_occurring_chars:

                    #Writes the occurring chars in the short form of the current position
                    str_short = ""
                    for c in str_occurring_chars:
                        str_short += c

                #if none of the previous edge cases occurred, the predfined short form from
                #the charSet is kept as representation of the RegExPart content
                self.reg_ex_str += f"[{str_short}]"

                #Generates the {min, max} brackets for the current RegExPart
                if str_min < str_max:
                    self.reg_ex_str += f"{{{str_min},{str_max}}}"
                elif str_min > str_max:
                    self.reg_ex_str += f"{{{str_max},{str_min}}}"

                #Adds a fixed length if all Strings at this position are of the same length
                elif str_min > 1:
                    self.reg_ex_str += f"{{{str_max}}}"

        return f"^{self.reg_ex_str}$"

    def get_reg_ex_parts(self) -> list[EvolvingRegExPart]:
        """Returns the actually present RegExParts with all included information.
        Used to merge RegularExpressions with each other."""
        return self.reg_ex_structure

    def get_reg_ex_order(self) -> list[EvolvingCharSet]:
        """Returns the structure in which the CharSets occur in this RegularExpression.
        Used to compare  RegularExpressions to each other."""
        reg_ex_order: list[EvolvingCharSet] = []
        for part in self.reg_ex_structure:
            reg_ex_order.append(part.get_char_set())

        return reg_ex_order
