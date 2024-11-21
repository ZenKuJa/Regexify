import google.generativeai as genai
import re

class LLMRegExGenerator:

  def __init__(self, google_API_KEY) -> str:
    self.google_API_KEY = google_API_KEY

  
  # Funktion, welche den Userinput zusammen mit den Promptanweisungen an das LLM sendet und die Antwort als String zurückgibt
  def generateRegEx(self, inputList):
    genai.configure(api_key=self.google_API_KEY)
    
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
      system_instruction= open(r'LLMRegExGen\LLMRegExGeneratorInstructions.txt','r').read())

    #Antwort generieren
    response = model.generate_content("Hier sind die Input Strings: " + " ; ".join(inputList))
    return response.text


  # Validiert den erzeugten RegEx, ob er korrekt ist
  def validategeneratedRegEx(self, generatedRegEx, inputList:list[str]):
    falseCounter = 0
    for oneInputstring in inputList:
      if not re.search((f'{generatedRegEx}').strip(), oneInputstring.strip()):
          falseCounter += 1

    if falseCounter == 0:
      return str(generatedRegEx)
    else: 
      return "The provided strings dont follow the same pattern"