import mysql.connector
import tkinter as tk
from tkinter import *

# Conexão com o banco de dados
conexao_banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='farmacia'
)

cursor = conexao_banco.cursor()

# Função para cadastrar um produto (exemplo)
def cadastrar_produto():
    # Implementação do cadastro de produto, ou abrir nova janela para entrada de dados
    pass

# Função para a janela de Funcionários com botões adicionais
def janela_funcionarios():
    janela = tk.Toplevel(janela_menu)
    janela.title("Funcionários")
    janela.geometry("300x300")
    
    # Título da janela
    Label(janela, text="Gestão de Funcionários", font=("Arial", 14)).pack(pady=10)

    # Botão para Cadastrar
    Button(janela, text="Cadastrar", width=20, command=cadastrar_funcionario).pack(pady=5)
    # Botão para Excluir
    Button(janela, text="Excluir", width=20, command=excluir_funcionario).pack(pady=5)
    # Botão para Alterar
    Button(janela, text="Alterar", width=20, command=alterar_funcionario).pack(pady=5)
    # Botão para Pesquisar
    Button(janela, text="Pesquisar", width=20, command=pesquisar_funcionario).pack(pady=5)

# Funções para cada ação
def cadastrar_funcionario():
    # Implementação da função de cadastro de funcionário
    pass

def excluir_funcionario():
    # Implementação da função para excluir um funcionário
    pass

def alterar_funcionario():
    # Implementação da função para alterar dados de um funcionário
    pass

def pesquisar_funcionario():
    # Implementação da função para pesquisar um funcionário
    pass

# Funções para as outras janelas (Vendas, Estoque, Financeiro)
def janela_vendas():
    janela = tk.Toplevel(janela_menu)
    janela.title("Vendas")
    janela.geometry("300x300")
    Label(janela, text="Página de Vendas").pack()

def janela_estoque():
    janela = tk.Toplevel(janela_menu)
    janela.title("Estoque")
    janela.geometry("300x300")
    Label(janela, text="Página de Estoque").pack()

def janela_financeiro():
    janela = tk.Toplevel(janela_menu)
    janela.title("Financeiro")
    janela.geometry("300x300")
    Label(janela, text="Página de Financeiro").pack()

# Janela principal do menu
janela_menu = Tk()
janela_menu.title('Farmacia')
janela_menu.geometry("1970x1080")

# Texto inicial
texto_inicial = Label(janela_menu, text='Selecione a opção desejada: ') 
texto_inicial.grid(column=0, row=0)

# Botões do menu
Button(janela_menu, text='Funcionários', command=janela_funcionarios).grid(column=0, row=1)
Button(janela_menu, text='Vendas', command=janela_vendas).grid(column=0, row=2)
Button(janela_menu, text='Estoque', command=janela_estoque).grid(column=0, row=3)
Button(janela_menu, text='Financeiro', command=janela_financeiro).grid(column=0, row=4)

# Loop da janela principal
janela_menu.mainloop()
