import tensorflow as tf

a = tf.constant([1,2], name="a", dtype=tf.float32)
b = tf.constant([3,4], name="b", dtype=tf.float32)
result = tf.add(a,b,name="add")
print(result)

with tf.Session() as sess:
	output = sess.run(result)
	print(output)