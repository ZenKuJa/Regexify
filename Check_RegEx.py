import re

text = "david@web.de; nischal@web.de "
regex = r"^[a-z]+@web\.de$"

falseCounter = 0

for i in text.split(";"):
    if re.search(regex, i.strip()):
      falseCounter =+ 1

if falseCounter == 0:
  print("Stimmt nicht überein!")
else:
  print("Stimmt überein!")