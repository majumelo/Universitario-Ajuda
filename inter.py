import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import webbrowser
from main import *
from operacoesbd import *

con = criarConexao('localhost', 'root', '12345', 'mapeamento')

def buscar_sala_interface():
    numero_sala = entrada_sala.get().lower().strip()

    mapeamento = {
        "a": {
            "a101": 1, "a102": 2, "a103": 3, "a104": 4, "a105": 5, "a106": 6, "a107": 7, "a108": 8, "a109": 9,
            "a110": 10, "a111": 11, "a112": 12, "a113": 13, "a114": 14, "a115": 15, "a116": 16, "a117": 17,
            "a118": 18, "a119": 19, "a201": 20, "a202": 21, "a203": 22, "a204": 23, "a205": 24, "a206": 25,
            "a207": 26, "a208": 27, "a209": 28, "a210": 29, "a211": 30, "a212": 31, "gestão": 32, "dep.física": 33,
            "dep.química": 34, "dep.computação": 35, "dep.engenharia sanitaria": 36, "dep.matemática": 37,
            "dep.estatistica": 38, "centro academico quimica industrial": 39, "centro academico computação": 40,
            "ctica": 41, "banheiro térreo": 42, "banheiros 1° andar": 43, "direção do cct": 44
        },
        "b": {
            "b101": 45, "b102": 46, "b103": 47, "b104": 48, "b105": 49, "banheiros bloco b": 50, "b107": 51,
            "b108": 52, "b109": 52, "b110": 53, "b112": 54, "laboratório pedagógico de matematica": 55,
            "laboratório de informática de matemática": 56, "b114": 57, "b115": 58, "banheiros 1° andar bloco b": 59,
            "b201": 60, "b202": 61, "b203": 62, "b204": 63, "b205": 64, "b206": 65, "b207": 66, "b208": 67,
            "b209": 68, "b210": 69, "cetic b": 70
        },
        "c": {
            "c101": 71, "c102": 72, "c103": 73, "c104": 74, "centro academico de eng. sanitaria e ambiental": 75,
            "c106": 76, "c107": 77, "c108": 78, "c109": 79, "c110": 80, "c201": 81, "c202": 82, "c203": 83,
            "c204": 84, "c205": 85, "c206": 86, "c207": 87, "c208": 88, "c209": 89, "c210": 90, "c301": 91,
            "c302": 92, "c303": 93, "c304": 94, "c305": 95, "c306": 96, "c307": 97, "c308": 98, "c309": 99,
            "c310": 100, "centro academico de física": 101, "cetic c": 102, "banheiros terreo bloco": 103,
            "banheiros 1° andar bloco c": 104, "banheiros 2° andar bloco c": 105
        }
    }

    # Determina o bloco e o valor da sala
    bloco = numero_sala[0]  # Primeiro caractere indica o bloco
    valor_sala = mapeamento.get(bloco, {}).get(numero_sala)

    if valor_sala is not None:
        bloco_coluna = f"Bloco{bloco.upper()}"
        sql = f"SELECT {bloco_coluna} FROM mapeamento WHERE Id{bloco_coluna} = {valor_sala};"

        resultado = buscarSala(con, sql)
        if resultado:
            messagebox.showinfo("Resultado da Busca", f"Sala encontrada: {resultado[0]}")
        else:
            messagebox.showwarning("Resultado da Busca", "Sala não encontrada.")


def maps_cct():
    maps = 'https://maps.app.goo.gl/JoqnY4FS8WQjRVfm9'
    webbrowser.open(maps)

def aviso_andamento():
    messagebox.showwarning("Aviso", "EM ANDAMENTO")

def mostrar_tela_inicial():
    frame_inicial.pack(fill="both") #fill BOTH expande a janela de forma uniforme para AMBOS, tanto para x, quanto para y.
    frame_busca_salas.pack_forget()
    frame_lanchonetes.pack_forget()

