# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import pickle
import sys

if len(sys.argv) < 4:
    print("python predict.py input.txt tokenizer.pkl weights.03-0.42.hdf5")
    exit(0)

with open(sys.argv[1], "r") as fh:
    text = fh.read().splitlines()
with open(sys.argv[2], "rb") as fh:
    tk = pickle.load(fh)

max_len = 140
val_tokenized = tk.texts_to_sequences(text)
X = pad_sequences(val_tokenized, maxlen=max_len)

model = tf.keras.models.load_model(sys.argv[3])

y = model.predict(X, verbose=0)

for i,s in enumerate(y):
    print(s[0]," ",text[i])


