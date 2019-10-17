# -*- coding: utf-8 -*-

# https://www.kaggle.com/kazanova/sentiment140
import pandas as pd
import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import re

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

data = pd.read_csv("training.1600000.processed.noemoticon.csv", encoding='latin-1', header=None, names = ["sentiment","id", "date", "query", "name", "text"]
)

#print(data[0].value_counts())

#nih = data[data[5].str.contains("nlm")]
#print(nih.shape)
data["text"] = data["text"].apply(lambda x : re.sub(r'@\w+|http\S+', '', x))
data["sentiment"] = data["sentiment"].apply(lambda x : 1 if x == 4 else 0)
train, test, validate = np.split(data.sample(frac=1), [int(0.8*len(data)), int(0.9*len(data))])
train.to_csv("train140.csv", index=False, encoding="utf-8")
test.to_csv("test140.csv", index=False, encoding="utf-8")
validate.to_csv("validate140.csv", index=False, encoding="utf-8")


