from tkinter import Label, Tk, Button, Entry, Frame, PhotoImage, Canvas
from PIL import Image
from PIL import ImageTk
import cv2
import numpy as np
import imutils
    
#-- FUNCION QUE PRENDE LA CAMARA DE OPENCV--#
def encender():
    global cap
    cap = cv2.VideoCapture(0)
    visualizar()

#FUNCION QUE APAGA LA CAMARA DE OPENCV--#
def apagar():
    global cap
    cap.release()
	
#-- FUNCION QUE CONTIENE TODA LA FUNCIONALIDAD DE OPENCV--#
def visualizar():
    global cap
    if cap is not None:
        ret,frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width=680)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #escala de grises
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            label_captura.configure(image=img)
            label_captura.config(width="680",height="600")
            label_captura.image = img
            label_captura.after(10, visualizar)
            boton.config(text="APAGAR", command=apagar)
        else:
            boton.config(text="ENCENDER", command=encender)
            label_captura.image = ""
            label_letra.config(text="APAGADO...",side="left", fill=None,expand=True)
           # label_captura.configure(text="APAGADO...")
            cap.release()
       
#----- CREACION DE LA VENTANA PRINCIPAL------#

#----CONFIGURACION DE ANCHO Y ALTO DE LA VENTANA PRINCIPAL---#
cap = None
ventana = Tk()
ventana.title("VISION POR COMPUTADORA (CURN)")
ventana.geometry("1080x600")
ventana.maxsize(1080, 600)
ventana.minsize(1080,600)
#---CONTENEDOR DE NAVBAR ---#
frame1 = Frame(ventana, bg="#F3800C",height=100, )
frame1.pack(fill='x')
label = Label(frame1, text="VISION POR COMPUTADORA (CURN)",height=2)
label.pack(side="left")
label.config(bg="#F3800C", font=("Segoe UI", 16), fg="#FFFFFF",justify="left",padx=10)

#---CONTENEDOR DE CARACTERISTICAS ---#
frame2 = Frame(ventana)
frame2.pack(side="left")
#frame2.place(x=0, y=67)
frame2.config(width="400",height="600")
frame2.config(bg="#707070")
frame2.pack_propagate(False)

#-- CONTENEDOR DE CARACTARISTICAS--#
frame3 = Frame(frame2)
frame3.pack(side="top", anchor="nw")
frame3.config(bg="#636060")
frame3.config(width="400",height="50")
frame3.pack_propagate(False)

#---LABEL DE CARACTERISTICAS--#
label2 = Label(frame3, text="CARACTERISTICAS", bg="#636060",height=2  ) 
label2.pack(side="left")
label2.config(font=("Segoe UI", 15),padx=14,fg="#FFFFFF")

#--LABEL DE FIGURA GEOMETRICA---#
frame_figu_geo = Frame(frame2,bg="#707070" )
frame_figu_geo.pack(pady=10)
frame_figu_geo.config(width="400",height="50")
frame_figu_geo.pack_propagate(False)
#--LABEL--#
label_geome = Label(frame_figu_geo, text="FIGURA GEOMETRICA", height=2)
label_geome.pack(side="left")
label_geome.config(font=("Segoe UI", 15),padx=14,fg="#FFFFFF",bg="#707070")
#--ENTRADA DE FIGURA---#
frame_entrada = Frame(frame2, bg="#8B8686")
frame_entrada.pack(pady=2)
frame_entrada.config(width="380",height="50")
frame_entrada.pack_propagate(False)
#--LABEL ENTRADA FIGURA--#
label_entrada = Label(frame_entrada,text="NOMBRE DE FIGURA GEOMETRICA", height=2)
label_entrada.pack(side="left")
label_entrada.config(font=("Segoe UI", 15),padx=14,fg="#FFFFFF",bg="#8B8686")

