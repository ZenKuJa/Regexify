from typing import List

def regex_generator_iso88591(strings: List[str]) -> str:
    """
    Generiert einen regulären Ausdruck (BRE-Standard), der alle 
    gegebenen Strings (ISO 8859-1) matcht und den gesamten 
    ISO 8859-1 Zeichenraum berücksichtigt.

    Args:
      strings: Eine Liste von Strings im ISO 8859-1 Zeichensatz.

    Returns:
      Einen regulären Ausdruck als String.
    """
    if not strings:
        return ""

    # 1. Alle eindeutigen Zeichen aus den Strings extrahieren
    zeichen = set()
    for string in strings:
        zeichen.update(string)

    # 2. Zeichen in Gruppen zusammenfassen (z.B. Buchstaben, Ziffern, Sonderzeichen)
    gruppen = {
        "Kontrollzeichen": "".join(chr(i) for i in range(0x01, 0x20)),
        "Leerzeichen": " ",
        "Satzzeichen": "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~",
        "Ziffern": "0123456789",
        "Großbuchstaben": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "Kleinbuchstaben": "abcdefghijklmnopqrstuvwxyz",
        "Sonderzeichen": "".join(chr(i) for i in range(0xA0, 0x100))
    }

    # 3. Zeichenklassen für jede Gruppe erstellen
    zeichenklassen = {}
    for name, gruppe in gruppen.items():
        zeichenklassen[name] = "[" + "".join(zeichen for zeichen in gruppe if zeichen in zeichen) + "]"

    # 4. Regulären Ausdruck aus den Zeichenklassen erstellen
    regex = ""
    for string in strings:
        temp_regex = ""
        for zeichen in string:
            for name, klasse in zeichenklassen.items():
                if zeichen in klasse:
                    # Hier die Korrektur: Zeichenklasse in eckige Klammern setzen
                    temp_regex += "[" + klasse + "]" 
                    break
            else:  # Zeichen nicht in den definierten Gruppen gefunden
                temp_regex += zeichen  # Zeichen literal verwenden
        if regex:
            regex += "|" + temp_regex
        else:
            regex = temp_regex

    return regex
strings = ["aba", "aba", "aba"  ]
regex = regex_generator_iso88591(strings)
print(regex)  # Ausgabe: a(b(c|d)|ec)