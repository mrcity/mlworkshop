# mlworkshop
Stephen Wylie's machine learning presentations

## Prerequisites for Getting Hands-on with Google’s Machine Learning APIs
This assumes you want to follow along in real-time with the examples ;)

### Sign up for Google Cloud Platform

* Go to https://console.cloud.google.com

* If you don’t have an account, there will be a button labeled “SIGN UP FOR FREE TRIAL”.  Click it.  It might show you a modal with various email settings and ToS acknowledgment; take care of this first.

#### Create a new project
* Click on the “Menu” icon in the top left corner with 3 lines.
* Click on “API Manager”.
* Next to where it says “Google Cloud Platform” at the top left, there should be a dropdown menu.  Click the dropdown to “Create project”.
* Give a name to your project, and then click “CREATE”.

#### Enable billing on the account
* Click on the “Menu” icon again.
* Click “Billing”.
* Follow the prompts to set up a billing account by adding your credit card info.  If you received a $300 GCP credit, you will not be billed for anything for at least 60 days.
* Now you need to link your project to your billing account.  Next to the word “Billing” in the top left, click on the dropdown, then click “Manage billing accounts”.
* Click “My projects”.
* Look for the project you just created.  Click on the horizontal ellipsis in the project’s row, then click “Change billing account”.
* Confirm the project name is correct in the modal that appears.  Choose your billing account in the dropdown menu, then click “SET ACCOUNT”.
* Note that if you delete this project or disable billing for it (by unlinking the billing account from the project) as soon as the class is over, then you will never get a bill from Google for running the examples, assuming you don’t somehow exceed your free credits in the meantime.

### Setting up for the Cloud Vision API demo

#### Install dependencies

* Install Node.js.
* Install bower.

#### Enable the Vision API within your app

* Go back to the API Manager through the menu at left.
* Click “Library”.
* Under “Google Cloud APIs”, find “Vision API”.  You may need to click the “More” button to see it.
* At the top left, next to where it says “Google Cloud Vision API”, click the word “ENABLE.”
* Create credentials to use your API endpoint at this time.  Start by clicking "Create credentials".
* Click on "Service account key".
* I created a new Service Account called "test" that had a limited number of roles selected (which ones?  TBD, one or more from the "Project" category).  Add sufficient roles by clicking on them to show a checkmark by them.  They will also appear below the word "Selected".
* Select the "JSON" key type (should already be selected).
* Click "Create".  When you do, it will prompt you to make sure you put the JSON file in a safe place, because it will not make the same one twice.  You need to put this JSON file wherever you will be using a library to access Cloud APIs.

#### Seed your Google Cloud Storage with some images to make your own Googly Eyes

* In the fold-out menu at left, click Storage.
* You might already have a bucket named after your application.  If not, add a new bucket.
* Click on the bucket to go inside it.
* Download some images containing human faces.
* Click "Upload Files" and select the images you just downloaded.
* Download the Googly Eyes code from this repo (coming soon).
* Modify the googly-eyes-ajax.html file and index.html file to replace "machine-learning-149606.appspot.com" with your own bucket name, and people.jpg with the name of one of your images.  These names show up in several places (shameful, I know), so search carefully.
* In app.js, change where it says require('./MachineLearning-dea72ee95678.json') to point to your own JSON cert you created earlier.
* Run `npm install` and `bower install` from the command line to download the dependencies you need to run particularly the Express server, the Google API Client, Polymer, and its Web components.

### Install TensorFlow

Follow the instructions at this link: https://www.tensorflow.org/versions/r0.11/get_started/os_setup.html

I had the best luck with the Docker development instance.  If you already have Docker installed and the Docker daemon running, run this from the command line:

`docker run -it b.gcr.io/tensorflow/tensorflow:latest-devel`

If you run latest rather than latest-devel, you might encounter a situation where you never get access to the terminal console for your Docker instance.  Very frustrating.

### Install some kind of RESTful client

I recommend Postman, which you can get from the Google Chrome Web Store.  It might not hurt to get the Postman Interceptor as well.
