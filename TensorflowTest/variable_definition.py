import tensorflow as tf
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

state = tf.Variable(0, name='counter')
# print(state.name)
one = tf.constant(1)

new_value = tf.add(state, one)  # 变量加常量1
update = tf.compat.v1.assign(state, new_value)  # 把new_value赋给state

init = tf.compat.v1.global_variables_initializer()
# 这一步很重要。如果你设置了变量，一定要初始化所有变量 （用session run一下才能生效）

with tf.compat.v1.Session() as sess:
    sess.run(init)
    for _ in range(3):  # 3次循环，_此处无实际意义
        sess.run(update)
        print(sess.run(state))  # 注意这里不能直接print(state) 要先run后才能生效
