import time

from CheckRegExController import CheckRegExController
from EvolvingRegExGen.EvolvingRegExGeneratorController import EvolvingRegExGeneratorController


def tests():
    mail_adressen: list[str] = [
        "chrissi@arbeitsamt.de", "scholz@bundestag.de", "donald@whitehouse.us"]

    ip_adressen: list[str] = [
        "192.168.1.1",
        "10.0.0.1",
        "172.16.0.1",
        "8.8.8.8",
        "1.1.1.1"]

    tel_nummern: list[str] = [
        "004916212345678",
        "004916209876543",
        "004900555019923"]

    test_fun(mail_adressen, "mail-adressen")
    test_fun(ip_adressen, "ip-adressen")
    test_fun(tel_nummern, "tel-nummern")

def test_fun(liste:[str], name: str) -> None:
    regExChecker: CheckRegExController = CheckRegExController()
    evolvingRegExGenController: EvolvingRegExGeneratorController = EvolvingRegExGeneratorController()

    print(f"~~~~~~~{name}~~~~~~~")
    print(f"{liste}")
    start = time.time()
    reg_ex:str =evolvingRegExGenController.generateRegExFromStringList(liste)
    end = time.time()
    print(f"regEx: {reg_ex}")
    valid: bool = regExChecker.check_for_match(reg_ex=reg_ex, string_list=liste)
    print(f"valid: {valid}")
    print(f"time: {(end-start)*100000}")




    ...
if __name__ == '__main__':
    tests()