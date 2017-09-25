import tensorflow as tf

# seed=1 make sue w1 and w2 get the same value as previous time
w1 = tf.Variable(tf.random_normal([2,3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3,1], stddev=1, seed=1))


# if we have n batches, each of them will be a node
# so it will have heavy system load
# use placehold as input and feed it when train on a certain batches
x = tf.placeholder(tf.float32, shape=(1,2), name="input")
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# globel_variable_initalizer will init all variable
# otherwise you need to init one by one
init = tf.global_variables_initializer()
print(tf.GraphKeys.TRAINABLE_VARIABLES)
with tf.Session() as sess:
	#sess.run(w1.initializer)
	#sess.run(w2.initializer)
	sess.run(init)
	print(sess.run(y, feed_dict={x: [[0.7,0.9]]}))