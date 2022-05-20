import tensorflow as tf
import numpy as np
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# w和b的初始值
Weights = tf.Variable(tf.random.uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))

# 建立优化器
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.5)  # 学习率，小于1的数，这里取0.5
train = optimizer.minimize(loss)  # 这里定义了train的算式，即要做什么：使得loss最小！

# 初始化我们的变量 使我们设计的学习结构活动起来
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()  # 创建一个session
sess.run(init)

for step in range(201):  # 迭代201次
    sess.run(train)
    if step % 20 == 0:  # 每隔20次输出一次信息
        print(step, sess.run(Weights), sess.run(biases))
