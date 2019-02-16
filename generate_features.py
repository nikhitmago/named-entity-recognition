#!/bin/python
from collections import OrderedDict
import numpy as np
import glob

filenames = glob.glob("lexicon_features/*.npy")
for filename in filenames:
    globals()[filename[:-4]] = OrderedDict()

def preprocess_corpus(train_sents):
    global filename
    for filename in filenames:
        globals()[filename[:-4]] = np.load(filename).item()
    

def token2features(sent, i, add_neighs = True):
    ftrs = []
    # bias
    ftrs.append("BIAS")
    # position features
    if i == 0:
        ftrs.append("SENT_BEGIN")
    if i == len(sent)-1:
        ftrs.append("SENT_END")

    # the word itself
    word = unicode(sent[i])
    ftrs.append("WORD=" + word)
    ftrs.append("LCASE=" + word.lower())
    # some features of the word
    if word.isalnum():
        ftrs.append("IS_ALNUM")
    if word.isnumeric():
        ftrs.append("IS_NUMERIC")
    if word.isdigit():
        ftrs.append("IS_DIGIT")
    if word.isupper():
        ftrs.append("IS_UPPER")
    if word.islower():
        ftrs.append("IS_LOWER")
    
    #my features
    if word[0].isupper() and word[1:].islower():
        ftrs.append("IS_FIRST_LETTER_CAPITAL")
    global filename
    for filename in filenames:
        if globals()[filename[:-4]].get(word.lower(), -1) != -1:
            ftrs.append("IS_" + filename[:-4].upper())

    # previous/next word feats
    if add_neighs:
        if i > 0:
            for pf in token2features(sent, i-1, add_neighs = False):
                ftrs.append("PREV_" + pf)
        if i < len(sent)-1:
            for pf in token2features(sent, i+1, add_neighs = False):
                ftrs.append("NEXT_" + pf)

    # return it!
    return ftrs

if __name__ == "__main__":
    sents = [
    [ "I", "love", "Food", "Mark"]
    ]
    preprocess_corpus(sents)
    for sent in sents:
        for i in xrange(len(sent)):
            print sent[i], ":", token2features(sent, i)
