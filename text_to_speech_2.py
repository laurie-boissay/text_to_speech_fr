#!/usr/bin/python3.8
# coding:u8


# RESSOURCES _________________________________________________________________________
# https://pypi.org/project/pyttsx3/
# https://sonsuzdesign.blog/2020/06/07/building-a-speech-translator-in-python/

import pyttsx3
engine = pyttsx3.init() 					# object creation.

# RATE _______________________________________________________________________________
rate = engine.getProperty('rate')   		# getting details of current speaking rate.
#print (rate)                        		# printing current voice rate.
engine.setProperty('rate', 110)     		# setting up new voice rate.

# VOLUME ______________________________________________________________________________
volume = engine.getProperty('volume')   	# getting to know current volume level (min=0 and max=1).
engine.setProperty('volume',1.0)    		# setting up volume level between 0 and 1.

# VOICE _______________________________________________________________________________
voices = engine.getProperty('voices')       # getting details of current voice.
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male.
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female.

# LANGUAGE ____________________________________________________________________________
fr_voice_id = "french"
engine.setProperty('voice', fr_voice_id)	# changing language to french.

# TEXT TO READ _________________________________________________________________________
text = "Bonjour je parle en français !\n"	# \n is important for the reading rhythm.
text += "J'aimerai bien apprendre à lire des sites web maintenant.\n"
text += "Il me faut l'aide d'un robot scraper."

# SAY __________________________________________________________________________________
engine.say(text)


engine.runAndWait()
engine.stop()


