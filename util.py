from nltk import word_tokenize, PorterStemmer
porter = PorterStemmer()
stopWords = ['a', 'is', 'the', 'of', 'all', 'and', 'to', 'can', 'be', 'as', 'once', 'for', 'at', 'am', 'are', 'has',
             'have', 'had', 'up', 'his', 'her', 'in', 'on', 'no', 'we', 'do']

prec = {"not": 3, "and": 2, "or": 1, "(": 0}  # define precendence of operators

# creates tokens from string using porter stemmer
def tokenise(text):
    tokens = [porter.stem(word) for word in word_tokenize(text) if word not in stopWords]
    if len(tokens) == 0:
        return
    elif len(tokens) == 1:
        return tokens[0]
    return tokens


# values in positional/inverted index are in string format and have to be converted to int
def convertToIntList(list):
    for a in range(len(list)):
        list[a] = int(list[a])
    return list

# this will get the last element of stack
def peek(stack):
    if stack:
        return stack[-1]  
    else:
        return None

# performs intersection or union of two sets based on operator value
def doOperation(operator, operand1, operand2):
    if operator == "or":
        return operand1.union(operand2)
    elif operator == "and":
        return operand1.intersection(operand2)
   
def isNotOperator(token):
    return token != 'and' and token != 'or' and token != 'not'

def isWithinDistance(posTerm1, posTerm2, distance):
    return abs(posTerm1 - posTerm2) - 1 <= int(distance)
