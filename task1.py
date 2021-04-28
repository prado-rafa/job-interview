def parseInt(hex):
    value = 0
    for i, v in enumerate(hex):
        o = ord(v)
        if (o >= 65 and o < 75):
            toAdd = o - 55
            value = value * 16 + toAdd
        elif (o >= 48 and o < 58):
            toAdd = o - 48
            value = value * 16 + toAdd
        else:
            return "Invalid Input"
    
    return value

print(parseInt("9F9F"))