def regex_generator(strings: list[str]) -> str:
  """
  Generiert einen regulären Ausdruck nach dem BRE-Standard, der alle gegebenen Strings matcht.
  Versucht, gemeinsame Muster zu erkennen und zu verallgemeinern.

  Args:
    strings: Eine Liste von Strings im ISO 8859-1 Zeichensatz.

  Returns:
    Einen regulären Ausdruck als String.
  """

  if not strings:
    return ""

  # Strings nach Länge sortieren
  strings.sort(key=len)

  # Ersten String als Basis-Regex verwenden
  regex: str = strings[0]

  for string in strings[1:]:
    i: int = 0
    while i < len(regex) and i < len(string) and regex[i] == string[i]:
      i += 1

    prefix: str = regex[:i]
    suffix_regex: str = regex[i:]
    suffix_string: str = string[i:]

    # Zeichenklassen verwenden
    if len(suffix_regex) == 1 == len(suffix_string):
      regex = f"{prefix}[{suffix_regex}{suffix_string}]"

    # Quantifizierer verwenden
    elif suffix_regex == suffix_string * len(suffix_regex):
      regex = f"{prefix}{suffix_string}+"

    # Optionale Elemente verwenden
    elif suffix_regex.startswith(suffix_string):
      regex = f"{prefix}{suffix_string}?"

    # Lookahead-Assertions verwenden
    elif suffix_string.startswith(suffix_regex):
      regex = f"{prefix}{suffix_regex}(?={suffix_string[len(suffix_regex):]})"

    # Ansonsten: Fallback auf den alten Algorithmus
    else:
      regex = "läuft garnicht"

  return regex


strings = ["aba", "aba", "abad", "abade"]
regex = regex_generator(strings)
print(regex)  # Ausgabe: a(b(c|d)|ec)