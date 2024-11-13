import google.generativeai as genai
import re

GOOGLE_API_KEY =  open('Gemini_Api_Key.txt','r').read()
genai.configure(api_key=GOOGLE_API_KEY)

# Parameter zum Fine Tuning des Modells 
generation_config = {
  "temperature": 0.5,
  "top_p": 0.8,
  "top_k": 20,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# Modellauswahl und Anweisungen
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="""Du bist ein Experte für RegEx beziehungsweise Reguläre Ausdrucke! Deine Antwort sollte kurz und möglichst präzise sein, 
                        wobei der Input möglichst detatilliert durch einen Regulären Ausdruck beschrieben wird!""")

# Funktion, welche den Userinput abfängt und zusammen mit den Promptanweisungen an das LLM gesendet, im Anschluss wird die Antwort validiert
# und je nachdem zurückgegeben. Zum Schluss wird abgefragt, ob der User noch eine Abfrage machen möchte
def einDurchlauf():
  userinput = input("Gib bitte deinen Input (nur einzelne Zeichenketten) mit ; sepereriert an! : ")
  promptInstruction = open('Tool_KI_instruction.txt','r').read()

  if userinput == "":
      print("Kein Input eingegeben!")
  else:
    response = model.generate_content(promptInstruction + "Hier sind die Input Strings: " + userinput)
    falseCounter = 0
 
    for oneInputstring in userinput.split(';'):
      if not re.search((f'{response.text}').strip(), oneInputstring.strip()):
          falseCounter += 1

  if falseCounter == 0:
    print("Der Reguläre Ausdruck für den eingegebenen Input ist : " + response.text)
  else: 
    print("Für den eingegebenen Input wurde kein valider Regulärer Ausdruck gefunden!")

  if (input("Eine weitere Abfrage (Y/n)? :") == "Y"):
        einDurchlauf()

# Tool starten
einDurchlauf()
