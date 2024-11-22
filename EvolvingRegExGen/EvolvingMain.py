from CheckRegEx import CheckRegEx
from CheckRegExController import CheckRegExController
from EvolvingRegExGen.EvolvingRegExGeneratorController import EvolvingRegExGeneratorController


def main():
    regExChecker: CheckRegExController = CheckRegExController()
    evolvingRegExGenController: EvolvingRegExGeneratorController = EvolvingRegExGeneratorController()

    str_list: list[str] = [
        "chrissi@arbeitsamt.de", "scholz@bundestag.de", "donald@whitehouse.us"]

    str_list_2: list[str] = [
        "192.168.1.1",
        "10.0.0.1",
        "172.16.0.1",
        "8.8.8.8",
        "1.1.1.1"]

    reg_ex:str = evolvingRegExGenController.generateRegExFromStringList(str_list)

    print(reg_ex)
    print(regExChecker.check_for_match(reg_ex=reg_ex, string_list=str_list))



if __name__ == '__main__':
    main()