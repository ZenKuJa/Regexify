from LLMRegExGenerator import LLMRegExGenerator

class LLMRegExGeneratorController:

    def generateRegExFromStringList(string_list:list[str]) -> str:
        regexGen = LLMRegExGenerator(open('Gemini_Api_Key.txt','r').read())  
            
        if string_list == "":
            print("No input entered!")
        else:
            erzeugterRegex = regexGen.generateRegEx(string_list)
            regexGen.validategeneratedRegEx(erzeugterRegex, string_list)
            


testinput = ["david@web.de", "nischal@Web.de", "jannes87@gmail.com", "Regex@stud.dhbw-ravensburg.de", "Regex@stud.dhbw-ravensburg.de"]
LLMRegExGeneratorController.generateRegExFromStringList(testinput)