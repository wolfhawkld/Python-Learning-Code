from __future__ import absolute_import, division, print_function, unicode_literals

# Import TensorFlow and tf.keras.
import tensorflow as tf
from tensorflow import keras

# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Import other lib.
import numpy as np
import matplotlib.pyplot as plt


# Function region.
def decode_review(text):
    return ' '.join([reverse_word_index.get(i, '?') for i in text])


# Download imdb data if there is no such data.
imdb = keras.datasets.imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

# print("Training entries: {}, labels:{}".format(len(train_data), len(train_labels)))

# Transform numbers to words.
word_index = imdb.get_word_index()
word_index = {k: (v+3) for k, v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
print(decode_review(train_data[0]))

# Transform numbers to tensors.
train_data = keras.preprocessing.sequence.pad_sequences(train_data,
                                                        value=word_index["<PAD>"],
                                                        padding='post',
                                                        maxlen=256)
test_data = keras.preprocessing.sequence.pad_sequences(test_data,
                                                       value=word_index["<PAD>"],
                                                       padding='post',
                                                       maxlen=256)
print(train_data[0])

# Build the model.
vocab_size = 10000
model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation=tf.nn.relu))
model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))
model.summary()

# Compile the model.
model.compile(optimizer=tf.compat.v1.train.AdamOptimizer(),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Partial validation.
x_val = train_data[:10000]
partial_x_train = train_data[10000:]
y_val = train_labels[:10000]
partial_y_train = train_labels[10000:]
history = model.fit(partial_x_train,
                   partial_y_train,
                   epochs=20,
                   batch_size=512,
                   validation_data=(x_val, y_val),
                   verbose=1)

# Evaluate the model.
results = model.evaluate(test_data, test_labels)
print(results)

# Visualization.
history_dict = history.history
# print(history_dict.keys())
acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']
epochs = range(1, len(acc) + 1)
# Loss:
# bo is for blue dot
plt.plot(epochs, loss, 'bo', label='Training loss')
# b is for solid blue line
plt.plot(epochs, val_loss, 'b', label='Validation loss')
# Accuracy:
# ro is for red dot
plt.plot(epochs, acc, 'ro', label='Training accuracy')
# r is for solid blue line
plt.plot(epochs, val_acc, 'r', label='Validation accuracy')
plt.title('Training and validation loss & accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss/Accuracy')
plt.legend()
plt.show()


