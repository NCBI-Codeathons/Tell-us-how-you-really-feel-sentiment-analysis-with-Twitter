# Tell-us-how-you-really-feel-sentiment-analysis-with-Twitter

Exploratory Case to see if twitter sentiment analysis informs NLM Consumer Health Group on how Consumers discussing health concerns; also inform positive/negative tweets to tailor NLM interactions with Consumers: trainings, campaigns,

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

Model Refinement:

increased the dimension 128; removed the drop out layer; prediction model quick check script 'i feel great' ; 'i don't feel well'--model works.

Apply to Reddit set (https://www.kaggle.com/amalinow/18000-reddit-comments-about-opioids)--reddit wierd data set; too much noise not sure how much about opioid; about pain in general.

DataSet 1: Three subanalyses of Flu (5K), Opioid (3K) Vaping ~5K worth of tweets vers1; looked at and labeling 0 negative; 1 positive X as neutral out of scope; label tweets that could information user needs/seeking (future prospective use) cleaning 
Repull get rid of duplicates; retweets Health Tweet training sets

Outcome: Twitter data is very dirty and noisy - dirty in that not complete words or sentences, contains emojicons which are not easy to interrept into sentiment; noisy as in tweets that are wrongly associated with hashtag subject areas, advertising for products, retweets adds bulk to the data set but they are duplicate. 
Figuring out how to best clean the data would need to be determined for tweets to be used. 

Plan to run Model Dataset 2: Health Twitter in News Headlines ( https://archive.ics.uci.edu/ml/datasets/Health+News+in+Twitter ) 63K instances titles titles have dates; sentiment time series to see if sentiment changes


