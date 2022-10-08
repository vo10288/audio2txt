#/!/Users/antonio/opt/anaconda3/bin/python
#python == 3.10.7
#by Visi@n 20221008 h.13.41

import speech_recognition as sr
from pydub import AudioSegment
import os
from datetime import datetime
import os, sys
import argparse
import time
from googletrans import Translator
import googletrans

import pygame
pygame.init()
import time
from gtts import gTTS 

translator = Translator()  

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-s", "--source", required=True,
#	help="id microphone source")
ap.add_argument("-i", "--input", default="wav",# required=True,
	help="input directory file to convert ")
ap.add_argument("-l", "--language", default="it",#required=True,
	help="input language, default Italian it")
ap.add_argument("-o", "--output", default="en",#required=True,
	help="output language, default Italian en")
ap.add_argument("-t", "--type", default="wav",  type=str,#required=True,
	help="type format file ogg mp3 flv wav opus")

#ap.add_argument("-o", "--output", default="it",#required=True,
#	help="output language, default Italian it")
	
args = vars(ap.parse_args())


global datastamp
datastamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 

dirs = os.listdir(str(args["input"]))

outputdirectory = (datastamp+"_"+str(args["input"])+"_"+str(args["language"])+"_"+str(args["output"]))

if not os.path.exists(outputdirectory):
	os.makedirs(outputdirectory)

documentoHTML = open(outputdirectory+"\\"+datastamp+".html", "a", encoding='utf-8')
documentoHTML.write("<html>")
documentoHTML.write("<head>")

documentoHTML.write("<style>")
documentoHTML.write("table, th, td {")
documentoHTML.write("	  border: 1px solid black;")
documentoHTML.write("}")
documentoHTML.write("</style>")
documentoHTML.write("<title>")
documentoHTML.write(str(args["input"]))
documentoHTML.write("</title>")
documentoHTML.write("</head>")
documentoHTML.write("<h1><font color='darkblue'> Audio2Text by Visi@n </font></h1>")
documentoHTML.write("<br><br>")

documentoHTML.write("<body>")
documentoHTML.write("<table>")

	
for file in dirs:
	filestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 

	print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
	print(str(args["input"])+'\\'+str(file))
##from_file', 'from_file_using_temporary_files', 'from_flv', 'from_mono_audiosegments', 'from_mp3', 'from_ogg', 'from_raw', 'from_wav

	#######################################################
	if (args["type"]) == str('opus'):
			if not os.path.exists(datastamp+"_"+str(args["type"])+"_WAV"):
				os.makedirs(datastamp+"_"+str(args["type"])+"_WAV")
			

			sound = AudioSegment.from_ogg(str(args["input"])+'\\'+str(file))
			sound.export(datastamp+"_"+str(args["type"])+"_WAV"+"\\"+str(file)+".wav", format="wav")

	#######################################################
	if (args["type"]) == str('ogg'):
			if not os.path.exists(datastamp+"_"+str(args["type"])+"_WAV"):
				os.makedirs(datastamp+"_"+str(args["type"])+"_WAV")
			

			sound = AudioSegment.from_ogg(str(args["input"])+'\\'+str(file))
			sound.export(datastamp+"_"+str(args["type"])+"_WAV"+"\\"+str(file)+".wav", format="wav")

	#######################################################
	if (args["type"]) == str('mp3'):
			if not os.path.exists(datastamp+"_"+str(args["type"])+"_WAV"):
				os.makedirs(datastamp+"_"+str(args["type"])+"_WAV")
			

			sound = AudioSegment.from_file(str(args["input"])+'\\'+str(file))
			sound.export(datastamp+"_"+str(args["type"])+"_WAV"+"\\"+str(file)+".wav", format="wav")

	#######################################################
	if (args["type"]) == str('flv'):
			if not os.path.exists(datastamp+"_"+str(args["type"])+"_WAV"):
				os.makedirs(datastamp+"_"+str(args["type"])+"_WAV")
			

			sound = AudioSegment.from_flv(str(args["input"])+'\\'+str(file))
			sound.export(datastamp+"_"+str(args["type"])+"_WAV"+"\\"+str(file)+".wav", format="wav")
	
	#######################################################
	if (args["type"]) == str('wav'):
			if not os.path.exists(datastamp+"_"+str(args["type"])+"_WAV"):
				os.makedirs(datastamp+"_"+str(args["type"])+"_WAV")
			

			sound = AudioSegment.from_wav(str(args["input"])+'\\'+str(file))
			sound.export(datastamp+"_"+str(args["type"])+"_WAV"+"\\"+str(file)+".wav", format="wav")
	
	#######################################################
	time.sleep(1)

	AUDIO_FILE = (datastamp+"_"+str(args["type"])+"_WAV"+"\\"+str(file)+".wav")

	# use the audio file as the audio source                                        
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)  # read the entire audio file
		testo =  r.recognize_google(audio, language=str(args["language"]))
		print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")                 

		print("Transcription: " + str(testo))
		print ("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
		
		rigatransA = translator.translate(testo,dest=str(args["output"])).text
		
		########################################################## save audio translated in mp3
		# Language in which you want to convert 
		global language
		language = (args["output"])
		# have a high speed 
		myobj = gTTS(text=rigatransA, lang=language, slow=False) 
		# welcome  
		myobj.save(datastamp+"_"+str(args["type"])+"_WAV"+"\\"+str(file)+"_"+args["language"]+"_"+args["output"]+".mp3") 
		# Playing the converted file 
		pygame.mixer.music.load(datastamp+"_"+str(args["type"])+"_WAV"+"\\"+str(file)+"_"+args["language"]+"_"+args["output"]+".mp3") 

		##########################################################			
				
		print(rigatransA)
        
        
		documento = open(outputdirectory+"\\"+str(file)+".csv", "a", encoding='utf-8')
		documento.write(str(testo))
		documento.write("                                                          ")
		documento.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		documento.write("                                                          ")
		documento.write(str(rigatransA))
		documento.close()
		
		documentoHTML.write("<tr><td><h4><font color='blue'><a target=\'_blank\' href=\'"+"..\\"+(str(args["input"])+'\\'+str(file))+"\'>"+(str(args["input"])+'\\'+str(file))+"</font></a></h2><br>")
		documentoHTML.write("<h4><font color='blue'><a target=\'_blank\' href=\'"+"..\\"+datastamp+"_"+str(args["type"])+"_WAV"+"\\"+str(file)+"_"+args["language"]+"_"+args["output"]+".mp3"+"\'>"+datastamp+"_"+str(args["type"])+"_WAV"+"\\"+str(file)+"_"+args["language"]+"_"+args["output"]+".mp3"+"</font></a></h2></td>")

		#datastamp+"_"+str(args["type"])+"_WAV"+"\\"+str(file)+"_"+args["language"]+"_"+args["output"]+".mp3"
		documentoHTML.write("<td><h4><font color='darkblue'>"+testo+"<br><p align='center'>"+"= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = </p>"+rigatransA+"<br></font></h2></td></tr>")



documentoHTML.write("</table>")
documentoHTML.write("</body>")
documentoHTML.write("</html>")
documentoHTML.close()
print(documentoHTML)
os.startfile(outputdirectory+"\\"+datastamp+".html")
		
