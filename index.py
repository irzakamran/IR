import json
import os
from collections import defaultdict
from nltk import word_tokenize
from util import tokenise, porter, stopWords
from re import compile

pattern = compile(r"[\d+\W]")

# creates positional index for short story documents
def createPosIndex():
    positionalIndex = defaultdict(list)
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    folder_path = __location__ + '/ShortStories/'
    x = os.listdir(folder_path)
    for filename in x:
        with open(folder_path + filename, 'r') as f:
            text = f.read()
            text = pattern.sub(" ", text).lower()  # remove punctuation and make lowercase
            tokens = [porter.stem(word) for word in word_tokenize(text)]  # tokenise
            filename = filename[:-4]  # remove .txt
            for i in range(len(tokens)):
                if tokens[i] not in positionalIndex:  # if token is not in positionalIndex
                    positionalIndex[tokens[i]] = {filename: [i]}
                elif filename in positionalIndex[tokens[i]]:  # if the filename is in positionalIndex
                    positionalIndex[tokens[i]][filename].append(i)
                else:
                    positionalIndex[tokens[i]][filename] = [i]
                    # stop words removed at the end to maintain original position of tokens with stop words
            for word in stopWords:  # remove stop words
                if word in positionalIndex:
                    del positionalIndex[word]

    with open("positionalIndex.json", "w") as f1: # write index to json file
        json.dump(positionalIndex, f1)

# creates inverted index for short story documents
def createInvertedIndex():
    invertedIndex = defaultdict(list)
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    folder_path = __location__ + '/ShortStories/'
    x = os.listdir(folder_path)  # get all files in folder
    for filename in x:
        with open(folder_path + filename, 'r') as f:
            text = f.read()
            text = pattern.sub(" ", text).lower()  # remove punctuation and make lowercase
            tokens = tokenise(text)
            filename = filename[:-4]  # remove .txt
            for token in tokens:
                if not invertedIndex[token]:  # if token is not in invertedIndex
                    invertedIndex[token].append(filename)
                elif invertedIndex[token][-1] != filename:  # if current filename not in list
                    invertedIndex[token].append(filename)
    with open("simpleindex.json", "w") as f1:  # write index to json file
        json.dump(invertedIndex, f1)


def readInvertedIndex():
    invertedIndex = {}
    with open("simpleindex.json", "r") as f:
        invertedIndex = json.load(f)
    return invertedIndex


def readPositionalIndex():
    positionalIndex = {}
    with open("positionalIndex.json", "r") as f:
        positionalIndex = json.load(f)
    return positionalIndex
