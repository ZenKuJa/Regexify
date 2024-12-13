import unittest

from CheckRegExController import CheckRegExController
from EvolvingRegExGen.EvolvingRegExGeneratorController import EvolvingRegExGeneratorController


class EvolvingRegExGenTest(unittest.TestCase):
    reg_ex_checker: CheckRegExController
    reg_ex_gen_controller: EvolvingRegExGeneratorController

    email_list_1: list[str] = ['thomas123@web.de', 'martin987@web.com', 'christian23@bundestag.gov']
    email_list_2: list[str] = ['max28@stud.dhbwravensburg.de', 'Moritz2000@outlook.de', 'InfoDHBW@gmail.com', 'support24@dhbwravensburg.de']

    ip_address_1: list[str] = ['123.234.46.122', '1.234.4.123', '123.0.12.111']
    ip_address_2: list[str] = ['192.168.254.99', '172.31.98.255', '10.203.56.210', '255.128.33.77']

    file_names_1: list[str] = ['Hintergrundbild.jpg', 'Semesterbescheid.pdf', 'Projektarbeit.docs']
    file_names_2: list[str] = ['Hintergrundbild4k.jpg', 'Semesterbescheid3Semester.pdf', 'PA1.docs', 'GeminiApiKey.txt']

    passwords_1: list[str] = ['Benutzer', 'hallo', 'Password', 'iloveyou']
    passwords_2: list[str] = ['gYnwit-cadwoj-7robbu', 'puwcub-4hucbe-tefPic', 'nekbop-5bohpu-vEcsut', 'zibQax-4zykta-syjget']

    tel_numbers_1: list[str] = ['004916212345678', '004916209876543', '004900555019923']
    tel_numbers_2: list[str] = ['01627654321', '+491521234567', '01519876543', '+491609876543']

    plz_1: list[str] = ['50667', '88662', '88214', '88212']
    plz_2: list[str] = ['80331', '13417', '8099', '70123']

    domains_1: list[str] = ['https://www.google.com/', 'https://elearning.dhbw-ravensburg.de/', 'https://rapla-ravensburg.dhbw.de/', 'https://dualis.dhbw.de/']
    domains_2: list[str] = ['https://github.com/ZenKuJa/Regexify', 'http://scholar.google.de/scholar?hl=de&as_sdt=0%2C5&q=RegEx&btnG=', 'https://finance.yahoo.com/quote/AAPL/']

    def setUp(self):
        self.reg_ex_checker = CheckRegExController()
        self.reg_ex_gen_controller = EvolvingRegExGeneratorController()

    def test_email_1(self):
        reg_ex: str = self.reg_ex_gen_controller.generateRegExFromStringList(self.email_list_1)
        self.assertTrue(self.reg_ex_checker.check_for_match(reg_ex, self.email_list_1))

    def test_email_2(self):
        reg_ex: str = self.reg_ex_gen_controller.generateRegExFromStringList(self.email_list_2)
        self.assertTrue(self.reg_ex_checker.check_for_match(reg_ex, self.email_list_2))

    def test_ip_address_1(self):
        reg_ex: str = self.reg_ex_gen_controller.generateRegExFromStringList(self.ip_address_1)
        self.assertTrue(self.reg_ex_checker.check_for_match(reg_ex, self.ip_address_1))

    def test_ip_address_2(self):
        reg_ex: str = self.reg_ex_gen_controller.generateRegExFromStringList(self.ip_address_2)
        self.assertTrue(self.reg_ex_checker.check_for_match(reg_ex, self.ip_address_2))

    def test_file_name_1(self):
        reg_ex: str = self.reg_ex_gen_controller.generateRegExFromStringList(self.file_names_1)
        self.assertTrue(self.reg_ex_checker.check_for_match(reg_ex, self.file_names_1))

    def test_file_name_2(self):
        reg_ex: str = self.reg_ex_gen_controller.generateRegExFromStringList(self.file_names_2)
        self.assertTrue(self.reg_ex_checker.check_for_match(reg_ex, self.file_names_2))

    def test_passwords_1(self):
        reg_ex: str = self.reg_ex_gen_controller.generateRegExFromStringList(self.passwords_1)
        self.assertTrue(self.reg_ex_checker.check_for_match(reg_ex, self.passwords_1))

    def test_passwords_2(self):
        reg_ex: str = self.reg_ex_gen_controller.generateRegExFromStringList(self.passwords_2)
        self.assertTrue(self.reg_ex_checker.check_for_match(reg_ex, self.passwords_2))

    def test_tel_numbers_1(self):
        reg_ex: str = self.reg_ex_gen_controller.generateRegExFromStringList(self.tel_numbers_1)
        self.assertTrue(self.reg_ex_checker.check_for_match(reg_ex, self.tel_numbers_1))

    def test_tel_numbers_2(self):
        reg_ex: str = self.reg_ex_gen_controller.generateRegExFromStringList(self.tel_numbers_2)
        self.assertTrue(self.reg_ex_checker.check_for_match(reg_ex, self.tel_numbers_2))

    def test_domains_1(self):
        reg_ex: str = self.reg_ex_gen_controller.generateRegExFromStringList(self.domains_1)
        self.assertTrue(self.reg_ex_checker.check_for_match(reg_ex, self.domains_1))

    def test_domains_2(self):
        reg_ex: str = self.reg_ex_gen_controller.generateRegExFromStringList(self.domains_2)
        self.assertTrue(self.reg_ex_checker.check_for_match(reg_ex, self.domains_2))


if __name__ == '__main__':
    unittest.main()