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



AUDIO_FILE = ("wav\\antonio3.wav")

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)  # read the entire audio file
		testo =  r.recognize_google(audio, language="it")
		print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")                 

		print("Transcription: " + str(testo))
		print ("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
				#tests = recognizer_instance.recognize_google(audio, language=str(args["input"]))		
#				tests = recognizer_instance.recognize_google(audio, language=str(args["language"]))
		rigatransA = translator.translate(testo,dest="en").text
					
				
		print(rigatransA)
        
		documento = open("testo.csv", "a", encoding='utf-8')
		documento.write(str(testo))
		documento.close()
