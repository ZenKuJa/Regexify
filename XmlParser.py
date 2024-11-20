import xml.etree.ElementTree as etree

tree = etree.parse(source="CharSetData.xml")
xml_char_set = tree.findall("//char_set")

for xml_element in xml_char_set :
    name: str = xml_element.find("name").text
    short_name: str = xml_element.find("short_name").text
    included_chars: str = xml_element.find("included_chars").text

    print(f"{name}/ {short_name} includes {included_chars}")
