class STEMMING:

    def __init__(self, all_words):
        self.words = all_words

        self.deleting_x()
        self.deleting_else()

    def deleting_x(self):

        for word in self.words:
            i = self.words.index(word)

            if word[-1:] == "x":
                if word[-3:] == "aux":
                    self.words[i] = word[:-3] + "al"
                else:
                    self.words[i] = word[:-1]

    def deleting_else(self):

        ends_fr = ["s", "r", "e", "é", "ement", "ament", "tion", "ption", "x", "aux", "al"]


        for word in self.words:
            i = self.words.index(word)
            for element in ends_fr:
                p = len(element)
                if word[-p:] == element:
                    self.words[i] = word[:-p]


    def show_words(self):
        return self.words




