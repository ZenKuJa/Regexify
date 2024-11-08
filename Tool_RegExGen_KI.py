import google.generativeai as genai

GOOGLE_API_KEY =  open('TI_Tool/Gemini_Api_Key.txt','r').read()
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "temperature": 0.5,
  "top_p": 0.8,
  "top_k": 20,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="Du bist ein Experte für RegEx beziehungsweise Reguläre Ausdrucke! Deine Antwort sollte kurz und möglichst präzise sein, wobei der Input möglichst detatilliert durch einen Regulären Ausdruck beschrieben wird!",
)

instruction = open('TI_Tool/Tool_KI_instruction.txt','r').read()

def einDurchlauf():
  userinput = input("Gib bitte deinen Input mit ; sepereriert an! : ")

  if userinput == "":
      print("Kein Input eingegeben!")
  else:
      response = model.generate_content(instruction + "Hier sind die Input Strings: " + userinput)
      print("Der Reguläre Ausdruck für den eingegebenen Input ist : " + response.text)

einDurchlauf()
while True:
    if (input("Eine weitere Abfrage (Y/n)? :") == "Y"):
        einDurchlauf()
    else:
        break
