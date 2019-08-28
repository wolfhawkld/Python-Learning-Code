import tensorflow as tf

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix1, matrix2)  # matrix multiply np.dot(m1, m2)

# method 1
sess = tf.Session()  # 创建session
result = sess.run(product)  # 通过session来运行部分图
print(result)
sess.close()  # 关闭会话

# method 2
with tf.Session() as sess:  # 通过with 自动关闭这次会话 降低内存占用
    result2 = sess.run(product)
    print(result2)
