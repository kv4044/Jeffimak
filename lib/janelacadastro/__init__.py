import tkinter as tk
from lib.funcao import *
from tkinter import messagebox

filepath = 'Motores.txt'


def janela_cadastrar(janela_principal):
    janela_principal.withdraw()

    def enter(event=None):
        # Apertar o enter
        mostrar_informacao()

    def mostrar_informacao():
        # Essa funçao mostra informaçoes e salva as informaçoes no arquivo Motores.txt
        nome = nome_motor.get()
        potencia = potencia_motor.get()
        try:
            corrente_e = corrente(int(potencia))
        except ValueError:
            messagebox.showwarning('ERRO', 'Digite um numero valido!')
        finally:
            fator_serv = fator_serviço(corrente_e)
            rolamento = rolamento_motor.get()
            acoplamento = acoplamento_motor.get()
            fixa = fixa_motor.get()

            resultado_corrente.config(text=f"A corrente é {corrente_e}A")
            resultado_fator.config(text=f"O corrente de serviço é {fator_serv}A")

        try:
            with open(filepath, 'a') as arquivo:
                arquivo.write(f'{nome}\nPontecia = {potencia}W \nCorrente nominal = {corrente_e}A\n'
                              f'Corrente de trabalho = {fator_serv}A \nRolamento = {rolamento}\n'
                              f'Acoplamento = {acoplamento} \nFixacao = {fixa}\n')
                arquivo.write('-----------------------------------------------------------------'
                              '----------------------------------------------------------------\n')
            label_salvo = tk.Label(cadastrar, text='Informações salvas com sucesso!',
                                   bg='grey', font=('helvica', 14, 'bold'))
            label_salvo.place(x=500, y=560)
        except Exception as e:
            messagebox.showerror("Salvar Arquivo", f"Ocorreu um erro ao salvar o arquivo: {e}")

    # Montagem da janela de cadastro
    cadastrar = tk.Toplevel()
    cadastrar.geometry('1280x720')
    cadastrar.configure(bg='grey')
    cadastrar.title('MOTORES')

    # Um titulo dentro da janela
    titulo = tk.Label(cadastrar, text="CADASTRO DE MOTORES", bg="#ff1a1a", font=('helvica', 14, 'bold'))
    titulo.pack(side=tk.TOP, fill=tk.X, ipady=20)

    # Para salvar o nome do motor
    label_nome = tk.Label(cadastrar, text='Nome do motor:', font=('helvica', 12), bg='grey')
    label_nome.place(x=40, y=180)
    nome_motor = tk.StringVar()
    entrada_nome = tk.Entry(cadastrar, textvariable=nome_motor, font=('helvica', 12))
    entrada_nome.place(x=40, y=200)

    # Para salvar a potencia do motor
    label_motor = tk.Label(cadastrar, text='Potencia do motor:', font=('helvica', 12), bg='grey')
    label_motor.place(x=40, y=260)
    potencia_motor = tk.StringVar()
    entrada_motor = tk.Entry(cadastrar, textvariable=potencia_motor, font=('helvica', 12))
    entrada_motor.place(x=40, y=280)

    # Tipo de rolamento
    label_rolamento = tk.Label(cadastrar, text='Rolamento:', font=('helvica', 12), bg='grey')
    label_rolamento.place(x=40, y=340)
    rolamento_motor = tk.StringVar()
    entrada_rolamento = tk.Entry(cadastrar, textvariable=rolamento_motor, font=('helvica', 12))
    entrada_rolamento.place(x=40, y=360)

    # Tipo de acoplamento
    label_acoplamento = tk.Label(cadastrar, text='Acoplamento:', font=('helvica', 12), bg='grey')
    label_acoplamento.place(x=300, y=260)
    acoplamento_motor = tk.StringVar()
    entrada_acoplamento = tk.Entry(cadastrar, textvariable=acoplamento_motor, font=('helvica', 12))
    entrada_acoplamento.place(x=300, y=280)

    # Tipo de fixação
    label_patas = tk.Label(cadastrar, text='Fixação:', font=('helvica', 12), bg='grey')
    label_patas.place(x=300, y=180)
    fixa_motor = tk.StringVar()
    entrada_patas = tk.Entry(cadastrar, textvariable=fixa_motor, font=('helvica', 12))
    entrada_patas.place(x=300, y=200)

    # Botão de salvar
    salvar_botao = tk.Button(cadastrar, text="Salvar", font=("helvica", 12), command=mostrar_informacao)
    salvar_botao.place(x=350, y=360)

    # Apertar o botao enter do teclado
    cadastrar.bind('<Return>', enter)

    # Escrita da corrente e fator na janela
    resultado_corrente = tk.Label(cadastrar, text="", font=("helvica", 12, 'bold'), bg='grey')
    resultado_corrente.place(x=590, y=200)
    resultado_fator = tk.Label(cadastrar, text="", font=("helvica", 12, 'bold'), bg='grey')
    resultado_fator.place(x=550, y=280)

    # Função para alternar entre tela cheia e janela normal
    def alternar_tela_cheia(event=None):
        estado_atual = cadastrar.attributes('-fullscreen')
        cadastrar.attributes('-fullscreen', not estado_atual)

    # Configuração da tecla para alternar entre tela cheia e janela normal (opcional)
    cadastrar.bind("<F11>", alternar_tela_cheia)
    cadastrar.bind("<Escape>", alternar_tela_cheia)

    # Abrir a janela em tela cheia
    cadastrar.attributes('-fullscreen', True)

    # Fecha a janela de cadastro e volta para a principal
    botao_sair = tk.Button(cadastrar,
                           text='Sair',
                           bg='#81ff1a',
                           command=lambda: fechar_janelacadastro(cadastrar, janela_principal),
                           font=('helvica', 12, 'bold'),
                           width=13,
                           height=1)
    botao_sair.place(x=590, y=640)

    cadastrar.mainloop()


def fechar_janelacadastro(nova_janela, janela_principal):
    # Fecha a janela de cadstro e volta para a principal
    nova_janela.destroy()
    janela_principal.deiconify()
