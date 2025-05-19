import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from lib.models_motor import initialize_db, buscar_motor, carregar_contador, salvar_contador


def ler_informacoes(equipamento):
    informacoes = buscar_motor(equipamento)
    if informacoes:
        return (f"Nome: {informacoes['nome']}\n"
                f"Potência: {informacoes['potencia']}\n"
                f"Corrente Nominal: {informacoes['corrente_nominal']}\n"
                f"Corrente de Trabalho: {informacoes['corrente_trabalho']}\n"
                f"Rolamento: {informacoes['rolamento']}\n"
                f"Acoplamento: {informacoes['acoplamento']}\n"
                f"Fixação: {informacoes['fixacao']}\n")
    return "Informações não encontradas para o equipamento."


def abrir_arquivo():
    contador = carregar_contador()
    if contador > 1:
        nome_arquivo = f'ORDEM_SERVIÇO_{contador - 1}.pdf'
        if os.path.exists(nome_arquivo):
            os.startfile(nome_arquivo)
        else:
            messagebox.showerror('Arquivo não encontrado', f'O arquivo {nome_arquivo} não existe.')
    else:
        messagebox.showwarning('Arquivo não criado', 'Nenhum arquivo de ordem de serviço foi criado ainda.')


def atualizar_relogio():
    global relogio, ordem
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    relogio.config(text=f'{agora}')
    ordem.after(1000, atualizar_relogio)


def atualizar_contador_na_interface():
    ordens_geradas.set(f'Ordens geradas: {carregar_contador() - 1}')


