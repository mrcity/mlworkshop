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

### (Might not be required or even possible beforehand?) Enable the Vision API within your app
* Go back to the API Manager through the menu at left.
* Click “Library”.
* Under “Google Cloud APIs”, find “Vision API”.  You may need to click the “More” button to see it.
* At the top left, next to where it says “Google Cloud Vision API”, click the word “ENABLE.”
* It might be beneficial to create credentials to use your API endpoint at this time.  Follow the prompts to do so.

### Install TensorFlow

Follow the instructions at this link: https://www.tensorflow.org/versions/r0.11/get_started/os_setup.html

### Install some kind of RESTful client

I recommend Postman, which you can get from the Google Chrome Web Store.  It might not hurt to get the Postman Interceptor as well.
