class ParallelRegexGenerator:

    def split(string1, string2):
        first = []
        second = []
        for char in string1:
            first.append(char)
        for char in string2:
            second.append(char)
        return first, second
    
 
    def encode(input):
        output = []
        for i in input:
            i = str(i)

            if i.islower():
                output.append(1)
            elif i.isupper():
                output.append(2)
            elif i.isnumeric():
                output.append(3)
            elif i in ["@" , "/" , "\\" , "*" , "#" , "-" , "_" , "€" , "\""]:
                output.append(4)
            elif i in ["." , "," , " " , "!" , "?" , ";" , ":"]:
                output.append(5)
            else:
                output.append(i)

        # ParallelRegexGenerator.to_regex(output)
        return output


    # optional function for one string to regex

    def to_regex(input_list):
        count_keys = []
        count_values = []

        counter = 1
        for i in range(len(input_list) - 1):
            if input_list[i] == input_list[i+1]:
                counter += 1
            else:
                count_keys.append(input_list[i])
                count_values.append(counter)
                counter = 1
        # counts[input_list[len(input_list) -1]] = counter
        count_keys.append(input_list[len(input_list) - 1])
        count_values.append(counter)

        keys_regex = []
        for i in count_keys:
            if i == 1:
                keys_regex.append("[a-z]")
            elif i == 2:
                keys_regex.append("[A-Z]")
            elif i == 3:
                keys_regex.append("[0-9]")
            elif i == 4:
                keys_regex.append("[@/\\*#-_€\"]")
            elif i == 5:
                keys_regex.append("[., !?;:]")
            else:
                keys_regex.append(str(i))


        return keys_regex, count_values




    def concatenate(final_keys, final_lower, final_upper):

        final = []
        case = []
        final.append("^")
        for i in range(len(final_keys)):
            final.append(final_keys[i])
            if final_lower[i] != final_upper[i]:
                case = 3
            elif final_lower[i] == final_upper[i]:
                case = 2
            elif final_lower[i] == final_upper[i] and final_lower == 1[i]:
                case = 1
            if case == 1:
                continue
            elif case == 2:
                if final_lower[i] == 1:
                    continue
                final.append("{" + str(final_lower[i]) + "}")
            elif case == 3:
                final.append("{" + f"{final_lower[i]},{final_upper[i]}" + "}")
        final.append("$")


        regex_string = ""
        for i in range(len(final)):
            regex_string += final[i]

        return(regex_string)
        # print(final)
        # print(regex_string)

    def generate(strings):
        counter = 0
        lower_values = []
        upper_values = []
        for i in range(len(strings)):
            j=0
            keys = []
            if i == len(strings) -1:
                j = i
            else: j = i+1
            first_split, second_split = ParallelRegexGenerator.split(strings[i], strings[j])
            first_enc = ParallelRegexGenerator.encode(first_split)
            second_enc = ParallelRegexGenerator.encode(second_split)
            first_keys_regex, first_values = ParallelRegexGenerator.to_regex(first_enc)
            second_keys_regex, second_values = ParallelRegexGenerator.to_regex(second_enc)

            if first_keys_regex != second_keys_regex:
                return("These strings do not follow a similar pattern")
            else: keys = first_keys_regex


            if counter == 0:
                upper, lower, initial = [], [], []
                initial = first_values.copy()
                upper = first_values.copy()
                lower = first_values.copy()
                counter += 1
            else:
                for i in range(len(keys)):
                    if first_values[i] < lower[i]:
                        lower[i] = first_values[i]
                    elif first_values[i] > upper[i]:
                        upper[i] = first_values[i]

        

        return ParallelRegexGenerator.concatenate(keys, lower, upper)
        
        
        # ParallelRegexGenerator.generate(strings)