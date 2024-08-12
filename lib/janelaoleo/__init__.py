import tkinter as tk
from tkinter import messagebox
from lib.models_oleo import inicializar_banco_oleos, fechar_banco_oleos, Oleo, atualizar_oleo, reiniciar_oleo


def atualizar_labels(oleo, label_nao_usado, label_usado):
    # Atualiza os labels com os valores atuais do óleo
    label_nao_usado.config(text=f"Total Não Usado: {oleo.total_nao_usado} litros")
    label_usado.config(text=f"Total Usado: {oleo.total_usado} litros")


def processar_entrada(oleo_nome, entrada_retirada, label_nao_usado, label_usado):
    try:
        usado_adicional = float(entrada_retirada.get())
        atualizar_oleo(oleo_nome, usado_adicional)
        oleo = Oleo.get(Oleo.nome == oleo_nome)
        atualizar_labels(oleo, label_nao_usado, label_usado)
        entrada_retirada.delete(0, tk.END)  # Limpa o campo de entrada após a atualização
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def reiniciar_oleo_click(oleo_nome, label_nao_usado, label_usado):
    try:
        reiniciar_oleo(oleo_nome)
        oleo = Oleo.get(Oleo.nome == oleo_nome)
        atualizar_labels(oleo, label_nao_usado, label_usado)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


inicializar_banco_oleos()


def janela_oleos(janela_principal):
    janela_principal.withdraw()

    janela_oleos = tk.Toplevel()
    janela_oleos.geometry('1280x720')
    janela_oleos.configure(bg='grey')
    janela_oleos.title('CONTROLE DE TODOS OS ÓLEOS')

    titulo = tk.Label(janela_oleos, text="CONTROLE DE TODOS OS ÓLEOS", bg="#5e34eb", font=('helvica', 16, 'bold'))
    titulo.pack(side=tk.TOP, fill=tk.X, ipady=20)

    # Criar uma lista de todos os óleos no banco de dados
    oleos = Oleo.select()

    for i, oleo in enumerate(oleos):
        y_position = 140 + i * 160  # Espaçamento entre as seções de cada óleo

        tk.Label(janela_oleos, text=f'{oleo.nome}', font=('helvica', 14, 'bold'), bg='grey').place(x=100,
                                                                                                   y=y_position)
        tk.Label(janela_oleos, text='Quantidade retirada:', font=('helvica', 14, 'bold'), bg='grey').place(
            x=100, y=y_position + 30)

        entrada_retirada = tk.Entry(janela_oleos, font=('helvica', 14, 'bold'))
        entrada_retirada.place(x=100, y=y_position + 60)

        label_nao_usado = tk.Label(janela_oleos, text=f"Total Não Usado: {oleo.total_nao_usado} litros",
                                   font=('helvica', 14, 'bold'), bg='grey')
        label_nao_usado.place(x=330, y=y_position)

        label_usado = tk.Label(janela_oleos, text=f"Total Usado: {oleo.total_usado} litros",
                               font=('helvica', 14, 'bold'), bg='grey')
        label_usado.place(x=330, y=y_position + 60)

        tk.Button(janela_oleos, text='Atualizar', bg='#81ff1a',
                  command=lambda o=oleo.nome, er=entrada_retirada, lnu=label_nao_usado, lu=label_usado:
                  processar_entrada(o, er, lnu, lu),
                  font=('helvica', 12, 'bold')).place(x=100, y=y_position + 100)

        tk.Button(janela_oleos, text='Reiniciar', bg='#ff1a1a',
                  command=lambda o=oleo.nome, lnu=label_nao_usado, lu=label_usado:
                  reiniciar_oleo_click(o, lnu, lu),
                  font=('helvica', 12, 'bold')).place(x=200, y=y_position + 100)

    janela_oleos.attributes('-fullscreen', True)

    botao_sair = tk.Button(janela_oleos, text='Sair', bg='#81ff1a',
                           command=lambda: fechar_janelacadastro(janela_oleos, janela_principal),
                           font=('helvica', 14, 'bold'), width=13, height=1)
    botao_sair.place(x=1170, y=640)

    janela_oleos.mainloop()
    fechar_banco_oleos()


def fechar_janelacadastro(nova_janela, janela_principal):
    nova_janela.destroy()
    janela_principal.deiconify()
