import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Conexão com o banco de dados
conexao_banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='farmacia'
)

cursor = conexao_banco.cursor()

# Função para abrir a janela de cadastro de funcionário
def abrir_cadastro_funcionario():
    janela_cadastro = tk.Toplevel(janela_menu)
    janela_cadastro.title("Cadastrar Funcionário")
    janela_cadastro.geometry("400x400")

    # Configuração do título
    tk.Label(janela_cadastro, text="Cadastrar Funcionário", font=("Arial", 14)).pack(pady=10)
    
    # Campo para o ID
    tk.Label(janela_cadastro, text="ID:").pack()
    ID_entry = tk.Entry(janela_cadastro, width=30)
    ID_entry.pack(pady=5)

    # Campo para Nome
    tk.Label(janela_cadastro, text="Nome:").pack()
    nome_entry = tk.Entry(janela_cadastro, width=30)
    nome_entry.pack(pady=5)

    # Campo para Cargo
    tk.Label(janela_cadastro, text="Cargo:").pack()
    cargo_entry = tk.Entry(janela_cadastro, width=30)
    cargo_entry.pack(pady=5)

    # Campo para Vendas Totais
    tk.Label(janela_cadastro, text="Vendas Totais:").pack()
    vendas_totais_entry = tk.Entry(janela_cadastro, width=30)
    vendas_totais_entry.pack(pady=5)

    # Campo para Salário
    tk.Label(janela_cadastro, text="Salário:").pack()
    salario_entry = tk.Entry(janela_cadastro, width=30)
    salario_entry.pack(pady=5)

    # Função para salvar o funcionário no banco de dados
    def salvar_funcionario():
        id_func = ID_entry.get()
        nome = nome_entry.get()
        cargo = cargo_entry.get()
        vendas_totais = vendas_totais_entry.get()
        salario = salario_entry.get()

        # Verifica se o ID já existe
        cursor.execute(f'SELECT * FROM funcionários WHERE ID_funcionário = "{id_func}"')
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showwarning("Aviso", "Este ID já está cadastrado!")
        else:
            # Inserindo os dados no banco de dados
            comando_sql = f'''INSERT INTO funcionários 
                             (ID_funcionário, Nome_funcionário, Cargo_funcionário, Vendas_totais_funcionários, Salário_funcionário) 
                             VALUES ("{id_func}","{nome}","{cargo}","{vendas_totais}","{salario}")'''
            cursor.execute(comando_sql)
            conexao_banco.commit()
            messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
            janela_cadastro.destroy()  # Fecha a janela de cadastro após salvar

    tk.Button(janela_cadastro, text="Salvar", command=salvar_funcionario).pack(pady=20)


    
# Função para a janela de Funcionários com botões adicionais
def janela_funcionarios():
    janela = tk.Toplevel(janela_menu)
    janela.title("Funcionários")
    janela.geometry("300x300")
    
    tk.Label(janela, text="Gestão de Funcionários", font=("Arial", 14)).pack(pady=10)

    # Botão para Cadastrar
    tk.Button(janela, text="Cadastrar", width=20, command=abrir_cadastro_funcionario).pack(pady=5)
    # Botões para Excluir, Alterar e Pesquisar podem ser adicionados com suas funções
    tk.Button(janela, text="Excluir", width=20, command=excluir_funcionario).pack(pady=5)
    tk.Button(janela, text="Alterar", width=20, command=alterar_funcionario).pack(pady=5)
    tk.Button(janela, text="Pesquisar", width=20, command=pesquisar_funcionario).pack(pady=5)

# Funções para as outras janelas (Vendas, Estoque, Financeiro)
def janela_vendas():
    janela = tk.Toplevel(janela_menu)
    janela.title("Vendas")
    janela.geometry("300x300")
    
    # Título da janela
    tk.Label(janela, text="Gestão de Vendas", font=("Arial", 14)).pack(pady=10)

    # Botão para Cadastrar
    tk.Button(janela, text="Cadastrar Venda", width=20, command=cadastrar_venda).pack(pady=5)
    # Botão para Excluir
    tk.Button(janela, text="Excluir Venda", width=20, command=excluir_venda).pack(pady=5)
    # Botão para Alterar
    tk.Button(janela, text="Alterar Venda", width=20, command=alterar_venda).pack(pady=5)
    # Botão para Pesquisar
    tk.Button(janela, text="Pesquisar Venda", width=20, command=pesquisar_venda).pack(pady=5)

# Funções para cada ação de vendas
def cadastrar_venda():
    # Implementação da função de cadastro de venda
    pass

def excluir_venda():
    # Implementação da função para excluir uma venda
    pass

def alterar_venda():
    # Implementação da função para alterar dados de uma venda
    pass

def pesquisar_venda():
    # Implementação da função para pesquisar uma venda
    pass
    

    

