import tkinter as tk
from tkinter import messagebox
from lib.models import Motor


def janela_edicao(janela_principal):
    janela_principal.withdraw()

    def carregar_dados():
        try:
            texto_editar.delete("1.0", tk.END)  # Limpa o conteúdo atual do Text

            # Buscar todos os motores do banco de dados
            motores = Motor.select()
            for motor in motores:
                texto_editar.insert(tk.END, f"ID: {motor.id}\n"
                                            f"Nome: {motor.nome}\n"
                                            f"Potência: {motor.potencia}W\n"
                                            f"Corrente Nominal: {motor.corrente_nominal}A\n"
                                            f"Corrente de Trabalho: {motor.corrente_trabalho}A\n"
                                            f"Rolamento: {motor.rolamento}\n"
                                            f"Acoplamento: {motor.acoplamento}\n"
                                            f"Fixação: {motor.fixacao}\n\n"
                                            "-----------------------------\n")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao carregar os dados: {e}")

    def salvar_dados():
        conteudo = texto_editar.get("1.0", tk.END).strip()  # Obtém o conteúdo atual do Text
        linhas = conteudo.split("\n-----------------------------\n")

        for linha in linhas:
            if linha.strip() == "":
                continue

            linhas_dados = linha.split("\n")
            try:
                id = int(linhas_dados[0].split(":")[1].strip())
                nome = linhas_dados[1].split(":")[1].strip()
                potencia = linhas_dados[2].split(":")[1].strip()
                corrente_nominal = linhas_dados[3].split(":")[1].strip()
                corrente_trabalho = linhas_dados[4].split(":")[1].strip()
                rolamento = linhas_dados[5].split(":")[1].strip()
                acoplamento = linhas_dados[6].split(":")[1].strip()
                fixacao = linhas_dados[7].split(":")[1].strip()

                # Atualiza o banco de dados com os novos dados
                motor = Motor.get(Motor.id == id)
                motor.nome = nome
                motor.potencia = potencia
                motor.corrente_nominal = corrente_nominal
                motor.corrente_trabalho = corrente_trabalho
                motor.rolamento = rolamento
                motor.acoplamento = acoplamento
                motor.fixacao = fixacao
                motor.save()

            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao salvar os dados: {e}")
                return

        messagebox.showinfo("Salvo", "Os dados foram salvos com sucesso.")

    # Montagem da janela de edição
    edicao = tk.Toplevel()
    edicao.geometry('1280x720')
    edicao.attributes('-fullscreen')
    edicao.configure(bg='grey')
    edicao.title('MOTORES')

    # Um título dentro da janela
    titulo = tk.Label(edicao, text="EDIÇÃO", bg="#00ff1e", font=('helvica', 14, 'bold'))
    titulo.pack(side=tk.TOP, fill=tk.X, ipady=20)

    # Definindo o widget de texto
    global texto_editar  # Usamos global para garantir que `texto_editar` seja acessível nas funções
    texto_editar = tk.Text(edicao, wrap=tk.WORD, font=("helvica", 12), height=25, width=140)
    texto_editar.place(x=40, y=150)

    # Botão para carregar dados do banco de dados
    botao_carregar = tk.Button(edicao, text="Carregar Dados", command=carregar_dados, font=('helvica', 12))
    botao_carregar.place(x=40, y=100)

    # Botão para salvar os dados no banco de dados
    botao_salvar = tk.Button(edicao, text="Salvar Dados", command=salvar_dados, font=('helvica', 12), width=13,
                             height=1)
    botao_salvar.place(x=1177, y=100)

    # Função para alternar entre tela cheia e janela normal
    def alternar_tela_cheia(event=None):
        estado_atual = edicao.attributes('-fullscreen')
        edicao.attributes('-fullscreen', not estado_atual)

    # Configuração da tecla para alternar entre tela cheia e janela normal
    edicao.bind("<F11>", alternar_tela_cheia)
    edicao.bind("<Escape>", alternar_tela_cheia)

    # Abrir a janela em tela cheia
    edicao.attributes('-fullscreen', True)

    # Fecha a janela de edição e volta para a principal
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
    # Fecha a janela de edição e volta para a principal
    nova_janela.destroy()
    janela_principal.deiconify()
