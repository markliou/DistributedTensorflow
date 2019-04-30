import tensorflow as tf
import numpy as np


X = tf.ones([32, 28, 28, 1])

with tf.device("/job:workers/task:1"):
    conv = tf.keras.layers.Conv2D(32, [3,3], padding='SAME')(X)
    for i in range(100):
        conv = tf.keras.layers.Conv2D(32, [3,3], padding='SAME')(conv)
with tf.device("/job:workers/task:2"):
    for i in range(100):
        conv = tf.keras.layers.Conv2D(32, [3,3], padding='SAME')(conv)
out = tf.keras.layers.Conv2D(32, [3,3], padding='SAME')(conv)

sess = tf.Session("grpc://127.0.0.1:50001")
sess.run(tf.global_variables_initializer())
print(sess.run(out))
sess.close()


