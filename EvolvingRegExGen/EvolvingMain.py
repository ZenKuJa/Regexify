from EvolvingRegExGen.EvolvingRegExGeneratorController import EvolvingRegExGeneratorController


def main():
    evolvingRegExGenController: EvolvingRegExGeneratorController = EvolvingRegExGeneratorController()

    str_list: list[str] = [
        "chrissi@arbeitsamt.de", "scholz@bundestag.de", "donald@whitehouse.us"]

    str_list_2: list[str] = [
        "192.168.1.1",
        "10.0.0.1",
        "172.16.0.1",
        "8.8.8.8",
        "1.1.1.1"]

    print(evolvingRegExGenController.generateRegExFromStringList(str_list))

if __name__ == '__main__':
    main()