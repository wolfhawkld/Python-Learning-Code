#代码说明参考Tensorflow官方tutorial:
# https://tensorflow.google.cn/guide/keras
import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Custom layer.
class MyLayer(layers.Layer):

    def __init__(self, output_dim, **kwargs):
        self.output_dim = output_dim
        super(MyLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        shape = tf.TensorShape((input_shape[1], self.output_dim))
        self.kernel = self.add_weight(name='kernel',
                                      shape=shape,
                                      initializer='uniform',
                                      trainable=True)
        super(MyLayer, self).build(input_shape)

    def call(self, inputs):
        return tf.matmul(inputs, self.kernel)

    def compute_output_shape(self, input_shape):
        shape = tf.TensorShape(input_shape).as_list()
        shape[-1] = self.output_dim
        return tf.TensorShape(shape)

    def get_config(self):
        base_config = super(MyLayer, self).get_config()
        base_config['output_dim'] = self.output_dim
        return base_config

    @classmethod
    def from_config(cls, config):
        return cls(**config)

# Subclassing Model.
class MyModel(tf.keras.Model):

    def __init__(self, num_classes=10):
        super(MyModel, self).__init__(name='my_model')
        self.num_classes = num_classes
        self.dense_1 = layers.Dense(32, activation='relu')
        self.dense_2 = layers.Dense(num_classes, activation='sigmoid')

    def call(self, inputs):
        # Forward pass.
        x = self.dense_1(inputs)
        return self.dense_2(x)

    def compute_out_shape(self, input_shape):
        shape = tf.TensorShape(input_shape).as_list()
        shape[-1] = self.num_classes
        return tf.TensorShape(shape)

'''
# Instance of subclass model.
model = MyModel(num_classes=10)
data = np.random.random((1000, 32))
labels = np.random.random((1000, 10))
model.compile(optimizer=tf.compat.v1.train.RMSPropOptimizer(0.001),
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=[tf.keras.metrics.categorical_accuracy])
model.fit(data, labels, batch_size=32, epochs=5)
'''

''''
# Instance of custom layer.
model = tf.keras.Sequential([
    MyLayer(10),
    layers.Activation('softmax')])
model.compile(optimizer=tf.compat.v1.train.RMSPropOptimizer(0.001),
             loss=tf.keras.losses.categorical_crossentropy,
             metrics=[tf.keras.metrics.categorical_accuracy])
data = np.random.random((1000, 32))
labels = np.random.random((1000, 10))
model.fit(data, labels, batch_size=32, epochs=5)
'''

'''
# Callback.
callbacks = [
    tf.keras.callbacks.EarlyStopping(patience=2, monitor='val_loss'),
    tf.keras.callbacks.TensorBoard(log_dir='logs')
]
val_data = np.random.random((100, 32))
val_labels = np.random.random((100, 10))
model.fit(data, labels, batch_size=32, epochs=5, callbacks=callbacks,
          validation_data=(val_data, val_labels))
'''

'''
# Save and load model.
model = tf.compat.v1.keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(32,)),
    layers.Dense(10, activation='softmax')])

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
data = np.random.random((1000, 32))
labels = np.random.random((1000, 10))

model.save('weights/my_model.h5')
model = tf.keras.models.load_model('weights/my_model.h5')
model.fit(data, labels, batch_size=32, epochs=5)
'''

'''
# Estimator
model = tf.keras.Sequential([layers.Dense(10, activation='softmax'),
                             layers.Dense(10, activation='softmax')])
model.compile(optimizer=tf.compat.v1.train.RMSPropOptimizer(0.001),
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=[tf.keras.metrics.categorical_accuracy])
estimator = tf.keras.estimator.model_to_estimator(model)
'''

# Multiple GPUs
model = tf.keras.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10,)))
model.add(layers.Dense(1, activation='sigmoid'))
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.2)
model.compile(loss=tf.keras.losses.binary_crossentropy, optimizer=optimizer)
model.summary()


def input_fn():
    x = np.random.random((1024, 10))
    y = np.random.randint(2, size=(1024, 1))
    x = tf.cast(x, tf.float32)
    dataset = tf.data.Dataset.from_tensor_slices((x, y))
    dataset = dataset.repeat(10)
    dataset = dataset.batch(32)
    return dataset


strategy = tf.contrib.distribute.MirroredStrategy()
config = tf.estimator.RunConfig(train_distribute=strategy)

keras_estimator = tf.keras.estimator.model_to_estimator(
    keras_model=model,
    config=config,
    model_dir='tmp/model_dir')
keras_estimator.train(input_fn=input_fn, steps=10)
