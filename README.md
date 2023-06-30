# BoarRoarDetector

This Python microservice is a small project that provides an API endpoint for sending sensor data alerts. The microservice accepts sound files from a sensor, processes the data (using AI algorithms, which need to be implemented), and sends an alert to the [WildAlertAPI](https://github.com/MossPiglets/wild-alert-api) with information about the detected animal and the timestamp of detection.

## Endpoints

The microservice expects a sound file to be uploaded with the correct authentication key (specified in incoming_api_key).
If the request is successful, the microservice will send a JSON payload to the WildAlertAPI on the following endpoint:
> POST /API/sensor/<sensor_id>/data

with the following information:
*detected_at*: The timestamp of when the animal was detected, in ISO 8601 format.
*detected_animal*: The type of animal detected, which is currently set to a default value of Boar in main.py.

And it requires correct API-Key in the Header for authentication purposes (specidied in wildalert_api_key).

## How to Run

To run the microservice:
1. Ensure that you have virtualenv with flask installed.
2. Ensure that the main.py and utils.py files are in the same directory.
3. Run the main.py file using the command python main.py.
4. The microservice will start running on http://localhost:5000.

To check communication with WildAlertAPI it also must be running.
