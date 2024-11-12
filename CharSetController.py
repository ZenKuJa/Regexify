import xml.etree.ElementTree as eTree
from CharSet import CharSet

class CharSetController:

    my_alphabet: list[CharSet] = []

    def __init__(self):
        tree = eTree.parse(source="CharSetData.xml")
        xml_char_set = tree.findall(".//char_set")

        for xml_element in xml_char_set:
            name: str = xml_element.find("name").text
            short_name: str = xml_element.find("short_name").text
            included_chars: str = xml_element.find("included_chars").text

            new_char_set: CharSet = CharSet(name=name, short_name=short_name, chars=included_chars)
            self.my_alphabet.append(new_char_set)

    def get_char_set(self, char: str) -> CharSet | None:
        for char_set in self.my_alphabet:
            if char in char_set.get_char_set():
                return char_set    
        return None