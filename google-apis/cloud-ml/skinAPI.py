from apiclient.discovery import build
import pprint

###############################################
# This function was copied directly from Google
###############################################

def predict_json(project, model, instances, version=None):
    """Send json data to a deployed model for prediction.

    Args:
        project (str): project where the Cloud ML Engine Model is deployed.
        model (str): model name.
        instances ([Mapping[str: Any]]): Keys should be the names of Tensors
            your deployed model expects as inputs. Values should be datatypes
            convertible to Tensors, or (potentially nested) lists of datatypes
            convertible to tensors.
        version: str, version of the model to target.
    Returns:
        Mapping[str: any]: dictionary of prediction results defined by the
            model.
    """
    # Create the ML Engine service object.
    # You could set the environment variable
    # GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
	# but I prefer to use config files
    service = build('ml', 'v1')
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']

instances = [{"hsv_values": [5., 49., 79.]},
			 {"hsv_values": [4., 59., 63.]},
			 {"hsv_values": [21., 67., 2.]},
			 {"hsv_values": [99., 99., 99.]},
			 {"hsv_values": [5., 35., 83.]},
			 {"hsv_values": [5., 29., 71.]}]

prediction = predict_json("bucket-name", "model-name", instances)
pprint.pprint(prediction)