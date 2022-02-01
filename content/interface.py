import tkinter as tk

from tkinter import font



window = tk.Tk()
window.geometry("400x400")

title_font = font.Font(family="Helvetica", size=20, weight=font.BOLD,
                         )
title = tk.Label(window, text="Criar usuário", 
                         font=title_font, width="40", anchor="w", height="2")

start_btn = tk.Button(window, text="Iniciar", width="40")
entry = tk.Entry(window, width="40")
entry.insert(0, 'username')
title.pack(padx=10)
entry.pack(pady=10)
start_btn.pack(padx=10)
window.mainloop()