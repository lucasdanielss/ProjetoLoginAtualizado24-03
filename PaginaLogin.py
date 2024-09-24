import tkinter as tk
from tkinter import *
from tkinter import messagebox
from banco import Banco  # Certifique-se de que o módulo banco.py está disponível e correto

class Login:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Login")

        self.janela39 = tk.Frame(master, padx=20)
        self.janela39.pack()

        # Corrigido para carregar a imagem corretamente
        try:
            self.img = PhotoImage(file="imagem/image.jpeg")  # Use o formato correto, como PNG
            self.lbimg = Label(self.janela39, image=self.img)
            self.lbimg.pack()
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")

        self.janela40 = tk.Frame(master, padx=20)
        self.janela40.pack()

        self.usuario_label = tk.Label(self.janela40, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = tk.Entry(self.janela40, width=20)
        self.usuario.pack(side="left")

        self.janela41 = tk.Frame(master, padx=20)
        self.janela41.pack()

        self.senha_label = tk.Label(self.janela41, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = tk.Entry(self.janela41, width=20, show="*")  # Oculta o texto da senha
        self.senha.pack(side="left")

        self.janela42 = tk.Frame(master, padx=20)
        self.janela42.pack()

        self.botao10 = tk.Button(self.janela42, width=10, text="Login", command=self.entrar)
        self.botao10.pack(side="left")

    def entrar(self):
        usuario = self.usuario.get()
        senha = self.senha.get()

        banco = Banco()  # Certifique-se de que a classe Banco está implementada corretamente
        cursor = banco.conexao.cursor()

        # Verificando se o usuário e a senha estão corretos
        cursor.execute("SELECT * FROM tbl_usuarios WHERE usuario=? AND senha=?", (usuario, senha))
        engual = cursor.fetchone()

        if engual:
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            self.abrir()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
        cursor.close()

    def abrir(self):
        self.new_window = tk.Toplevel(self.master)
        # A linha abaixo está comentada porque você deve definir a classe Mainform corretamente
        # self.app = Mainform(self.new_window)

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")  # Ajuste o tamanho da janela principal
    app = Login(master=root)
    root.mainloop()
