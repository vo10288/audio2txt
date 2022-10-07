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
ap.add_argument("-t", "--type", default="opus",  type=str,#required=True,
	help="type format file ogg mp3 flv wav opus")

#ap.add_argument("-o", "--output", default="it",#required=True,
#	help="output language, default Italian it")
	
args = vars(ap.parse_args())


global datastamp
datastamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 

if not os.path.exists(str(datastamp)):
	os.makedirs(str(datastamp))
if not os.path.exists(str(datastamp+"/txt")):
	os.makedirs(str(datastamp+"/txt"))

documentoHTML = open(datastamp+"\\"+datastamp+".html", "a", encoding='utf-8')
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
		print(str(args["input"])+'\\'+str(file))
####################################################
		if (args["type"]) == str('ogg'):
			if not os.path.exists(str(datastamp+"\\ogg")):
				os.makedirs(str(datastamp+"\\ogg"))
			if not os.path.exists(str(datastamp+"\\txt\\")):
				os.makedirs(str(datastamp+"\\txt\\"))
	
			sound = AudioSegment.from_ogg(str(args["input"])+'\\'+str(file))
			sound.export(datastamp+"\\ogg\\"+str(file)+".wav", format="wav")
################ opus okei #######################
		if (args["type"]) == str('opus'):
			if not os.path.exists(str(datastamp+"\\opus")):
				os.makedirs(str(datastamp+"\\opus"))
			if not os.path.exists(str(datastamp+"\\txt\\")):
				os.makedirs(str(datastamp+"\\txt\\"))
	
			sound = AudioSegment.from_ogg(str(args["input"])+'\\'+str(file))
			sound.export(datastamp+"\\opus\\"+str(file)+".wav", format="wav")
#######################################################
		if (args["type"]) == str('mp3'):
			if not os.path.exists(str(datastamp+"\\mp3")):
				os.makedirs(str(datastamp+"\\mp3"))
			if not os.path.exists(str(datastamp+"\\txt\\")):
				os.makedirs(str(datastamp+"\\txt\\"))

			sound = AudioSegment.from_file(str(args["input"])+'\\'+str(file))
			sound.export(datastamp+"\\mp3\\"+str(file)+".wav", format="wav")

		if (args["type"]) == str('flv'):
			if not os.path.exists(str(datastamp+"\\flv")):
				os.makedirs(str(datastamp+"\\flv"))
			if not os.path.exists(str(datastamp+"\\txt\\")):
				os.makedirs(str(datastamp+"\\txt\\"))

			sound = AudioSegment.from_flv(str(args["input"])+'\\'+str(file))
			sound.export(datastamp+"\\flv\\"+str(file)+".wav", format="wav")

		if (args["type"]) == str('wav'):
			if not os.path.exists(str(datastamp+"\\wav")):
				os.makedirs(str(datastamp+"\\wav"))
			if not os.path.exists(str(datastamp+"\\txt\\")):
				os.makedirs(str(datastamp+"\\txt\\"))
		

			sound = AudioSegment.from_wav(str(args["input"])+'\\'+str(file))
			sound.export(datastamp+"\\wav\\"+str(file)+".wav", format="wav")


#time.sleep(29)

# transcribe audio file                                                         
		AUDIO_FILE = (datastamp+"\\"+str(args["input"])+'\\'+str(file)+".wav")

# use the audio file as the audio source                                        
		r = sr.Recognizer()
		with sr.AudioFile(AUDIO_FILE) as source:
				audio = r.record(source)  # read the entire audio file
				testo =  r.recognize_google(audio, language=str(args["language"]))
				print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")                 

				print("Transcription: " + str(testo))
				print ("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
				
			
				documento = open(datastamp+"\\txt\\"+str(file)+".csv", "a", encoding='utf-8')
				documento.write(str(testo))
				documento.close()
				
				documentoHTML.write("<tr><td><h2><font color='blue'><a target=\'_blank\' href=\'"+"..\\"+(str(args["input"])+'\\'+str(file))+"\'>"+(str(args["input"])+'\\'+str(file))+"</font></a></h2></td>")
				documentoHTML.write("<td><h2><font color='darkblue'>"+testo+"<br></font></h2></td></tr>")
except:
	print("AHIAHAI C'è UN PROBLEMA IN QUALCHE IMMAGINE!!")	

documentoHTML.write("</table>")
documentoHTML.write("</body>")
documentoHTML.write("</html>")
documentoHTML.close()
print(documentoHTML)
os.startfile(datastamp+"\\"+datastamp+".html")

exit
