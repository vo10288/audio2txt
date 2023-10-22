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
import subprocess

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

print(
'Albert              en_US    # I have a frog in my throat. No, I mean a real frog!\n'
'Alice               it_IT     Salve, mi chiamo Alice e sono una voce italiana.\n'
'Alva                sv_SE     Hej, jag heter Alva. Jag är en svensk röst.\n'
'Amélie              fr_CA    '# Bonjour, je m'appelle Amélie. Ma voix est en français canadien.\n'
'Amira               ms_MY    # Helo, nama saya Amira. Saya bercakap Bahasa Melayu.\n'
'Anna                de_DE    # Hallo, ich heiße Anna und ich bin eine deutsche Stimme.\n'
'Bad News            en_US    # I sure like being inside this fancy computer\n'
'Bahh                en_US    # Do not pull the wool over my eyes.\n'
'Bells               en_US    # Time flies when you are having fun.\n'
'Boing               en_US    '# Spring has sprung, fall has fell, winter's here and it's colder than usual.\n'
'Bubbles             en_US    # I sure like being inside this fancy computer\n'
'Carmit              he_IL    # שלום. קוראים לי כרמית, ואני קול בשפה העברית.\n'
'Cellos              en_US    # Doo da doo da dum dee dee doodly doo dum dum dum doo da doo da doo da doo da doo da doo da doo\n'
'Damayanti           id_ID    # Halo, nama saya Damayanti. Saya berbahasa Indonesia.\n'
'Daniel              en_GB    # Hello, my name is Daniel. I am a British-English voice.\n'
'Daria               bg_BG    # Здравей, казвам се Дария и съм български глас.\n'
'Wobble              en_US    # I sure like being inside this fancy computer\n'
'Eddy (Tedesco (Germania)) de_DE    '# Hallo! Ich heiße Eddy.\n'
'Eddy (Inglese (UK)) en_GB    '# Hello! My name is Eddy.\n'
'Eddy (Inglese (USA)) en_US    # Hello! My name is Eddy.\n'
'Eddy (Spagnolo (Spagna)) es_ES    # ¡Hola! Me llamo Eddy.\n'
'Eddy (Spagnolo (Messico)) es_MX    # ¡Hola! Me llamo Eddy.\n'
'Eddy (Finlandese (Finlandia)) fi_FI    # Hei! Nimeni on Eddy.\n'
'Eddy (Francese (Canada)) fr_CA    # Bonjour! Je m’appelle Eddy.\n'
'Eddy (Francese (Francia)) fr_FR    # Bonjour, je m’appelle Eddy.\n'
'Eddy (Italiano (Italia)) it_IT    # Ciao! Mi chiamo Eddy.\n'
'Eddy (Portoghese (Brasile)) pt_BR    # Olá, meu nome é Eddy.\n'
'Ellen               nl_BE    # Hallo, mijn naam is Ellen. Ik ben een Belgisch-Nederlandse stem.\n'
'Emma (Premium)      it_IT    # Salve, mi chiamo Emma e sono una voce italiana.\n'
'Flo (Tedesco (Germania)) de_DE    # Hallo! Ich heiße Flo.\n'
'Flo (Inglese (UK))  en_GB    # Hello! My name is Flo.\n'
'Flo (Inglese (USA)) en_US    # Hello! My name is Flo.\n'
'Flo (Spagnolo (Spagna)) es_ES    # ¡Hola! Me llamo Flo.\n'
'Flo (Spagnolo (Messico)) es_MX    # ¡Hola! Me llamo Flo.\n'
'Flo (Finlandese (Finlandia)) fi_FI    # Hei! Nimeni on Flo.\n'
'Flo (Francese (Canada)) fr_CA    # Bonjour! Je m’appelle Flo.\n'
'Flo (Francese (Francia)) fr_FR    # Bonjour, je m’appelle Flo.\n'
'Flo (Italiano (Italia)) it_IT    # Ciao! Mi chiamo Flo.\n'
'Flo (Portoghese (Brasile)) pt_BR    # Olá, meu nome é Flo.\n'
'Fred                en_US    # I sure like being inside this fancy computer\n'
'Good News           en_US    # Congratulations you just won the sweepstakes and you don t have to pay income tax again.\n'
'Grandma (Tedesco (Germania)) de_DE    # Hallo! Ich heiße Grandma.\n'
'Grandma (Inglese (UK)) en_GB    # Hello! My name is Grandma.\n'
'Grandma (Inglese (USA)) en_US    # Hello! My name is Grandma.\n'
'Grandma (Spagnolo (Spagna)) es_ES    # ¡Hola! Me llamo Grandma.\n'
'Grandma (Spagnolo (Messico)) es_MX    # ¡Hola! Me llamo Grandma.\n'
'Grandma (Finlandese (Finlandia)) fi_FI    # Hei! Nimeni on Grandma.\n'
'Grandma (Francese (Canada)) fr_CA    # Bonjour! Je m’appelle Grandma.\n'
'Grandma (Francese (Francia)) fr_FR    # Bonjour, je m’appelle Grandma.\n'
'Grandma (Italiano (Italia)) it_IT    # Ciao! Mi chiamo Grandma.\n'
'Grandma (Portoghese (Brasile)) pt_BR    # Olá, meu nome é Grandma.\n'
'Grandpa (Tedesco (Germania)) de_DE    # Hallo! Ich heiße Grandpa.\n'
'Grandpa (Inglese (UK)) en_GB    # Hello! My name is Grandpa.\n'
'Grandpa (Inglese (USA)) en_US    # Hello! My name is Grandpa.\n'
'Grandpa (Spagnolo (Spagna)) es_ES    # ¡Hola! Me llamo Grandpa.\n'
'Grandpa (Spagnolo (Messico)) es_MX    # ¡Hola! Me llamo Grandpa.\n'
'Grandpa (Finlandese (Finlandia)) fi_FI    # Hei! Nimeni on Grandpa.\n'
'Grandpa (Francese (Canada)) fr_CA    # Bonjour! Je m’appelle Grandpa.\n'
'Grandpa (Francese (Francia)) fr_FR    # Bonjour, je m’appelle Grandpa.\n'
'Grandpa (Italiano (Italia)) it_IT    # Ciao! Mi chiamo Grandpa.\n'
'Grandpa (Portoghese (Brasile)) pt_BR    # Olá, meu nome é Grandpa.\n'
'Jester              en_US    # Please stop tickling me!\n'
'Ioana               ro_RO    # Bună, mă cheamă Ioana. Sunt o voce românească.\n'
'Jacques             fr_FR    # Bonjour, je m’appelle Jacques.\n'
'Joana               pt_PT    # Olá, chamo-me Joana e dou voz ao português falado em Portugal.\n'
'Junior              en_US    # My favorite food is pizza.\n'
'Kanya               th_TH    # สวัสดีค่ะ ดิฉันชื่อกันยา\n'
'Karen               en_AU    # Hello, my name is Karen. I am an Australian-English voice.\n'
'Kathy               en_US    # Isn t it nice to have a computer that will talk to you?\n'
'Kyoko               ja_JP    # こんにちは、私の名前はきょうこです。日本語の音声をお届けします。\n'
'Lana                hr_HR    # Bog! Moje je ime Lana. Ja sam hrvatski glas.\n'
'Laura               sk_SK    # Ahoj. Volám sa Laura. Som hlas v slovenskom jazyku.\n'
'Lekha               hi_IN    # नमस्कार, मेरा नाम लेखा है! मैं हिन्दी में बोलने वाली आवाज़ हूँ!\n'
'Lesya               uk_UA    # Привіт, мене звуть Леся. Я — український голос.\n'
'Linh                vi_VN    # Xin chào, tên tôi là Linh. Tôi là giọng nói Tiếng Việt.\n'
'Luciana             pt_BR    # Olá, o meu nome é Luciana e a minha voz corresponde ao português que é falado no Brasil'
'Majed               ar_001 \n' # # مرحبًا، اسمي ماجد. أنا صوتٌ عرب'ي''''#\
'Tünde               hu_HU     Üdvözlöm! Tünde vagyok. Én vagyok a magyar hang.\n'
'Meijia              zh_TW    # 你好，我叫美佳。我說國語。\n'
'Melina              el_GR    # ονομάζομαι Μελίνα. Μιλάω ελληνικά.\n'
'Milena              ru_RU    # Здравствуйте, меня зовут Милена. Я — русский голос системы.\n'
'Moira               en_IE    # Hello, my name is Moira. I am an Irish-English voice.\n'
'Mónica              es_ES    # Hola, me llamo Mónica y soy una voz española.\n'
'Montse              ca_ES    # Hola, em dic Montse i soc una veu catalana.\n'
'Nora                nb_NO    # Hei, jeg heter Nora. Jeg er en norsk stemme.\n'
'Organ               en_US    # We must rejoice in this morbid voice.\n'
'Paulina             es_MX    # Hola, me llamo Paulina y soy una voz mexicana.\n'
'Superstar           en_US    # When I grow up I m going to be a scientist.\n'
'Ralph               en_US    # The sum of the squares of the legs of a right triangle is equal to the square of the hypotenuse.\n'
'Reed (Tedesco (Germania)) de_DE    # Hallo! Ich heiße Reed.\n'
'Reed (Inglese (UK)) en_GB    # Hello! My name is Reed.\n'
'Reed (Inglese (USA)) en_US    # Hello! My name is Reed.\n'
'Reed (Spagnolo (Spagna)) es_ES    # ¡Hola! Me llamo Reed.\n'
'Reed (Spagnolo (Messico)) es_MX    # ¡Hola! Me llamo Reed.\n'
'Reed (Finlandese (Finlandia)) fi_FI    # Hei! Nimeni on Reed.\n'
'Reed (Francese (Canada)) fr_CA    # Bonjour! Je m’appelle Reed.\n'
'Reed (Italiano (Italia)) it_IT    # Ciao! Mi chiamo Reed.\n'
'Reed (Portoghese (Brasile)) pt_BR   # Olá, meu nome é Reed.\n'
'Rishi               en_IN    # Hello, my name is Rishi. I am an Indian-English voice.\n'
'Rocko (Tedesco (Germania)) de_DE    # Hallo! Ich heiße Rocko.\n'
'Rocko (Inglese (UK)) en_GB    # Hello! My name is Rocko.\n'
'Rocko (Inglese (USA)) en_US    # Hello! My name is Rocko.\n'
'Rocko (Spagnolo (Spagna)) es_ES    # ¡Hola! Me llamo Rocko.\n'
'Rocko (Spagnolo (Messico)) es_MX    # ¡Hola! Me llamo Rocko.\n'
'Rocko (Finlandese (Finlandia)) fi_FI    # Hei! Nimeni on Rocko.\n'
'Rocko (Francese (Canada)) fr_CA    # Bonjour! Je m’appelle Rocko.\n'
'Rocko (Francese (Francia)) fr_FR    # Bonjour, je m’appelle Rocko.\n'
'Rocko (Italiano (Italia)) it_IT    # Ciao! Mi chiamo Rocko.\n'
'Rocko (Portoghese (Brasile)) pt_BR    # Olá, meu nome é Rocko.\n'
'Samantha            en_US    # Hello, my name is Samantha. I am an American-English voice.\n'
'Sandy (Tedesco (Germania)) de_DE    # Hallo! Ich heiße Sandy.\n'
'Sandy (Inglese (UK)) en_GB    # Hello! My name is Sandy.\n'
'Sandy (Inglese (USA)) en_US    # Hello! My name is Sandy.\n'
'Sandy (Spagnolo (Spagna)) es_ES    # ¡Hola! Me llamo Sandy.\n'
'Sandy (Spagnolo (Messico)) es_MX    # ¡Hola! Me llamo Sandy.\n'
'Sandy (Finlandese (Finlandia)) fi_FI    # Hei! Nimeni on Sandy.\n'
'Sandy (Francese (Canada)) fr_CA    # Bonjour! Je m’appelle Sandy.\n'
'Sandy (Francese (Francia)) fr_FR    # Bonjour, je m’appelle Sandy.\n'
'Sandy (Italiano (Italia)) it_IT    # Ciao! Mi chiamo Sandy.\n'
'Sandy (Portoghese (Brasile)) pt_BR    # Olá, meu nome é Sandy.\n'
'Sara                da_DK    # Hej, jeg hedder Sara. Jeg er en dansk stemme.\n'
'Satu                fi_FI    # Hei, minun nimeni on Satu. Olen suomalainen ääni.\n'
'Shelley (Tedesco (Germania)) de_DE    # Hallo! Ich heiße Shelley.\n'
'Shelley (Inglese (UK)) en_GB   # Hello! My name is Shelley.\n'
'Shelley (Inglese (USA)) en_US    # Hello! My name is Shelley.\n'
'Shelley (Spagnolo (Spagna)) es_ES    # ¡Hola! Me llamo Shelley.\n'
'Shelley (Spagnolo (Messico)) es_MX    # ¡Hola! Me llamo Shelley.\n'
'Shelley (Finlandese (Finlandia)) fi_FI    # Hei! Nimeni on Shelley.\n'
'Shelley (Francese (Canada)) fr_CA    # Bonjour! Je m’appelle Shelley.\n'
'Shelley (Francese (Francia)) fr_FR    # Bonjour, je m’appelle Shelley.\n'
'Shelley (Italiano (Italia)) it_IT    # Ciao! Mi chiamo Shelley.\n'
'Shelley (Portoghese (Brasile)) pt_BR    # Olá, meu nome é Shelley.\n'
'Sinji               zh_HK   # 你好，我叫善怡。我講廣東waa2。\n'
'Tessa               en_ZA    # Hello, my name is Tessa. I am a South African-English voice.\n'
'Thomas              fr_FR    # Bonjour, je m appelle Thomas. Je suis une voix française.\n'
'Tingting            zh_CN    # 你好，我叫 婷婷。我是中文普通话语音。\n'
'Trinoids            en_US    # We cannot communicate with these carbon units.\n'
'Whisper             en_US    # Pssssst, hey you, Yeah you, Who do ya think I m talking to, the mouse?\n'
'Xander              nl_NL   # Hallo, mijn naam is Xander. Ik ben een Nederlandse stem.\n'
'Yelda               tr_TR    # Merhaba, benim adım Yelda. Ben Türkçe bir sesim.\n'
'Yuna                ko_KR    # 안녕하세요. 제 이름은 유나입니다. 저는 한국어 음성입니다.\n'
'Zarvox              en_US    # That looks like a peaceful planet.\n'
'Zosia               pl_PL    # Witaj. Mam na imię Zosia, jestem głosem kobiecym dla języka polskiego.\n'
'Zuzana              cs_CZ    # Dobrý den, jmenuji se Zuzana. Jsem český hlas.\n'

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
ap.add_argument("-r", "--trans", default="Shelley",  type=str,#required=True,
	help="Meijia Sandy Shelley Red Rocko")
ap.add_argument("-s", "--say", default="Meijia",  type=str,#required=True,
	help="Meijia Sandy Shelley Red Rocko")

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
				time.sleep(6)
				try:
				#tests = recognizer_instance.recognize_google(audio, language=str(args["input"]))		
#				tests = recognizer_instance.recognize_google(audio, language=str(args["language"]))
					time.sleep(1)
					rigatransA = translator.translate(testo,dest=(str(args["output"]))).text
					
				
					time.sleep(9)
					print("Translated: " +str(rigatransA))
        
					documento = open(datastamp+"/txt/"+str(file)+"_"+str(args["input"])+"_.csv", "a", encoding='utf-8')
					documento.write(testo)
					documento.close()
					time.sleep(2)
					
					comando = ('say -v '+str(args["say"])+'  \"'+str(testo))+'\"'
					subprocess.Popen(comando, shell=True)
					time.sleep(9)
					
					documento2 = open(datastamp+"/txt/"+str(file)+"_"+str(args["language"])+"_.csv", "a", encoding='utf-8')
					documento2.write(rigatransA)
					documento2.close()
					time.sleep(2)
					
					#comando = ('say -v '+str(args["trans"])+'  \"'+str(rigatransA))+'\"'
					comando = ('say '+'\"'+str(rigatransA))+'\"'
					subprocess.Popen(comando, shell=True)
					time.sleep(9)
					
#				time.sleep(39)

#				documento = open(datastamp+"/txt/"+str(file)+"_"+(str["output"])+"_"+".csv", "a", encoding='utf-8')
#				documento.write(str(rigatransA))
#				documento.close()
				except Exception as e:
					print("Translation error:", e)
except Exception as e:
	print("ALL error:", e)
	#print("AHIAHAI C'è UN PROBLEMA IN QUALCHE IMMAGINE!!")	
exit
