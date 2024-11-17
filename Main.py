from RegEx import RegularExpression
from RegExGenerator import RegExGenerator

def main():
    reg_ex_gen: RegExGenerator = RegExGenerator()

    str_list: list[str] = [
        "chrissi@arbeitsamt.de", "scholz@bundestag.de", "donald@whitehouse.us"
        , "charlie@bundestag.us", "lucifermorningstar@whitehouse.us"]

    str_list_2: list[str] = [
        "192.168.1.1",
        "10.0.0.1",
        "172.16.0.1",
        "8.8.8.8",
        "1.1.1.1"
    ]

    reg_ex_list: list[RegularExpression] = reg_ex_gen.generate_list(str_list)

    reg_ex_list_2: list[RegularExpression] = reg_ex_gen.generate_list(str_list_2)

    merged_reg_ex: RegularExpression = reg_ex_gen.merge_reg_ex_list(reg_ex_list)
    merged_reg_ex_2: RegularExpression = reg_ex_gen.merge_reg_ex_list(reg_ex_list_2)

    if merged_reg_ex is not None:
        print(merged_reg_ex.to_str())
    else:
        print("something failed")

    if merged_reg_ex_2 is not None:
        print(merged_reg_ex_2.to_str())
    else:
        print("something failed")

if __name__ == '__main__':
    main()