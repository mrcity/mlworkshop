import os
import tensorflow as tf

tf.reset_default_graph()

# Variables about variables
dims = 3
n_hidden_1 = 256
n_classes = 2
# Get the variables used in the model.
W1 = tf.get_variable("weights_1", shape=[dims, n_hidden_1])
b1 = tf.get_variable("biases_1", shape=[n_hidden_1])
W2 = tf.get_variable("weights_2", shape=[n_hidden_1, n_classes])
b2 = tf.get_variable("biases_2", shape=[n_classes])
# Initialize placeholder for the input data.
x = tf.placeholder(tf.float32, [None, dims], name="hsv_values")
# Define the neural network layer interactions.
y1 = tf.add(tf.matmul(x, W1), b1)
y = tf.add(tf.matmul(y1, W2), b2)

# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, use the saver to restore variables from disk, and
# do some work with the model.
with tf.Session() as sess:
	# Restore variables from disk.
	saver.restore(sess, os.path.join(os.getcwd(), "skintone.ckpt"))
	print("Model restored.")
	#print("W1 : %s" % W1.eval())
	#print("b1 : %s" % b1.eval())
	#print("W2 : %s" % W2.eval())
	#print("b2 : %s" % b2.eval())
	# Run through skin tones
	output = sess.run(y, feed_dict={x: [[5., 49., 79.]]})
	print(output)

	###########################
	#### Output into .pb file
	###########################

	export_path_base = "./"
	export_path = os.path.join(export_path_base, "skinmodel.pb")
	print('Exporting trained model to', export_path)
	builder = tf.saved_model.builder.SavedModelBuilder(export_path)

	# Build the signature_def_map for classification.
#	classification_inputs = tf.saved_model.utils.build_tensor_info(
#		serialized_tf_example)
#	classification_outputs_classes = tf.saved_model.utils.build_tensor_info(
#		prediction_classes)
#	classification_outputs_scores = tf.saved_model.utils.build_tensor_info(values)

	# Build the signature_def_map for prediction.
	# Note: Using predict_signature_def() rather than build_signature_def() really shortens things!
	prediction_signature = (
		tf.saved_model.signature_def_utils.predict_signature_def(
			inputs={'hsv_values': x},
			outputs={'skin_class': y}))
	
	isValid = tf.saved_model.signature_def_utils.is_valid_signature(prediction_signature)
	print("Is a valid signature?", isValid)
	
	builder.add_meta_graph_and_variables(
		sess,
		tags=[tf.saved_model.tag_constants.SERVING],
		signature_def_map={
			tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
				prediction_signature
		},
		main_op=tf.saved_model.main_op.main_op())
	builder.save()