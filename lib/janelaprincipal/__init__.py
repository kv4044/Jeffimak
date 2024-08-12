import tkinter as tk
from lib.janelamotores import janela_motores
from lib.janelacadastro import janela_cadastrar
from lib.janelacadastro import contar_motores
from lib.janelaediçao import janela_edicao
from lib.janelaordemservico import janela_ordem
from lib.janelaoleo import janela_oleos
from lib.models_motor import carregar_contador


def atualizar_tela_principal():
    total_motores = contar_motores()
    total_os = carregar_contador() - 1

    # Atualizar os rótulos com as novas contagens
    total_motores_label.config(text=f'Total de motores: {total_motores}')
    total_os_label.config(text=f'Total de ordem de serviço: {total_os}')


def sair():
    janela.destroy()


# Criação da janela principal
janela = tk.Tk()
janela.geometry('750x500')
janela.configure(bg='grey')
janela.title('MOTORES')

# Titulo da janela
titulo = tk.Label(janela, text="MENU", bg="#1af4ff", font=('helvica', 14, 'bold'))
titulo.pack(side=tk.TOP, fill=tk.X, ipady=20, )

# Labels para mostrar contagens
total_motores_label = tk.Label(janela, font=('helvica', 12, 'bold'), bg='grey')
total_motores_label.place(x=55, y=260)

total_os_label = tk.Label(janela, font=('helvica', 12, 'bold'), bg='grey')
total_os_label.place(x=520, y=260)

# Atualizar a tela inicial com contagens
atualizar_tela_principal()

# Botão que leva para janela de cadastro
botao1 = tk.Button(text='Cadastrar motor',
                   bg='lightgreen',
                   command=lambda: janela_cadastrar(janela, atualizar_tela_principal),
                   font=('helvica', 12, 'bold'),
                   width=16,
                   height=2)
botao1.place(x=40, y=150)

# Botão que leva para janela de motores cadastrados
botao2 = tk.Button(text='Motores cadastrados',
                   bg='lightgreen',
                   command=lambda: janela_motores(janela),
                   font=('helvica', 12, 'bold'),
                   width=16,
                   height=2)
botao2.place(x=300, y=150)

# Botão que leva para janela de ediçao dos motores cadastrados
botao3 = tk.Button(text='Editar',
                   bg='lightgreen',
                   command=lambda: janela_edicao(janela),
                   font=('helvica', 12, 'bold'),
                   width=16,
                   height=2)
botao3.place(x=560, y=150)

# Botão de gerar ordem de serviço
botao4 = tk.Button(text='Ordem de serviço',
                   bg='lightgreen',
                   command=lambda: janela_ordem(janela, atualizar_tela_principal),
                   font=('helvica', 12, 'bold'),
                   width=16,
                   height=2)
botao4.place(x=300, y=250)

# Botão de controle do oleo
botao5 = tk.Button(text='Controle de óleo',
                   bg='lightgreen',
                   command=lambda: janela_oleos(janela),
                   font=('helvica', 12, 'bold'),
                   width=16,
                   height=2)
botao5.place(x=300, y=340)

# Botão de sair
botao_sair = tk.Button(text='Sair',
                       bg='lightgreen',
                       command=sair,
                       font=('helvica', 12, 'bold'),
                       width=16,
                       height=2)
botao_sair.place(x=300, y=430)

janela.mainloop()
