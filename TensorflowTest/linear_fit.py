import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 第一步：使用np.random.normal生成正态分布的数据，即y = 0.1*x + 0.3
data = []
num_data = 1000
for i in range(num_data):
    x_data = np.random.normal(0.0, 0.55)
    y_data = 0.1 * x_data + 0.3 + np.random.normal(0.0, 0.03)
    data.append([x_data, y_data])

# 第二步：将数据进行分配，分成特征和标签(将数据分为X_data 和 y_data)
X_data = [v[0] for v in data]
y_data = [v[1] for v in data]

# 第三步：对参数W和b, 使用tf.Variable()进行初始化，对于参数W，使用tf.random_normal([1], -1.0, 1.0)构造初始值，对于参数b，使用tf.zeros([1]) 构造初始值
W = tf.Variable(tf.random.normal([1], -1.0, 1.0), name='W')
print("The shape of W is :{0}" .format(W))
b = tf.Variable(tf.zeros([1]))
print("The shape of b is :{0}" .format(b))

# 第四步：使用X_data * W + b 计算损失值(使用W * X_data + b 构造出预测值y_pred )
y_pred = X_data * W + b

# 第五步：使用均分误差来作为损失值(tf.reduce_mean(tf.square(y_data - y_pred)))
loss = tf.reduce_mean(tf.square(y_data - y_pred))

# 第六步：使用梯度下降来降低损失值(opt = tf.train.GradientDescentOptimizer(0.5).minimize(loss) )
opt = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.5).minimize(loss)

# 参数初始化操作
sess = tf.compat.v1.Session()
init = tf.compat.v1.global_variables_initializer()
sess.run(init)
for i in range(20):
    # 第七步：循环，使用sess.run(opt) 执行梯度降低损失值的操作，并打印w，b和loss
    sess.run(opt)
    print('W:%g b:%g loss:%g' % (sess.run(W), sess.run(b), sess.run(loss)))

# 第八步： 画图操作,画出散点图和拟合好的曲线图
plt.scatter(X_data, y_data, c='r')
plt.plot(X_data, sess.run(W) * X_data + sess.run(b))
plt.show()
