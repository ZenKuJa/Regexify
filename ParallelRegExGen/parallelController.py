from ParallelRegExGen.parallel import ParallelRegexGenerator
class ParallelController:

    def generate_regex_from_strings(self, strings:list[str]):
        return ParallelRegexGenerator.generate(strings)

    