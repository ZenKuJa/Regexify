from tkinter import *

window = Tk() 
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
window.geometry("1366x768")
window.title('RegEx Generator')

mainPage= Frame(window)
davidPage=Frame(window)
jannesPage=Frame(window)
mattiPage=Frame(window)
checkPage=Frame(window)

for frame in (mainPage,davidPage,jannesPage,mattiPage,checkPage):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(mainPage)

regex_output= "[A-Za-z0-9\-\_\.\+]{1,64}@[A-Za-z0-9\-\_\.]+\.[a-zA-Z]+"

def copy_to_clipboard(page,output):
    page.clipboard_clear()
    page.clipboard_append(output.cget("text"))
    page.update()  

#-----------menu page ----------------

mainPage_canvas = Canvas(
    mainPage,
    bg = "black",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
mainPage_canvas.place(x = 0, y = 0)
mainPage_canvas.create_rectangle(
    15.0,
    16.0,
    890.0,
    752.0,
    fill="#2D3436",
    outline="")

mainPage_canvas.create_text(
    200,
    268,
    anchor="nw",
    text="RegEx Generator",
    fill="white",
    font=("Cooper Black", 64 * -1)
)

mainPage_choose = Label(mainPage,text='Choose your model',anchor='center',background='#0184FF',font=('fixedsys',20),fg='white')
mainPage_choose.place(x=115,y=359,width=675,height=100)

mainPage_davidButton= Button(mainPage,text='KI-Ansatz',width=50,height=5,anchor='center',bg='#0184FF',fg='white',command=lambda: show_frame(davidPage))
mainPage_davidButton.place(x=947,y=225)
mainPage_jannesButton= Button(mainPage,text='Jannes',width=50,height=5,bg='#0184FF',fg='white',command=lambda: show_frame(jannesPage))
mainPage_jannesButton.place(x=947,y=344)
mainPage_mattiButton= Button(mainPage,text='Matti',width=50,height=5,bg='#0184FF',fg='white',command=lambda: show_frame(mattiPage))
mainPage_mattiButton.place(x=947,y=463)

mainPage_checkButton= Button(mainPage, text='RegEx Check',width=30,height=2,bg='#0056A7',fg='white',command=lambda: show_frame(checkPage))
mainPage_checkButton.place(x=345,y=630)

#-----------david page ----------------

davidPage_canvas = Canvas(
    davidPage,
    bg = "black",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
davidPage_canvas.place(x = 0, y = 0)
davidPage_canvas.create_rectangle(
    15.0,
    16.0,
    890.0,
    752.0,
    fill="#2D3436",
    outline="")

davidPage_textfield = Text(davidPage, wrap=WORD, font=("Helvetica", 14))
davidPage_textfield.place(x=26, y=40, height=435, width=850)

davidPage_generateButton= Button(davidPage, text='RegEx Check',bg='#0184FF',fg='white')
davidPage_generateButton.place(x=26,y=515,width=850,height=70)

davidPage_output= Label(davidPage,text=regex_output,anchor='center',background="#2D3436",font=20,fg='white')
davidPage_output.place(x=25,y=625,width=750,height=75)

davidPage_copy= Button(davidPage,text='c',command=copy_to_clipboard(davidPage,davidPage_output))
davidPage_copy.place(x=800,y=635,width=50,height=50)

davidPage_menuButton = Button(davidPage,text='RegEx Generator',background='#0184FF',fg='white',command=lambda: show_frame(mainPage))
davidPage_menuButton.place(x=1055,y=660,width=150,height=30)

davidPage_model= Label(davidPage,text='KI-Ansatz',anchor='center',background='#0184FF',font=('fixedsys',20),fg='white')
davidPage_model.place(x=944,y=82,width=375,height=75)

davidPage_loremlabel = Label(
    davidPage, 
    text=(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
        "when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    ),
    wraplength=300,  
    justify="left", 
    font=("Helvetica", 20 ), anchor=('n'),
    fg='white',
    bg='#1B1C1E'
)
davidPage_loremlabel.place(x=944,y=165,width=375,height=465)

#-----------jannes page ----------------

jannesPage_canvas = Canvas(
    jannesPage,
    bg = "black",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
jannesPage_canvas.place(x = 0, y = 0)
jannesPage_canvas.create_rectangle(
    15.0,
    16.0,
    890.0,
    752.0,
    fill="#2D3436",
    outline="")

jannesPage_textfield_one = Entry(jannesPage)
jannesPage_textfield_one.place(x=26,y=40,height=75,width=850)
jannesPage_textfield_two = Entry(jannesPage)
jannesPage_textfield_two.place(x=26,y=130,height=75,width=850)
jannesPage_textfield_three = Entry(jannesPage)
jannesPage_textfield_three.place(x=26,y=220,height=75,width=850)
jannesPage_textfield_four = Entry(jannesPage)
jannesPage_textfield_four.place(x=26,y=310,height=75,width=850)
jannesPage_textfield_five = Entry(jannesPage)
jannesPage_textfield_five.place(x=26,y=400,height=75,width=850)

jannesPage_generateButton= Button(jannesPage, text='RegEx Check',bg='#0184FF',fg='white')
jannesPage_generateButton.place(x=26,y=515,width=850,height=70)

jannesPage_output= Label(jannesPage,text=regex_output,anchor='center',background="#2D3436",font=20,fg='white')
jannesPage_output.place(x=25,y=625,width=750,height=75)

jannesPage_copy= Button(jannesPage,text='c',command=copy_to_clipboard(jannesPage,jannesPage_output))
jannesPage_copy.place(x=800,y=635,width=50,height=50)

jannesPage_menuButton = Button(jannesPage,text='RegEx Generator',background='#0184FF',fg='white',command=lambda: show_frame(mainPage))
jannesPage_menuButton.place(x=1055,y=660,width=150,height=30)

jannesPage_model= Label(jannesPage,text='Jannes',anchor='center',background='#0184FF',font=('fixedsys',20),fg='white')
jannesPage_model.place(x=944,y=82,width=375,height=75)

jannesPage_loremlabel = Label(
    jannesPage, 
    text=(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
        "when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    ),
    wraplength=300,  
    justify="left", 
    font=("Helvetica", 20 ), anchor=('n'),
    fg='white',
    bg='#1B1C1E'

)
jannesPage_loremlabel.place(x=944,y=165,width=375,height=465)

#-----------matti page ----------------

mattiPage_canvas = Canvas(
    mattiPage,
    bg = "black",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
mattiPage_canvas.place(x = 0, y = 0)
mattiPage_canvas.create_rectangle(
    15.0,
    16.0,
    890.0,
    752.0,
    fill="#2D3436",
    outline="")

mattiPage_textfield_one = Entry(mattiPage)
mattiPage_textfield_one.place(x=26,y=40,height=75,width=850)
mattiPage_textfield_two = Entry(mattiPage)
mattiPage_textfield_two.place(x=26,y=130,height=75,width=850)
mattiPage_textfield_three = Entry(mattiPage)
mattiPage_textfield_three.place(x=26,y=220,height=75,width=850)
mattiPage_textfield_four = Entry(mattiPage)
mattiPage_textfield_four.place(x=26,y=310,height=75,width=850)
mattiPage_textfield_five = Entry(mattiPage)
mattiPage_textfield_five.place(x=26,y=400,height=75,width=850)

mattiPage_generateButton= Button(mattiPage, text='RegEx Check',bg='#0184FF',fg='white')
mattiPage_generateButton.place(x=26,y=515,width=850,height=70)

mattiPage_output= Label(davidPage,text=regex_output,anchor='center',background="#2D3436",font=20,fg='white')
mattiPage_output.place(x=25,y=625,width=750,height=75)

mattiPage_copy= Button(mattiPage,text='c',command=copy_to_clipboard(jannesPage,jannesPage_output))
mattiPage_copy.place(x=800,y=635,width=50,height=50)


mattiPage_menuButton = Button(mattiPage,text='RegEx Generator',background='#0184FF',fg='white',command=lambda: show_frame(mainPage))
mattiPage_menuButton.place(x=1055,y=660,width=150,height=30)

mattiPage_model= Label(mattiPage,text='Matti',anchor='center',background='#0184FF',font=('fixedsys',20),fg='white')
mattiPage_model.place(x=944,y=82,width=375,height=75)

mattiPage_loremlabel = Label(
    mattiPage, 
    text=(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
        "when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    ),
    wraplength=300,  
    justify="left", 
    font=("Helvetica", 20 ), anchor=('n'),
    fg='white',
    bg='#1B1C1E'
)
mattiPage_loremlabel.place(x=944,y=165,width=375,height=465)

#-----------check page ----------------

checkPage_canvas = Canvas(
    checkPage,
    bg = "black",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
checkPage_canvas.place(x = 0, y = 0)
checkPage_canvas.create_rectangle(
    15.0,
    16.0,
    890.0,
    752.0,
    fill="#0184FF",
    outline="")

checkPage_textfield_one = Entry(checkPage)
checkPage_textfield_one.place(x=26,y=40,height=275,width=850)
checkPage_textfield_two = Entry(checkPage)
checkPage_textfield_two.place(x=26,y=320,height=275,width=850)

checkPage_checkButton= Button(checkPage, text='RegEx Check',width=65,height=4,bg='#555A5E',fg='white')
checkPage_checkButton.place(x=219,y=645)

checkPage_menuButton = Button(checkPage,text='RegEx Generator',background='#0184FF',fg='white',command=lambda: show_frame(mainPage))
checkPage_menuButton.place(x=1055,y=660,width=150,height=30)

checkPage_model= Label(checkPage,text='Funktion',anchor='center',background='#0184FF',font=('fixedsys',20),fg='white')
checkPage_model.place(x=944,y=82,width=375,height=75)

checkPage_loremlabel = Label(
    checkPage, 
    text=(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
        "when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    ),
    wraplength=300,  
    justify="left", 
    font=("Helvetica", 20 ), anchor=('n'),
    fg='white',
    bg='#1B1C1E'
)
checkPage_loremlabel.place(x=944,y=165,width=375,height=465)


window.mainloop()


