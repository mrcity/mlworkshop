# prediction

Demonstration of Google's Prediction APIs, consisting of a car loan evaluator application.  (This readme is still in BETA.)

## Before you begin

Be sure you have followed the setup steps in the README file in the google-apis directory so you can get set up with the Google Cloud Platform in general.

## Setting up for the Cloud Vision API demo

### Install dependencies

* Install Python 3.
* Install the Google API library for Python

`pip install --upgrade google-api-python-client`

* Install Flask

`pip install flask`

### Enable the Prediction API within your app

* I will need to go back through my notes and see if the following steps were actually necessary.  I don't recall having to explicitly enable Prediction in the API Console, but a lot happened so maybe I forgot.
** Go back to the API Manager through the menu at left.
** Click “Library”.
** Under “Google Cloud APIs”, find “Prediction API”.  You may need to click the “More” button to see it.
** At the top left, next to where it says “Google Prediction API”, click the word “ENABLE.”
* Create credentials to use your API endpoint at this time.  Start by clicking "Create credentials".
* Click on "Service account key".
* I created a new Service Account called "test" that had a very permissive generic role selected (which ones?  TBD).  Add sufficient roles by clicking on them to show a checkmark by them.  They will also appear below the word "Selected".
* Select the "JSON" key type (should already be selected).
* There was another box I checked that was something to the effect of Give your service account Google Apps / User Domain / G Suite or etc . access, which then followed up with another prompt or two with stuff I had to fill out.  Basically the premise here is to give your service account similar permissions as any particular user on your Google App domain.
* Click "Create".  When you do, it will prompt you to make sure you put the JSON file in a safe place, because it will not make the same one twice.  Put the JSON credential file in mlworkshop/google-apis/keys (../keys from here).

### Seed your Google Cloud Storage with the data

* Download this file: <a href="http://users.eecs.northwestern.edu/~ahu340/eecs349-ps2/train.csv">http://users.eecs.northwestern.edu/~ahu340/eecs349-ps2/train.csv</a>.
* Edit the data so that the columns are in the right format for the classifier.  What I recall this entailing was I needed to move the classification label for each example from the first column to the last column, and also to make sure I got rid of any and all double-quotes in the data set, so the only thing in the CSV file were alphanumeric characters and commas (and the occasional question mark representing missing data).
* Upload this to your Google Cloud Storage bucket.
* Using the APIs Explorer or some other means, make a new model and initiate the training on this data set.
