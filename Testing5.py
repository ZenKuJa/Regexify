def print_iso_8859_1_chars():
    """Gibt alle ISO 8859-1 Schriftzeichen aus."""
    # Definiere die ISO 8859-1 Kodierung
    iso_8859_1_encoding = "ISO-8859-1"

    # Iteriere über alle Codepunkte von 0 bis 255
    for i in range(256):
        try:
            # Wandle den Codepunkt in ein Byte um
            byte_value = bytes([i])

            # Dekodiere das Byte mit der ISO 8859-1 Kodierung
            char = byte_value.decode(iso_8859_1_encoding)

            # Gib das Zeichen aus
            print(f"Codepunkt: {i}, Zeichen: {char}")
        except UnicodeDecodeError:
            # Ignoriere nicht darstellbare Zeichen
            pass

# Funktionsaufruf
print_iso_8859_1_chars()