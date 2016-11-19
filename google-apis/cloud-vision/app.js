var express = require('express');
var app = express();

var google = require('googleapis');
var vision = google.vision('v1');

var key = require('../keys/MachineLearning-key.json');
var jwtClient = new google.auth.JWT(
    key.client_email,
    null,
    key.private_key,
    ['https://www.googleapis.com/auth/cloud-platform'],
    null
);

jwtClient.authorize(function (err, tokens) {
    if (err) {
        console.log(err);
      return;
    }
});

app.use('/', express.static('dist'));

app.get('/api/googlyEyes', function(req, res) {
    var request = {
        "resource": {
            "requests": [
                {
                    "image": {
                        "source": {
                            "gcsImageUri": "gs://" + req.query.gcsBucket + "/" + req.query.gcsFileName
                        }
                    },
                    "features": [
                        {
                            "type": "FACE_DETECTION",
                            "maxResults": 10
                        }
                    ]
                }
            ]
        },
        auth: jwtClient
    };

    vision.images.annotate(request, function(err, result) {
        if (err) {
            res.send(err);
        } else {
            res.send(result);
        }
    });
});

app.listen(3000);
