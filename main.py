# importações
from tkinter import Tk
from tkinter import Button, Entry, Label
from tkinter import messagebox
from tkinter.ttk import Treeview 
from PIL import ImageTk, Image 
import login 


# instanciando tkinter
root = Tk()


class Main:
    def __init__(self) -> None:
        # referenciando
        self.root = root

        # chamando métodos da classe
        self.configuarJanela()
        self.inserirImagens()
        self.criarBotoes()

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
        self.labelFundo.place(relx=0, rely=-0, relwidth=1, relheight=1)
    
    # criar botões 
    def criarBotoes(self):
        self.btnEstudantes = Button(self.root, text='Estudantes', bg='#FF8C00', fg='white', bd=0, 
            activebackground='#FF4500', activeforeground='white', command=lambda: login.Login(self.root))
        self.btnEstudantes.place(relx=0.01, rely=0.05, relwidth=0.14, relheight=0.1)

        self.btnProfessores = Button(self.root, text='Professores', bg='#DC143C', fg='white', bd=0, 
            activebackground='#B22222', activeforeground='white')
        self.btnProfessores.place(relx=0.01, rely=0.2, relwidth=0.14, relheight=0.1)

        self.btnDirecao = Button(self.root, text='Direção', bg='#483D8B', fg='white', bd=0, 
            activebackground='#4B0082', activeforeground='white',)
        self.btnDirecao.place(relx=0.01, rely=0.35, relwidth=0.14, relheight=0.1)
        
        
# chamando classe
Main()
