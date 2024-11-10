from MyRegEx import MyRegEx
from RegExGenerator import RegExGenerator

regEx: MyRegEx = MyRegEx()
regExGen: RegExGenerator = RegExGenerator()

input_str: str = "abcdFGH12345678"

regEx.set_reg_ex_list(regExGen.get_reg_ex_list_for(input_str))

print(regEx.get_reg_ex_string())
