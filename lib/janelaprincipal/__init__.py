import tkinter as tk
from lib.janelamotores import janela_motores
from lib.janelacadastro import janela_cadastrar
from lib.janelaediçao import janela_edicao
from lib.janelaordemservico import janela_ordem


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

# Botão que leva para janela de cadastro
botao1 = tk.Button(text='Cadastrar motor',
                   bg='lightgreen',
                   command=lambda: janela_cadastrar(janela),
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
                   command=lambda: janela_ordem(janela),
                   font=('helvica', 12, 'bold'),
                   width=16,
                   height=2)
botao4.place(x=300, y=250)

# Botão de sair
botao5 = tk.Button(text='Sair',
                   bg='lightgreen',
                   command=sair,
                   font=('helvica', 12, 'bold'),
                   width=16,
                   height=2)
botao5.place(x=300, y=430)

janela.mainloop()
