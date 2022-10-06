#/!/Users/antonio/opt/anaconda3/bin/python
#   #!/usr/bin/python3

import speech_recognition as sr
from os import path
from pydub import AudioSegment
from datetime import datetime
import os, sys
import argparse
import time
from googletrans import Translator
import googletrans

translator = Translator()  


print(" SPEECH TRANSLATE IN PYTHON BY VISI@N \n")
     

print(
	  'af :' 'afrikaans', 'sq :' 'albanian', 'am :' 'amharic', 'ar :' 'arabic', 'hy :' 'armenian', 'az :' 'azerbaijani', '\n'
      'eu :' 'basque', 'be :' 'belarusian', 'bn :' 'bengali', 'bs :' 'bosnian', 'bg :' 'bulgarian', 'ca :' 'catalan', '\n'
      'ceb :' 'cebuano', 'ny :' 'chichewa', 'zh-cn :' 'chinese (simplified)', 'zh-tw :' 'chinese (traditional)', '\n'
      'co :' 'corsican', 'hr :' 'croatian', 'cs :' 'czech', 'da :' 'danish', 'nl :' 'dutch', 'en :' 'english', '\n'
      'eo :' 'esperanto', 'et :' 'estonian', 'tl :' 'filipino', 'fi :' 'finnish', 'fr :' 'french', 'fy :' 'frisian', '\n'
      'gl :' 'galician', 'ka :' 'georgian', 'de :' 'german', 'el :' 'greek', 'gu :' 'gujarati', 'ht :' 'haitian creole', '\n'
      'ha :' 'hausa', 'haw :' 'hawaiian', 'iw :' 'hebrew', 'he :' 'hebrew', 'hi :' 'hindi', 'hmn :' 'hmong', '\n'
      'hu :' 'hungarian', 'is :' 'icelandic', 'ig :' 'igbo', 'id :' 'indonesian', 'ga :' 'irish', 'it :' 'italian', '\n'
      'ja :' 'japanese', 'jw :' 'javanese', 'kn :' 'kannada', 'kk :' 'kazakh', 'km :' 'khmer', 'ko :' 'korean', '\n'
      'ku :' 'kurdish (kurmanji)', 'ky :' 'kyrgyz','lo :' 'lao', 'la :' 'latin', 'lv :' 'latvian', 'lt :' 'lithuanian', '\n'
      'lb :' 'luxembourgish', 'mk :' 'macedonian', 'mg :' 'malagasy', 'ms :' 'malay', 'ml :' 'malayalam', 'mt :' 'maltese','\n'
      'mi :' 'maori', 'mr :' 'marathi', 'mn :' 'mongolian', 'my :' 'myanmar (burmese)', 'ne :' 'nepali', 'no :' 'norwegian', '\n'
      'or :' 'odia', 'ps :' 'pashto', 'fa :' 'persian', 'pl :' 'polish', 'pt :' 'portuguese', 'pa :' 'punjabi', '\n'
      'ro :' 'romanian', 'ru :' 'russian', 'sm :' 'samoan', 'gd :' 'scots gaelic', 'sr :' 'serbian', 'st :' 'sesotho', '\n'
      'sn :' 'shona', 'sd :' 'sindhi', 'si :' 'sinhala', 'sk :' 'slovak', 'sl :' 'slovenian', 'so :' 'somali', '\n'
      'es :' 'spanish', 'su :' 'sundanese', 'sw :' 'swahili', 'sv :' 'swedish', 'tg :' 'tajik', 'ta :' 'tamil', '\n'
      'te :' 'telugu', 'th :' 'thai', 'tr :' 'turkish', 'uk :' 'ukrainian', 'ur :' 'urdu', 'ug :' 'uyghur', 'uz :' 'uzbek', '\n'
      'vi :' 'vietnamese', 'cy :' 'welsh', 'xh :' 'xhosa', 'yi :' 'yiddish', 'yo :' 'yoruba', 'zu :' 'zulu', '\n'

	)

#from imutils import paths


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-s", "--source", required=True,
#	help="id microphone source")
ap.add_argument("-i", "--input", required=True,
	help="input directory to convert in wav ")
ap.add_argument("-l", "--language", default="it",#required=True,
	help="input language, default Italian it")
ap.add_argument("-o", "--output", default="en",#required=True,
	help="output language, default Italian en")
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
				time.sleep(22)
				try:
				#tests = recognizer_instance.recognize_google(audio, language=str(args["input"]))		
#				tests = recognizer_instance.recognize_google(audio, language=str(args["language"]))
					time.sleep(15)
					rigatransA = translator.translate(testo,dest=(str["output"])).text
					
				
					time.sleep(29)
					print(rigatransA)
        
					documento = open(datastamp+"/txt/"+str(file)+".csv", "a", encoding='utf-8')
					documento.write(str(testo))
					documento.close()
				
#				time.sleep(39)

#				documento = open(datastamp+"/txt/"+str(file)+"_"+(str["output"])+"_"+".csv", "a", encoding='utf-8')
#				documento.write(str(rigatransA))
#				documento.close()
				except:
					print("Houston there is a problem!")
except:
	print("AHIAHAI C'è UN PROBLEMA IN QUALCHE IMMAGINE!!")	
exit
