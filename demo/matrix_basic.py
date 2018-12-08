import tensorflow as tf

data1 = tf.placeholder(tf.float32)
data2 = tf.placeholder(tf.float32)
dataAdd = tf.add(data1, data2)
with tf.Session() as session:
    print(session.run(dataAdd, feed_dict={data1: 6, data2: 2}))

data1 = tf.constant([[6, 8]])
data2 = tf.constant([[0], [1]])
data3 = tf.constant([[3, 3]])
data4 = tf.constant([[1, 2], [3, 4], [5, 6]])
print(data4.shape)  # 打印纬度
with tf.Session() as session:
    print(session.run(data4))
    print(session.run(data4[0]))  # 某一行
    print(session.run(data4[:, 0]))  # 某一列
    print(session.run(data4[0, 0]))
matMul = tf.matmul(data1, data2)
matMul2 = tf.multiply(data1, data2)  # 普通乘法
matAdd = tf.add(data1, data3)
with tf.Session() as session:
    print(session.run(matMul))
    print(session.run(matAdd))
    print(session.run(matMul2))
    print(session.run([matAdd, matMul]))

mat0 = tf.zeros([2, 3])
mat1 = tf.ones([3, 2])
mat2 = tf.fill([2, 3], 16)
with tf.Session() as session:
    print(session.run(mat0))
    print(session.run(mat1))
    print(session.run(mat2))
mat0 = tf.constant([[2], [3], [4]])
mat1 = tf.zeros_like(mat0)
mat2 = tf.linspace(0.0, 2.0, 11)  # 0.0-2.0 10等分
mat3 = tf.random_uniform([2, 3], -1, 2)  # -1-2之间随机
with tf.Session() as session:
    print(session.run(mat1))
    print(session.run(mat2))
    print(session.run(mat3))
