# Exercise: Game
**Ryan Lagoy**

This excercise required both a hardware and cloud based solution.

On the hardware side of things, the Ras Pi micropython code required some implementation. The following key tasks were:

1. Implement the scorer, and define a data structure to hold each score.
2. Post the data to a REST API (see cloud section).

Note 1: the data dict included a user pk number so that the cloud could differentiate between users. For this implementation, 2 users
were created. Additionally, an ID was assigned for each score record.

Note 2: I linted the exercise_game.py file, so it meets the Python coding standards.

On the cloud side of things, a Django project was created that implemented the following features:

1. Allauth for Google/social log-ins
2. Implemented a PostGres Database
3. Implemented a REST API for the score data
4. Created a dashboard with bootstrap formating

The source code for this project can be found here: https://github.com/rlagoy/2024-mini-cloud.
There is a deploy folder which includes all of the required files for deploying to a droplet.

Lastly, the final code wasn't tested on the RasPi, since one of the students borrowed mine, and I wasn't able to re-test.
