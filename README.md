## Tell-us-how-you-really-feel-sentiment-analysis-with-Twitter <img src="tweet-birs-2.svg" alt="tweeting bird" width="80" height="90">

### BUSINESS CASE
Pulling from [the NLM Jobjar project repository](https://sharepoint.nlm.nih.gov/Projects/jobjar/Lists/Associate%20Project%20Proposals/Browse%20Projects.aspx), **LO/PSD Online health information seeking: awareness and sentiment** to develop an exploratory methodology for twitter sentiment analysis and how that might inform the NLM Consumer Health Group on positive/negative tweets to contribute towards  NLM interactions with Consumers on various fronts such as awareness campaigns, trainings.

### MATERIALS AND METHODS
Training dataset for building the Model dataset: [Sentiment140 in Kaggle]https://www.kaggle.com/kazanova/sentiment140]
Sentiment140 dataset conTains 1,600,000 tweets extracted using the Twitter API. The tweets have been annotated (0 = negative, 4 = positive) and they can be used to detect sentiment.

### Building the model
Igor Sentiment 140 twitter 1.6 mill tweets; 
Recurrent Neural Network model applied to data standard DL state of the art RNN to use performs well; takes into account words in tweets and how combined together learn semantic meaning for each word and how they combined together model predicts into sentiment
stripped out URLS; https
stripped out @ ; 
modified sentiment scale from 0-4 to 0/1 (binary)
80% ~ 1.2 million tweets 
Trained the model on 1.2 mill tweets
Model: embedding layer with 64 dimension
Bidirectional LSTM 64 dimension 
Bi LSTM layer 32
fully connected layer with 64 dimensional output
dropout .5 regularization method standard approach keep model from overfeeding
output layer single sigmoid function (generates output representing between 0-1 )

train overnight 80% accuracy ~1.0 training data 12K tweets (1K regular intervals)

20% leftover run validation20% validation set accuracy 80%

### Model Refinement:

training increased the dimension 128; removed the drop out layer; prediction model quick check script 'i feel great' ; 'i don't feel well'--model works.

### Data on which we ran Model

### Health News in Twitter dataset (UCI Machine Learning Repository
( https://archive.ics.uci.edu/ml/datasets/Health+News+in+Twitter ). The data was collected in 2015 using the Twitter API. It contains health news from more than 15 major health news agencies such as BBC, CNN, and NYT - so the majority fo the tweets are direct headlines from news sories published online. 63K instances of titles have dates. Because of this, we will exaamine sentiment  and time series to see if sentiment changes. 


Ran Model for sentiment analysis


profit/nonprofit

ebola
![alt text](ebola-profit-nonprofit.png

cancer
![alt text](cancer-profit-nonprofit.png)



### Exploratory Datasets for Cleaning Analysis from Twitter

#### Dataset 1 - Health specific tweets from TWitter API
Three subanalyses of Flu (5K), Opioid (3K) Vaping ~5K worth of tweets were accessed from the Twitter API for over the past 7 days. Flu and Opioid were downloaded into seperate spreadsheets. Vaping was accessed and explored directly through the API. 

Flu and Opioid sets were examined manually to learn the nature of the tweets and to devise a cleaning strategy. The following fields were Twitter were brought into the spreadsheet: the Tweet text, polarity, subjectivity, and location. In additon, the humans labeled each tweet as: 0 negative; 1 positive; or X as neutral or out of scope.

#### Flu (5K)
We filtered through the data to see if the data is usable for determining if it would be useful for consumer health, and usable int he model. As a genarlization, most of the posts that wre not out of scope were about people discussing getting the flu shot. There was a large amount of medicine advertisment. 

#### Opioid (3K)
The opioid set contains 5,001 tweets. After filtering out duplicate tweets, the set was reduced to 

#### Vaping (5K)

Outcome of examining the Twitter data: It quickly became aparant that Twitter data is very dirty and noisy - dirty in that not Tweets are contain incomplete words, user generated abbreivations for common words, sentences and phrases that are not complete thoughts, contains emojicons which are not easy to interrept into sentiment; noisy as in Tweets that are wrongly associated with hashtag subject areas, advertising for products, retweets adds bulk to the data set because they are duplicate. 

Future considerations: There are many Twitter libraries that are avaible to reduce unnessicary data in tweets such slang, various spellings of a word, etc. Figuring out how to best clean the data for consumer health level health terms would need to be determined for tweets to be used for sentiment anaylsis.

### Reddit Dataset
The 18,000+ Reddit Comments About Opioids set from Kaggle (https://www.kaggle.com/amalinow/18000-reddit-comments-about-opioids)was exaimined. It also presented issues with noise and dirt. The comments were very private and seemed to be off-topic. Some were about general pain.

Future considerations: Much like Twitter, a plan to best clean the data would need to be devised and tested.

### Biostars Dataset
Used the Biostars API to bring in information into Pyhton. We caputured post, title, and comment text - we used 100,000 post. We filtered with 9 key words: SPR; BLAST; GeneBank; RefSeek; PubMed; PMC; CDD; PubChem; SRAtoolkit. Output will be saved in .csv to be used in the model. 

### OUTCOMES


### FUTURE CONSIDERSATIONS:

Biostars json data--still 

Ryan Connor suggested blogs to try:

random assortment of science blog things that may or may not be useful:
https://python.gotrained.com/tf-idf-twitter-sentiment-analysis/
http://www.rna-seqblog.com/
https://mirnablog.com/
http://www.lncrnablog.com/
https://www.bioinformatics.org/news/?group_id=10&summaries=1
https://www.reddit.com/r/flu/
https://www.reddit.com/r/bioinformatics/
https://www.reddit.com/r/librarians/


## Acknowledgments: Thanks to Victor CID for sharing his personal Twitter account information for our use.

### Team
Laura Bartlett - LO/OET

Frances Devanbu - NCBI/CSD

Igor Filippov - NCBI/IEB

Anna Ripple - LHC/CgSB

Toshu Takamaru- LO/TSD/CaMMS
