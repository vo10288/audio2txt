#Nel contesto dell informatica forense, spesso ci troviamo ad affrontare l analisi di chat provenienti da Social Network come Whatsapp. Molti dei rinomati software di laboratorio sono in grado di estrarre in modo eccellente l'intero database, comprensivo di chat testuali e allegati come immagini, video e messaggi vocali. Tuttavia, l'aumentato utilizzo di messaggi vocali rappresenta una sfida, poiché ascoltare lunghe registrazioni può essere inefficace per l investigatore.
#Una strategia intelligente consiste nella conversione di questi file audio in testo utilizzando software di speech-to-text. Alcuni esempi di questi software sono disponibili su GitHub, e alcuni di essi sono inclusi nella distribuzione Linux disponibile su tsurugi-linux.org. È importante notare che tali software rispettano la riservatezza delle indagini, poiché non effettuano chiamate esterne attraverso API.
#Tuttavia, la sfida diventa più complessa quando è necessario non solo convertire l audio in testo, ma anche tradurlo o trasliterarlo. I migliori software per la traduzione richiedono un dataset ben addestrato con milioni di impronte vocali. Questi software, per mantenere la loro precisione, effettuano chiamate API per accedere a fonti di Machine Learning continuamente aggiornate tramite migliaia, se non milioni, di interazioni degli utenti sulle piattaforme come Google, Microsoft o IBM.
#È interessante notare che, al momento della stesura di questo articolo, alcune importanti aziende specializzate in informatica forense, soprattutto nel contesto di dispositivi mobili, stanno integrando o hanno già integrato capacità di traduzione basate su dataset di Machine Learning addestrati che operano completamente offline.
#In pratica, implementare questo processo richiede l utilizzo di librerie e API. Ad esempio, per la conversione da audio a testo, è possibile utilizzare la libreria Google Speech-to-Text in Python. Ecco un esempio di codice:
#python
# Codice per la conversione da audio a testo utilizzando Google Speech-to-Text API

import requests
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import translate_v2 as translate
import os

# Imposta la variabile d'ambiente GOOGLE_APPLICATION_CREDENTIALS
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google-cloud-sdk/platform/gsutil/gslib/tests/test_data/test_external_account_authorized_user_credentials.json"

def speech_to_text(audio_file_path):
    client = speech.SpeechClient()
    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="zh-CN"
    )

    response = client.recognize(config=config, audio=audio)

    return " ".join(result.alternatives[0].transcript for result in response.results)

# Esempio di utilizzo
audio_file_path = "it_zh-CN..wav"
text_from_audio = speech_to_text(audio_file_path)
print("Testo estratto dall'audio:", text_from_audio)

# Codice per la traduzione del testo utilizzando Google Cloud Translation API

def translate_text(text, target_language="it"):
    client = translate.Client()
    translation = client.translate(text, target_language=target_language)
    return translation["input"], translation["translatedText"]

# Esempio di utilizzo
original_text, translated_text = translate_text(text_from_audio)
print(f"Testo originale: {original_text}")
print(f"Testo tradotto: {translated_text}")
