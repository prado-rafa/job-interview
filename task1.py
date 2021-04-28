def parseInt(hex):
    value = 0
    for i, v in enumerate(hex):
        o = ord(v)
        if (o >= 65 and o < 71):
            value = value * 16 + o - 55
        elif (o >= 48 and o < 58):
            value = value * 16 + o - 48
        else:
            return "Invalid Input"
    
    return value

print(parseInt("9F9F"))