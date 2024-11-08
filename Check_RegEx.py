import re

text = "david@gmail.com; nischal@web.de"
pattern = r"^[a-zA-Z0-9\-]+@[a-zA-Z]+\.(com|net|org)$"

if re.search(pattern, text):
  print("Stimmt überein!")
else:
  print("Stimmt nicht überein!")