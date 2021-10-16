# importações
from tkinter import Tk
from tkinter import Button, Entry, Label
from tkinter import messagebox
from tkinter.ttk import Treeview 
from PIL import ImageTk, Image 

# instanciando tkinter
root = Tk()

class Main:
    def __init__(self) -> None:
        # referenciando
        self.root = root

        # chamando métodos da classe
        self.configuarJanela()
        self.inserirImagens()

        # gerando o loop infinito da tela
        self.root.mainloop()

    # método para configuração da tela principal
    def configuarJanela(self) -> None:
        self.root.title('Sistema Escolar')
        self.root.geometry('890x500')
        self.root.resizable(False, False)
        

    # método para pegar as imagens 
    def inserirImagens(self):
        self.fotoFundo = ImageTk.PhotoImage(Image.open('images/fundo.jpg'))
        self.labelFundo = Label(self.root, image=self.fotoFundo)
        self.labelFundo.place(relx=0, rely=0, relwidth=1, relheight=1)
    

# chamando classe
Main()
