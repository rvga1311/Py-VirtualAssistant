from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import pyttsx3
from threading import Thread
from Asistente import assistant

# =============== reconocimiento de voz =============== #
listener = sr.Recognizer()

# =============== voz del asistente =============== #
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[3].id) # eleccion de voz
engine.setProperty('rate', 160) # velocidad

def thing():
    thread1 = Thread(target=assistant, args=(engine, listener, record_txtBox))
    thread1.start()

# =============== Ventana principal =============== #
window = Tk()
window.title("Asistente virtual")
window.geometry('600x500')
window.iconbitmap('D:/Programacion/Proyectos Personales/Python/Asistente Virtual/Media/robotica.ico')


# =============== Boton para reconocimiento de voz =============== #
img = Image.open("D:/Programacion/Proyectos Personales/Python/Asistente Virtual/Media/microphone.png")
size = 100
new_img = img.resize((size,size))
imagetest = ImageTk.PhotoImage(new_img)
record_btn = Button(window, image=imagetest, command=thing, height = size, width = size, borderwidth=5, bg='#32a6a8')
record_btn.pack(pady=20)

# =============== TextBox para reconocimiento de voz =============== #
size = 12
record_txtBox = Text(window, height= size, width= size*3)
record_txtBox.pack(pady=20)

# =============== Loop principal =============== #
window.mainloop()


