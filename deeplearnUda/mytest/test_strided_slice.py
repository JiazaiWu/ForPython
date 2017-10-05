import tensorflow as tf   

data = [[[1, 1, 1], [2, 2, 2]],   
        [[3, 3, 3], [4, 4, 4]],   
        [[5, 5, 5], [6, 6, 6]]]

print(tf.constant(data).shape) # shape 3x2x3 = 18
x = tf.strided_slice(data,[0,0,0], [2,2,2], strides=[1,2,1])
# strided_slice word as
# for 1st dim, pick from [0,2)
# so get [[[1,1,1],[2,2,2]],
#        [[3,3,3],[4,4,4]]]
# for 2nd dim, pick from [0,2) and pad = 2 like 0 2 4...
# so get [[[1,1,1]],
#        [[3,3,3]]]
# for 3rd  dim, pick from [0,2)
# so get [[[1,1]],
#        [[3,3]]]
with tf.Session() as sess:   
    print(sess.run(x))  
