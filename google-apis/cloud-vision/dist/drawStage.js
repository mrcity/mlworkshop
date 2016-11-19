function drawStage(respObj)
{
    context.globalCompositeOperation = "source-over";

    var image = new Image();
    var rotation = 0;
    image.src = imageSrc;
    image.onload = function() {
        // Resize the canvas
        var ct = document.getElementById('measure');
        ct.appendChild(image);
        canvas.height = image.height;
        canvas.width = image.width;
        ct.removeChild(image);

        context.drawImage(image, 0, 0, canvas.width, canvas.height);

        if (respObj === undefined)
            return;

        for (var r in respObj.responses) {
            var response = respObj.responses[r];
            if (response.faceAnnotations !== undefined) {
                for (var a in response.faceAnnotations) {
                    var landmarks = response.faceAnnotations[a].landmarks;
                    var eyeX = 0, eyeY = 0;
                    var leftEyePos, rightEyePos, eyeMidpoint;
                    var leftGooglyEyes = [];
                    var rightGooglyEyes = [];
                    var leftEyeSize = {
                        x: 0,
                        y: 0,
                        z: 0
                    };
                    var rightEyeSize = {
                        x: 0,
                        y: 0,
                        z: 0
                    };
                    for (var l in landmarks) {
                        var landmark = landmarks[l];
                        if (landmark.type == "LEFT_EYE") {
                            leftEyePos = landmark.position;
                        } else if (landmark.type == "RIGHT_EYE") {
                            rightEyePos = landmark.position;
                        } else if (landmark.type == "MIDPOINT_BETWEEN_EYES") {
                            eyeMidpoint = landmark.position;
                        } else if (landmark.type == "LEFT_EYE_LEFT_CORNER") {
                            leftEyeSize.x -= landmark.position.x;
                            leftEyeSize.y -= landmark.position.y;
                            leftEyeSize.z -= landmark.position.z;
                        } else if (landmark.type == "LEFT_EYE_RIGHT_CORNER") {
                            leftEyeSize.x += landmark.position.x;
                            leftEyeSize.y += landmark.position.y;
                            leftEyeSize.z += landmark.position.z;
                        } else if (landmark.type == "RIGHT_EYE_LEFT_CORNER") {
                            rightEyeSize.x -= landmark.position.x;
                            rightEyeSize.y -= landmark.position.y;
                            rightEyeSize.z -= landmark.position.z;
                        } else if (landmark.type == "RIGHT_EYE_RIGHT_CORNER") {
                            rightEyeSize.x += landmark.position.x;
                            rightEyeSize.y += landmark.position.y;
                            rightEyeSize.z += landmark.position.z;
                        }
                    }
                    // Find the maximum size of the eye
                    var eyeSize = eyeScale * Math.max(
                            Math.sqrt(Math.pow(leftEyeSize.x, 2), Math.pow(leftEyeSize.y, 2)),
                            Math.sqrt(Math.pow(rightEyeSize.x, 2), Math.pow(rightEyeSize.y, 2))
                        );

                    // Find the correct offset for the eyes given the scale
                    var leftEyeAngle = Math.atan((eyeMidpoint.y - leftEyePos.y) / (eyeMidpoint.x - leftEyePos.x));
                    var rightEyeAngle = Math.atan((eyeMidpoint.y - rightEyePos.y) / (eyeMidpoint.x - rightEyePos.x));
                    var moveScale = eyeScale * ((eyeScale - 1) / 2);

                    // Draw the eyes
                    var googlyEyes = new Image();
                    googlyEyes.src = "https://static1.fjcdn.com/comments/Here+is+a+googly+eye+png+make+me+proud+people+_0a191ef5ef16fdd0d08483fbfa9419bd.png";
                    googlyEyes.eyeSize = eyeSize;
                    googlyEyes.eyePos = leftEyePos;
                    googlyEyes.eyeAngle = leftEyeAngle;
                    googlyEyes.moveScale = moveScale;
                    googlyEyes.onload = myImageOnLoad;

                    googlyEyes = new Image();
                    googlyEyes.src = "https://static1.fjcdn.com/comments/Here+is+a+googly+eye+png+make+me+proud+people+_0a191ef5ef16fdd0d08483fbfa9419bd.png";
                    googlyEyes.eyeSize = eyeSize;
                    googlyEyes.eyePos = rightEyePos;
                    googlyEyes.eyeAngle = rightEyeAngle;
                    googlyEyes.moveScale = moveScale;
                    googlyEyes.onload = myImageOnLoad;
                }
            }
        }
    };
}

var myImageOnLoad = function() {
    rotation = Math.random() * 6.28;
    context.globalCompositeOperation = "source-over";
    context.translate(this.eyePos.x - (this.moveScale * Math.cos(this.eyeAngle)), this.eyePos.y - (this.moveScale * Math.sin(this.eyeAngle)));
    context.rotate(rotation);
    context.drawImage(this, -(this.eyeSize/2.0), -(this.eyeSize/2.0), this.eyeSize, this.eyeSize);
    context.rotate(-rotation);
    context.translate(-this.eyePos.x + (this.moveScale * Math.cos(this.eyeAngle)), -this.eyePos.y + (this.moveScale * Math.sin(this.eyeAngle)));
}