from RegEx import RegularExpression
from RegExGenerator import RegExGenerator

def main():
    reg_ex_gen: RegExGenerator = RegExGenerator()
    input_str: str = "chrissi@arbeitsamt.de"
    reg_ex: RegularExpression = reg_ex_gen.generate(input_str)
    print(reg_ex.to_str())

if __name__ == '__main__':
    main()