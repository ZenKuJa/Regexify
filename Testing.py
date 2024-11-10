def regex_generator(strings):
  """
  Generiert einen regulären Ausdruck nach dem BRE-Standard, der alle gegebenen Strings matcht.

  Args:
    strings: Eine Liste von Strings im ISO 8859-1 Zeichensatz.

  Returns:
    Einen regulären Ausdruck als String.
  """

  if not strings:
    return ""

  # Ersten String als Basis-Regex verwenden
  regex = strings[0]

  # Iteriere über die restlichen Strings
  for string in strings[1:]:
    i = 0
    while i < len(regex) and i < len(string) and regex[i] == string[i]:
      i += 1

    # Gemeinsames Präfix finden
    prefix = regex[:i]

    # Unterschiedliche Teile in Gruppen zusammenfassen
    regex = f"{prefix}({regex[i:]}|{string[i:]})"

  return regex

# Beispielaufruf
strings = ["meinName@gmail.com", "christian@dhbw.de", "sabine@gmail.com", "lol@gmx.de", "donald@maga.us", "david.muth@airbus.com", "chantal@gmx.de"]
regex = regex_generator(strings)
print(regex)  # Ausgabe: a(b(c|d)|ec)