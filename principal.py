import tkinter as tk
from tkinter import *
import sqlite3

# Classe de conexão com o banco de dados
class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.create_table()

    def create_table(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS tbl_usuarios (
            idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            usuario TEXT,
            senha TEXT,
            cidade TEXT
        )""")
        self.conexao.commit()
        c.close()

    def get_connection(self):
        return self.conexao

class Usuarios:
    def __init__(self):
        self.banco = Banco()

    def selectUser(self, idusuario):
        conexao = self.banco.get_connection()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tbl_usuarios WHERE idusuario = ?", (idusuario,))
        usuario = cursor.fetchone()
        conexao.close()
        if usuario:
            self.idusuario, self.nome, self.telefone, self.email, self.usuario, self.senha, self.cidade = usuario
            return f"Usuário {idusuario} encontrado!"
        else:
            return "Usuário não encontrado."

    def insertUser(self):
        conexao = self.banco.get_connection()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO tbl_usuarios (nome, telefone, email, usuario, senha, cidade) VALUES (?, ?, ?, ?, ?, ?)",
                       (self.nome, self.telefone, self.email, self.usuario, self.senha, self.cidade))
        conexao.commit()
        conexao.close()
        return "Usuário inserido com sucesso!"

    def updateUser(self):
        conexao = self.banco.get_connection()
        cursor = conexao.cursor()
        cursor.execute("UPDATE tbl_usuarios SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ?, cidade = ? WHERE idusuario = ?",
                       (self.nome, self.telefone, self.email, self.usuario, self.senha, self.cidade, self.idusuario))
        conexao.commit()
        conexao.close()
        return "Usuário atualizado com sucesso!"

    def deleteUser(self):
        conexao = self.banco.get_connection()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM tbl_usuarios WHERE idusuario = ?", (self.idusuario,))
        conexao.commit()
        conexao.close()
        return "Usuário excluído com sucesso!"

    def getAllUsers(self):
        conexao = self.banco.get_connection()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tbl_usuarios")
        usuarios = cursor.fetchall()
        conexao.close()
        return usuarios

class SistemaGestao:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontePadrao = ("Arial", "12")
        self.janela.pack(fill=BOTH, expand=True)

        self.titulo = Label(self.janela, text="Informe os dados")
        self.titulo["font"] = ("Arial", 20, "bold")
        self.titulo.pack(pady=20)

        self.janela_campos = Frame(self.janela)
        self.janela_campos.pack(pady=10)

        self.idUsuarioLabel = Label(self.janela_campos, text="ID Usuário:", font=self.fontePadrao)
        self.idUsuarioLabel.grid(row=0, column=0, padx=5, pady=5, sticky=E)
        self.idUsuario = Entry(self.janela_campos)
        self.idUsuario.grid(row=0, column=1, padx=5, pady=5)

        self.btn_buscar = Button(self.janela_campos, text="Buscar", font=self.fontePadrao, command=self.buscarUsuario)
        self.btn_buscar.grid(row=0, column=2, padx=5, pady=5)

        self.nomeLabel = Label(self.janela_campos, text="Nome:", font=self.fontePadrao)
        self.nomeLabel.grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self.nome = Entry(self.janela_campos)
        self.nome.grid(row=1, column=1, padx=5, pady=5)

        self.telefoneLabel = Label(self.janela_campos, text="Telefone:", font=self.fontePadrao)
        self.telefoneLabel.grid(row=2, column=0, padx=5, pady=5, sticky=E)
        self.telefone = Entry(self.janela_campos)
        self.telefone.grid(row=2, column=1, padx=5, pady=5)

        self.emailLabel = Label(self.janela_campos, text="Email:", font=self.fontePadrao)
        self.emailLabel.grid(row=3, column=0, padx=5, pady=5, sticky=E)
        self.email = Entry(self.janela_campos)
        self.email.grid(row=3, column=1, padx=5, pady=5)

        self.usuarioLabel = Label(self.janela_campos, text="Usuário:", font=self.fontePadrao)
        self.usuarioLabel.grid(row=4, column=0, padx=5, pady=5, sticky=E)
        self.usuario = Entry(self.janela_campos)
        self.usuario.grid(row=4, column=1, padx=5, pady=5)

        self.senhaLabel = Label(self.janela_campos, text="Senha:", font=self.fontePadrao)
        self.senhaLabel.grid(row=5, column=0, padx=5, pady=5, sticky=E)
        self.senha = Entry(self.janela_campos, show="*")
        self.senha.grid(row=5, column=1, padx=5, pady=5)

        self.cidadeLabel = Label(self.janela_campos, text="Cidade:", font=self.fontePadrao)
        self.cidadeLabel.grid(row=6, column=0, padx=5, pady=5, sticky=E)
        self.cidade = Entry(self.janela_campos)
        self.cidade.grid(row=6, column=1, padx=5, pady=5)

        self.janela_botoes = Frame(self.janela)
        self.janela_botoes.pack(pady=20)

        self.btn_inserir = Button(self.janela_botoes, text="Inserir", font=self.fontePadrao, width=10, command=self.inserirUsuario)
        self.btn_inserir.grid(row=0, column=0, padx=5)

        self.btn_alterar = Button(self.janela_botoes, text="Alterar", font=self.fontePadrao, width=10, command=self.alterarUsuario)
        self.btn_alterar.grid(row=0, column=1, padx=5)

        self.btn_excluir = Button(self.janela_botoes, text="Excluir", font=self.fontePadrao, width=10, command=self.excluirUsuario)
        self.btn_excluir.grid(row=0, column=2, padx=5)

        self.btn_sair = Button(self.janela_botoes, text="Sair", font=self.fontePadrao, width=10, command=self.sairAplicativo)
        self.btn_sair.grid(row=0, column=3, padx=5)

        self.lblmsg = Label(self.janela, text="", font=self.fontePadrao)
        self.lblmsg.pack()

        self.frame_lista = Frame(self.janela)
        self.frame_lista.pack(pady=20, fill=BOTH, expand=True)

        self.lista_usuarios = Listbox(self.frame_lista, width=80, height=20, selectmode=SINGLE)
        self.lista_usuarios.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar_vertical = Scrollbar(self.frame_lista, orient=VERTICAL, command=self.lista_usuarios.yview)
        self.scrollbar_vertical.pack(side=RIGHT, fill=Y)

        self.lista_usuarios.config(yscrollcommand=self.scrollbar_vertical.set)

        self.scrollbar_horizontal = Scrollbar(self.frame_lista, orient=HORIZONTAL, command=self.lista_usuarios.xview)
        self.scrollbar_horizontal.pack(side=BOTTOM, fill=X)

        self.lista_usuarios.config(xscrollcommand=self.scrollbar_horizontal.set)

        self.atualizarListaUsuarios()

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idUsuario.get()
        self.lblmsg["text"] = user.selectUser(idusuario)
        if self.lblmsg["text"].startswith("Usuário encontrado!"):
            self.idUsuario.delete(0, END)
            self.idUsuario.insert(INSERT, user.idusuario)
            self.nome.delete(0, END)
            self.nome.insert(INSERT, user.nome)
            self.telefone.delete(0, END)
            self.telefone.insert(INSERT, user.telefone)
            self.email.delete(0, END)
            self.email.insert(INSERT, user.email)
            self.usuario.delete(0, END)
            self.usuario.insert(INSERT, user.usuario)
            self.senha.delete(0, END)
            self.senha.insert(INSERT, user.senha)
            self.cidade.delete(0, END)
            self.cidade.insert(INSERT, user.cidade)
        else:
            self.limparCampos()

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        user.cidade = self.cidade.get()
        self.lblmsg["text"] = user.insertUser()
        self.limparCampos()
        self.atualizarListaUsuarios()

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.idUsuario.get()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        user.cidade = self.cidade.get()
        self.lblmsg["text"] = user.updateUser()
        self.limparCampos()
        self.atualizarListaUsuarios()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.idUsuario.get()
        self.lblmsg["text"] = user.deleteUser()
        self.limparCampos()
        self.atualizarListaUsuarios()

    def limparCampos(self):
        self.idUsuario.delete(0, END)
        self.nome.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)
        self.senha.delete(0, END)
        self.cidade.delete(0, END)

    def atualizarListaUsuarios(self):
        self.lista_usuarios.delete(0, END)
        user = Usuarios()
        usuarios = user.getAllUsers()
        for u in usuarios:
            self.lista_usuarios.insert(END, f"ID: {u[0]} | Nome: {u[1]} | Telefone: {u[2]} | Email: {u[3]} | Usuário: {u[4]} | Cidade: {u[6]}")

    def sairAplicativo(self):
        self.janela.master.destroy()  # Fecha a aplicação

def abrir_pagina_principal():
    root = Tk()
    root.title("Sistema de Gestão")
    root.geometry("800x600")
    SistemaGestao(root)
    root.mainloop()

# Não executar automaticamente ao ser importado
if __name__ == "__main__":
    abrir_pagina_principal()
