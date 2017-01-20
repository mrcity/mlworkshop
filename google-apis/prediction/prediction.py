import httplib2
import json
import pprint
from apiclient.discovery import build
from flask import Flask, request, send_from_directory
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/prediction']

credentials = ServiceAccountCredentials.from_json_keyfile_name('../keys/Prediction-key.json', scopes=scopes)

# If no credentials are found or the credentials are invalid due to expiration, new credentials need to be obtained from the authorization server. The oauth2client.tools.run_flow() function attempts to open an authorization server page in your default web browser. The server asks the user to grant your application access to the user's data.  If the user grants access, the run_flow() function returns new credentials.  The new credentials are also stored in the supplied Storage object, which updates the credentials.dat file.
if credentials is None or credentials.invalid:
    credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

# Create an httplib2.Http object to handle our HTTP requests, and authorize it using the credentials.authorize() function.
http = httplib2.Http()
http = credentials.authorize(http)

app = Flask(__name__)

@app.route("/classify")
def runStuff():
    service = build('prediction', 'v1.6', http=http)
    body = {
      "input": {
        "csvInstance": [
            str(request.args.get("salary")),
            str(request.args.get("commission")),
            str(request.args.get("age")),
            str(request.args.get("gender")),
            str(request.args.get("marital")),
            str(request.args.get("elevel")),
            str(request.args.get("car")),
            str(request.args.get("zipcode")),
            str(request.args.get("creditscore")),
            str(request.args.get("hvalue")),
            str(request.args.get("hyears")),
            str(request.args.get("loan"))
        ]
      }
    }
    googleRequest = service.trainedmodels().predict(project="machine-learning-149606", id="credit-ml2010", body=body)
    response = googleRequest.execute(http=http)
    #response = body
    return json.dumps(response)

#@app.route("/classifyTest")
#def mock():
#    return '{"kind": "prediction#output", "id": "credit-ml2010", "selfLink": "https://www.googleapis.com/prediction/v1.6/projects/machine-learning-149606/trainedmodels/credit-ml2010/predict", "outputLabel": "no", "outputMulti": [{"label": "no", "score": "0.434271"}, {"label": "yes", "score": "0.565729"}]}'

@app.route('/<path:path>')
def the_interface(path):
    return send_from_directory('dist', path)

if __name__ == "__main__":
    app.run()
