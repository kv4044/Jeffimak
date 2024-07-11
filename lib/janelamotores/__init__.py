import tkinter as tk
from tkinter import messagebox

filepath = 'Motores.txt'


def janela_motores(janela_principal):
    janela_principal.withdraw()

    def Buscar():
        #
        texto_motores.delete("1.0", tk.END)

        # Obter a palavra do entrada_busca
        palavra = entrada_busca.get()

        if not palavra:
            messagebox.showwarning("Entrada vazia", "Por favor, insira uma palavra para buscar.")
            return

        try:
            # Abrir e ler o arquivo
            with open("Motores.txt", "r") as file:
                linhas = file.readlines()

            # Procurar a palavra nas linhas do arquivo
            results = [linha for linha in linhas if palavra in linha]

            # Mostrar os resultados no texto_motores
            if results:
                for result in results:
                    texto_motores.insert(tk.END, result)
            else:
                texto_motores.insert(tk.END, "Nenhuma ocorrência encontrada.")

        except FileNotFoundError:
            messagebox.showerror("Erro", "O arquivo não foi encontrado.")

    def mostrar_tudo():
        # opçao de mostrar todos os motores cadastrados
        try:
            with open(filepath, 'r')as arquivo:
                conteudo = arquivo.read()
                texto_motores.delete('1.0', tk.END)
                texto_motores.insert(tk.END, conteudo)
        except FileNotFoundError:
            messagebox.showwarning('Abrir arquivo', f'O arquivo {filepath} não foi encontrado.')

    # Montagem da janela de lista dos motores
    motores = tk.Toplevel()
    motores.geometry('750x500')
    motores.configure(bg='grey')
    motores.title('MOTORES')

    # Um titulo dentro da janela
    titulo = tk.Label(motores, text="VER MOTORES CADASTRADOS", bg="#fff01a", font=('helvica', 14, 'bold'))
    titulo.pack(side=tk.TOP, fill=tk.X, ipady=20)

    # Buscar motor pelo nome ou potencia
    botao_buscar= tk.Button(motores, text='Buscar', font=('helvica', 12), command=Buscar)
    botao_buscar.place(x=240, y=105)
    entrada_busca = tk.Entry(motores, font=('helvica', 12))
    entrada_busca.place(x=40, y=110)

    # Ver todos os motores cadastrados
    botao_ver = tk.Button(motores, text='Ver todos', command=mostrar_tudo, font=('helvica', 12), width=13, height=1)
    botao_ver.place(x=590, y=110)

    # motores cadastrados
    texto_motores = tk.Text(motores, state=tk.NORMAL, wrap=tk.WORD, font=("helvica", 12), height=15, width=75)
    texto_motores.place(x=40, y=150)

    # Fecha a janela de cadastro e volta para a principal
    botao_sair = tk.Button(motores,
                           text='Sair',
                           bg='#81ff1a',
                           command=lambda: fechar_janelacadastro(motores, janela_principal),
                           font=('helvica', 12, 'bold'),
                           width=13,
                           height=1)
    botao_sair.place(x=590, y=440)

    motores.mainloop()


def fechar_janelacadastro(nova_janela, janela_principal):
    # Fecha a janela de vizualizar motores e volta para a principal
    nova_janela.destroy()
    janela_principal.deiconify()
