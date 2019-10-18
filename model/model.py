# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import pickle

data = pd.read_csv("train140.csv")

max_len = 140 
tk = Tokenizer(oov_token="UNK")
tk.fit_on_texts(data['text'].values)
train_tokenized = tk.texts_to_sequences(data['text'].values)
X = pad_sequences(train_tokenized, maxlen=max_len)
y = data['sentiment'].values
vocab_size = X.max() + 1
with open("tokenizer.pkl", "wb") as fh:
    pickle.dump(tk,fh)


strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, 64, mask_zero=True),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(loss='binary_crossentropy',
                  optimizer=tf.keras.optimizers.Adam(1e-4),
                  metrics=['accuracy'])



batch_size = 4096
history = model.fit(X, 
                    y,
                    epochs = 10, 
                    batch_size=batch_size, 
                    validation_split=0.01,
                    verbose=2,
                    callbacks=[tf.keras.callbacks.ModelCheckpoint("checkpoints/weights.{epoch:02d}-{val_accuracy:.2f}.hdf5", 
                                                                  monitor="val_accuracy", save_best_only=True),
                               tf.keras.callbacks.TensorBoard(update_freq=10000)])

