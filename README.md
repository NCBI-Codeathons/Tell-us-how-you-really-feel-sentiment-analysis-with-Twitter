# Tell-us-how-you-really-feel-sentiment-analysis-with-Twitter

## Exploratory Case
to see if twitter sentiment analysis informs NLM Consumer Health Group on how Consumers discussing health concerns; also inform positive/negative tweets to tailor NLM interactions with Consumers: trainings, campaigns,

## Train dataset
dataset: provided by Sentiment140 in Kaggle
https://www.kaggle.com/kazanova/sentiment140

Context
This is the sentiment140 dataset. It contains 1,600,000 tweets extracted using the twitter api . The tweets have been annotated (0 = negative, 4 = positive) and they can be used to detect sentiment .

Content
It contains the following 6 fields:

target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
ids: The id of the tweet ( 2087)
date: the date of the tweet (Sat May 16 23:58:44 UTC 2009)
flag: The query (lyx). If there is no query, then this value is NO_QUERY.
user: the user that tweeted (robotickilldozr)
text: the text of the tweet (Lyx is cool)

The Kaggle data set comes from http://help.sentiment140.com/home. Sentiment140 was created by Alec Go, Richa Bhayani, and Lei Huang, who were Computer Science graduate students at Stanford University. Sentiment140 allows you to discover the sentiment of a brand, product, or topic on Twitter.

## Building the model
10/17/19 Igor Sentiment 140 twitter 1.6 mill tweets; 
Recurrent Neural Network model applied to data
stripped out URLS; https
stripped out @
modified sentiment scale from 0-4 to 0/1 (binary)
80% ~ 1.2 million tweets 
Trained the model on 1.2 mill tweets
Model: embedding layer with 64 dimension
Bidirectional LSTM 64 dimension 
Bi LSTM layer 32
fully connected layer with 64 dimensional output
dropout .5 regularization method standard approach keep model from overfeeding
output layer single sigmoid function (generates output representing between 0-1 )
train overnight 80% accuracy ~1.0 training data 12K tweets

~600K unique words; vectorized setting small; fast tensor flow recipe 
Standard Recurrent Neural Network Methodology

## Model Refinement:

increased the dimension 128; removed the drop out layer; prediction model quick check script 'i feel great' ; 'i don't feel well'--model works.


## Data we ran
### Dataset 1 - Health specific tweets from TWitter API
Three subanalyses of Flu (5K), Opioid (3K) Vaping ~5K worth of tweets were accessed from the Twitter API for over the past 7 days. Flu and Opioid were downloaded into seperate spreadsheets. Vaping was accessed and explored directly through the API. 

Flu and Opioid sets were examined by humand to lern more baout the nature of the tweets and to devise a cleaning strategy. The following fields were Twitter were brought into the spreadsheet: the Tweet text, polarity, subjectivity, and location. In additon, the humans labeled each tweet as: 0 negative; 1 positive; or X as neutral or out of scope.

#### Flu

#### Opioid

#### Vaping

Outcome: It quickly became aparant that Twitter data is very dirty and noisy - dirty in that not Tweets are contain incomplete words, user generated abbreivations for common words, sentences and phrases that are not complete thoughts, contains emojicons which are not easy to interrept into sentiment; noisy as in Tweets that are wrongly associated with hashtag subject areas, advertising for products, retweets adds bulk to the data set because they are duplicate. 

Future considerations: There are many Twitter libraries that are avaible to reduce unnessicary data in tweets such slang, various spellings of a word, etc. Figuring out how to best clean the data for consumer health level health terms would need to be determined for tweets to be used for sentiment anaylsis.

### Dataset 2
The 18,000+ Reddit Comments About Opioids set from Kaggle (https://www.kaggle.com/amalinow/18000-reddit-comments-about-opioids)was exaimined. It also presented issues with noise and dirt. The comments were very private and seemed to be off-topic. Some were about general pain.

Outcome: Two comments were run throgh the model to test ofr valdity. 

Future considerations: Much like Twitter, a plan to best clean the data would need to be devised and tested.

### Dataset 3
The Health News in Twitter dataset was accessed from UCI Machine Learning Repositiory ( https://archive.ics.uci.edu/ml/datasets/Health+News+in+Twitter ). The dataset incldues tweets from major news organziations - so the majority fo the tweets are direct headlines from news sories published online. 63K instances titles titles have dates; sentiment time series to see if sentiment changes

Outcome:

### Dataset 4
Biostars json data








### Team
Laura Bartlett - LO/OET

Frances Devanbu - NCBI/CSD

Igor Filippov - NCBI/IEB

Anna Ripple - LHC/CSB

Toshu Takamaru- LO/TSD/CaMMS
