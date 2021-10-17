# importações
from tkinter import Tk, Toplevel
from tkinter import Button, Entry, Label
from tkinter import messagebox
from tkinter.constants import CENTER
from tkinter.ttk import Treeview 
from PIL import ImageTk, Image 


# classe principal
class Login:
    def __init__(self, master) -> None:
        self.janela = Toplevel(master)

        # chamando métodos
        self.configuar()
        self.inserirImagens()
        self.criarLabel()
        self.criarEntrys()
        self.criarBotoes()

        self.janela.transient(master)
        

     # método para configuração da tela principal
    def configuar(self) -> None:
        self.janela.title('Login')
        self.janela.geometry('400x350')
        self.janela.resizable(False, False)
        

    # método para mudar o tamanho das imagens
    def redimencionarImagem(self, width, caminho):
        global imagemUser

        img = Image.open(caminho)
        width = width

        wpercent = (width/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))

        img = img.resize((width, hsize), Image.ANTIALIAS)

        imagemUser = ImageTk.PhotoImage(img)

        return imagemUser

    # método para inserir imagens
    def inserirImagens(self):
        self.foto = self.redimencionarImagem(100, 'images/user.png')
        self.labelFoto = Label(self.janela, image=self.foto)
        self.labelFoto.place(relx=0.39, rely=0.05)

    # método para criar labels
    def criarLabel(self):
        self.labelUser = Label(self.janela, text='Usuário')
        self.labelUser.place(relx=0.1, rely=0.43)

        self.labelSenha = Label(self.janela, text='Senha')
        self.labelSenha.place(relx=0.1, rely=0.59)

    # método para criar entries
    def criarEntrys(self):
        self.entryUser = Entry(self.janela, justify=CENTER)
        self.entryUser.place(relx=0.3, rely=0.4, relheight=0.1)

        self.entrySenha = Entry(self.janela, justify=CENTER)
        self.entrySenha.place(relx=0.3, rely=0.57, relheight=0.1)

    # método para criar botões
    def criarBotoes(self):
        self.btnLogar = Button(self.janela, text='Fazer Login', bg='#FF8C00', fg='white')
        self.btnLogar.place(relx=0.3, rely=0.74, relwidth=0.4, relheight=0.12)
