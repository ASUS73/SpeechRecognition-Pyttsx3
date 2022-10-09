import pyttsx3

engine = pyttsx3.init()

#rate
rate = engine.getProperty('rate')
print(rate)

#Change default rate
engine.setProperty('rate', 120)

#Volume
#setting up volume Level between 0 and 1 (min:0, max:1)
volume = engine.getProperty('volume')
print('volume is {0}'.format(volume))

#Change the default volume
engine.setProperty('volume', 1)

#Voices
voices = engine.getProperty('voices')

# Male voice of index 0 & Female voice of index 1
print('Male Voice: {0}'.format(voices[0].id))
print('Female Voice: {0}'.format(voices[1].id))

#Setting up voice
#engine.setProperty('voice', voices[0].id)

engine.say('What\'s the OpenCV')
engine.runAndWait()
