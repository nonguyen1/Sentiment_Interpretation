# Sentiment/Emotion Analysis

Live depoloyment can be seen here.  
https://rocky-garden-38647.herokuapp.com

## To run locally
1. To run the server you will need to install some dependencies.
namely herokuCLI, Django, and postgresql installed 

1. Once you have all the dependencies simple run `heroku local web`. This will run the server locally.

1. Once the server is running head to `0.0.0.0:5000` in your perfered browser
1. Alternatively you can play with a live deployment at the link at the top of readme.

## Models
### Sentiment Analysis
Logistic Regression trained with 5 fold cross validation on 70k review sentences
Uses tdidf weights and bigrams.

We've tested trigrams and unigrams but found that bigrams worked best.

### Emotion Analysis
We trained a multiclass logistic regression model using 5 fold cross
validation on 40k Twitter tweets. The mode uses tdidf weights and bigrams.

We've experimented with trigrams and unigrams but again found bigrams worked
best.

The original dataset had 13 classes but we binned similar classes down to 5
total classes.
## Acknowledgement
The 'Emotion in Text' dataset by CrowdFlower