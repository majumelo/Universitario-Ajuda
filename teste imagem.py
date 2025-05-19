from tkinter import *

janela = Tk()

img = PhotoImage(file="images/cantina_cct.png")

label_img = Label(janela, image = img).pack()

janela.mainloop()