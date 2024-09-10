# Exercise: Response time measurement and cloud upload

The LED blinks at random intervals.
The exercise_game.py script measures response time.

## Questions

1. Edit the exercise_game.py code to compute average, minimum, maximum response time for 10 flashes total.
2. Have the Pi Pico automatically upload the response time data (say via HTTP POST to a REST server to a cloud server of your choice (e.g. Firebase, Heroku, etc.)

The response to these questions is your unique code and results in Report.md in your team's forked GitHub repository.

## Cloud service notes

Students have used Google
[Firebase](
https://firebase.google.com/docs)
and
[FireStore](https://firebase.google.com/docs/firestore/quickstart)
but you're free to use whatever service you choose.
Note that the Pico MicroPython can't run the "boto3" and in general will run only libraries desired for MicroPython.
Thus it is probably better to use a service that has a REST API where you can HTTP POST JSON to the cloud server.

The JSON you create is
[PUT](https://firebase.google.com/docs/reference/rest/database/#section-put)
to the cloud service like:

```python
import requests

database_api_url = "https://cloud.invalid/pico-data/"
response = requests.post(database_api_url, json=score_dict)
```
