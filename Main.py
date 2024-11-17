from RegEx import RegularExpression
from RegExGenerator import RegExGenerator

def main():
    reg_ex_gen: RegExGenerator = RegExGenerator()

    str_list: list[str] = ["192.186.80.156", "192.456.80.880"]

    reg_ex_list: list[RegularExpression] = reg_ex_gen.generate_list(str_list)

    merged_reg_ex: RegularExpression = reg_ex_gen.merge_reg_ex_list(reg_ex_list)

    if merged_reg_ex is not None:
        print(merged_reg_ex.to_str())
    else:
        print("something failed")

if __name__ == '__main__':
    main()