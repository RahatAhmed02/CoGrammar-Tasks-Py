# Practical Task 1
# 
# 1) Create a file called semantic.py and run all the code extracts above.

import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - " + str(similarity))


# 2) Write a note on what you noticed about the similarities between cat, monkey and banana and think of an example of your own.

# Notes on similarities between 'cat', 'monkey' & 'banana':
# 
# The similarity score between 'cat' and 'monkey' is 0.59, which is relatively high. 
# This reflects that both terms are animals and share some contextual relationships in how they are used in language.
# 
# The similarity score between 'monkey' and 'banana' is 0.40, which is lower than 'cat' and 'monkey' but still significant.
# This is likely because monkeys are often associated with bananas in popular culture and discourse.
# 
# The similarity score between 'cat' and 'banana' is 0.22, which is quite low, indicating that these words are not closely related. 
# One is an animal and the other is a fruit, and are not often associated with each other so do not often appear in similar contexts.

# Example of my own

word4 = nlp("dog")
word5 = nlp("bark")
word6 = nlp("tree")

print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))


# 3) Run the example file on with the simpler language model en_core_web_sm 
# and write a note on what you notice may be different from the model en_core_web_md

# Notes on en_core_web_sm vs en_core_web_md:
# 
# The smaller en_core_web_sm model lacks word vectors, 
# which means it won't be as effective at capturing semantic similarities as the en_core_web_md model, 
# which includes word vectors for a more nuanced understanding of text. 
# Therefore, when you compare texts for similarity using the en_core_web_sm model, 
# you notice that the similarity scores are different—potentially less accurate or lower—than those produced by the en_core_web_md model. 
# This difference would be due to the en_core_web_sm model's reliance on the context of surrounding words alone, 
# without the benefit of word vectors to enhance its understanding of the text.
# Word vectors are numerical representations of words that capture their 
# meanings, relationships, and context, allowing computers to understand language similarly to humans.

# Practical Task 2

# Read in the movies.txt file. Each separate line is a description of a different movie.

import pandas as pd

# Reading text file as a DataFrame with ':' as the separator. The file is assumed to have no header.
df = pd.read_csv('movies.txt',sep=':', header=None, names=['Movie', 'Description'])

print(df)


# Your task is to create a function to return which movies a user would watch next if they have watched Planet Hulk 
# with the descrtiption "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
# the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
# Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# A multiline string containing the description of the movie "Planet Hulk".
Planet_Hulk = """
Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.
"""


# The function should take in the description as a parameter and return the title of the most similar movie.

# Defining a function to recommend a movie based on a given description.
def recommend_movie(input_description):
     # Processing the input description with a nlp.
    input_doc = nlp(input_description)
    # Initialising two variables to track similarity score and movie title.
    recommended_similarity = 0
    movie_title = None
    
     # Iterating over each row in the DataFrame to compare the input description with each movie description.
    for index, row in df.iterrows():
        movie_description = nlp(row['Description'])
        # Calculating the similarity between the input description and the current movie description.
        local_similarity = input_doc.similarity(movie_description)
        
          # If current similarity score is higher than the highest score found so far, update the highest score.
        if local_similarity > recommended_similarity:
            recommended_similarity = local_similarity
            movie_title = row['Movie']
    
    # Returning the title of the most similar movie and the similarity score.
    return movie_title, recommended_similarity

# Calling the recommend_movie function with the description of "Planet Hulk".
recommend_movie(Planet_Hulk)



