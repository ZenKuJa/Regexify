import re

text = ["david@web.de", "nischal@Web.de", "jannes87@gmail.com", "Matti102834@web.gov"]
regex = r"^[a-zA-Z0-9]+@[a-zA-Z]+\.(de|com|gov)$"

falseCounter = 0
for i in text:
    if re.search(regex, i.strip()):
      falseCounter =+ 1

if falseCounter == 0:
  print("Stimmt nicht überein!")
else:
  print("Stimmt überein!")