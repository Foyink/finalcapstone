import spacy
nlp = spacy.load(
'en_core_web_md'
)
word1 = nlp(
"cat"
)
word2 = nlp(
"monkey"
)
word3 = nlp(
"banana"
)
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
#Based on the scores, we can interpret that "cat" and "monkey"
# are more similar in meaning compared to "banana" and "monkey,"
# while "banana" and "cat" have the lowest similarity score,
#suggesting they are the least similar in meaning among the three word pairs.