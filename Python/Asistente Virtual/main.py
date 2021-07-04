# ============================== Librerias ============================== #
from tkinter import *
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import speech_recognition as sr
import pyttsx3, os
from threading import Thread
from Asistente import assistant
from pytube import YouTube

#=================================================================================
# ============================== inicializaciones ============================== #
# =============== reconocimiento de voz =============== #
listener = sr.Recognizer()
# =============== voz del asistente =============== #
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[3].id) # eleccion de voz
engine.setProperty('rate', 160) # velocidad

#==========================================================================
# ============================== Funciones ============================== #
def virtualAssitant_func():
    thread = Thread(target=assistant, args=(engine, listener, record_txtBox))
    thread.start()

Folder_Name = ""
#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        file = Folder_Name
        if len(Folder_Name) > 36:
            file = ".../"+ os.path.basename(file)
        path_lbl.config(text=file,fg="green")

    else:
        path_lbl.config(text="Porfavor, seleccione una direccion valida.",fg="red")

def upload():
    url = link_entry.get()
    if(len(url)>1):
        yt = YouTube(url)
def ytDownload():
    print("a")



#==================================================================================
# ============================== Ventana principal ============================== #
window = Tk()
window.title("Asistente virtual")
window.geometry('1000x700')
window.iconbitmap('D:/Programacion/Proyectos Personales/Python/Asistente Virtual/Media/robotica.ico')
window.resizable(False, False)

fontWindow = ("Segoe Print", 12)

#==================================================================
# =============== Frame Asistente Virtual por voz =============== #
virtualAssitant_frame =  Frame(window, width=750, height=700)

# Label titulo
title_lbl = Label(virtualAssitant_frame, text="Asistente Virtual", font=("Segoe Print", 24))
title_lbl.pack(pady=20, padx= 100, side=TOP)

# Boton para reconocimiento de voz
img = Image.open("D:/Programacion/Proyectos Personales/Python/Asistente Virtual/Media/microphone.png")
size = 100
new_img = img.resize((size,size))
imagetest = ImageTk.PhotoImage(new_img)
record_btn = Button(virtualAssitant_frame, image=imagetest, command=virtualAssitant_func, height = size, width = size, borderwidth=5, bg='#32a6a8')
record_btn.pack(pady=20, padx= 100, side=TOP)

# TextBox para reconocimiento de voz
size = 12
record_txtBox = Text(virtualAssitant_frame, height= size, width= size*3)
record_txtBox.pack(pady=20, padx= 100, side=TOP)

#===========================================================
# =============== Frame Youtube Downloader =============== #
ytDownloader_frame =  Frame(window, width=750, height=700, bg="green")
# Label titulo
title_lbl2 = Label(ytDownloader_frame, text="Youtube Downloader", font=("Segoe Print", 24))
title_lbl2.pack(pady=20, padx= 10, side=TOP)

#================================================ #
link_frame = Frame(ytDownloader_frame, bg="red")
link_frame.pack(side=TOP)

#Label Link
link_lbl = Label(link_frame,text="Link:",font=("Segoe Print",15))
link_lbl.pack(pady=20, padx= 10, side=LEFT)

#TexBox link
link_entryVar = StringVar()
link_entry = Entry(link_frame,width=20,textvariable=link_entryVar, font=("Segoe Print",13))
link_entry.pack(pady=20, padx= 10, side=LEFT)

#upload path
upload_button = Button(link_frame,text="Cargar",font=("Segoe Print",15), command=upload, borderwidth=2, bg='#32a6a8')
upload_button.pack(padx= 10, side=LEFT)

#================================================ #
path_frame = Frame(ytDownloader_frame, bg="blue")
path_frame.pack(side=LEFT)

#Button path
path_button = Button(path_frame,text="Folder:",font=("Segoe Print",15), command=openLocation, borderwidth=4, bg='#32a6a8')
path_button.pack(pady=20, padx= 10, side=LEFT)

#label path
path_lbl = Label(path_frame,font=("Segoe Print",12))
path_lbl.pack(pady=20, padx= 10, side=LEFT)

#================================================ #
quality_frame = Frame(ytDownloader_frame, bg="red")
quality_frame.pack(side=LEFT)

#Label quality
quality_lbl = Label(quality_frame,text="Calidad:",font=("Segoe Print",15))
quality_lbl.pack(pady=20, padx= 10, side=LEFT)

#combobox calidad
ytdchoices_combBox = ttk.Combobox(quality_frame)
ytdchoices_combBox.pack(pady=20, padx= 10, side=LEFT)


#===================================================
# =============== Frame txt_Speech =============== #
txt_Speech_frame =  Frame(window, width=750, height=700)



#===============================================================
#=============== funciones para dibujar frames =============== #
def draw_virtualAssitant_frame(): # =============== Frame Asistente Virtual por voz =============== #
    ytDownloader_frame.pack_forget()
    txt_Speech_frame.pack_forget()
    virtualAssitant_frame.pack(side=LEFT)    

def draw_ytDownloader_frame(): # =============== Frame Youtube Downloader =============== #
    virtualAssitant_frame.pack_forget()
    txt_Speech_frame.pack_forget()
    ytDownloader_frame.pack(side=LEFT, padx=50)

def draw_txt_Speech_frame(): # =============== Frame txt_Speech =============== #
    virtualAssitant_frame.pack_forget()
    ytDownloader_frame.pack_forget()
    txt_Speech_frame.pack(side=LEFT)

#=============================================
# =============== Frame Menu =============== #
spacing = 10
#Frame
menu_frame =  Frame(window, width=250, height=700)
menu_frame.pack(side=LEFT)

#boton del frame asistente de voz
virtualAsstitant_btn = Button(menu_frame, text="Asistente Virtual por voz", command=draw_virtualAssitant_frame, borderwidth=4, bg='#32a6a8', font=fontWindow)
virtualAsstitant_btn.pack(side=TOP,pady=spacing, padx=spacing)

#boton del frame Youtube Downloader
ytDownloader_btn = Button(menu_frame, text="Youtube Downloader", command=draw_ytDownloader_frame, borderwidth=4, bg='#32a6a8', font=fontWindow)
ytDownloader_btn.pack(side=TOP,pady=spacing, padx=spacing)

#boton del frame Text <=> Speech
txt_Speech = Button(menu_frame, text="Text <=> Speech", command=draw_txt_Speech_frame, borderwidth=4, bg='#32a6a8', font=fontWindow)
txt_Speech.pack(side=TOP,pady=spacing, padx=spacing)



#=================================================
# =============== Loop principal =============== #
draw_virtualAssitant_frame()
window.mainloop()