def abrir_busca_salas():
    frame_inicial.pack_forget()
    frame_busca_salas.pack(fill="both")
    frame_lanchonetes.pack_forget()

def abrir_lanchonetes():
    frame_inicial.pack_forget()
    frame_busca_salas.pack_forget()
    frame_lanchonetes.pack(fill="both")

def voltar_tela_inicial():
    mostrar_tela_inicial()


######## CONFIG. JANELA ########
janela1 = ttk.Window(themename="solar")
janela1.title("Universitário Ajuda")
janela1.geometry("700x500")
janela1.iconbitmap("images/logo.ico")

######## FRAME TELA INICIAL ########
frame_inicial = ttk.Frame(janela1)
frame_inicial.pack(fill="both")

logo_projeto = PhotoImage(file="images\logo.png").subsample(4, 4)
logo = Label(frame_inicial, image=logo_projeto)
logo.pack(padx=10, pady=10)

texto_inicial = ttk.Label(frame_inicial, text="Seja bem-vindo ao Universitário Ajuda.")
texto_inicial.pack(padx=10, pady=10)
texto_inicial.config(font="Helvetica 15 bold")

texto_inicial1_2 = ttk.Label(frame_inicial, text="Aqui você poderá se localizar dentro do CCT do Campus I da UEPB \nO que você deseja fazer?", justify=CENTER)
texto_inicial1_2.pack(padx=10, pady=10)
texto_inicial1_2.config(font="Helvetica 12 bold", )

botao_encontrar_salas = ttk.Button(frame_inicial, text="Encontrar salas e coordenação", bootstyle=(PRIMARY, OUTLINE), command=abrir_busca_salas)
botao_encontrar_salas.pack(padx=10, pady=10)

botao_lanchonetes = ttk.Button(frame_inicial, text="Lanchonetes", bootstyle=(PRIMARY, OUTLINE), command=abrir_lanchonetes)
botao_lanchonetes.pack(padx=10, pady=10)

######## FRAME BUSCAR SALAS ########
frame_busca_salas = ttk.Frame(janela1)

texto_inicial2 = ttk.Label(frame_busca_salas, text="Digite o número da sala que você deseja ir \nCertifique-se de que você esteja na entrada do CCT.", justify = CENTER)
texto_inicial2.pack(pady=30)
texto_inicial2.config(font="Helvetica 15 bold")

botao_cct = tk.Button(frame_busca_salas, text = "Nao sabe onde é a entrada do CCT? \nClique aqui.", anchor="center", width= 50, command= maps_cct)
botao_cct.config(font="Helvetica 12 bold")
botao_cct.pack(pady=15)

entrada_sala = ttk.Entry(frame_busca_salas, width=30)
entrada_sala.pack(pady=30)

botao_pesquisar = ttk.Button(frame_busca_salas, text="Pesquisar", command= buscar_sala_interface, bootstyle=SECONDARY)
botao_pesquisar.pack(pady=10)

botao_voltar_busca = ttk.Button(frame_busca_salas, text="Voltar", command=voltar_tela_inicial, bootstyle=PRIMARY)
botao_voltar_busca.pack(pady=30)

######## FRAME LANCHONETES ########
frame_lanchonetes = ttk.Frame(janela1)

cantina = PhotoImage(file="images/cantina_cct.png").subsample(2, 2)
label_img = Label(frame_lanchonetes, image=cantina)
label_img.grid(row=0, column=0, padx=10, pady=10)

texto_cantina = ttk.Label(frame_lanchonetes, text="CANTINA DO CCT")
texto_cantina.config(font="Helvetica 15 bold")
texto_cantina.grid(row=0, column=1, sticky="w", padx=10, pady=10)

botao_voltar_lanchonete = ttk.Button(frame_lanchonetes, text="Voltar", command=voltar_tela_inicial, bootstyle=PRIMARY)
botao_voltar_lanchonete.grid(row=2, column=1, padx=10, pady=10)

mostrar_tela_inicial() #chama a função para começar na tela inicial

janela1.mainloop()
