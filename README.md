# Coding Tasks - Customer Sentiment Analysis using NLP
This coding task exercises was created in the course of my Data Science Bootcamp with HyperionDev.

## Description
This is a Natural Language Processing model built to analyse the Sentiment of Customer Reviews. 
It returns a simple Sentiment output which is either:
- Positive,
- Negative, or
- Neutral

This model can be useful to classify Customer reviews in simple buckets which can then be used for further Data Analytics.

## How to install
Python 3 is required to run this model.
The following Python libraries will also need to be installed:
- SpaCy
- Random
- re
- Pandas
- Numpy

The model also uses *SpacyTextBlob* and the English language trained model from SpaCy: *en_core_web_sm*.

## How to use
This model is built using the [Customer Reviews data from Amazon](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products). However, it can be used with any other Customer review data. <br>

For this, the source file must be in .csv format and you can either rename the review column in your csv file to *reviews.text* or update the code to the specific name of your csv file's text review column.

## Credits
This model was built by myself with the support material provided by **HyperionDev** in my Task assignment.

## License
No license is required.
