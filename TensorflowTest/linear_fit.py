import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


# 第一步：使用np.random.normal创建数据，即y = 0.1*x + 0.3
data = []
num_data = 1000
for i in range(num_data):
    x_data = np.random.normal(0.0, 0.55)
    y_data = 0.1 * x_data + 0.3 + np.random.normal(0.0, 0.03)
    data.append([x_data, y_data])

# 第二步：将数据进行分配，分成特征和标签
X_data = [v[0] for v in data]
y_data = [v[1] for v in data]

# 第三步：使用tf.Variable进行参数的初始化操作
W = tf.Variable(tf.random_normal([1], -1.0, 1.0), name='W')
b = tf.Variable(tf.zeros([1]))
# 第四步：使用X_data * W + b 计算损失值
y_pred = X_data * W + b
# 第五步：使用均分误差来作为损失值
loss = tf.reduce_mean(tf.square(y_data - y_pred))
# 第六步：使用梯度下降来降低损失值
opt = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(loss)
# 参数初始化操作
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
for i in range(20):
    # 第七步：循环，执行梯度下降操作，打印w，b和loss
    sess.run(opt)
    print('W:%g b:%g loss:%g'%(sess.run(W), sess.run(b), sess.run(loss)))

# 第八步： 画图操作
plt.scatter(X_data, y_data, c='r')
plt.plot(X_data, sess.run(W) * X_data + sess.run(b))
plt.show()