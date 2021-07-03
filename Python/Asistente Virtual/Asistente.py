import speech_recognition as sr
import pyttsx3, pywhatkit, datetime
from tkinter import *
from threading import Thread

def assistant(engine, listener, txtBox):
    saludo = "Que deseas que haga por ti, jefe"
    thread = Thread(target=voiceAsistente, args=(engine, saludo))
    thread.start()

    with sr.Microphone() as source:
        print("Escuchando...")
        rec = listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        rec= listener.listen(source)
        rec= listener.recognize_google(voice, language = "es" )
        rec =  rec.lower()

    txtBox.delete('1.0', END)
    txtBox.insert(END,rec)

    if 'busca en google' in rec:
        search = rec
        search =  search.replace('busca en google ','') 
        frase = "Buscando en google " + search
        thread.join()
        thread = Thread(target=voiceAsistente, args=(engine, frase))
        thread.start()
        pywhatkit.search(search)
    elif 'reproduce' in rec:
        music = rec
        music =  music.replace('reproduce ','') 
        frase = "Reproduciendo " + music + ", que lo disfrutes"
        thread.join()
        thread = Thread(target=voiceAsistente, args=(engine, frase))
        thread.start()
        pywhatkit.playonyt(music)
    elif 'que hora' in rec or 'qué hora' in rec:
        hora = datetime.datetime.now().strftime('%H:%M %p')
        thread = Thread(target=voiceAsistente, args=(engine, "Son las "+ hora))
        thread.start()
    else:
        frase = "Vuelve a intentarlo."
        thread.join()
        thread = Thread(target=voiceAsistente, args=(engine, frase))
        thread.start()

def voiceAsistente(engine,frase):
    engine.say(frase)
    engine.runAndWait()
