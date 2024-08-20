d1 = {
    'a': 12,
    'b': 45,
    'c': 27,
    'd': 14,
    'e': 29,
    'f': 78,
    'g': 89,
    'h': 50,
    'i': 33,
    'j': 60
}

d2 = {
    'a': 91,
    'b': 35,
    'c': 73,  
    'k': 25,
    'l': 47,
    'm': 59,
    'n': 82,
    'o': 66,
    'p': 19,
    'q': 38,
    'r': 77,
    's': 94,
    't': 55,
    'u': 62,
    'v': 84
}

def jodo(d1,d2):
    result = {}

    for k in d1.keys():
        result[k] = d1[k]

    for k in d2.keys():
        if k in result.keys():
            result[k] += d2[k]
        else:
            result[k] = d2[k]

    return result

print(jodo(d1,d2))