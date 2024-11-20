from Tool_RegExGen_KI import Tool_RegExGen_KI

class LLMRegExGeneratorController:

    def generateRegExFromStringList(string_list:list[str]) -> str:
        regexGen = Tool_RegExGen_KI(open('Gemini_Api_Key.txt','r').read())  
            
        if string_list == "":
            print("Kein Input eingegeben!")
        else:
            erzeugterRegex = regexGen.generateRegEx(string_list)
            regexGen.validategeneratedRegEx(erzeugterRegex, string_list)
            



input = ["david@web.de", "nischal@Web.de", "jannes87@gmail.com", "Regex@stud.dhbw-ravensburg.de", "Regex@stud.dhbw-ravensburg.de"]
LLMRegExGeneratorController.generateRegExFromStringList(input)