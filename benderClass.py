import yaml
import numpy as np

class bender():
    def __init__(self):
        super().__init__()
        stream = open('dialogues.yaml','r')
        dictionary = yaml.full_load(stream)
        stream.close()
        self.rand_quote = dictionary["BENDER"]
        self.a_quote = []; self.s_quote = []; self.p_quote = []; self.ap_quote = []; self.intro = []; self.greetings = []

        for quote in self.rand_quote:
            if "mad " in quote:
                self.a_quote.append(quote)
                self.rand_quote.remove(quote)
            if "sad " in quote:
                self.s_quote.append(quote)
                self.rand_quote.remove(quote)
            if "crying " in quote or "cry " in quote:
                self.p_quote.append(quote)
                self.rand_quote.remove(quote)
            if "sorry "in quote or "Sorry " in quote:
                self.ap_quote.append(quote)
                self.rand_quote.remove(quote)
            if "introduce " in quote:
                self.intro.append(quote)
                self.rand_quote.remove(quote)
            if "hello " in quote or "hi " in quote:
                self.greetings.append(quote)
                self.rand_quote.remove(quote)

if __name__ == "__main__":
    for i in bender().intro:
        print(i)