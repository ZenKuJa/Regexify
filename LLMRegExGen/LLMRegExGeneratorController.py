from LLMRegExGen.LLMRegExGenerator import LLMRegExGenerator

class LLMRegExGeneratorController:

    def generateRegExFromStringList(self, string_list:list[str]) -> str:
        regexGen = LLMRegExGenerator(open(r'LLMRegExGen\Gemini_Api_Key.txt','r').read())
        if string_list == "":
            return "No input entered!"
        else:
            try:
                erzeugterRegex = regexGen.generateRegEx(string_list)
                approvedRegEx =  regexGen.validategeneratedRegEx(str(erzeugterRegex), string_list)
                return approvedRegEx
            except:
                return "The API is currently not available!"