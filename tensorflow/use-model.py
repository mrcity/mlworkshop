import os.path
import time
import math
import numpy
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import pprint

# Basic model parameters as external flags.
flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('train_dir', 'data', 'Directory to put the training data.')
flags.DEFINE_string('checkpoint_dir', '.', 'Directory to put the checkpoints.')
flags.DEFINE_string('index', '0', 'Image to use from among MNIST sample data.')

NUM_CLASSES = 10
IMAGE_PIXELS = 28 * 28
hidden1_units = 128
hidden2_units = 32
batch_size = 1

images = tf.placeholder(tf.float32, shape=(batch_size, IMAGE_PIXELS))
labels = tf.placeholder(tf.float32, shape=(batch_size))

# IMPORTANT: This is where you initialize the graph in the same manner it was
# made when running training.  For the MNIST example, this code can be (and in
# fact was) copied straight out of the inference() function in mnist.py.
with tf.name_scope('hidden1'):
    weights = tf.Variable(
        tf.truncated_normal([IMAGE_PIXELS, hidden1_units],
            stddev=1.0 / math.sqrt(float(IMAGE_PIXELS))),
        name='weights')
    biases = tf.Variable(tf.zeros([hidden1_units]),
        name='biases')
    hidden1 = tf.nn.relu(tf.matmul(images, weights) + biases)

# Hidden 2
with tf.name_scope('hidden2'):
    weights = tf.Variable(
        tf.truncated_normal([hidden1_units, hidden2_units],
            stddev=1.0 / math.sqrt(float(hidden1_units))),
        name='weights')
    biases = tf.Variable(tf.zeros([hidden2_units]),
        name='biases')
    hidden2 = tf.nn.relu(tf.matmul(hidden1, weights) + biases)

# Linear
with tf.name_scope('softmax_linear'):
    weights = tf.Variable(
        tf.truncated_normal([hidden2_units, NUM_CLASSES],
            stddev=1.0 / math.sqrt(float(hidden2_units))),
        name='weights')
    biases = tf.Variable(tf.zeros([NUM_CLASSES]),
        name='biases')
    logits = tf.matmul(hidden2, weights) + biases

saver = tf.train.Saver()  # defaults to saving all variables - in this case w and b

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    # Here's where you're restoring the variables w and b.
    # Note that the graph is exactly as it was when the variables were
    # saved in a prior training run.
    ckpt = tf.train.get_checkpoint_state(FLAGS.checkpoint_dir)
    if ckpt and ckpt.model_checkpoint_path:
        saver.restore(sess, ckpt.model_checkpoint_path)
    else:
        print "No checkpoint found in this directory.  Exiting."

    # Now you can run the model to get predictions
    batch_x = input_data.read_data_sets(FLAGS.train_dir, False)
    batch_x = batch_x.train._images[FLAGS.index]
    for i in range(0, 784):
        if (i % 28 == 0):
            print ""
        if (batch_x[i] > 0.5):
            print "1",
        else:
            print "0",
    print "\n==="
    predictions = sess.run(logits, feed_dict={images: [batch_x]})
    pprint.pprint(predictions)
    print "The algorithm guessed this is a", numpy.argmax(predictions[0], 0)
