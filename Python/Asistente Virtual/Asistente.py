import speech_recognition as sr
import pyttsx3, pywhatkit, datetime, os, winshell
from tkinter import *
from tkinter import filedialog, messagebox
from threading import Thread
from pytube import YouTube

def voiceAssistant(engine,phrase):
    engine.say(phrase)
    engine.runAndWait()


def assistant(engine, listener, txtBox):
    saludo = "Que deseas que haga por ti, jefe"
    thread = Thread(target=voiceAssistant, args=(engine, saludo))
    thread.start()

    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            rec = listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            rec= listener.listen(source)
            rec= listener.recognize_google(voice, language = "es" )
            rec =  rec.lower()

        txtBox.delete('1.0', END)
        txtBox.insert(END,rec)

        if 'busca' in rec:
            search = rec
            search =  search.replace('busca ','')
            search =  search.replace(' en google','') 
            phrase = "Buscando en google: " + search
            thread.join()
            thread = Thread(target=voiceAssistant, args=(engine, phrase))
            thread.start()
            pywhatkit.search(search)
        elif 'reproduce' in rec:
            music = rec
            music =  music.replace('reproduce ','') 
            phrase = "Reproduciendo: " + music + ", que lo disfrutes"
            thread.join()
            thread = Thread(target=voiceAssistant, args=(engine, phrase))
            thread.start()
            pywhatkit.playonyt(music)
        elif 'que hora' in rec or 'qué hora' in rec:
            hora = datetime.datetime.now().strftime('%H:%M %p')
            thread.join()
            thread = Thread(target=voiceAssistant, args=(engine, "Son las "+ hora))
            thread.start()
        elif 'abre' in rec:
            if 'el navegador' in rec:
                thread.join()
                thread = Thread(target=voiceAssistant, args=(engine, "Abriendo el navegador, que tengas buenas partidas"))
                thread.start()
                os.system('start C:/Users/RVGA1/AppData/Roaming/Microsoft/Windows/"Start Menu"/Programs/"Opera GX".lnk')
        elif 'cierra' in rec:
            if 'el navegador' in rec:
                thread.join()
                thread = Thread(target=voiceAssistant, args=(engine, "Cerrando el navegador..."))
                thread.start()
                os.system('taskkill /F /IM opera.exe')
        elif 'la papelera' in rec:
            thread.join()
            thread = Thread(target=voiceAssistant, args=(engine, "Vaciando la papelera de reciclaje"))
            thread.start()
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        else:
            frase = "Vuelve a intentarlo."
            thread.join()
            thread = Thread(target=voiceAssistant, args=(engine, frase))
            thread.start()
    except:
        thread = Thread(target=voiceAssistant, args=(engine, "Ha ocurrido un error, vuelve a intentarlo."))
        thread.start()


link_video = ""
    

#donwload video
def DownloadVideo(label, choices, choices_combBox, link_txtbox,Folder_Name):
    choice = choices_combBox.get()

    if(len(link_video)>1):
        label.config(text="")
        yt = YouTube(link_video)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            label.config(text="Paste Link again!!",fg="red")

    #download function
    try:
        select.download(Folder_Name)
        label.config(text="Download Completed!!")
    except:
        messagebox.showerror("Error","La descarga no se ha podido ejecutar de manera correcta.")

