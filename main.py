import eel
from re import compile
# nltk.download('punkt')
from index import createPosIndex, createInvertedIndex
from query import queryPositionalIndex, queryInvertedIndex

# first create the positional and inverted indexes from short stories
createInvertedIndex()
createPosIndex()

eel.init("Web")
@eel.expose
def runQuery(query): # main function to process the query
    terms = query.split()
    if '/' in query:
        distance = terms[len(terms) - 1].split('/')[1]
        return queryPositionalIndex(terms[0], terms[1], distance)
    else:
        return queryInvertedIndex(query)

eel.start("index.html", size=(1200, 700))