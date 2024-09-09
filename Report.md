# Exercise 1:

    For this exercise we installed Micropython and Thonny and then setup our Microcontroller with the resistor and light sensor. 
    An issue we ran into when testing this was not having the resistor and sensor securely placed within the microntroller, which led to us not getting any data when first running the script. 
    After fixing this, we then found the max and min values of this sensor by putting flashlights to the sensor and by putting the sensor in a completely dark drawer. 
    The values we found from this were Min: 2500 Max: 51000.

# Exercise 2:

    For this exercise, I modified the original code to play a sequence of musical notes from the song Twinkle, Twinkle, Little Star.
    I defined a dictionary containing frequencies for musical notes and created a list of tuples representing the melody, with each tuple consisting of a note and its duration.
    I then implemented the `play_song()` function to loop through the melody, playing each note for its corresponding duration using PWM output on pin GP16, connected to a speaker. 
    After each note, the speaker is silenced to create a pause, and the PWM signal is turned off once the song is complete.

# Exercise 3:

    We created a dictionary to keep track of the reaction times of the user. We still need to update this data to cloud for the specific user account.

    