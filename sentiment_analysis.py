'''
================================
Importing Libraries and Dataset
================================
'''
# Importing libraries
import pandas as pd
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import re
import random

# TextBlob
from textblob import TextBlob
from spacytextblob.spacytextblob import SpacyTextBlob


# import the dataset
df = pd.read_csv('amazon_product_reviews.csv')





'''
==================
IMPLEMENTING MODEL
==================
'''
# Loading the English language trained model using SpaCy
nlp = spacy.load("en_core_web_sm")

# Add SpacyTextBlob to the pipeline
nlp.add_pipe('spacytextblob')





'''
==================
DATA PREPROCESSING
==================

We retrieve the 'reviews.text' data from the cleaned dataset, 
because we don't need the other features for our Sentiment Analysis.
'''
# Create dataframe with only the 'reviews.text' feature
reviews_data = df['reviews.text']

# Removing potential missing values from the new dataframe
clean_data = reviews_data.dropna()



# Creating a Preprocessing Function to clean up the dataset
# This will help improve our Sentiment Analysis model.
def preprocess_text(msg):

    # Create a spaCy document
    doc = nlp(msg)
    msg = re.sub('[^A-Za-z]+', ' ', str(msg)) # replace any sequence of non-letters with a space
    
    # Remove stopwords, punctuation, digits, and currency
    filtered_tokens = [token for token in doc if not token.is_stop and not token.is_punct and not token.is_digit and not token.is_currency]
    
    # Lemmatize the tokens
    lemmatized_tokens = [token.lemma_.lower() for token in filtered_tokens]
    
    # Join the lemmatized tokens back into a string
    preprocessed_text = ' '.join(lemmatized_tokens)
    
    return preprocessed_text


# Apply Preprocessing Function to dataset, 
# NOTE: This may take more than 3mins
clean_data.apply(preprocess_text)





'''
==================
SENTIMENT ANALYSIS
==================
'''
# Function performing Sentiment Analysis
def analyze_sentiment(msg):
    # Create a spaCy document
    doc = nlp(msg)
    
    # Get the sentiment polarity and sentiment
    polarity = doc._.blob.polarity
    sentiment = doc._.blob.sentiment
    
    # Determine the sentiment label
    if polarity > 0:
        result = 'Positive'
    elif polarity < 0:
        result = 'Negative'
    else:
        result = 'Neutral'
    
    return result, sentiment


'''
TESTING
-------


create FUNCTION that:

    creates 5 random numbers in range of dataset 

    iterate 'num' through the random numbers selected 
        each num value to select an item i in the dataset of that index [num]
        test the model 'analyze_sentiment' on that item[num]

    print the 'analyze_sentiment' result and [num] index review number
    print the item[num]

'''

# Function that tests a given number of reviews taken randomly in the dataset
def Test_random_reviews(number):
    # Get list of n random numbers
    my_rand = random.sample(range(1, len(clean_data)+1),number) # Select a defined number of random numbers in a range of the size of the dataset

    # Iterate each random number as the index of our dataset and run the sentiment function score
    for num in my_rand:
        choice = clean_data[num]
        
        # Print Sentiment analysis score
        print("Sentiment score for Product review #",num,": ",analyze_sentiment(choice)) 

        # Print original Review to check the validity of the Sentiment analysis
        print("Review: ",clean_data[num],"\n")


# Test Sentiment analysis on 2 random reviews from the dataset
Test_random_reviews(2)

'''
A polarity of 1 = very positive sentiment
A polarity of 0 = very neutral sentiment
A polarity of -1 = very negative sentiment
'''





'''
===================
SEMANTIC SIMILARITY
===================
Let's compare the semantic simnilarity between two reviews.
'''

# Function to run similarity score
def calculate_similarity (rev1, rev2):

    # process the sentences to obtain Doc objects
    doc1 = nlp(rev1)
    doc2 = nlp(rev2)

    # Access the vector representations of the entire reviews.
    embedding1, embedding2 = doc1.vector, doc2.vector

    # Calculate the similarity between each review
    similarity = doc1.similarity(doc2)

    # Print the similarity
    print("Similarity between the two reviews: ", similarity)


# Choosing two reviews to compare
my_review_of_choice_1 = clean_data[6]
my_review_of_choice_2 = clean_data[41]

# Run the function to get similarity score between chosen reviews
calculate_similarity(my_review_of_choice_1,my_review_of_choice_2)

'''
If similarity score is close to 1: it means both reviews are very similar.
If similarity score is close to 0: it means both reviews are very different. 
'''