import mysql.connector
import tkinter as tk
from tkinter import *

conexao_banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='farmacia'
)

cursor = conexao_banco.cursor()

def cadastrar_produto():
    nome_input = nome.get()
    categoria_input = categoria.get()
    tarja_input = tarja.get()
    fabmar_input = fabmar.get()
    valor_prod_input = valor_prod.get()
    quantidade_input = quantidade.get()
    comando_sql = f'SELECT * FROM estoque WHERE Nome_produto = "{nome_input}"'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    if dados_tabela <= 0:
        comando_sql = f'INSERT INTO estoque (Nome_produto, Categoria, Tarja_remedio, Farbricante/Marca, Valor_produto, Quantidade_estoque ) VALUES ("{nome_input}", "{categoria_input}", "{tarja_input}", "{fabmar_input}", "{valor_prod_input}", "{quantidade_input}")'
        cursor.execute(comando_sql)
        conexao_banco.commit()
    janelaCadastro = tk.Toplevel(root)
    janelaCadastro.title("Cadastrar: ")

    

    janelaCadastro.geometry("300x300")

janela = Tk()
janela.title('Farmacia') #nome da janela

texto_inicial = Label(janela, text='Selecione a opção desejada: ')
texto_inicial.grid(column=0, row=0)

botao = Button(janela, text='Cadastrar', command=cadastrar_produto())
botao.grid(column=0, row=1)

janela.mainloop() #loop da janela

