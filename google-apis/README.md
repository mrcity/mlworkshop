# Google Machine Learning API Examples

These are the general prerequisites you need to follow in order to get started with using Google APIs.  For using a specific API, please see the README file in the corresponding directory, which will contain further information on how to set up datasets, authenticate yourself to the service, etc.

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

Follow the instructions in the google-apis/cloud-vision README file.
