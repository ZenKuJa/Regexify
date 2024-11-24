import google.generativeai as genai
import re

class LLMRegExGenerator:

  def __init__(self, google_API_KEY) -> str:
    self.google_API_KEY = google_API_KEY



  def generateRegEx(self, inputList):
    genai.configure(api_key=self.google_API_KEY)


    generation_config = {
      "temperature": 0.25,
      "top_p": 0.9,
      "top_k": 10,
      "max_output_tokens": 128,
      "response_mime_type": "text/plain",
    }


    model = genai.GenerativeModel(
      model_name="gemini-1.5-pro",
      generation_config=generation_config,
      system_instruction= open(r'LLMRegExGen\LLMRegExGeneratorInstructions.txt','r').read())


    response = model.generate_content("Hier sind die Input Strings: " + " ; ".join(inputList))
    return response.text


  def validategeneratedRegEx(self, generatedRegEx, inputList:list[str]):
    falseCounter = 0
    for oneInputstring in inputList:
      if not re.search((f'{generatedRegEx}').strip(), oneInputstring.strip()):
          falseCounter += 1

    if falseCounter == 0:
      return str(generatedRegEx)
    else: 
      return "The provided strings dont follow the same pattern"