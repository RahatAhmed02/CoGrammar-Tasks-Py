# Import necessary libraries
import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob

# Initialise spaCy with 'en_core_web_sm' model and add SpacyTextBlob component to pipeline
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

# Initialise a separate spaCy model 'en_core_web_md' for computing similarity as it includes word vectors
nlpx = spacy.load('en_core_web_md')

# Load reviews from a CSV file and remove rows where the 'reviews.text' column is empty
df = pd.read_csv('amazon_product_reviews.csv', sep=',')
reviews_data = df['reviews.text'].dropna()

# Understand the size of the data frame
print(df.shape)

# Function to clean reviews
def clean_reviews(product_reviews):
    # Dictionary to store cleaned reviews
    cleaned_reviews = {}
    
    # Loop over the reviews data using the index
    for index in product_reviews.index:
        review = product_reviews[index]
        # Process the text of the review with spaCy
        doc = nlp(review)
        # List of tokens stripped, lower case, no stop words, no punctuation, no whitespace
        cleaned_review = [
            token.text.strip().lower() for token in doc 
            if not token.is_stop and not token.is_punct and not token.text.isspace()
        ]
        
        # Join the tokens back into a string and store in a dictionary with the review's index as the key
        cleaned_reviews[index] = " ".join(cleaned_review)

    # Return the dictionary of 'collected' cleaned tokens     
    return cleaned_reviews

# Function to perform sentiment analysis on the reviews
def sentiment_analysis(reviews):
    for key, value in reviews.items():
        # Process the text with spaCy
        doc = nlp(value)
        
        # Calculate polarity and assign mood based on the polarity score
        polarity = doc._.blob.polarity
        if -0.15 <= polarity <= 0.15:
            Mood = "Neutral"
        elif -1 <= polarity < -0.15:
            Mood = "Negative"
        elif 0.15 < polarity <= 1:
            Mood = "Positive"
            
        # Print the review, its sentiment, and mood
        print(f"\nReview: {key}, {value}")
        print(f"Sentiment: {doc._.blob.sentiment}")
        print(f"Mood: {Mood}")

# Sample of reviews to analyse to reduce computational load
reviews_data_sample = reviews_data.iloc[[1, 25, 54, 76, 100, 299, 804, 3202, 6043, 13598]]
        
# Perform sentiment analysis on the cleaned reviews
sentiment_analysis(clean_reviews(reviews_data_sample))

# Select two specific reviews to compare for similarity
first_review = reviews_data[34]
second_review = reviews_data[18754]

# Define a function to calculate the similarity between two reviews
def similarity_analysis(review_1, review_2):
    # Calculate the similarity score between the two spaCy documents using 'en_core_web_md' for word vectors
    similarity_score = nlpx(review_1).similarity(nlpx(review_2))
    
    # Return the calculated similarity score
    return similarity_score

# Perform similarity analysis on the selected reviews and print the results
print(f"\nFirst Review: {first_review}")
print(f"Second Review: {second_review}")
print(f"Similarity: {similarity_analysis(first_review, second_review)}")
