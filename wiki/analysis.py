import re, string
import wikipedia
import nltk
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import FreqDist

#wikiSummary = wikipedia.summary("Python programming language")

#Tokenizing the Data
#wiki_tokens = nltk.word_tokenize(wikiSummary)

#Normalizing the Data
#wiki_normal = pos_tag(wiki_tokens)

#Clean and Normalize Data
def remove_noise(wiki_token, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(wiki_token):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens
#cleanData = remove_noise(wiki_tokens)

def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        #for token in tokens:
        yield tokens
#allwWords = get_all_words(cleanData)

"""
frequenceWords = FreqDist(allwWords)
mostCommon = frequenceWords.most_common(10)

convertoDict = dict(mostCommon)
convertToList = list(convertoDict.values())
"""

def final(text):
    wikiSummary = wikipedia.summary(text)
    wiki_tokens = nltk.word_tokenize(wikiSummary)
    cleanData = remove_noise(wiki_tokens)
    allwWords = get_all_words(cleanData)
    frequenceWords = FreqDist(allwWords)
    mostCommon = frequenceWords.most_common(10)
    convertoDict = dict(mostCommon)
    convertToList = list(convertoDict.values())
    return convertToList

"""
final = final("Wikipedia")
print(final)
"""







