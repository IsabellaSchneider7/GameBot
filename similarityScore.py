import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import numpy
def compare_sentence(A, B):
    score = 0
    A_list = word_tokenize(A.lower())
    B_list = word_tokenize(B.lower())

    # sw contains the list of stopwords
    sw = stopwords.words('english')

    # remove stop words from the string
    newA_list = []
    newB_list = []
    for item in A_list:
        if not item in sw:
            newA_list.append(item)
    for item in B_list:
        if not item in sw:
            newB_list.append(item)
    # form a set containing keywords of both strings
    same_list = list(set.intersection(set(newA_list), set(newB_list)))
    score += 100*len(same_list)/len(newA_list)
    score += get_synonyms(newA_list, newB_list, same_list)
    print(score)
    return score

def get_synonyms(A_list, B_list, same_list):
    add_score = 0
    for item in A_list:
        syn_list = []
        if not item in same_list:
            syns = wordnet.synsets(item)
            for syn in syns:
                for l in syn.lemmas():
                    syn_list.append(l.name())

            for word in syn_list:
                if word in B_list:
                    add_score += 75*1/(len(A_list))
                    break
            print(syn_list)

    return add_score

#compare_sentence("house dog cats happy", "home dog cat glad")