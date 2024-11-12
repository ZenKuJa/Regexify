from RegEx import regular_expression
from RegExGenerator import regular_expression_generator

reg_ex_gen: regular_expression_generator = regular_expression_generator()

input_str: str = "chrissi@arbeitsamt.de"

reg_ex: regular_expression = reg_ex_gen.generate(input_str)

print(reg_ex.to_str())
