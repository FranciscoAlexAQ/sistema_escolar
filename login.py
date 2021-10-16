from tkinter import Tk, Toplevel
from tkinter import Button, Entry, Label
from tkinter import messagebox
from tkinter.constants import ANCHOR, CENTER
from tkinter.ttk import Treeview 
from PIL import ImageTk, Image 


class Login:
    def __init__(self, master) -> None:
        if __name__ != 'main':
            self.janela = Toplevel(master)

            self.configuar()
            self.inserirImagens()
            self.criarLabel()
            self.criarEntrys()
            self.criarBotoes()

            self.janela.transient(master)
        else:
            self.janela = Tk()

            self.configuar()
            self.inserirImagens()
            self.criarLabel()
            self.criarEntrys()
            self.criarBotoes()

            self.janela.mainloop()


     # método para configuração da tela principal
    def configuar(self) -> None:
        self.janela.title('Login')
        self.janela.geometry('400x350')
        self.janela.resizable(False, False)

    def redimencionarImagem(self, width, caminho):
        img = Image.open(caminho)
        width = width

        wpercent = (width/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))

        img = img.resize((width, hsize), Image.ANTIALIAS)

        self.imagemUser = ImageTk.PhotoImage(img)

        return self.imagemUser

    def inserirImagens(self):
        self.foto = self.redimencionarImagem(100, 'images/user.png')
        self.labelFoto = Label(self.janela, image=self.foto)
        self.labelFoto.place(relx=0.39, rely=0.05)

    def criarLabel(self):
        self.labelUser = Label(self.janela, text='Usuário')
        self.labelUser.place(relx=0.1, rely=0.43)

        self.labelSenha = Label(self.janela, text='Senha')
        self.labelSenha.place(relx=0.1, rely=0.59)

    def criarEntrys(self):
        self.entryUser = Entry(self.janela, justify=CENTER)
        self.entryUser.place(relx=0.3, rely=0.4, relheight=0.1)

        self.entrySenha = Entry(self.janela, justify=CENTER)
        self.entrySenha.place(relx=0.3, rely=0.57, relheight=0.1)


    def criarBotoes(self):
        self.btnLogar = Button(self.janela, text='Fazer Login')
        self.btnLogar.place(relx=0.3, rely=0.74, relwidth=0.4, relheight=0.12)

