from index import readInvertedIndex
from util import tokenise, convertToIntList, prec, peek, doOperation, isNotOperator

invInd = readInvertedIndex()

# evaluate postfix expression
def postfixEval(postfixList):
    operandStack = []
    for token in postfixList:
        if token in invInd and token != "not" and token != "or":  # if token is a word
            operandStack.append(set(invInd[token]))
        elif token == "not":
            operand = operandStack.pop()
            result = getAllDocsWithoutOperand(operand) 
            operandStack.append(result)
        elif token == "and" or token == "or":
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doOperation(token, operand1, operand2)
            operandStack.append(result)
        else:  # if token not an operand and also not in index
            operandStack.append(set())  # empty set
    if peek(operandStack) == set():
        operandStack.pop()
        return "Term(s) not in any of the documents"
    docsList = convertToIntList(list(operandStack.pop()))
    docsList.sort()
    return docsList


# convert infix expressions to postfix
def infixToPostfix(infixexpr):
    opStack = []  # stack structure for operators
    postfixList = []
    tokenList = infixexpr.split()
    for i in range(len(tokenList)):
        if isNotOperator(tokenList[i]):
            tokenList[i] = tokenise(tokenList[i])
    for token in tokenList:
        if isNotOperator(token) and token != "(" and token != ")":
            postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            top = opStack.pop()
            while top != '(':
                postfixList.append(top)
                top = opStack.pop()
        elif not isNotOperator(token):
            while (peek(opStack)) and (prec[peek(opStack)] >= prec[token]): # if the precedence of the top of the stack is >= the precedence of the token
                postfixList.append(opStack.pop())
            opStack.append(token)
    while opStack:
        postfixList.append(opStack.pop())
    return postfixList


# returns list of documents without the given operand 
def getAllDocsWithoutOperand(operand):
    result = list()
    i = 1
    while i <= 50:
        if str(i) not in operand:
            result.append(str(i))
        i += 1
    return set(result)



