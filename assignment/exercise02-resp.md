# Exercise: PWM sound output
**Ryan Lagoy**


I wanted to play Sweet Caroline on my Rasp Pi, and so I followed these steps:
1. Found the sheet music here: https://musescore.com/user/34214067/sweet-caroline-2012-neil-diamond-piano-arrangement
2. I noticed the song used the A major scale, so I defined a dictionary of all of the notes in the scale that were needed.
3. I created a Note dataclass which stores the pitch and the duration.
4. Using the output from the previous steps I was able to play the first few bars of Sweet Caroline.
