from collections import Counter, defaultdict
from random import choice, choices


class TextGenerator:
    def __init__(self):
        self.tokens = []
        self.bigrams = []
        self.bigrams_w_tails_freq = {}
        self.random_text = []
        self.trigrams = []
        self.trigrams_w_tails_freq = {}
        self.main()

    def main(self):
        with open(input(), "r", encoding="UTF-8") as corpus:
            self.tokens = corpus.read().split()
        for i in range(len(self.tokens) - 1):
            self.bigrams.append((self.tokens[i], self.tokens[i + 1]))
        for i in range(len(self.tokens) - 2):
            self.trigrams.append((self.tokens[i] + " " + self.tokens[i + 1], self.tokens[i + 2]))
        self.bigrams_w_tails_freq = defaultdict(Counter)
        for head, tail in self.bigrams:
            self.bigrams_w_tails_freq[head][tail] += 1
        self.trigrams_w_tails_freq = defaultdict(Counter)
        for head, tail in self.trigrams:
            self.trigrams_w_tails_freq[head][tail] += 1
        self.generate_trigrams_sentences()

    def check_tokens(self):
        print("Corpus statistics")
        print("All tokens: ", len(self.tokens))
        print("Unique tokens: ", len(set(self.tokens)))
        while (x := input()) != "exit":
            try:
                print(self.tokens[int(x)])
            except IndexError:
                print("Index Error. Please input an integer that is in the range of the corpus.")
            except ValueError:
                print("Type Error. Please input an integer.")

    def check_bigrams(self):
        print("Number of bigrams: ", len(self.bigrams))
        while (x := input()) != "exit":
            try:
                head, tail = self.bigrams[int(x)]
                print(f"Head: {head}\tTail: {tail}")
            except IndexError:
                print("Index Error. Please input a value that is not greater than the number of all bigrams.")
            except ValueError:
                print("Typ Error. Please input an integer.")

    def chain_model(self):
        while (word := input()) != "exit":
            print("Head:", word)
            try:
                tails = self.bigrams_w_tails_freq[word]
                for tail, count in tails.most_common():
                    print(f"Tail: {tail}\tCount: {count}")
            except KeyError:
                print("The requested word is not in the model. Please input another word.")

    def generate_random_text(self):
        start = choice(self.tokens[:-1])
        self.random_text.append(start)
        while len(self.random_text) < 100:
            tails = self.bigrams_w_tails_freq[start]
            tail = []
            count = []
            for k, v in tails.most_common():
                tail.append(k), count.append(v)
            start = choices(tail, tuple(count))[0]
            self.random_text.append(start)
        for i in range(10):
            start = str(i) + "0"
            stop = str(i) + "9"
            sentence = self.random_text[int(start):int(stop) + 1]
            print(" ".join(sentence))

    def generate_full_sentences(self):
        for _ in range(10):
            full_sentences = []
            start = choice([x for x in self.tokens[:-1] if not x.islower() and x[-1] not in "….!?"])
            full_sentences.append(start)
            while len(full_sentences) < 5 or (full_sentences[-1][-1] not in ".?!"):
                tails = self.bigrams_w_tails_freq[full_sentences[-1]]
                tail = []
                count = []
                for k, v in tails.most_common():
                    tail.append(k), count.append(v)
                full_sentences += choices(tail, tuple(count))
            print(" ".join(full_sentences))
            
    def generate_bigrams_sentences(self):
        for _ in range(10):
            full_sentences = []
            start = choice([x for x in self.tokens[:-1] if not x.islower() and x[-1] not in "….!?"])
            full_sentences.append(start)
            while len(full_sentences) < 5 or (full_sentences[-1][-1] not in ".?!"):
                tails = self.bigrams_w_tails_freq[full_sentences[-1]]
                tail = []
                count = []
                for k, v in tails.most_common():
                    tail.append(k), count.append(v)
                full_sentences += choices(tail, tuple(count))
            print(" ".join(full_sentences))

    def generate_trigrams_sentences(self):
        new_bigrams = [x + " " + y for x, y in self.bigrams if x[-1] not in "….!?"]
        for _ in range(10):
            full_sentences = []
            x, y = choice([x for x in new_bigrams if x[0].isupper() and x[-1] not in "….!?"]).split()
            full_sentences.append(x)
            full_sentences.append(y)
            while len(full_sentences) < 5 or (full_sentences[-1][-1] not in ".?!"):
                tails = self.trigrams_w_tails_freq[full_sentences[-2] + " " + full_sentences[-1]]
                tail = []
                count = []
                for k, v in tails.most_common():
                    tail.append(k), count.append(v)
                full_sentences += choices(tail, tuple(count))
            print(" ".join(full_sentences))


if __name__ == '__main__':
    program = TextGenerator()
