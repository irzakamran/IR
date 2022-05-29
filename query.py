from exp_parsing import postfixEval, infixToPostfix
from index import readPositionalIndex
from util import tokenise, convertToIntList, isWithinDistance

posIndex = readPositionalIndex()

# queries the positional index
def queryPositionalIndex(term1, term2, distance):
    term1 = tokenise(term1)
    term2 = tokenise(term2)
    result = []
    if term1 in posIndex and term2 in posIndex:
        commonDocsList = convertToIntList(list(set(posIndex[term1].keys()).intersection(set(posIndex[term2].keys()))))
        commonDocsList.sort()
        for i in range(len(commonDocsList)):  # iterate over all common documents
            # lists of positions for term 1 and term 2 in doc
            posTerm1 = convertToIntList(list((posIndex[term1])[str(commonDocsList[i])]))
            posTerm2 = convertToIntList(list((posIndex[term2])[str(commonDocsList[i])]))
            posTerm1.sort()
            posTerm2.sort()
            x = y = 0  # index vars for posTerm1 and posTerm2
            while x < len(posTerm1) and y < len(posTerm2):  # while the end of both lists not reached
                if isWithinDistance(posTerm1[x], posTerm2[y], distance):
                    result.append(commonDocsList[i])
                    x += 1
                    y += 1
                    break
                elif posTerm1[x] < posTerm2[y]:
                    x += 1
                else:
                    y += 1
        return result


# queries the inverted index
def queryInvertedIndex(query):
    return postfixEval(infixToPostfix(query))


