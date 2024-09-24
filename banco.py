import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.create_table()

    def create_table(self):
        c = self.conexao.cursor()
        # Verifica se a tabela já existe antes de criar
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

def adicionar_coluna_cidade():
    conexao = sqlite3.connect('banco.db')
    c = conexao.cursor()

    # Verifica se a coluna já existe para evitar erros
    c.execute("PRAGMA table_info(tbl_usuarios)")
    colunas = [col[1] for col in c.fetchall()]
    if 'cidade' not in colunas:
        c.execute("ALTER TABLE tbl_usuarios ADD COLUMN cidade TEXT")

    conexao.commit()
    conexao.close()

# Executa a função para garantir que a coluna cidade exista
adicionar_coluna_cidade()
