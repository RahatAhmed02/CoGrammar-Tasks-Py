
# Find at least 2 garden path sentences from the web, or think up your own.
# 
# Store the sentences you have identified or created in a list called gardenpathSentences.
# 
# Add the following sentences to your list:
# 
# - Mary gave the child a Band-Aid.
# - That Jill is never here hurts.
# - The cotton clothing is made of grows in Mississippi.

import spacy
nlp = spacy.load("en_core_web_sm")

gardenpathSentences = [
    "Scottish miners refuse to work after death.",
    "Hospitals sued by 7 foot doctors.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]


# Tokenize each sentence in the list, and perform named entity recognition.

for sentence in gardenpathSentences:
    doc = nlp(sentence)

    print([token.orth_ for token in doc if not token.is_punct | token.is_space])
    
    print([(i, i.label_, i.label) for i in doc.ents])


# Examine how SpaCy has categorised each sentence. Then, use spacy.explain to look up and print the meaning of entities that you don't understand. 
# For example: print(spacy.explain("FAC"))

print(f"NORP: {spacy.explain('NORP')}")
print(f"GPE: {spacy.explain('GPE')}")
print(f"PERSON: {spacy.explain('PERSON')}")
print(f"QUANTITY: {spacy.explain('QUANTITY')}")

# At the bottom of your file, write a comment about two entities that you looked up. For each entity answer the following questions:
# 
# - What was the entity and its explanation that you looked up?
# - Did the entity make sense in terms of the word associated with it?

# NORP:
# The NORP entity is for nationalities, religious or political groups
# The entity was used to categorise the word "Scottish", this contextually makes sense
# Scottish is indeed a nationality used to describe people from Scotland

# GPE:
# The GPE entity is for countries, cities and states
# The entity was used to categorise the word "Mississippi"
# Mississippi is a state in USA

