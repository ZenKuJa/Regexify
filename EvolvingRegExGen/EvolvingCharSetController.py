import xml.etree.ElementTree as eTree
from EvolvingRegExGen.EvolvingCharSet import EvolvingCharSet

class EvolvingCharSetController:

    my_alphabet: list[EvolvingCharSet] = []

    def __init__(self):
        """Reads the XML File containing the necessary information to create all charSets"""
        tree = eTree.parse(source="../Data/CharSetData.xml")
        xml_char_set = tree.findall(".//char_set")

        for xml_element in xml_char_set:
            name: str = xml_element.find("name").text
            short_name: str = xml_element.find("short_name").text
            included_chars: str = xml_element.find("included_chars").text

            new_char_set: EvolvingCharSet = EvolvingCharSet(name=name, short_name=short_name, chars=included_chars)
            self.my_alphabet.append(new_char_set)

    def get_char_set(self, char: str) -> EvolvingCharSet | None:
        """Returns the charSet, that contains the given char or returns none
        when the given char does not exist in any charSet"""
        for char_set in self.my_alphabet:
            if char in char_set.get_char_set():
                return char_set    
        return None