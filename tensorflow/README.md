# Tensorflow Examples

## use-model.py

This file demonstrates how to use an existing trained model in separate code from that which trained the model.

The main thing here is that you initialize the exact same variables in the exact same manner you did during training, or else the Saver will not know to load the trained model into your variables.  Notice that the creation of variables was basically copied and pasted from the inception function of mnist.py if you downloaded the Docker "latest-devel" image (id 76669b92928f).
