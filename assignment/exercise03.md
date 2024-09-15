# Exercise: Response time measurement and cloud upload

The LED blinks at random intervals.
The exercise_game.py script measures response time.

## Questions

1. Edit the exercise_game.py code to compute average, minimum, maximum response time for 10 flashes total.
2. Have the Pi Pico automatically upload the response time data, say via HTTP POST to a REST server to a cloud server of your choice (e.g. Firebase, Heroku, etc.)

The response to these questions is in your team's forked GitHub repository:

* your Python code (including the game code, and what you added to send data to the cloud server, etc.)
* User story (a couple sentences) in Report.md

Note: there is no "app" to develop -- the Cloud slideshow discusses React, Flutter, etc. but we do NOT use them for this MiniProject.

## WiFi connection

To avoid storing Kerberos password in the insecure Pico or accidentally in the GitHub code, consider making a temporary WiFi hotspot from your laptop or mobile phone.
Don't share the WiFi password in the GitHub code or other people worldwide can see your password and WiFi ID!

[WiFi example](../examples/internet_connect.py)

## Cloud service notes

Students have used Google
[Firebase](
https://firebase.google.com/docs)
and
[FireStore](https://firebase.google.com/docs/firestore/quickstart)
but you're free to use whatever service you choose.

Note that the Pico MicroPython can't run "boto3" and in general will run only libraries desired for MicroPython.
Thus it is easier to use a service that has a REST API where you can HTTP POST JSON to the cloud server.

The JSON you create is
[PUT](https://firebase.google.com/docs/reference/rest/database/#section-put)
to the cloud service like:

```python
import urequests

database_api_url = "https://cloud.invalid/pico-data/"
response = urequests.post(database_api_url, json=score_dict)
```