def janela_estoque():
    janela = tk.Toplevel(janela_menu)
    janela.title("Estoque")
    janela.geometry("300x300")
    tk.Label(janela, text="Página de Estoque").pack()

def janela_financeiro():
    janela = tk.Toplevel(janela_menu)
    janela.title("Financeiro")
    janela.geometry("300x300")
    tk.Label(janela, text="Página de Financeiro").pack()

# Funções para as outras operações de Funcionários (placeholders)
def excluir_funcionario():
    janela_excluir = tk.Toplevel(janela_menu)
    janela_excluir.title("Excluir Funcionário")
    janela_excluir.geometry("400x400")

    # Configuração do título
    tk.Label(janela_excluir, text="Excluir Funcionário", font=("Arial", 14)).pack(pady=10)
    
    # Campo para o ID
    tk.Label(janela_excluir, text="ID:").pack()
    ID_entry = tk.Entry(janela_excluir, width=30)
    ID_entry.pack(pady=5)

    # Função para salvar o funcionário no banco de dados
    def apagar_funcionario():
        id_func = ID_entry.get()

        # Verifica se o ID já existe
        cursor.execute(f'SELECT * FROM funcionários WHERE ID_funcionário = "{id_func}"')
        resultado = cursor.fetchone()

        if resultado:
            # Inserindo os dados no banco de dados
            comando_sql = f'''DELETE FROM funcionários WHERE ID_funcionário = {id_func}'''
            cursor.execute(comando_sql)
            conexao_banco.commit()
            messagebox.showinfo("Sucesso", "Funcionário excluido com sucesso!")
            janela_excluir.destroy()  # Fecha a janela de excluir após salvar
            
        else:
            messagebox.showwarning("Aviso", "Este ID não existe!")

    tk.Button(janela_excluir, text="Excluir", command=apagar_funcionario).pack(pady=20)

def alterar_funcionario():
    janela_alterar = tk.Toplevel(janela_menu)
    janela_alterar.title("Alterar Funcionário")
    janela_alterar.geometry("400x500")

    # Título da janela
    tk.Label(janela_alterar, text="Alterar Funcionário", font=("Arial", 14)).pack(pady=10)

    # Opção para buscar por ID ou Nome
    tk.Label(janela_alterar, text="Pesquisar por:").pack(pady=5)
    busca_var = tk.StringVar(value="ID")
    tk.Radiobutton(janela_alterar, text="ID", variable=busca_var, value="ID").pack()
    tk.Radiobutton(janela_alterar, text="Nome", variable=busca_var, value="Nome").pack()
    #Radiobutton = bolinhas de escolha

    # Entrada para ID ou Nome
    tk.Label(janela_alterar, text="Digite o ID ou Nome:").pack(pady=5)
    busca_entry = tk.Entry(janela_alterar, width=30)
    busca_entry.pack(pady=5)

    # Opção de campo a alterar (Vendas Totais ou Salário)
    tk.Label(janela_alterar, text="Escolha o campo a alterar:").pack(pady=10)
    campo_var = tk.StringVar(value="Vendas Totais")
    tk.Radiobutton(janela_alterar, text="Vendas Totais", variable=campo_var, value="Vendas Totais").pack()
    tk.Radiobutton(janela_alterar, text="Salário", variable=campo_var, value="Salário").pack()
    tk.Radiobutton(janela_alterar, text="Cargo", variable=campo_var, value="Cargo").pack()

    # Entrada para o novo valor
    tk.Label(janela_alterar, text="Novo valor/cargo:").pack(pady=5)
    novo_valcarg_entry = tk.Entry(janela_alterar, width=30)
    novo_valcarg_entry.pack(pady=5)

    # Função para buscar e alterar o funcionário
    def buscar_e_alterar():
        tipo_busca = busca_var.get()
        busca_valor = busca_entry.get()
        campo = campo_var.get()
        novo_valor = novo_valcarg_entry.get()

        # Condicional para busca por ID ou Nome
        if tipo_busca == "ID":
            cursor.execute(f'SELECT * FROM funcionários WHERE ID_funcionário = "{busca_valor}"')
        else:
            cursor.execute(f'SELECT * FROM funcionários WHERE Nome_funcionário = "{busca_valor}"')

        funcionario = cursor.fetchone()

        # Verificação se o funcionário existe
        if funcionario:
            if campo == "Vendas Totais":
                campo_sql = "Vendas_totais_funcionários"
            elif campo == "Salário":
                campo_sql = "Salário_funcionário"
            else:
                campo_sql = "Cargo_funcionário"

            # Atualiza o campo escolhido
            comando_sql = f'UPDATE funcionários SET {campo_sql} = "{novo_valor}" WHERE ID_funcionário = "{funcionario[0]}"'
            cursor.execute(comando_sql)
            conexao_banco.commit()
            messagebox.showinfo("Sucesso", f"{campo} atualizado com sucesso!")
            janela_alterar.destroy()
        else:
            messagebox.showwarning("Aviso", "Funcionário não encontrado!")

    # Botão para realizar a alteração
    tk.Button(janela_alterar, text="Alterar", command=buscar_e_alterar).pack(pady=20)

