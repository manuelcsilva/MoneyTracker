
from tkinter import StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, messagebox, filedialog, Menu

window = Tk()

window.geometry("294x320")
window.configure(bg = "#FFFFFF")
window.title("MoneyTracker")

menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Novo", command=lambda: print("Novo arquivo"))
filemenu.add_command(label="Abrir", command=lambda: print("Abrir arquivo"))
filemenu.add_command(label="Salvar", command=lambda: print("Salvar arquivo"))
filemenu.add_separator()
filemenu.add_command(label="Sair", command=window.quit)

menubar.add_cascade(label="Ficheiro", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Desfazer", command=lambda: print("Desfazer"))
editmenu.add_command(label="Refazer", command=lambda: print("Refazer"))
editmenu.add_separator()
editmenu.add_command(label="Cortar", command=lambda: print("Cortar"))
editmenu.add_command(label="Copiar", command=lambda: print("Copiar"))
editmenu.add_command(label="Colar", command=lambda: print("Colar"))

menubar.add_cascade(label="Editar", menu=editmenu)

viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label="Zoom In", command=lambda: print("Zoom In"))
viewmenu.add_command(label="Zoom Out", command=lambda: print("Zoom Out"))

menubar.add_cascade(label="Ver", menu=viewmenu)

window.resizable(True, True)
window.mainloop()