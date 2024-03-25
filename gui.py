from pathlib import Path
from tkinter import StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()

window.geometry("294x320")
window.configure(bg = "#FFFFFF")



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
    text="Data da despesa",
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
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=211.0,
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
    command=lambda: print(checkbox2_var.get()),
    relief="flat"
)
button_2.place(
    x=131.0,
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

