import tkinter as tk
from tkinter import messagebox
from lib.models_oleo import inicializar_banco_oleos, fechar_banco_oleos, Oleo, atualizar_oleo, reiniciar_oleo


def atualizar_labels(oleo):
    # Atualiza os labels com os valores atuais do óleo
    label_nao_usado.config(text=f"Total Não Usado: {oleo.total_nao_usado} litros")
    label_usado.config(text=f"Total Usado: {oleo.total_usado} litros")


def processar_entrada():
    global oleo_selecionado
    try:
        usado_adicional = float(entrada_retirada.get())
        atualizar_oleo(oleo_selecionado, usado_adicional)
        oleo = Oleo.get(Oleo.nome == oleo_selecionado)
        atualizar_labels(oleo)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def reiniciar_oleo_click():
    global oleo_selecionado
    try:
        reiniciar_oleo(oleo_selecionado)
        oleo = Oleo.get(Oleo.nome == oleo_selecionado)
        atualizar_labels(oleo)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def janela_oleo_68(janela_principal):
    janela_principal.withdraw()

    oleo_68 = tk.Toplevel()
    oleo_68.geometry('1280x720')
    oleo_68.configure(bg='grey')
    oleo_68.title('CONTROLE DE ÓLEO')

    titulo = tk.Label(oleo_68, text="ÓLEO 68", bg="#5e34eb", font=('helvica', 16, 'bold'))
    titulo.pack(side=tk.TOP, fill=tk.X, ipady=20)

    tk.Label(oleo_68, text='Equipamento:', font=('helvica', 14, 'bold'), bg='grey').place(x=100, y=140)
    entrada_e = tk.Entry(oleo_68, font=('helvica', 14, 'bold'))
    entrada_e.place(x=100, y=170)

    tk.Label(oleo_68, text='Quantidade retirada:', font=('helvica', 14, 'bold'), bg='grey').place(x=100, y=230)
    global entrada_retirada
    entrada_retirada = tk.Entry(oleo_68, font=('helvica', 14, 'bold'))
    entrada_retirada.place(x=100, y=260)

    global label_nao_usado
    global label_usado
    label_nao_usado = tk.Label(oleo_68, text="", font=('helvica', 14, 'bold'), bg='grey')
    label_nao_usado.place(x=330, y=170)
    label_usado = tk.Label(oleo_68, text="", font=('helvica', 14, 'bold'), bg='grey')
    label_usado.place(x=330, y=260)

    # Inicializa o óleo selecionado e atualiza os labels
    global oleo_selecionado
    oleo_selecionado = "Oleo 68"
    oleo = Oleo.get(Oleo.nome == oleo_selecionado)
    atualizar_labels(oleo)

    tk.Button(oleo_68, text='Atualizar', bg='#81ff1a', command=processar_entrada,
              font=('helvica', 12, 'bold')).place(x=100, y=300)

    tk.Button(oleo_68, text='Reiniciar', bg='#ff1a1a', command=reiniciar_oleo_click,
              font=('helvica', 12, 'bold')).place(x=200, y=300)

    def alternar_tela_cheia(event=None):
        estado_atual = oleo_68.attributes('-fullscreen')
        oleo_68.attributes('-fullscreen', not estado_atual)

    oleo_68.attributes('-fullscreen', True)

    botao_sair = tk.Button(oleo_68, text='Sair', bg='#81ff1a',
                           command=lambda: fechar_janelacadastro(oleo_68, janela_principal),
                           font=('helvica', 14, 'bold'), width=13, height=1)
    botao_sair.place(x=1170, y=640)

    oleo_68.mainloop()
    fechar_banco_oleos()


def fechar_janelacadastro(nova_janela, janela_principal):
    nova_janela.destroy()
    janela_principal.deiconify()
