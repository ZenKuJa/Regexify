import logging

from EvolvingRegExGen.EvolvingRegEx import EvolvingRegularExpression
from EvolvingRegExGen.EvolvingRegExGenerator import EvolvingRegExGenerator


class EvolvingRegExGeneratorController:

    evolvingRegExGen: EvolvingRegExGenerator
    logger: logging.Logger

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.evolvingRegExGen = EvolvingRegExGenerator()

    def generateRegExFromStringList(self, string_list:list[str]) -> str:
        """Takes a list of type string and returns the corresponding regular expression as a string.
        If the generator failed to generator failed to generate a regular expression, a string with a fitting error description is returned"""
        generated_regex: str = ""
        merged_regex: EvolvingRegularExpression

        if len(string_list) == 1:
            merged_regex = self.evolvingRegExGen.generate(string_list[0])
        elif len(string_list) > 1:
            regex_list: list[EvolvingRegularExpression] = self.evolvingRegExGen.generate_list(string_list)
            merged_regex = self.evolvingRegExGen.merge_reg_ex_list(regex_list)
        else:
            merged_regex = None

        if merged_regex is not None:
            generated_regex = merged_regex.to_str()
            return generated_regex
        else:
            self.logger.warning("Couldn't recognize a pattern present in all strings.")
            return "The provided strings dont follow the same pattern"
