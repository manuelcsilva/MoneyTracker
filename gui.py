from pathlib import Path
from tkinter import StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, messagebox, filedialog, Menu
import openpyxl


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

# Load Excel File (.xlsx)
wb = openpyxl.load_workbook('exportmodel.xlsx')
main = wb.active

# Variaveis globais
tipo = ''
linha = ''


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def novo():
    global tipo, linha, currency_style, checkbox_var, checkbox2_var
    print(checkbox_var.get(), checkbox2_var.get())
    if checkbox_var.get() == '1' and checkbox2_var.get() == '0':
        tipo = 'Receita'
    elif checkbox_var.get() == '0' and checkbox2_var.get() == '1':
        tipo = 'Despesa'
    else:
        messagebox.showwarning('Tipo', 'Tipo invalido (Receita ou Despesa?)')
        return
    linha = main[f'F2'].value
    main[f'F2'] = linha + 1
    print('Linha:',linha)
    main[f'A{linha}'] = entry_1.get()
    print(entry_1.get())
    main[f'B{linha}'] = entry_2.get()
    print(entry_2.get())
    main[f'C{linha}'] = entry_4.get("1.0", "end-1c")
    print(entry_4.get("1.0", "end-1c"))
    if tipo == 'Despesa':
        main[f'D{linha}'] = float(entry_3.get())
        main[f'D{linha}'].number_format = '#,##0.00 €' 
        print(entry_3.get())
    elif tipo == 'Receita':
        main[f'E{linha}'] = float(entry_3.get())
        main[f'E{linha}'].number_format = '#,##0.00 €' 
        print(entry_3.get())
    entry_1.delete(0, 2)
    entry_2.delete(0, 40)
    entry_3.delete(0, 40)
    entry_4.delete("1.0", "end")

def salvar():
    global linha
    filename = filedialog.asksaveasfilename(title = "Select a File", 
                                          filetypes = (("Excel", 
                                                        "*.xlsx*"), 
                                                       ("all files", 
                                                        "*.*")),defaultextension='.xlsx')
    print(filename)
    wb.save(filename)
    print(f'Gurdado no ficheiro "{filename}".')
    messagebox.showinfo('Guardado', f'Gurdado em {filename}')

def load():
    global wb, main
    filename = filedialog.askopenfilename(title = "Select a File", 
                                          filetypes = (("Excel", 
                                                        "*.xlsx*"), 
                                                       ("all files", 
                                                        "*.*")),defaultextension='.xlsx')
    wb = openpyxl.load_workbook(filename)
    main = wb.active
    print(main[f'F2'].value)
    print(filename)
    


window = Tk()

window.geometry("294x320")
window.configure(bg = "#FFFFFF")
window.title("MoneyTracker")
window.call("wm", "iconphoto", window._w, PhotoImage(file=relative_to_assets("icon.png")))


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 320,
    width = 294,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    294.0,
    72.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    75.0,
    27.0,
    anchor="nw",
    text="MoneyTracker",
    fill="#000000",
    font=("JetBrains Mono", 20 * -1)
)

canvas.create_text(
    21.0,
    97.0,
    anchor="nw",
    text="Dia (DD/MM/AAAA)",
    fill="#000000",
    font=("JetBrains Mono", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    219.0,
    105.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=169.0,
    y=97.0,
    width=100.0,
    height=14.0
)

canvas.create_text(
    21.0,
    127.0,
    anchor="nw",
    text="Despesa",
    fill="#000000",
    font=("JetBrains Mono", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    204.0,
    135.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=139.0,
    y=127.0,
    width=130.0,
    height=14.0
)

canvas.create_text(
    21.0,
    207.0,
    anchor="nw",
    text="Valor",
    fill="#000000",
    font=("JetBrains Mono", 12 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    204.0,
    215.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=139.0,
    y=207.0,
    width=130.0,
    height=14.0
)

canvas.create_text(
    21.0,
    157.0,
    anchor="nw",
    text="Descrição",
    fill="#000000",
    font=("JetBrains Mono", 12 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    204.0,
    175.0,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=141.0,
    y=157.0,
    width=126.0,
    height=34.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: novo(),
    relief="flat",
    background='#FFFFFF'
)
button_1.place(
    x=194.0,
    y=267.0,
    width=66.0,
    height=36.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: salvar(),
    relief="flat",
    background='#FFFFFF'
)
button_2.place(
    x=114.0,
    y=267.0,
    width=66.0,
    height=36.0
)
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: load(),
    relief="flat",
    background='#FFFFFF'
)
button_3.place(
    x=34.0,
    y=267.0,
    width=66.0,
    height=36.0
)

checkbox_var = StringVar()
checkbox_var = StringVar(value='0')

checkbox = Checkbutton(window,
                text='Receita',
                variable=checkbox_var,                
                onvalue='1',
                offvalue='0',
                bg='#FFFFFF', font=("JetBrains Mono", 12 * -1))
checkbox.place(x=38,y=238)

checkbox2_var = StringVar()
checkbox2_var = StringVar(value=0)  

checkbox2 = Checkbutton(window,
                text='Despesa',
                variable=checkbox2_var,
                onvalue='1',
                offvalue='0',
                bg='#FFFFFF', font=("JetBrains Mono", 12 * -1))
checkbox2.place(x=159,y=238)


window.resizable(False, False)
window.mainloop()

