# Coding Tasks - Customer Sentiment Analysis using NLP
This coding task exercises was created in the course of my Data Science Bootcamp with HyperionDev.

## Table fo Contents
[Description](https://github.com/CatherineSchalbroeck/codingTasks/edit/main/README.md#description)<br>
[How to install](https://github.com/CatherineSchalbroeck/codingTasks/edit/main/README.md#how-to-install)<br>
[How to use](https://github.com/CatherineSchalbroeck/codingTasks/edit/main/README.md#how-to-use) <br>
[Credits](https://github.com/CatherineSchalbroeck/codingTasks/edit/main/README.md#credits) <br>
[License](https://github.com/CatherineSchalbroeck/codingTasks/edit/main/README.md#license)  

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
This model is built using the [Customer Reviews data from Amazon](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products) which is a .csv file. However, it can be used with any other Customer review data. To use this model with a different file, you can simply rename the target file in the code by replacing the file name in *'amazon_product_reviews.csv'*<br>
![image](https://github.com/CatherineSchalbroeck/codingTasks/assets/77054227/2a8c9df7-def5-4cf1-9b91-4455e975804b)<br>

Then you can either rename the review column in your csv file to *reviews.text* to match what is in the code, or you can update the code to the specific column name of your csv file's text review. For this, replace the text in quotation marks in code Line 50: *'reviews.text'*<br>
![image](https://github.com/CatherineSchalbroeck/codingTasks/assets/77054227/a93691a9-b521-4b62-8882-d678293e82e3)

## Credits
This model was built by myself with the support material provided by **HyperionDev** in my Task assignment.

## License
No license is required.
