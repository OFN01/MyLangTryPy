import console

class Token:
    val = ""
    subtokens = []

    def __init__(self, value: str, subtokens: list):
        self.val = value
        self.subtokens = subtokens

    def __str__(self):
        res = self.val
        if len(self.subtokens) != 0:
            res += ":\n"
        for token in self.subtokens:
            res += "    " + str(token) + "\n"
        return res

    def parse(str):
        str = str.strip()

        token = ""
        subtokens = []

        subtoken = ""

        brnum = 0

        isended = False

        for char in str:
            if isended and (char != " " or char != "\n" or char != "\0"):
                console.Except("Token Error: Only one token can be parsed!")
            if char == '{':
                brnum += 1
                if brnum > 1:
                    subtoken += char
            elif char == '}':
                brnum -= 1
                if brnum > 1:
                    subtoken += char
                if brnum == 0:
                    isended = True
                subtokens.append(subtoken)
            elif brnum == 0:
                token += char
            else:
                if char == ';' and brnum == 1:
                    subtoken += char
                    subtokens.append(subtoken)
                    subtoken = ""
                else:
                    subtoken += char

        finalsubtokens = []

        for tkn in subtokens:
            if tkn.strip() == "":
                continue
            finalsubtokens.append(Token.parse(tkn.strip()))
        
        token = token.strip()

        return Token(token, finalsubtokens)