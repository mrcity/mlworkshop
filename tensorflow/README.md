# Tensorflow Examples

### use-model.py

This file demonstrates how to use an existing trained model in separate code from that which trained the model.

The main thing here is that you initialize the exact same variables in the exact same manner you did during training, or else the Saver will not know to load the trained model into your variables.  Notice that the creation of variables was basically copied and pasted from the inception function of mnist.py if you downloaded the Docker "latest-devel" image (id 76669b92928f).

## Install TensorFlow

Follow the instructions at this link: https://www.tensorflow.org/get_started/os_setup

I had the best luck with the Docker development instance.  If you already have Docker installed and the Docker daemon running, run this from the command line:

`docker run -it b.gcr.io/tensorflow/tensorflow:latest-devel`

(Note: this Docker URL seems to have changed if you read the link above...)

If you run latest rather than latest-devel, you might encounter a situation where you never get access to the terminal console for your Docker instance.  Very frustrating.
