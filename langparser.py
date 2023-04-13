from classes import *

brackets = ""

def parse(str):
    str = str.strip()

    tokens = []
    token = ""
    
    brnum = 0

    for char in str:
        if char in ["(", ")", "[", "]", "{", "}"]:
            brackets += char
        if char == '{':
            brnum += 1
            token += char
        elif char == '}':
            brnum -= 1
            if brnum > 0:
                token += char
            if brnum == 0:
                token += char
                tokens.append(token)
                token = ""
        else:
            if char == ';' and brnum == 0:
                token += char
                tokens.append(token)
                token = ""
            else:
                token += char

    finaltokens = []

    for tkn in tokens:
        if tkn.strip() == "":
            continue
        finaltokens.append(Token.parse(tkn.strip()))

    return finaltokens