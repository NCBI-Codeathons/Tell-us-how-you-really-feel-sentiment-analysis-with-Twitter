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
    print("python evaluate.py validate140-1000.csv tokenizer.pkl weights.03-0.42.hdf5")
    exit(0)

data = pd.read_csv(sys.argv[1])
with open(sys.argv[2], "rb") as fh:
    tk = pickle.load(fh)

max_len = 140
val_tokenized = tk.texts_to_sequences(data['text'].values)
X = pad_sequences(val_tokenized, maxlen=max_len)
y = data['sentiment'].values

model = tf.keras.models.load_model(sys.argv[3])

test_loss, test_acc = model.evaluate(X,y)

print('Test Loss: {}'.format(test_loss))
print('Test Accuracy: {}'.format(test_acc))
