import tkinter as tk

from tkinter import font
from automate import initialize


window = tk.Tk()
window.geometry("300x400")

title_font = font.Font(family="Helvetica", size=20, weight=font.BOLD,
                         )
title = tk.Label(window, text="Criar usuário", 
                         font=title_font, width="40", anchor="w", height="2")


qnt_placeholder = tk.Label(window, text="Digite a quantidade de usuário", 
                          width="40", anchor="w")
qnt_entry = tk.Entry(window, width="40", justify="left")


starter_placeholder = tk.Label(window, text="Digite o número do usuário inicial", 
                          width="40", anchor="w")
starter_entry = tk.Entry(window, width="40", justify="left")


start_btn = tk.Button(window, text="Iniciar", width="40")


imprimir = tk.Button(window, text="Imprimir", width="40")


status_text = tk.Label(window, text="status", 
                          width="40", anchor="w")

title.pack(padx=10)
qnt_placeholder.pack()
qnt_entry.pack()

starter_placeholder.pack()
starter_entry.pack()

start_btn.pack(padx=10, pady=20)
imprimir.pack(padx=10)
status_text.pack()


def handle_click(event):
    print(qnt_entry.get())

    initialize(qnt_entry.get(), starter_entry.get())


start_btn.bind("<Button-1>", handle_click)

window.mainloop()