
import tkinter as tk
from tkinter import messagebox
from main import *
from operacoesbd import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *



def aviso_andamento():
    messagebox.showwarning("Aviso", "EM ANDAMENTO")

def abrir_busca_salas():
    
    texto_inicial.pack_forget()
    texto_inicial1_2.pack_forget()
    botao_encontrar_salas.pack_forget()
    botao_lanchonetes.pack_forget()

    global texto_inicial2, entry, botao_voltar
    texto_inicial2 = ttk.Label(janela1, text= "Digite o número da sala que você deseja ir")
    texto_inicial2.pack(pady = 30)
    texto_inicial2.config(font="Helvetica 15 bold")

    entry = ttk.Entry(janela1, width = 30)
    entry.pack(pady = 30)

    botao_voltar = ttk.Button(janela1, text="Voltar", command= voltar_tela_inicial ,bootstyle = PRIMARY)
    botao_voltar.pack(pady = 30)

def voltar_tela_inicial():
    texto_inicial2.pack_forget()
    entry.pack_forget()
    botao_voltar.pack_forget()

    texto_inicial.pack(pady = 30)
    texto_inicial1_2.pack(pady=30)
    botao_encontrar_salas.pack(padx=10, pady=15)
    botao_lanchonetes.pack(padx=5, pady=10)

janela1 = ttk.Window(themename="solar")
janela1.geometry("500x350")

texto_inicial = ttk.Label(janela1, text= "Seja bem vindo ao Universitário Ajuda.")
texto_inicial.pack(pady = 30)
texto_inicial.config(font="Helvetica 15 bold")

texto_inicial1_2 = ttk.Label(janela1, text="""Aqui você podera se localizar dentro do Campus I da UEPB
                            O que você deseja fazer?""")
texto_inicial1_2.pack(pady=15)
texto_inicial1_2.config(font="Halvetica 12 bold")

botao_encontrar_salas = ttk.Button(janela1, text="Encontrar salas e coordenação", bootstyle=(PRIMARY,OUTLINE), command=abrir_busca_salas)
botao_encontrar_salas.pack(padx=10, pady=15)

botao_lanchonetes = ttk.Button(janela1, text="Lanchonetes", bootstyle=(PRIMARY, OUTLINE), command= aviso_andamento)
botao_lanchonetes.pack(padx=5, pady=10)

janela1.mainloop()
