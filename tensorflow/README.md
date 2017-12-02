# Tensorflow Examples

### use-model.py

This file demonstrates how to use an existing trained model in separate code from that which trained the model.

The main thing here is that you initialize the exact same variables in the exact same manner you did during training, or else the Saver will not know to load the trained model into your variables.  Notice that the creation of variables was basically copied and pasted from the inception function of mnist.py if you downloaded the Docker "latest-devel" image (id 76669b92928f).

## Install TensorFlow

Follow the instructions at this link for your specific environment: https://www.tensorflow.org/install/

I recommend installing the main-line Docker image.  If you already have Docker installed and the Docker daemon running, run this from the command line:

`docker run -it [-p <optional ports; read below>] -v [host-volume:container-volume] gcr.io/tensorflow/tensorflow`

## Configuring ports

You must configure external ports with one or more `-p` arguments in order to facilitate use of your Docker instance, since generally applications running on ports within your Docker container are not exposed to the host unless you have defined these ahead of time.  There is no way to add ports later, so you must specify all the ports you will need upfront or else start over with a new Docker container.

Here are handy ports to expose for a Tensorflow instance:

* 3000: The usual Node server port
* 5000: The usual Tornado server port
* 6006: Tensorboard
* 8081: Google Cloud Datalab
* 8888: Jupyter notebook -- don't miss out on its convenient capabilities!

`-p` is specified in its simplified form as `-p hostPort:containerPort`; for more details, consult the Docker documentation: https://docs.docker.com/engine/reference/run/#expose-incoming-ports

## Configuring volumes

You will probably want to mount a directory from your host into your Docker container so that you can pass files between them easily.  This is what the `-v` argument facilitates.  Simply write the absolute path to the host directory to share, followed by a colon, followed by the absolute directory path where it should exist in the Docker instance.  For more information, look at https://docs.docker.com/engine/reference/run/#volume-shared-filesystems

## Alternate Docker containers available

Instead of going along with the main-line Docker version of Tensorflow, you could also choose one that leverages a GPU (gcr.io/tensorflow/tensorflow:latest-gpu), a development build (gcr.io/tensorflow/tensorflow:latest-devel), or one that does both (gcr.io/tensorflow/tensorflow:latest-gpu-devel).  Here are the differences between the main-line and devel versions:

Mainline:

* Comes with Jupyter notebook
* Does not have many libraries or examples installed, but easy to clone them from Git

Devel build:

* Does not come with the Jupyter notebook; everything must be done from the shell
* Has most extra libraries & examples such as MNIST already installed, but these could be in the wrong place for where something like Tensorflow Serving might be expecting them, so you might have to clone it from Git anyway to get things to work

## Other ways to install Tensorflow

You could go with an installation right on your "bare iron" or through Anaconda.  I haven't had much luck with Conda personally, probably because I'm on computers with tightly locked-down permissions.  However, installing Tensorflow with `pip` has always gone smoothly for me (assuming no proxy problems) and hasn't really caused a lot of grief with other things.
