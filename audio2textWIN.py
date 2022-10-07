#/!/Users/antonio/opt/anaconda3/bin/python
#   #!/usr/bin/python3

import speech_recognition as sr
from os import path
from pydub import AudioSegment
from datetime import datetime
import os
import argparse
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-s", "--source", required=True,
#	help="id microphone source")
ap.add_argument("-i", "--input", required=True,#default=str(filename)+'.txt',#required=True,
	help="input file to convert in wav ")
ap.add_argument("-l", "--language", default="it",#required=True,
	help="input language, default Italian it")
ap.add_argument("-t", "--type", default="ogg",  type=str,#required=True,
	help="type format file ogg mp3 flv wav ")

#ap.add_argument("-o", "--output", default="it",#required=True,
#	help="output language, default Italian it")
	
args = vars(ap.parse_args())


global datastamp
datastamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 

if not os.path.exists(str(datastamp)):
	os.makedirs(str(datastamp))
if not os.path.exists(str(datastamp+"\\txt")):
	os.makedirs(str(datastamp+"\\txt"))

	    
time.sleep(2)

# convert mp3 file to wav 
#sound = AudioSegment.from_opus(str(args["input"]))                                                      

#from_file', 'from_file_using_temporary_files', 'from_flv', 'from_mono_audiosegments', 'from_mp3', 'from_ogg', 'from_raw', 'from_wav

if (args["type"]) == str('ogg'):
	if not os.path.exists(str(datastamp+"\\ogg")):
		os.makedirs(str(datastamp+"\\ogg"))
	if not os.path.exists(str(datastamp+"\\txt\\ogg")):
		os.makedirs(str(datastamp+"\\txt\\ogg"))
	
	sound = AudioSegment.from_ogg(str(args["input"]))
	sound.export(datastamp+"\\"+str(args["input"])+".wav", format="wav")

if (args["type"]) == str('opus'):
	if not os.path.exists(str(datastamp+"\\opus")):
		os.makedirs(str(datastamp+"\\opus"))
	if not os.path.exists(str(datastamp+"\\txt\\opus")):
		os.makedirs(str(datastamp+"\\txt\\opus"))
	
	sound = AudioSegment.from_ogg(str(args["input"]))
	sound.export(datastamp+"\\"+str(args["input"])+".wav", format="wav")

if (args["type"]) == str('mp3'):
	if not os.path.exists(str(datastamp+"\\mp3")):
		os.makedirs(str(datastamp+"\\mp3"))
	if not os.path.exists(str(datastamp+"\\txt\\mp3")):
		os.makedirs(str(datastamp+"\\txt\\mp3"))

	sound = AudioSegment.from_mp3(str(args["input"]))
	sound.export(datastamp+"\\"+str(args["input"])+".wav", format="wav")

if (args["type"]) == str('flv'):
	if not os.path.exists(str(datastamp+"\\flv")):
		os.makedirs(str(datastamp+"\\flv"))
	if not os.path.exists(str(datastamp+"\\txt\\flv")):
		os.makedirs(str(datastamp+"\\txt\\flv"))
		

	sound = AudioSegment.from_mp3(str(args["input"]))
	sound.export(datastamp+"\\"+str(args["input"])+".wav", format="wav")

if (args["type"]) == str('wav'):
	if not os.path.exists(str(datastamp+"\\wav")):
		os.makedirs(str(datastamp+"\\wav"))
	if not os.path.exists(str(datastamp+"\\txt\\wav")):
		os.makedirs(str(datastamp+"\\txt\\wav"))
		

	sound = AudioSegment.from_mp3(str(args["input"]))
	sound.export(datastamp+"\\"+str(args["input"])+".wav", format="wav")

#time.sleep(29)

# transcribe audio file                                                         
AUDIO_FILE = (datastamp+"\\"+str(args["input"])+".wav")

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
        testo =  r.recognize_google(audio, language=str(args["language"]))                 

        print("Transcription: " + str(testo))
        
        documento = open(datastamp+"\\txt\\"+str(args["input"])+".csv", "a", encoding='utf-8')
        documento.write(str(testo))
        documento.close()
exit        
