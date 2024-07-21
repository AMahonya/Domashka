class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.replace(',',
                                        '').replace('.',
                                                    '').replace('=',
                                                                '').replace('!',
                                                                            '').replace('?',
                                                                                        '').replace(
                        ';', '').replace(':', '').replace(' ', ' ')
                    words.extend(line.split())
            all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            positions = [i for i, w in enumerate(words) if w.lower() == word.lower()]
            if positions:
                result[name] = positions[0]
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            count = sum(1 for w in words if w.lower() == word.lower())
            if count > 0:
                result[name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
