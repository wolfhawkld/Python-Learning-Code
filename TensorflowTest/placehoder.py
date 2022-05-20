import tensorflow as tf
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 创建placehoder 就可以先不输入值
input1 = tf.compat.v1.placeholder(tf.float32)
input2 = tf.compat.v1.placeholder(tf.float32)
ouput = tf.multiply(input1, input2)

with tf.compat.v1.Session() as sess:
    # 用feed_dict,字典的形式传入值
    print(sess.run(ouput, feed_dict={input1: [7.0], input2: [2.0]}))
