def parseInt(hex):
    value = 0
    for i, v in enumerate(hex):
        o = ord(v)
        toAdd = o - 55 if o >= 65 else o - 48
        value = value * 16 + toAdd
    
    return value

print(parseInt("1F"))