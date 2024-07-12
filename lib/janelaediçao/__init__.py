import tkinter as tk
from tkinter import messagebox


def janela_edicao(janela_principal):
    janela_principal.withdraw()

    def carregar_arquivo():
        try:
            with open("Motores.txt", "r") as arquivo:
                conteudo = arquivo.read()
                text_editar.delete("1.0", tk.END)  # Limpa o conteúdo atual do Text
                text_editar.insert(tk.END, conteudo)  # Insere o conteúdo do arquivo no Text
        except FileNotFoundError:
            messagebox.showerror("Erro", "O arquivo não foi encontrado.")

    # Função para salvar o conteúdo do widget Text de volta para o arquivo
    def salvar_arquivo():
        conteudo = text_editar.get("1.0", tk.END)  # Obtém o conteúdo atual do Text
        with open("Motores.txt", "w") as arquivo:
            arquivo.write(conteudo)
        messagebox.showinfo("Salvo", "O arquivo foi salvo com sucesso.")

    # Montagem da janela de ediçao
    edicao = tk.Toplevel()
    edicao.geometry('1280x720')
    edicao.attributes('-fullscreen')
    edicao.configure(bg='grey')
    edicao.title('MOTORES')

    # Um titulo dentro da janela
    titulo = tk.Label(edicao, text="EDIÇÃO DA LSITA DE MOTORES", bg="#00ff1e", font=('helvica', 14, 'bold'))
    titulo.pack(side=tk.TOP, fill=tk.X, ipady=20)

    text_editar = tk.Text(edicao, wrap=tk.WORD, font=("helvica", 12), height=25, width=140)
    text_editar.place(x=40, y=150)

    # Botão para carregar o arquivo
    botao_carregar = tk.Button(edicao, text="Carregar Arquivo", command=carregar_arquivo, font=('helvica', 12))
    botao_carregar.place(x=40, y=100)

    # Botão para salvar o arquivo
    botao_salvar = tk.Button(edicao, text="Salvar", command=salvar_arquivo, font=('helvica', 12), width=13, height=1)
    botao_salvar.place(x=1177, y=100)

    # Função para alternar entre tela cheia e janela normal
    def alternar_tela_cheia(event=None):
        estado_atual = edicao.attributes('-fullscreen')
        edicao.attributes('-fullscreen', not estado_atual)

    # Configuração da tecla para alternar entre tela cheia e janela normal (opcional)
    edicao.bind("<F11>", alternar_tela_cheia)
    edicao.bind("<Escape>", alternar_tela_cheia)

    # Abrir a janela em tela cheia
    edicao.attributes('-fullscreen', True)

    # Fecha a janela de cadastro e volta para a principal
    botao_sair = tk.Button(edicao,
                           text='Sair',
                           bg='#81ff1a',
                           command=lambda: fechar_janelacadastro(edicao, janela_principal),
                           font=('helvica', 12, 'bold'),
                           width=13,
                           height=1)
    botao_sair.place(x=590, y=640)

    edicao.mainloop()


def fechar_janelacadastro(nova_janela, janela_principal):
    # Fecha a janela de cadstro e volta para a principal
    nova_janela.destroy()
    janela_principal.deiconify()
