import tkinter as tk
from lib.oleo.oleo_68 import *
from lib.oleo.oleo_46 import *
from lib.oleo.oleo_460 import *

inicializar_banco_oleos()


def janela_oleo(janela_principal):
    janela_principal.withdraw()

    oleo = tk.Toplevel()
    oleo.geometry('1280x720')
    oleo.configure(bg='grey')
    oleo.title('CONTROLE DE ÓLEO')

    titulo = tk.Label(oleo, text="CONTROLE DE ÓLEO", bg="#320036", font=('helvica', 14, 'bold'))
    titulo.pack(side=tk.TOP, fill=tk.X, ipady=20)

    botao_oleo1 = tk.Button(oleo,
                            text='Óleo 46',
                            bg='#81ff1a',
                            command=lambda: janela_oleo_46(oleo),
                            font=('helvica', 12, 'bold'),
                            width=13,
                            height=1)
    botao_oleo1.place(x=150, y=150)

    botao_oleo2 = tk.Button(oleo,
                            text='Óleo 68',
                            bg='#81ff1a',
                            command=lambda: janela_oleo_68(oleo),
                            font=('helvica', 12, 'bold'),
                            width=13,
                            height=1)
    botao_oleo2.place(x=350, y=150)

    botao_oleo3 = tk.Button(oleo,
                            text='Óleo 460',
                            bg='#81ff1a',
                            command=lambda: janela_oleo_460(oleo),
                            font=('helvica', 12, 'bold'),
                            width=13,
                            height=1)
    botao_oleo3.place(x=550, y=150)






    def alternar_tela_cheia(event=None):
        estado_atual = oleo.attributes('-fullscreen')
        oleo.attributes('-fullscreen', not estado_atual)

    oleo.attributes('-fullscreen', True)

    botao_sair = tk.Button(oleo,
                           text='Sair',
                           bg='#81ff1a',
                           command=lambda: fechar_janelacadastro(oleo, janela_principal),
                           font=('helvica', 12, 'bold'),
                           width=13,
                           height=1)
    botao_sair.place(x=1170, y=640)

    oleo.mainloop()


def fechar_janelacadastro(nova_janela, janela_principal):
    nova_janela.destroy()
    janela_principal.deiconify()
