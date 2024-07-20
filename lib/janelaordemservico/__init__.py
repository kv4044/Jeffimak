import tkinter as tk
from datetime import datetime
import os

data = datetime.now()
data_atual = data.strftime("%d/%m/%Y")

# Nome do arquivo que armazena o contador
arquivo_contador = 'contador_os.txt'


def carregar_contador():
    """Função para carregar o valor do contador do arquivo"""
    if os.path.exists(arquivo_contador):
        with open(arquivo_contador, 'r') as f:
            return int(f.read().strip())
    else:
        return 1


def salvar_contador(valor):
    """Função para salvar o valor do contador no arquivo"""
    with open(arquivo_contador, 'w') as f:
        f.write(str(valor))


def janela_ordem(janela_principal):
    janela_principal.withdraw()

    # Inicializa o contador a partir do arquivo
    contador = carregar_contador()

    def criar_arquivo():
        nonlocal contador  # Usar 'nonlocal' para modificar a variável do escopo externo
        nome = nome_requisitante.get()
        setor = nome_setor.get()
        equipamento = nome_equipamento.get()
        problema = nome_problema.get()
        solucao = nome_solucao.get()
        causa = nome_causa.get()
        responsavel = nome_responsavel.get()

        nome_arquivo = f'ORDEM_SERVIÇO_{contador}.txt'
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f'\n'
                          f'                   AlfaRigor madeiras\n'
                          f'\n'
                          f'ORDEM DE SERVIÇO Nº {contador}\n'
                          f'_______________________________________________________\n'
                          f'\n'
                          f'Data: {data_atual}\n'
                          f'_______________________________________________________\n'
                          f'\n'
                          f'Nome: {nome}\n'
                          f'_______________________________________________________\n'
                          f'\n'
                          f'Setor: {setor}\n'
                          f'_______________________________________________________\n'
                          f'\n'
                          f'Equipamento: {equipamento}\n'
                          f'_______________________________________________________\n'
                          f'\n'
                          f'Problema: {problema}\n'
                          f'_______________________________________________________\n'
                          f'\n'
                          f'_______________________________________________________\n'
                          f'\n'
                          f'Solução: {solucao}\n'
                          f'_______________________________________________________\n'
                          f'\n'
                          f'_______________________________________________________\n'
                          f'\n'
                          f'Causa: {causa}\n'
                          f'_______________________________________________________\n'
                          f'\n'
                          f'_______________________________________________________\n'
                          f'\n'
                          f'Data de execução: / / Técnico: {responsavel}\n'
                          f'_______________________________________________________\n')
        tk.Label(ordem, text='Ordem de serviço feita com sucesso!', font=('Helvetica', 14, 'bold'),
                 bg='grey').place(x=600, y=350)
        contador += 1
        salvar_contador(contador)

    # Montagem da janela de ordem de serviço
    ordem = tk.Toplevel()
    ordem.geometry('1280x720')
    ordem.configure(bg='grey')
    ordem.title('MOTORES')

    # Um título dentro da janela
    titulo = tk.Label(ordem, text="ORDEM DE SERVIÇO", bg="#fff01a", font=('Helvetica', 14, 'bold'))
    titulo.pack(side=tk.TOP, fill=tk.X, ipady=20)

    # Definição de variáveis
    global nome_equipamento, nome_problema, nome_solucao, nome_causa, nome_requisitante, nome_responsavel, nome_setor

    nome_equipamento = tk.StringVar()
    nome_problema = tk.StringVar()
    nome_solucao = tk.StringVar()
    nome_causa = tk.StringVar()
    nome_requisitante = tk.StringVar()
    nome_responsavel = tk.StringVar()
    nome_setor = tk.StringVar()

    # Labels e Entradas
    tk.Label(ordem, text='Qual equipamento:', font=('Helvetica', 12), bg='grey').place(x=40, y=180)
    tk.Entry(ordem, textvariable=nome_equipamento, font=('Helvetica', 12)).place(x=40, y=200)

    tk.Label(ordem, text='Qual o problema:', font=('Helvetica', 12), bg='grey').place(x=40, y=270)
    tk.Entry(ordem, textvariable=nome_problema, font=('Helvetica', 12)).place(x=40, y=290)

    tk.Label(ordem, text='Qual a solução:', font=('Helvetica', 12), bg='grey').place(x=40, y=350)
    tk.Entry(ordem, textvariable=nome_solucao, font=('Helvetica', 12)).place(x=40, y=370)

    tk.Label(ordem, text='Qual a causa:', font=('Helvetica', 12), bg='grey').place(x=40, y=430)
    tk.Entry(ordem, textvariable=nome_causa, font=('Helvetica', 12)).place(x=40, y=450)

    tk.Label(ordem, text='Requisitante:', font=('Helvetica', 12), bg='grey').place(x=310, y=270)
    tk.Entry(ordem, textvariable=nome_requisitante, font=('Helvetica', 12)).place(x=310, y=290)

    tk.Label(ordem, text='Responsável:', font=('Helvetica', 12), bg='grey').place(x=310, y=350)
    tk.Entry(ordem, textvariable=nome_responsavel, font=('Helvetica', 12)).place(x=310, y=370)

    tk.Label(ordem, text=f'Data:', font=('Helvetica', 12), bg='grey').place(x=310, y=180)
    tk.Label(ordem, text=f'{data_atual}', font=('Helvetica', 12), bg='grey').place(x=310, y=200)

    tk.Label(ordem, text='Setor:', font=('Helvetica', 12), bg='grey').place(x=310, y=430)
    tk.Entry(ordem, textvariable=nome_setor, font=('Helvetica', 12)).place(x=310, y=450)

    # Botão de salvar
    tk.Button(ordem, text="Salvar", font=("Helvetica", 12), command=criar_arquivo).place(x=550, y=450)

    def alternar_tela_cheia(event=None):
        estado_atual = ordem.attributes('-fullscreen')
        ordem.attributes('-fullscreen', not estado_atual)

    ordem.bind("<F11>", alternar_tela_cheia)
    ordem.bind("<Escape>", alternar_tela_cheia)

    # Abrir a janela em tela cheia
    ordem.attributes('-fullscreen', True)

    # Fecha a janela de ordem de serviço e volta para a principal
    tk.Button(ordem, text='Sair', bg='#81ff1a', command=lambda: fechar_janelacadastro(ordem, janela_principal),
              font=('Helvetica', 12, 'bold'), width=13, height=1).place(x=1170, y=640)

    ordem.mainloop()


def fechar_janelacadastro(nova_janela, janela_principal):
    # Fecha a janela de ordem de serviço e volta para a principal
    nova_janela.destroy()
    janela_principal.deiconify()