def pesquisar_funcionario():
    janela_pesquisa = tk.Toplevel(janela_menu)
    janela_pesquisa.title("Pesquisar Funcionário")
    janela_pesquisa.geometry("600x700")

    tk.Label(janela_pesquisa, text="Pesquisar Funcionário", font=("Arial", 14)).pack(pady=10)

    # Opção de pesquisa
    tk.Label(janela_pesquisa, text="Pesquisar por:").pack(pady=5)
    criterio_var = tk.StringVar(value="ID")
    tk.Radiobutton(janela_pesquisa, text="ID", variable=criterio_var, value="ID").pack()
    tk.Radiobutton(janela_pesquisa, text="Nome", variable=criterio_var, value="Nome").pack()
    tk.Radiobutton(janela_pesquisa, text="Cargo", variable=criterio_var, value="Cargo").pack()
    tk.Radiobutton(janela_pesquisa, text="Faixa de Salário", variable=criterio_var, value="Faixa de Salário").pack()
    tk.Radiobutton(janela_pesquisa, text="Quantidade de Vendas", variable=criterio_var, value="Quantidade de Vendas").pack()

    # Entrada para o valor de pesquisa
    tk.Label(janela_pesquisa, text="Digite o valor de pesquisa:").pack(pady=5)
    valor_entry = tk.Entry(janela_pesquisa, width=30)
    valor_entry.pack(pady=5)

    # Listbox para mostrar os resultados
    lista_resultados = tk.Listbox(janela_pesquisa, width=90, height=15)
    lista_resultados.pack(pady=10)

    # Função para buscar e exibir resultados
    def buscar():
        criterio = criterio_var.get()
        valor = valor_entry.get()
        lista_resultados.delete(0, tk.END)  # Limpa resultados anteriores

        if criterio == "ID":
            comando_sql = f'SELECT * FROM funcionários WHERE ID_funcionário = "{valor}"'
        elif criterio == "Nome":
            comando_sql = f'SELECT * FROM funcionários WHERE Nome_funcionário LIKE "%{valor}%"'
        elif criterio == "Cargo":
            comando_sql = f'SELECT * FROM funcionários WHERE Cargo_funcionário LIKE "%{valor}%"'
        elif criterio == "Faixa de Salário":
            try:
                salario_min, salario_max = map(float, valor.split("-"))
                comando_sql = f'SELECT * FROM funcionários WHERE Salário_funcionário BETWEEN {salario_min} AND {salario_max}'
            except ValueError:
                messagebox.showwarning("Formato Incorreto", "Por favor, insira uma faixa de salário no formato: min-max")
                return
        elif criterio == "Quantidade de Vendas":
            try:
                vendas_min, vendas_max = map(int, valor.split("-"))
                comando_sql = f'SELECT * FROM funcionários WHERE Vendas_totais_funcionários BETWEEN {vendas_min} AND {vendas_max}'
            except ValueError:
                messagebox.showwarning("Formato Incorreto", "Por favor, insira uma faixa de vendas no formato: min-max")
                return

        # Executa a pesquisa no banco de dados
        cursor.execute(comando_sql)
        resultados = cursor.fetchall()

        # Exibe os resultados na lista
        if resultados:
            for funcionario in resultados:
                lista_resultados.insert(tk.END, f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Cargo: {funcionario[2]}, Vendas: {funcionario[3]}, Salário: {funcionario[4]}")
        else:
            lista_resultados.insert(tk.END, "Nenhum resultado encontrado.")

    # Botão para realizar a busca
    tk.Button(janela_pesquisa, text="Buscar", command=buscar).pack(pady=10)

# Configuração da janela principal
janela_menu = tk.Tk()
janela_menu.title('Farmacia')
janela_menu.state('zoomed')  # Ativa o modo tela cheia

# Frame centralizado para os botões
frame_central = tk.Frame(janela_menu)
frame_central.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Texto inicial
texto_inicial = tk.Label(frame_central, text='Selecione a opção desejada:', font=("Arial", 24))
texto_inicial.pack(pady=20)

# Botões centralizados e maiores
tk.Button(frame_central, text='Funcionários', font=("Arial", 18), width=20, height=2, command=janela_funcionarios).pack(pady=10)
tk.Button(frame_central, text='Vendas', font=("Arial", 18), width=20, height=2, command=janela_vendas).pack(pady=10)
tk.Button(frame_central, text='Estoque', font=("Arial", 18), width=20, height=2, command=janela_estoque).pack(pady=10)
tk.Button(frame_central, text='Financeiro', font=("Arial", 18), width=20, height=2, command=janela_financeiro).pack(pady=10)

# Loop da janela principal
janela_menu.mainloop()
