import nltk
#nltk.download('punkt')#required for tokenizing
nltk.download("stopwords") #required to filter toke lists
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
example_string = """
... Muad'Dib learned rapidly because his first training was in how to learn.
... And the first lesson of all was the basic trust that he could learn.
... It's shocking to find how many people do not believe they can learn,
... and how many more believe learning to be difficult."""
worf_quote = "Sir, I protest. I am not a merry man!"

sentenceList = sent_tokenize(example_string) #splits up example string into its three sentences
print(sentenceList)
wordList = word_tokenize(example_string)
print(wordList)

words_in_quote = word_tokenize(worf_quote)
print(words_in_quote)
stop_words = set(stopwords.words("english"))
filtered_list = []
for word in words_in_quote:
    if word.casefold() not in stop_words:
        filtered_list.append(word)
print(filtered_list)