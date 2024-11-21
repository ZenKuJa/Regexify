from EvolvingRegExGen.EvolvingRegEx import EvolvingRegularExpression
from EvolvingRegExGen.EvolvingRegExGenerator import EvolvingRegExGenerator


class EvolvingRegExGeneratorController:

    evolvingRegExGen: EvolvingRegExGenerator

    def __init__(self):
        self.evolvingRegExGen = EvolvingRegExGenerator()
        ...

    def generateRegExFromStringList(self, string_list:list[str]) -> str:
        generated_regex: str = ""

        regex_list: list[EvolvingRegularExpression] = self.evolvingRegExGen.generate_list(string_list)
        merged_regex: EvolvingRegularExpression = self.evolvingRegExGen.merge_reg_ex_list(regex_list)

        if merged_regex is not None:
            generated_regex = merged_regex.to_str()
            return generated_regex

        else:
            return "The provided strings dont follow the same pattern"
