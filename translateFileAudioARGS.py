#/!/Users/antonio/opt/anaconda3/bin/python
import speech_recognition as sr
import os
from datetime import datetime
import os, sys
import argparse
import time
from googletrans import Translator
import googletrans

translator = Translator()  

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-s", "--source", required=True,
#	help="id microphone source")
ap.add_argument("-i", "--input", default="wav\\antonio3.wav",# required=True,
	help="input file to convert ")
ap.add_argument("-l", "--language", default="it",#required=True,
	help="input language, default Italian it")
ap.add_argument("-o", "--output", default="en",#required=True,
	help="output language, default Italian en")

#ap.add_argument("-o", "--output", default="it",#required=True,
#	help="output language, default Italian it")
	
args = vars(ap.parse_args())


global datastamp
datastamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 


AUDIO_FILE = (str(args["input"]))

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)  # read the entire audio file
		testo =  r.recognize_google(audio, language=str(args["input"]))
		print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")                 

		print("Transcription: " + str(testo))
		print ("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
				#tests = recognizer_instance.recognize_google(audio, language=str(args["input"]))		
#				tests = recognizer_instance.recognize_google(audio, language=str(args["language"]))
		rigatransA = translator.translate(testo,dest=str(args["output"])).text
					
				
		print(rigatransA)
        
		documento = open("testo.csv", "a", encoding='utf-8')
		documento.write(str(testo))
		documento.close()
