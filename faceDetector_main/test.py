import gtts
from playsound import playsound
age='30'
gender='Male'
t1 = gtts.gTTS("Sounds Good. Your gender is {} and Age is {} years. I am improving myself. sorry if any mistak".format(gender,age[1:-1]))
# save the audio file
t1.save("detection.mp3")
# play the audio file
playsound("detection.mp3")
