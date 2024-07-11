import tkinter as tk
from lib.funcao import *
from tkinter import messagebox

filepath = 'Motores.txt'


def janela_cadastrar(janela_principal):
    janela_principal.withdraw()

    def mostrar_informacao():
        # Essa funçao mostra informaçoes e salva as informaçoes no arquivo Motores.txt
        nome = nome_motor.get()
        potencia = potencia_motor.get()
        corrente_e = corrente(int(potencia))
        fator_serv = fator_serviço(corrente_e)
        resultado_corrente.config(text=f"A corrente é {corrente_e}A")
        resultado_fator.config(text=f"O corrente de serviço é {fator_serv}A")
        try:
            with open(filepath, 'a') as arquivo:
                arquivo.write(f'{nome} = Pontecia: {potencia}W , Corrente nominal: {corrente_e}A ,'
                              f' Corrente de trabalho: {fator_serv}A\n')
                arquivo.write('-----------------------------------------------------------------'
                              '----------------------------------------------------------------\n')
            label_salvo = tk.Label(cadastrar, text='Informações salvas com sucesso!',
                                   bg='grey', font=('helvica', 14, 'bold'))
            label_salvo.place(x=200, y=350)
        except Exception as e:
            messagebox.showerror("Salvar Arquivo", f"Ocorreu um erro ao salvar o arquivo: {e}")

    # Montagem da janela de cadastro
    cadastrar = tk.Toplevel()
    cadastrar.geometry('750x500')
    cadastrar.configure(bg='grey')
    cadastrar.title('MOTORES')

    # Um titulo dentro da janela
    titulo = tk.Label(cadastrar, text="CADASTRO DE MOTORES", bg="#ff1a1a", font=('helvica', 14, 'bold'))
    titulo.pack(side=tk.TOP, fill=tk.X, ipady=20)

    # Para salvar o nome do motor
    label_nome = tk.Label(cadastrar, text='Nome do motor:', font=('helvica', 12), bg='grey')
    label_nome.place(x=40, y=150)
    nome_motor = tk.StringVar()
    entrada_nome = tk.Entry(cadastrar, textvariable=nome_motor, font=('helvica', 12))
    entrada_nome.place(x=40, y=170)

    # Para salvar a potencia do motor
    label_motor = tk.Label(cadastrar, text='Potencia do motor:', font=('helvica', 12), bg='grey')
    label_motor.place(x=40, y=230)
    potencia_motor = tk.StringVar()
    entrada_motor = tk.Entry(cadastrar, textvariable=potencia_motor, font=('helvica', 12))
    entrada_motor.place(x=40, y=250)

    # Botão de salvar
    salvar_botao = tk.Button(cadastrar, text="Salvar", font=("helvica", 12), command=mostrar_informacao)
    salvar_botao.place(x=250, y=245)

    # Escrita da corrente e fator na janela
    resultado_corrente = tk.Label(cadastrar, text="", font=("helvica", 12, 'bold'), bg='grey')
    resultado_corrente.place(x=350, y=180)
    resultado_fator = tk.Label(cadastrar, text="", font=("helvica", 12, 'bold'), bg='grey')
    resultado_fator.place(x=350, y=250)

    # Fecha a janela de cadastro e volta para a principal
    botao_sair = tk.Button(cadastrar,
                           text='Sair',
                           bg='#81ff1a',
                           command=lambda: fechar_janelacadastro(cadastrar, janela_principal),
                           font=('helvica', 12, 'bold'),
                           width=13,
                           height=1)
    botao_sair.place(x=590, y=440)

    cadastrar.mainloop()


def fechar_janelacadastro(nova_janela, janela_principal):
    # Fecha a janela de cadstro e volta para a principal
    nova_janela.destroy()
    janela_principal.deiconify()
