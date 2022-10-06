#/!/Users/antonio/opt/anaconda3/bin/python
#   #!/usr/bin/python3

import speech_recognition as sr
from os import path
from pydub import AudioSegment
from datetime import datetime
import os
import argparse


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-s", "--source", required=True,
#	help="id microphone source")
ap.add_argument("-i", "--input", required=True,#default=str(filename)+'.txt',#required=True,
	help="input file to convert in wav ")
ap.add_argument("-l", "--language", default="it",#required=True,
	help="input language, default Italian it")
#ap.add_argument("-o", "--output", default="it",#required=True,
#	help="output language, default Italian it")
	
args = vars(ap.parse_args())



#datastamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 

#f not os.path.exists(str(datastamp)):
#	os.makedirs(str(datastamp))    


# convert mp3 file to wav 
#sound = AudioSegment.from_opus(str(args["input"]))                                                      

##sound = AudioSegment.from_mp3(str(args["input"]))
##sound.export("datastamp/"+str(args["input"])+".wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = (str(args["input"]))

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio, language=str(args["language"])))
