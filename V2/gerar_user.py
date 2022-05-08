import tkinter as tk

from tkinter import font
from automate import initialize


window = tk.Tk()
window.geometry("300x400")


# Titulo Criar usuario
title_font = font.Font(family="Helvetica", size=20, weight=font.BOLD,)
title = tk.Label(window, text="Criar usuário", 
                         font=title_font, width="40", anchor="w", height="2")



# Label Quantidade de usuario
qnt_placeholder = tk.Label(window, text="Digite a quantidade de usuário", 
                          width="40", anchor="w")
qnt_entry = tk.Entry(window, width="40", justify="left")

# Label Numero inicial de user
starter_placeholder = tk.Label(window, text="Digite o número do usuário inicial", 
                          width="40", anchor="w")
starter_entry = tk.Entry(window, width="40", justify="left")

#Iniciar
start_btn = tk.Button(window, text="Iniciar", width="40")
imprimir_banheiro = tk.Button(window, text="Imprimir Banheiro", width="40")



#Imprimir

imprimir = tk.Button(window, text="Imprimir", width="40")


title.pack(padx=10)
qnt_placeholder.pack()
qnt_entry.pack()

starter_placeholder.pack()
starter_entry.pack()

start_btn.pack(padx=10, pady=20)
imprimir_banheiro.pack()
imprimir.pack(padx=10)


def handle_click(event):
    print(qnt_entry.get())

    initialize(qnt_entry.get(), starter_entry.get(),0 )


def handle_click_banho(event):
    initialize(qnt_entry.get(), starter_entry.get(), 1)
    pass


imprimir_banheiro.bind("<Button-1>", handle_click_banho)


start_btn.bind("<Button-1>", handle_click)
window.mainloop()