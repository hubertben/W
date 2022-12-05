import math
from wObject import *

class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.tokens = []

        if isinstance(text, str):
            self.tokens = self.tokenize(text)
        elif isinstance(text, list):
            self.tokens = text

    def tokenize(self, text):
        tokens = []
        token = ""
        for char in text:
            if char == " ":
                if token != "":
                    tokens.append(token)
                    token = ""
            else:
                token += char
        if token != "":
            tokens.append(token)
        return tokens

    def strain(self):
        for i in range(len(self.tokens)):
            try:
                self.tokens[i] = WobjectNumber(float(self.tokens[i]))
            
            except ValueError:
                
                if self.tokens[i] == "true":
                    self.tokens[i] = WobjectBoolean(True)
                elif self.tokens[i] == "false":
                    self.tokens[i] = WobjectBoolean(False)
                elif self.tokens[i] == "null":
                    self.tokens[i] = WobjectNull(None)
                elif self.tokens[i] == "undefined":
                    self.tokens[i] = WobjectUndefined(None)
                else:

                    if self.tokens[i] in ["+", "-", "*", "/", "%", "^", "!", "(", ")", "[", "]", "{", "}", ",", ".", ":", ";", "=", "<", ">", "&", "|", "~", "?"]:
                        self.tokens[i] = WobjectOperator(self.tokens[i])
                    else:
                        self.tokens[i] = WobjectString(self.tokens[i])

    def display(self):
        for token in self.tokens:
            print(token.value_, token.type_)
        

t = Tokenizer("345 + -98")
t.strain()
t.display()

