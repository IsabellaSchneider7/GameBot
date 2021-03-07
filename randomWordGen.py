from random_word import RandomWords
r = RandomWords()


def get_rand_phrase():
    word1 = r.get_random_word(includePartOfSpeech="noun", minCorpusCount = 9, minDictionaryCount=30)
    word2 = r.get_random_word(includePartOfSpeech="verb", excludePartOfSpeech= "noun, adjective", minCorpusCount=15, minDictionaryCount=40)
    word3 = r.get_random_word(includePartOfSpeech="adjective", minCorpusCount = 15, minDictionaryCount=50)
    return (str(word1) + " " + str(word2) + " "+ str(word3))

for i in range(10):
    print(get_rand_phrase())
