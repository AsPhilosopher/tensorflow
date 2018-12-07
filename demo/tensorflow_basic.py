import tensorflow as tf

data1 = tf.constant(2.5)
data2 = tf.Variable(10, name='myName')
print(data1)
print(data2)
session = tf.Session()
print(session.run(data1))
data3 = tf.constant(2, dtype=tf.int32)
print(data3)
init = tf.global_variables_initializer()
session.run(init)
print(session.run(data2))
session.close()

# tensorflow = tensor + 计算图
# tensor 数据
# op
# 计算图 graphs 数据操作
# session中计算处理

init = tf.global_variables_initializer()
session = tf.Session()
# with语句时用于对try except finally 的优化，让代码更加美观
# 这条语句就好简洁很多，当with里面的语句产生异常的话，也会正常关闭文件
with session:
    session.run(init)
    print(session.run(data2))

int1 = tf.constant(6)
int2 = tf.constant(2)
add = tf.add(int1, int2)
sub = tf.subtract(int1, int2)
mul = tf.multiply(int1, int2)
div = tf.divide(int1, int2)
with tf.Session() as session:
    print(session.run(add))
    print(session.run(sub))
    print(session.run(mul))
    print(session.run(div))

int1 = tf.constant(6)
int2 = tf.Variable(2)
add = tf.add(int1, int2)
dataCopy = tf.assign(int2, add)  # add -> int2
sub = tf.subtract(int1, int2)
mul = tf.multiply(int1, int2)
div = tf.divide(int1, int2)
init = tf.global_variables_initializer()
with tf.Session() as session:
    session.run(init)
    print(session.run(add))
    print(session.run(sub))
    print(session.run(mul))
    print(session.run(div))
    print("copy:", session.run(dataCopy))
    print("eval:", dataCopy.eval())
    print("default_session:", tf.get_default_session().run(dataCopy))
