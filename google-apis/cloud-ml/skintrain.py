import numpy as np
import os
import tensorflow as tf
import time

t = time.time()
# There are 3 dimensions in the HSV space: Hue, Saturation, and Value
dims = 3
# Consider each dimension in the HSV space to have quantized values as integers in [0, 99]
size = 100
# Define the size of the hidden layer
n_hidden_1 = 256
# Define the number of classes (skin & not-skin)
n_classes = 2
# Make a 1-column row matrix consisting of integer values [0, 99]
hsvValues = np.arange(size)[None].transpose()
# Expand this to be a table of each possible HSV value
for moreDims in range(0, 2):
	hsvValues = [ np.c_[np.ones(size ** (moreDims + 1)) * i, hsvValues] for i in range(0, size) ]
	hsvValues = np.concatenate(hsvValues)

# Load the positive skin tone examples from the training data
hsvIsSkin = np.zeros(size ** dims)
with open("skintones.txt", "r") as skintones:
	for line in skintones:
		vals = [int(n) for n in line.split(",")]
		val = (vals[0] * (size ** 2)) + (vals[1] * size) + vals[2]
		hsvIsSkin[val] += 1
# Quick metric
print("Maximum skin tone count is at HSV value", np.argmax(hsvIsSkin, 0))
# Apply thresholding
hsvIsSkin[hsvIsSkin < 2] = 0
hsvIsSkin[hsvIsSkin >= 2] = 1
hsvIsSkinWeights = (hsvIsSkin * 20) + 1
hsvIsSkinUnique = hsvIsSkin
hsvIsSkin = np.array([hsvIsSkin, -(hsvIsSkin - 1)]).T

print("Done schlogging data in %f seconds" % (time.time() - t))

t = time.time()
# Set up the neural network
x = tf.placeholder(tf.float32, [None, dims], name="hsv_values")
W1 = tf.Variable(tf.random_normal([dims, n_hidden_1], mean=1.0, stddev=1.0, dtype=tf.float32), name="weights_1")
b1 = tf.Variable(tf.random_normal([n_hidden_1], mean=1.0, stddev=1.0, dtype=tf.float32), name="biases_1")
W2 = tf.Variable(tf.random_normal([n_hidden_1, n_classes], mean=1.0, stddev=1.0, dtype=tf.float32), name="weights_2")
b2 = tf.Variable(tf.random_normal([n_classes], mean=1.0, stddev=1.0, dtype=tf.float32), name="biases_2")
y1 = tf.add(tf.matmul(x, W1), b1)
y1 = tf.nn.relu(y1)
logits_y = tf.add(tf.matmul(y1, W2), b2)
y = tf.nn.sigmoid(logits_y)

# Define loss and optimizer
y_ = tf.placeholder(tf.int32, [None, 2], name="labels")
training_weights = tf.placeholder(tf.float32, [None, 1], name="training_weights")

#cross_entropy = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=y_, logits=y, name="loss"))
cross_entropy = tf.reduce_mean(tf.losses.sigmoid_cross_entropy(labels=y_, logits=logits_y, weights=training_weights)) # TensorFlow is funny in that the cross-entropy function wants a "logit". Think of the logit as the value before passing through the non-linearity.
#cross_entropy = tf.reduce_mean(tf.nn.weighted_cross_entropy_with_logits(y_, y, 20))
#cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y, labels=y_))
train_step = tf.train.GradientDescentOptimizer(0.005).minimize(cross_entropy)
#train_step = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cross_entropy)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()
saver = tf.train.Saver()
print("Done setting up neural network in %f seconds" % (time.time() - t))

# Run Tensorflow
t = time.time()
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	# Statistics
	whoIsSkin = tf.placeholder(tf.float32, [None], name="labels_for_unique_count")
	uwc = tf.unique_with_counts(whoIsSkin)
	[values, _, counts] = sess.run(uwc, feed_dict={whoIsSkin: hsvIsSkinUnique})
	print("Done displaying data statistics in %f seconds" % (time.time() - t))
	t = time.time()
	# Train
	#print(W1.eval())
	#print(b1.eval())
	#print(W2.eval())
	#print(b2.eval())
	for i in range(16500):
		#print(W1.eval())
		#print(b1.eval())
		#print(W2.eval())
		#print(b2.eval())
		# x's are from hsvValues, y_'s are from hsvIsSkin
		min = (i * 10000) % hsvIsSkinUnique.size
		max = min + 10000
		batch_xs = hsvValues[min:max]
		batch_ys = hsvIsSkin[min:max]
		#batch_ys = batch_ys[None].transpose()
		tw = hsvIsSkinWeights[min:max]
		tw = tw[None].transpose()
		[_, cost] = sess.run([train_step, cross_entropy], feed_dict={x: batch_xs, y_: batch_ys, training_weights: tw})
		if (i % 100 == 0):
			print ("Epoch %d, cost = %f" % ((i / 100), cost))
	save_path = saver.save(sess, os.path.join(os.getcwd(), "skintone.ckpt"))
	print("Done calculating the neural network in %f seconds" % (time.time() - t))
	t = time.time()
	output = sess.run(y, feed_dict={x: [[6., 49., 79.]]})
	print("Done calculating a single output value in %f seconds" % (time.time() - t))
	print(output)

	t = time.time()
	# Test model
	correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
	# Calculate accuracy
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
	# Calculate precision
	precision, pre_op = tf.metrics.precision(labels=tf.argmax(y_, 1), predictions=tf.argmax(y, 1))
	# Calculate recall
	recall, recall_op = tf.metrics.recall(labels=tf.argmax(y_, 1), predictions=tf.argmax(y, 1))
	print("Accuracy:", accuracy.eval({x: hsvValues, y_: hsvIsSkin}))
	sess.run(tf.local_variables_initializer())
	print("Precision:", sess.run(pre_op, feed_dict={x: hsvValues, y_: hsvIsSkin}))
	sess.run(tf.local_variables_initializer())
	print("Recall:", sess.run(recall_op, feed_dict={x: hsvValues, y_: hsvIsSkin}))
	print("Done displaying performance metrics in %f seconds" % (time.time() - t))