def janela_ordem(janela_principal, atualizar_funcao):
    global relogio, ordem, ordens_geradas, nome_equipamento, nome_problema, nome_solucao, nome_causa, nome_requisitante, nome_responsavel, nome_setor, contador

    janela_principal.withdraw()

    def gerar_os():
        global contador

        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

        nome = nome_requisitante.get()
        setor = nome_setor.get()
        equipamento = nome_equipamento.get()
        problema = nome_problema.get()
        solucao = nome_solucao.get()
        causa = nome_causa.get()
        responsavel = nome_responsavel.get()

        informacoes_adicionais = ler_informacoes(equipamento)
        nome_arquivo = f'ORDEM_SERVIÇO_{contador}.pdf'

        # Gerar PDF com reportlab
        c = canvas.Canvas(nome_arquivo, pagesize=A4)
        largura, altura = A4
        y = altura - 50

        def escrever_linha(texto, pulo=20):
            nonlocal y
            c.drawString(50, y, texto)
            y -= pulo

        escrever_linha("AlfaRigor Madeiras", 30)
        escrever_linha(f"ORDEM DE SERVIÇO Nº {contador}", 20)
        escrever_linha("__________________________________________________________________", 20)
        escrever_linha("INFORMAÇÕES DO MOTOR:", 20)
        for linha in informacoes_adicionais.strip().split("\n"):
            escrever_linha(linha)
        escrever_linha("__________________________________________________________________", 20)
        escrever_linha(f"Data: {data_atual}", 20)
        escrever_linha("__________________________________________________________________", 20)
        escrever_linha(f"Nome: {nome}", 20)
        escrever_linha(f"Setor: {setor}", 20)
        escrever_linha(f"Equipamento: {equipamento}", 20)
        escrever_linha("__________________________________________________________________", 20)
        escrever_linha(f"Problema: {problema}", 20)
        escrever_linha("__________________________________________________________________", 20)
        escrever_linha(f"Solução: {solucao}", 20)
        escrever_linha("__________________________________________________________________", 20)
        escrever_linha(f"Causa: {causa}", 20)
        escrever_linha("__________________________________________________________________", 20)
        escrever_linha(f"Data de execução:    /   /                     Técnico: {responsavel}", 20)
        escrever_linha("__________________________________________________________________", 20)

        c.save()

        tk.Label(ordem, text='Ordem de serviço feita com sucesso!', font=('Helvetica', 14, 'bold'), bg='grey').place(
            x=600, y=350)

        contador += 1
        salvar_contador(contador)

        nome_requisitante.set("")
        nome_setor.set("")
        nome_equipamento.set("")
        nome_problema.set("")
        nome_solucao.set("")
        nome_causa.set("")
        nome_responsavel.set("")

        atualizar_contador_na_interface()
        atualizar_funcao()

    initialize_db()

    nome_equipamento = tk.StringVar()
    nome_problema = tk.StringVar()
    nome_solucao = tk.StringVar()
    nome_causa = tk.StringVar()
    nome_requisitante = tk.StringVar()
    nome_responsavel = tk.StringVar()
    nome_setor = tk.StringVar()

    contador = carregar_contador()

    ordem = tk.Toplevel()
    ordem.geometry('1280x720')
    ordem.configure(bg='grey')
    ordem.title('MOTORES')

    titulo = tk.Label(ordem, text="ORDEM DE SERVIÇO", bg="#1b15d1", font=('Helvetica', 16, 'bold'))
    titulo.pack(side=tk.TOP, fill=tk.X, ipady=20)

    ordens_geradas = tk.StringVar()
    ordens_geradas.set(f'Ordens geradas: {contador - 1}')
    tk.Label(ordem, textvariable=ordens_geradas, font=('helvica', 14, 'bold'), bg='grey').place(x=40, y=150)

    tk.Label(ordem, text='Equipamento:', font=('helvica', 14, 'bold'), bg='grey').place(x=40, y=180)
    tk.Entry(ordem, textvariable=nome_equipamento, font=('helvica', 14, 'bold')).place(x=40, y=210)

    tk.Label(ordem, text='Problema:', font=('helvica', 14, 'bold'), bg='grey').place(x=40, y=270)
    tk.Entry(ordem, textvariable=nome_problema, font=('helvica', 14, 'bold')).place(x=40, y=300)

    tk.Label(ordem, text='Solução:', font=('helvica', 14, 'bold'), bg='grey').place(x=40, y=350)
    tk.Entry(ordem, textvariable=nome_solucao, font=('helvica', 14, 'bold')).place(x=40, y=380)

    tk.Label(ordem, text='Causa:', font=('helvica', 14, 'bold'), bg='grey').place(x=40, y=430)
    tk.Entry(ordem, textvariable=nome_causa, font=('helvica', 14, 'bold')).place(x=40, y=460)

    tk.Label(ordem, text='Requisitante:', font=('helvica', 14, 'bold'), bg='grey').place(x=310, y=270)
    tk.Entry(ordem, textvariable=nome_requisitante, font=('helvica', 14, 'bold')).place(x=310, y=300)

    tk.Label(ordem, text='Responsável:', font=('helvica', 14, 'bold'), bg='grey').place(x=310, y=350)
    tk.Entry(ordem, textvariable=nome_responsavel, font=('helvica', 14, 'bold')).place(x=310, y=380)

    tk.Label(ordem, text='Data:', font=('helvica', 14, 'bold'), bg='grey').place(x=310, y=180)
    relogio = tk.Label(ordem, text=f'{datetime.now().strftime("%d/%m/%Y %H:%M")}', font=('helvica', 14, 'bold'), bg='grey')
    relogio.place(x=310, y=210)

    tk.Label(ordem, text='Setor:', font=('helvica', 14, 'bold'), bg='grey').place(x=310, y=430)
    tk.Entry(ordem, textvariable=nome_setor, font=('helvica', 14, 'bold')).place(x=310, y=460)

    tk.Button(ordem, text="Salvar", font=('helvica', 14, 'bold'), command=gerar_os).place(x=550, y=450)
    tk.Button(ordem, text="Imprimir", font=('helvica', 14, 'bold'), command=abrir_arquivo).place(x=670, y=450)

    def alternar_tela_cheia(event=None):
        estado_atual = ordem.attributes('-fullscreen')
        ordem.attributes('-fullscreen', not estado_atual)

    ordem.bind("<F11>", alternar_tela_cheia)
    ordem.bind("<Escape>", lambda e: ordem.attributes('-fullscreen', False))
    ordem.attributes('-fullscreen', True)

    tk.Button(ordem, text='Sair', bg='#81ff1a', command=lambda: fechar_janelacadastro(ordem, janela_principal),
              font=('Helvetica', 14, 'bold'), width=13, height=1).place(x=1170, y=640)

    atualizar_relogio()
    ordem.mainloop()


def fechar_janelacadastro(nova_janela, janela_principal):
    nova_janela.destroy()
    janela_principal.deiconify()
