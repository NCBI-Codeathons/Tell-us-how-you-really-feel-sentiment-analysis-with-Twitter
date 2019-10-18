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
    print("python news.py tokenizer.pkl weights.03-0.42.hdf5 HIV plot.png Health-Tweets/bbchealth.txt")
    exit(0)


tk_file = sys.argv[1]
weights = sys.argv[2]
term = str(sys.argv[3])
img = sys.argv[4]

term = term.lower()

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

with open(tk_file, "rb") as fh:
    tk = pickle.load(fh)

max_len = 140
model = tf.keras.models.load_model(weights)

all = pd.DataFrame()
for i in range(5,len(sys.argv)):
    data = pd.read_csv(sys.argv[i], encoding='latin-1', header=None, names = ["id", "date", "text"], sep="|")
    data["text"] = data["text"].apply(lambda x : re.sub(r'AUDIO\:|VIDEO\:|http\S+', '', x))
    data["text"] = data["text"].apply(lambda x : str(x).lower())
    data.drop(["id"], axis=1, inplace=True)
    data["date"] = pd.to_datetime(data["date"])

    val_tokenized = tk.texts_to_sequences(data.text.values)
    X = pad_sequences(val_tokenized, maxlen=max_len)

    y = model.predict(X, verbose=0)
    data["sentiment"] = y
    selected = data[data.text.str.contains(term)]
    selected = selected.set_index(['date'])
    selected[sys.argv[i] + " trend"] = selected["sentiment"].rolling(5).mean()
    selected.drop(["text", "sentiment"], axis=1, inplace=True)
    all = pd.concat([all, selected], sort=False)

plt.figure()
all.plot()

plt.suptitle(term + " sentiment trends")
plt.savefig(img)



