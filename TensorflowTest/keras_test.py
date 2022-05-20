#代码说明参考Tensorflow官方tutorial:
# https://tensorflow.google.cn/guide/keras
import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


model = tf.keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(32,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')])

model.compile(optimizer=tf.compat.v1.train.AdamOptimizer(0.001),
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=[tf.keras.metrics.categorical_accuracy])


def random_one_hot_labels(shape):
    n, n_class = shape
    classes = np.random.randint(0, n_class, n)
    labels = np.zeros((n, n_class))
    labels[np.arange(n), classes] = 1
    return labels


data = np.random.random((1000, 32))
labels = random_one_hot_labels((1000, 10))
val_data = np.random.random((100, 32))
val_labels = random_one_hot_labels((100, 10))


dataset = tf.data.Dataset.from_tensor_slices((data, labels))
dataset = dataset.batch(32).repeat()
val_dataset = tf.data.Dataset.from_tensor_slices((val_data, val_labels))
val_dataset = val_dataset.batch(32).repeat()


'''
# Input NumPy data
model.fit(data, labels, epochs=10, batch_size=32,
          validation_data=(val_data, val_labels))
'''

'''
# Input tf.data datasets
model.fit(dataset, epochs=10, steps_per_epoch=30,
          validation_data=val_dataset,
          validation_steps=3)
'''

'''
# Evaluate data
model.evaluate(data, labels, batch_size=32)
model.evaluate(dataset, steps=30)
'''

'''
# Predict data
ret_data = model.predict(data, batch_size=32)
ret_dataset = model.predict(dataset, steps=30)
print(ret_data.shape)
print(ret_dataset.shape)
'''

# Functional API
inputs = tf.keras.Input(shape=(32,))
x = layers.Dense(64, activation='relu')(inputs)
x = layers.Dense(64, activation='relu')(x)
predictions = layers.Dense(10, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=predictions)
model.compile(optimizer=tf.compat.v1.train.RMSPropOptimizer(0.001),
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=[tf.keras.metrics.categorical_accuracy])
model.fit(data, labels, batch_size=32, epochs=5)


