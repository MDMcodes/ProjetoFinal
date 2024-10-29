import mysql.connector

conexao_banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='farmacia'
)

cursor = conexao_banco.cursor()

def cadastrar_produto():
    nome_input = input('Insira o nome do produto: ')
    categoria_input = input('Insira a categoria do produto: ')
    tarja_input = input('Insira a tarja do produto: ')
    fabmar_input = input('Insira o fabricante/marca do produto: ')
    valor_prod_input = float(input('Insira o valor do produto: '))