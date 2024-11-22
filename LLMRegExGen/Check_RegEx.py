import re

text = ["moin@web.de", "nischal@gmail.com"]
regex = r'^[a-z]{4,7}[@/\*#-_€"][a-z]{3,5}[., !?;:][a-z]{2,3}$'


falseCounter = 0
for i in text:
    if re.search(regex, i.strip()):
      falseCounter =+ 1

if falseCounter == 0:
  print("Stimmt nicht überein!")
else:
  print("Stimmt überein!")