#/!/Users/antonio/opt/anaconda3/bin/python
#   #!/usr/bin/python3

import speech_recognition as sr
from os import path
from pydub import AudioSegment
from datetime import datetime
import os, sys
import argparse
import time
#from imutils import paths


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-s", "--source", required=True,
#	help="id microphone source")
ap.add_argument("-i", "--input", required=True,
	help="input directory to convert in wav ")
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

if not os.path.exists(str(datastamp+"/wav")):
	os.makedirs(str(datastamp+"/wav"))

if not os.path.exists(str(datastamp+"/txt")):
	os.makedirs(str(datastamp+"/txt"))
	    
#time.sleep(2)

# convert mp3 file to wav 
#sound = AudioSegment.from_opus(str(args["input"]))                                                      

#from_file', 'from_file_using_temporary_files', 'from_flv', 'from_mono_audiosegments', 'from_mp3', 'from_ogg', 'from_raw', 'from_wav

####################### DIR LIST #####################
dirs = os.listdir(str(args["input"]) )

try:
	
	
	# loop over the image paths
	for file in dirs:
		print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
		print(str(args["input"])+'/'+str(file))
####################################################
		if (args["type"]) == str('ogg'):

			sound = AudioSegment.from_ogg(str(args["input"])+'/'+str(file))
			sound.export(datastamp+"/wav/"+str(file)+".wav", format="wav")

		if (args["type"]) == str('mp3'):

			sound = AudioSegment.from_mp3(str(args["input"])+'/'+str(file))
			sound.export(datastamp+"/wav/"+str(file)+".wav", format="wav")

		if (args["type"]) == str('flv'):

			sound = AudioSegment.from_flv(str(args["input"])+'/'+str(file))
			sound.export(datastamp+"/wav/"+str(file)+".wav", format="wav")

		if (args["type"]) == str('wav'):

			sound = AudioSegment.from_wav(str(args["input"])+'/'+str(file))
			sound.export(datastamp+"/wav/"+str(file)+".wav", format="wav")

#time.sleep(29)

# transcribe audio file                                                         
		AUDIO_FILE = (datastamp+"/wav/"+str(file)+".wav")

# use the audio file as the audio source                                        
		r = sr.Recognizer()
		with sr.AudioFile(AUDIO_FILE) as source:
				audio = r.record(source)  # read the entire audio file
				testo =  r.recognize_google(audio, language=str(args["language"]))
				print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")                 

				print("Transcription: " + str(testo))
				print ("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
        
				documento = open(datastamp+"/txt/"+str(file)+".csv", "a", encoding='utf-8')
				documento.write(str(testo))
				documento.close()
except:
	print("AHIAHAI C'è UN PROBLEMA IN QUALCHE IMMAGINE!!")	
exit
