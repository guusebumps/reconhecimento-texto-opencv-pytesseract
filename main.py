import pytesseract
import numpy as np
import cv2
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from tkinter.filedialog import askopenfile
from tkinter import filedialog

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gusta\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
janela = tk.Tk()
janela.geometry("800x600")
janela.title('Ler Texto de Imagem')
fonte1 = ('times', 18, 'bold')

def abrir():
    global imagem
    janela.filename = filedialog.askopenfilename(initialdir='/text-recognize-main/imagens', title="Ler Texto de Imagem", filetypes=(("png files", "*.png"),("jpg files", "*.jpg"),("all files", "*.*")))
    imagem = ImageTk.PhotoImage(Image.open(janela.filename))
    label_imagem = Label(image=imagem)
    label_imagem.grid(row=1, column=1)

def read_from_img():

    img = cv2.imread(janela.filename)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    texto = pytesseract.image_to_string(rgb, lang='por')
    print(texto)    
    label2 = tk.Label(janela, text=texto, width=30, font=fonte1)
    label2.grid(row=2, column=1)    

label1 = tk.Label(janela, text='Enviar e ler imagem', width=30, font=fonte1)
label1.grid(row=1, column=1)
botao1 = Button(janela, text="Abrir Arquivo de Imagem", command=abrir)
botao1.grid(row=3, column=1)
botao2 = Button(janela, text="Ler Texto da Imagem", command=read_from_img)
botao2.grid(row=4, column=1)

janela.mainloop()