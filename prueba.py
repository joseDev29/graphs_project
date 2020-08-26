from Modelo.Grafo import *
from tkinter import *
from tkinter import ttk
import pygame, sys, random, json

from Modelo.Grafo import *
from tkinter import *
from tkinter import ttk
import pygame, sys, random, json

def archivo(self):
    raiz.filename= filedialo.askopenfilename(initialdir="/Data/", title="Cargar Grafo", filetypes=(("json files","*.json")))
raiz= Tk()

frame1= Frame(raiz)
frame1.pack(fill='both', expand="True")
frame1.config(width='70', height='500')
frame1.config(bg='limegreen')
boton=Button(frame1, text='Saludar',font=("Verdana",13), command=archivo).place(x=60,y=100)


raiz.mainloop()