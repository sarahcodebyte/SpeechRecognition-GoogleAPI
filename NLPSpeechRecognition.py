import googletrans
import speech_recognition as sr 
import pyttsx3

engine=pyttsx3.init()
recogonizer=sr.Recogonizer()

with sr.Microphone() as source:
    print('wait for callibration')
    recogonizer.adjust_for_ambient_noise(source, 1)
    print('start speaking')
    audio=recogonizer.listen(source)
    print('recorded succesfully')
    speech=recogonizer.recognize_google(audio)
    speech=speech.lower()
    print(speech)
    
    
def trans():
    print('Translating...')
    print(googletrans.LANGCODES)
    language=input('Type the translation lagugae code').lower()
    translator=googletrans.Translator()
    translation=translator.translate(text=speech, dest=language) 
    print('Translation: ', translation.text)
    engine.setProperty('rate', 120)
    engine.say(translation.pronunciation)
    engine.runAndWait()
    
trans()       