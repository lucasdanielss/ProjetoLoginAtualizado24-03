import sqlite3
from banco import Banco

class Usuarios:
    def __init__(self):
        self.banco = Banco()
        self.conexao = self.banco.get_connection()

    def selectUser(self, idusuario):
        c = self.conexao.cursor()
        c.execute("SELECT * FROM tbl_usuarios WHERE idusuario = ?", (idusuario,))
        user = c.fetchone()
        c.close()
        if user:
            self.idusuario, self.nome, self.telefone, self.email, self.usuario, self.senha, self.cidade = user
            return f"Usuário {idusuario} encontrado!"
        else:
            return "Usuário não encontrado!"

    def insertUser(self):
        c = self.conexao.cursor()
        c.execute("""INSERT INTO tbl_usuarios (nome, telefone, email, usuario, senha, cidade)
                     VALUES (?, ?, ?, ?, ?, ?)""",
                   (self.nome, self.telefone, self.email, self.usuario, self.senha, self.cidade))
        self.conexao.commit()
        c.close()
        return "Usuário inserido com sucesso!"

    def updateUser(self):
        c = self.conexao.cursor()
        c.execute("""UPDATE tbl_usuarios 
                     SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ?, cidade = ?
                     WHERE idusuario = ?""",
                   (self.nome, self.telefone, self.email, self.usuario, self.senha, self.cidade, self.idusuario))
        self.conexao.commit()
        c.close()
        return "Usuário atualizado com sucesso!"

    def deleteUser(self):
        c = self.conexao.cursor()
        c.execute("DELETE FROM tbl_usuarios WHERE idusuario = ?", (self.idusuario,))
        self.conexao.commit()
        c.close()
        return "Usuário excluído com sucesso!"
