# sonderZeichen = ['!', '@']

# 1 = Klein
# 2 = Groß
# 3 = Zahl 
# 4 = @
# 0 = Fehler!/Nichts gefunden!

def encodeInput(email):
    email_encoded = []
    
    for i in email:
        if i.islower():
            email_encoded.append(1)
        elif i.isupper():
            email_encoded.append(2)
        elif i.isnumeric():
            email_encoded.append(3)
        elif i == "@":
            email_encoded.append(4)
        else:
            email_encoded.append(0)

        # elif i in sonderZeichen:
        #     email_encoded.append(4)

    return email_encoded

def countElements(Array):
    counts = {}
    current_num = None
    count = 0

    for num in Array:
        if num != current_num:
            if current_num is not None:
                counts[current_num] = count
            current_num = num
            count = 1
        else:
            count += 1

    counts[current_num] = count
    return counts


#dictInput = countElements(encodeInput(input("Gib einen Input ein: ")))

userInput = "Hallo187"
encodedInput = encodeInput(userInput)
dictInput = countElements(encodedInput)

print(encodedInput)
print(dictInput)

for key, value in dictInput.items():
    match key:
        case 1: 
            print("[a-z]" + str(value))
        case 2: 
            print("[A-Z]" + str(value))

