import json

class TOKENIZE:

    def __init__(self, text):
        self.text = text
        self.all_sentences = []
        self.sentence = ""
        self.new_text = ""
        self.all_words = []
        self.tokenize_matrix = []

        stopwords = open('../assets/stopwords/stop_words_french.json', 'r')
        self.stopwords = json.load(stopwords)

        self.text_to_sentences()

    def text_to_sentences(self):
        end_sentence = ['!', '?', '.', ':']

        for car in self.text:
            if car in end_sentence:
                self.sentence = self.text.split(car, 1)[0]
                self.new_text = self.text.split(car, 1)[1]
                self.all_sentences.append(self.sentence)
                self.text = self.new_text

        self.tokenize()

    def remove_stopwords(self):
        temp_list = [word for word in self.all_words if (word.lower() not in self.stopwords and word != "")]
        return temp_list

    def tokenize(self):

        words_occ = {}

        for sentence in self.all_sentences:
            words = sentence.strip(" ").split(" ")
            self.all_words += words

        self.all_words = self.remove_stopwords()

        for sentence in self.all_sentences:
            for e in self.all_words:
                if e in sentence:
                    if e in words_occ:
                        words_occ[e] += 1
                    else:
                        words_occ[e] = 1
                else:
                    words_occ[e] = 0

            occurences = list(words_occ.values())
            self.tokenize_matrix.append(occurences)

    def show_sentences(self):
        return self.all_sentences, self.tokenize_matrix, self.all_words
