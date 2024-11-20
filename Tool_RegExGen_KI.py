import google.generativeai as genai
import re

GOOGLE_API_KEY =  open('Gemini_Api_Key.txt','r').read()
genai.configure(api_key=GOOGLE_API_KEY)

# Parameter zum Fine Tuning des Modells 
generation_config = {
  "temperature": 0.3,
  "top_p": 0.9,
  "top_k": 10,
  "max_output_tokens": 256,
  "response_mime_type": "text/plain",
}

# Modellauswahl und Anweisungen
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction= open('Tool_KI_instruction.txt','r').read())


# Funktion, welche den Userinput abfängt und zusammen mit den Promptanweisungen an das LLM sendet, im Anschluss wird die Antwort validiert und je nachdem zurückgegeben
def generateRegEx(inputList):
  if inputList == "":
      print("Kein Input eingegeben!")
  else:
    response = model.generate_content("Hier sind die Input Strings: " + " ; ".join(inputList))
    
    falseCounter = 0
    for oneInputstring in inputList:
      if not re.search((f'{response.text}').strip(), oneInputstring.strip()):
          falseCounter += 1

  if falseCounter == 0:
    print("Der Reguläre Ausdruck für den eingegebenen Input ist : " + response.text)
  else: 
    print("Für den eingegebenen Input wurde kein valider Regulärer Ausdruck gefunden!")

    
generateRegEx(["david@web.de", "nischal@Web.de", "jannes87@gmail.com", "Regex@stud.dhbw-ravensburg.de", "Regex@stud.dhbw-ravensburg.de"])