#-- FRAME COLOR DE LA FIGURA
frame_color = Frame(frame2, bg="#707070")
frame_color.pack(pady=10)
frame_color.config(width="400",height="50")
frame_color.pack_propagate(False)
#--TITULO--#
label_color = Label(frame_color, text="COLOR DE LA FIGURA", height=2)
label_color.pack(side="left")
label_color.config(font=("Segoe UI", 15),padx=14,fg="#FFFFFF",bg="#707070")
#--ENTRADA COLOR---#
frame_entrada_color = Frame(frame2,bg="#8B8686" )
frame_entrada_color.pack(pady=2)
frame_entrada_color.config(width="380",height="50")
frame_entrada_color.pack_propagate(False)
#--LABEL ENTRADA DE COLOR--#
label_entrada_color = Label(frame_entrada_color, text="COLOR DE FIGURA GEOMETRICA", height=2)
label_entrada_color.pack(side="left")
label_entrada_color.config(font=("Segoe UI", 15),padx=14,fg="#FFFFFF",bg="#8B8686")

#-- FRAME COORDENADAS DE FIGURA
frame_coordenadas = Frame(frame2, bg="#707070")
frame_coordenadas.pack(pady=10)
frame_coordenadas.config(width="400",height="50")
frame_coordenadas.pack_propagate(False)
#--TITULO--#
label_coordenadas = Label(frame_coordenadas, text="COORDENADAS", height=2)
label_coordenadas.pack(side="left")
label_coordenadas.config(font=("Segoe UI", 15),padx=14,fg="#FFFFFF",bg="#707070")
#--CONTENEDOR COORDENADAS --#
frame_contenedor_coor = Frame(frame2,bg="#707070" )
frame_contenedor_coor.pack()
frame_contenedor_coor.config(width="400",height="50")
frame_contenedor_coor.pack_propagate(False)
#--LABEL TITULO X--#
label_titulo_x = Label(frame_contenedor_coor, text="X: ", height=2)
label_titulo_x.pack(side="left")
label_titulo_x.config(font=("Segoe UI", 15),padx=20,fg="#FFFFFF",bg="#707070")
#--LABEL ENTRADA X --#
label_entrada_x = Label(frame_contenedor_coor, text="0 ", height=2)
label_entrada_x.pack(side="left")
label_entrada_x.config(font=("Segoe UI", 15),padx=20,fg="#FFFFFF",bg="#8B8686")
#--LABEL TITULO Y --#
label_titulo_y = Label(frame_contenedor_coor, text="Y: ", height=2)
label_titulo_y.pack(side="left")
label_titulo_y.config(font=("Segoe UI", 15),padx=20,fg="#FFFFFF",bg="#707070")
#--LABEL ENTRADA Y--#
label_entrada_y = Label(frame_contenedor_coor, text="0 ", height=2)
label_entrada_y.pack(side="left")
label_entrada_y.config(font=("Segoe UI", 15),padx=20,fg="#FFFFFF",bg="#8B8686")

#-- CAPTURA DE PANTALLA --#
frame_captura_pantalla = Frame(ventana,bg="#FFFFFF")
frame_captura_pantalla.pack()
frame_captura_pantalla.config(width="680",height="470")
frame_captura_pantalla.pack_propagate(False)

label_captura = Label(frame_captura_pantalla)
label_captura.pack()
label_captura.config(bg="#1C1A1A",width="680",height="470",fg="#FFFFFF")
label_captura.pack_propagate(False)

label_letra = Label(label_captura, text="APAGADO...",fg="#FFFFFF",bg="#1C1A1A")
label_letra.pack(side="left", fill=None,expand=True)
label_letra.config(font=("Segoe UI", 15))

#---FRAME PARA BOTONES--#
frame_botones = Frame(ventana, bg="#636060")
frame_botones.pack(side="bottom", fill="both")
frame_botones.config(width="400",height="80")
frame_botones.pack_propagate(False)
boton = Button(frame_botones, text="ENCENDER", command=encender)
boton.pack(side="right", fill="x", expand=False)
boton.config(height="70",font=("Segoe UI", 10),padx=20,fg="#FFFFFF",bg="#F3800C")   

encender()
ventana.mainloop()