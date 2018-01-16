# cloud-ml

Demonstration of Google's Cloud Machine Learning API, consisting of a skin tone classifier built in Tensorflow and deployed to the cloud.

## Before you begin

Be sure you have followed the setup steps in the README file in the google-apis directory so you can get set up with the Google Cloud Platform in general.

## Setting up for the Cloud ML API demo

### Install dependencies & set up environment

Install Tensorflow in the manner you desire.  (See [my Tensorflow README](https://github.com/mrcity/mlworkshop/blob/master/tensorflow/README.md) for more details on this.)

Run `pip install --upgrade --user google-api-python-client` to installl the Google API Python client.

Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to be the path to your JSON credentials file for accessing the APIs.

## Contents

* ex-skin*.bmp - Pixels that represent skin tones
* rgb2hsv.py - Convert these bitmaps into a list of HSV values
* skintrain.py - Build a model, save a checkpoint
* skinclassify.py - Convert the checkpoint into a SavedModel
* skinAPI.py - Use the model uploaded to Google Cloud Platform

## Logistics

It will take about 5 minutes for your model to deploy as a cloud API service.  You might even see it error out.  Rest assured it will go OK.

There are steps you need to perform in order to bridge the gap between skinclassify.py and skinAPI.py.  Come out to one of my talks in order to see what to do. ;)  Or, just look it up on Google.  It's not that hard.