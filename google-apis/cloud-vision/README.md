# cloud-vision

Demonstration of Google's Cloud Vision APIs, consisting of a "googly eyes" generator implemented with Node.js and Polymer.

Josef Stalin is a friendlier person when wearing Googly Eyes:

![Stalin with Googly Eyes](http://stev-o.us/stalin-googly.png)

## Before you begin

Be sure you have followed the setup steps in the main README in the root directory of this repository so you can get set up with the Google Cloud Platform in general.

## Setting up for the Cloud Vision API demo

### Install dependencies

* Install Node.js.
* Install Bower.
* Switch to this directory (cloud-vision) in your console.
* run `npm install` to install the Node dependencies for the server.
* run `bower install` to install the Bower components for the front-end pages. 

### Enable the Vision API within your app

* Go back to the API Manager through the menu at left.
* Click “Library”.
* Under “Google Cloud APIs”, find “Vision API”.  You may need to click the “More” button to see it.
* At the top left, next to where it says “Google Cloud Vision API”, click the word “ENABLE.”
* Create credentials to use your API endpoint at this time.  Start by clicking "Create credentials".
* Click on "Service account key".
* I created a new Service Account called "test" that had a limited number of roles selected (which ones?  TBD, one or more from the "Project" category).  Add sufficient roles by clicking on them to show a checkmark by them.  They will also appear below the word "Selected".
* Select the "JSON" key type (should already be selected).
* Click "Create".  When you do, it will prompt you to make sure you put the JSON file in a safe place, because it will not make the same one twice.  Put the JSON credential file in mlworkshop/google-apis/keys (../keys from here).

### Seed your Google Cloud Storage with some images to make your own Googly Eyes

* In the fold-out menu at left, click Storage.
* You might already have a bucket named after your application.  If not, add a new bucket.
* Click on the bucket to go inside it.
* Download some images containing human faces.
* Click "Upload Files" and select the images you just downloaded.
* When the upload is complete, select the corresponding checkbox in the "Share publicly" column.  This will check the box and write "Public link" in that column, signifying permission to use the image in your app.
* Modify the dist/googly-eyes-helpers/googly-eyes-helpers.html file to replace "name-of-your-bucket" with your own bucket name, and "a-file-with-faces.jpg" with the name of one of your images.
