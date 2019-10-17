# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
import re
import sys
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

if len(sys.argv) < 6:
    print("python news.py Health-Tweets/bbchealth.txt tokenizer.pkl weights.03-0.42.hdf5 HIV plot.png")
    exit(0)

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

data = pd.read_csv(sys.argv[1], encoding='latin-1', header=None, names = ["id", "date", "text"], sep="|")


data["text"] = data["text"].apply(lambda x : re.sub(r'AUDIO\:|VIDEO\:|http\S+', '', x))
data.drop(["id"], axis=1, inplace=True)
data["datetime"] = pd.to_datetime(data["date"])
data["date"] = data["datetime"]

with open(sys.argv[2], "rb") as fh:
    tk = pickle.load(fh)

max_len = 140
val_tokenized = tk.texts_to_sequences(data.text.values)
X = pad_sequences(val_tokenized, maxlen=max_len)

model = tf.keras.models.load_model(sys.argv[3])

y = model.predict(X, verbose=0)
data["sentiment"] = y

selected = data[data.text.str.contains(str(sys.argv[4]))]
selected = selected.set_index(['datetime'])
print(selected.head())
selected["trend"] = selected["sentiment"].rolling(5).mean()

selected.plot(x="date", y="trend")
plt.suptitle(str(sys.argv[4]) + " sentiment trends")
plt.savefig(sys.argv[5])



