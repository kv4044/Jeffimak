import tkinter as tk
from tkinter import messagebox
from lib.models import Motor


def janela_motores(janela_principal):
    janela_principal.withdraw()

    def enter(event=None):
        Buscar()

    def Buscar():
        texto_motores.delete("1.0", tk.END)
        palavra = entrada_busca.get()
        if not palavra:
            messagebox.showwarning("Entrada vazia", "Por favor, insira uma palavra para buscar.")
            return

        try:
            resultados = Motor.select().where(
                (Motor.nome.contains(palavra)) |
                (Motor.potencia.contains(palavra)) |
                (Motor.rolamento.contains(palavra)) |
                (Motor.acoplamento.contains(palavra)) |
                (Motor.fixacao.contains(palavra))
            )

            if resultados:
                for motor in resultados:
                    texto_motores.insert(tk.END, f"Nome: {motor.nome}\n"
                                                 f"Potência: {motor.potencia}W\n"
                                                 f"Corrente Nominal: {motor.corrente_nominal}A\n"
                                                 f"Corrente de Trabalho: {motor.corrente_trabalho}A\n"
                                                 f"Rolamento: {motor.rolamento}\n"
                                                 f"Acoplamento: {motor.acoplamento}\n"
                                                 f"Fixação: {motor.fixacao}\n\n"
                                                 "-----------------------------\n")
            else:
                texto_motores.insert(tk.END, "Nenhuma ocorrência encontrada.")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    def mostrar_tudo():
        try:
            resultados = Motor.select()
            texto_motores.delete('1.0', tk.END)
            if resultados:
                for motor in resultados:
                    texto_motores.insert(tk.END, f"id: {motor.id}\n"
                                                 f"Nome: {motor.nome}\n"
                                                 f"Potência: {motor.potencia}W\n"
                                                 f"Corrente Nominal: {motor.corrente_nominal}A\n"
                                                 f"Corrente de Trabalho: {motor.corrente_trabalho}A\n"
                                                 f"Rolamento: {motor.rolamento}\n"
                                                 f"Acoplamento: {motor.acoplamento}\n"
                                                 f"Fixação: {motor.fixacao}\n"
                                                 "------------------------------------------------\n\n")
            else:
                texto_motores.insert(tk.END, "Nenhum motor cadastrado.")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    motores = tk.Toplevel()
    motores.geometry('1280x720')
    motores.configure(bg='grey')
    motores.title('MOTORES')

    titulo = tk.Label(motores, text="MOTORES CADASTRADOS", bg="#fff01a", font=('helvica', 14, 'bold'))
    titulo.pack(side=tk.TOP, fill=tk.X, ipady=20)

    botao_buscar = tk.Button(motores, text='Buscar', font=('helvica', 12), command=Buscar)
    botao_buscar.place(x=240, y=105)
    entrada_busca = tk.Entry(motores, font=('helvica', 12))
    entrada_busca.place(x=40, y=110)
    motores.bind('<Return>', enter)

    botao_ver = tk.Button(motores, text='Ver todos', command=mostrar_tudo, font=('helvica', 12), width=13, height=1)
    botao_ver.place(x=1177, y=110)

    texto_motores = tk.Text(motores, state=tk.NORMAL, wrap=tk.WORD, font=("helvica", 12), height=25, width=140)
    texto_motores.place(x=40, y=150)

    def alternar_tela_cheia(event=None):
        estado_atual = motores.attributes('-fullscreen')
        motores.attributes('-fullscreen', not estado_atual)

    motores.bind("<F11>", alternar_tela_cheia)
    motores.bind("<Escape>", alternar_tela_cheia)

    motores.attributes('-fullscreen', True)

    botao_sair = tk.Button(motores,
                           text='Sair',
                           bg='#81ff1a',
                           command=lambda: fechar_janelacadastro(motores, janela_principal),
                           font=('helvica', 12, 'bold'),
                           width=13,
                           height=1)
    botao_sair.place(x=1170, y=640)

    motores.mainloop()


def fechar_janelacadastro(nova_janela, janela_principal):
    nova_janela.destroy()
    janela_principal.deiconify()
