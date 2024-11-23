from EvolvingRegExGen.EvolvingRegExGeneratorController import EvolvingRegExGeneratorController
from LLMRegExGen.LLMRegExGeneratorController import LLMRegExGeneratorController
from ParallelRegExGen.parallelController import ParallelController
from CheckRegExController import CheckRegExController
from tkinter import *

evolvingRegExGenController: EvolvingRegExGeneratorController = EvolvingRegExGeneratorController()
llmRegExGeneratorController: LLMRegExGeneratorController= LLMRegExGeneratorController()
checkRegExController: CheckRegExController = CheckRegExController()
parallelController: ParallelController = ParallelController()

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
    global current_frame
    current_frame = frame  
    frame.tkraise()
    
show_frame(mainPage)
current_frame = None

#-------- colors and fonts --------
label_font = ("fixedsys", 16, "bold")
higlight_blue = '#0184FF'
frame_background = '#050A37'
secondary_background = '#063A6B'
#----------------------------------

copy_image = PhotoImage(file='copy_button.png')
copy_image_label = Label(image=copy_image)
instruction_text="Enter your string input(s). You may provide multiple strings. \nIf the inputs share a common pattern, a regular expression (regex) \nwill be generated when you press the 'Generate' button"
results = ['hallo@gmail.com']
checkPage_input = []
checkPage_input_regex: str
regex_output = ''

def get_text_and_source():
    global current_frame, regex_output
    if current_frame == davidPage:
        text = davidPage_textfield.get("1.0", "end-1c").strip()
        results = text.splitlines()
        test = llmRegExGeneratorController.generateRegExFromStringList(results)
        regex_output = test
        davidPage_output.configure(text=regex_output)
        print("Frame: DavidPage")
        print("Output: "+test+"                                "+regex_output)
        print("Button: RegEx Check (DavidPage)")
    elif current_frame == jannesPage:
        text = jannesPage_textfield.get("1.0", "end-1c").strip()
        results = text.splitlines()
        test = evolvingRegExGenController.generateRegExFromStringList(results)
        regex_output = test
        jannesPage_output.configure(text=regex_output)
        print("Frame: JannesPage")
        print("Output: "+test+".."+regex_output)
        print("Button: RegEx Check (JannesPage)")
    elif current_frame == mattiPage:
        text = mattiPage_textfield.get("1.0", "end-1c").strip()
        results = text.splitlines()
        test = parallelController.generate_regex_from_strings(results)
        regex_output = test
        mattiPage_output.configure(text=regex_output)
        print("Frame: MattiPage")
        print("Output: "+" "+regex_output)
        print("Button: RegEx Check (MattiPage)")
    
    else:
        print("Kein unterstützter Frame aktiv.")
        return

    print("Results (Liste von Strings):", results)

def get_text_from_checkpage():
    global checkPage_input,checkPage_input_regex
    text = checkPage_textfield_one.get("1.0", "end-1c").strip()
    checkPage_input = text.splitlines()
    checkPage_input_regex = checkPage_textfield_two.get("1.0",'end-1c')
    print(checkPage_input)
    print(checkPage_input_regex +' \n\n')
    
    info = checkRegExController.check_for_match(checkPage_input_regex,checkPage_input)
    if info == False:
        checkPage_checkButton.configure(bg='#D85456',fg='white')
    else:
        checkPage_checkButton.configure(bg='#7AB495',fg='white')

def copy_to_clipboard(page, output):
    page.clipboard_clear()
    page.clipboard_append(output.cget("text"))
    page.update()

def create_text_widget(parent, instruction, x, y, height, width):
    text_widget = tk.Text(parent, wrap=WORD, font=("Helvetica", 14), fg="grey")
    text_widget.place(x=x, y=y, height=height, width=width)
    text_widget.insert("1.0", instruction)
    
    # Event handler to clear preset text on the first click
    def clear_text_on_click(event):
        if text_widget.get("1.0", "end-1c") == instruction:  # Check if it's the preset text
            text_widget.delete("1.0", "end")  # Clear the widget
            text_widget.config(fg="black")  # Change text color to black for user input
            text_widget.unbind("<Button-1>")  # Unbind the event after first click

    text_widget.bind("<Button-1>", clear_text_on_click)  # Bind the left mouse click event
    return text_widget


#-----------menu page ----------------

mainPage_canvas = Canvas( mainPage,bg = frame_background,height = 768,width = 1366,bd = 0,highlightthickness = 0,relief = "ridge")
mainPage_canvas.place(x = 0, y = 0)
mainPage_canvas.create_rectangle(15.0,16.0,890.0,752.0,fill=secondary_background,outline="")
mainPage_canvas.create_text(175,300,anchor="nw",text="RegEx Generator",fill="white",font=("Cooper Black", 64 * -1))

mainPage_choose = Label(mainPage,text='Choose your model',anchor='center',background=higlight_blue,font=('fixedsys',20),fg='white')
mainPage_choose.place(x=115,y=380,width=675,height=100)

mainPage_davidButton= Button(mainPage,text='KI-Ansatz',font=label_font,bg=higlight_blue,fg='white',command=lambda: show_frame(davidPage))
mainPage_davidButton.place(x=947, y=175, width=360, height=80)
mainPage_jannesButton= Button(mainPage,text='Jannes',width=50,font=label_font,height=5,bg=higlight_blue,fg='white',command=lambda: show_frame(jannesPage))
mainPage_jannesButton.place(x=947,y=294, width=360, height=80)
mainPage_mattiButton= Button(mainPage,text='Matti',width=50,height=5,font=label_font,bg=higlight_blue,fg='white',command=lambda: show_frame(mattiPage))
mainPage_mattiButton.place(x=947,y=413, width=360, height=80)

mainPage_checkButton= Button(mainPage, text='RegEx Check',width=30,height=2,bg='#0056A7',fg='white',font='fixedsys',command=lambda: show_frame(checkPage))
mainPage_checkButton.place(x=1000,y=580)

#-----------david page ----------------

davidPage_canvas = Canvas(davidPage,bg = frame_background,height = 768,width = 1366,bd = 0,highlightthickness = 0,relief = "ridge")
davidPage_canvas.place(x = 0, y = 0)
davidPage_canvas.create_rectangle(15.0,16.0,890.0,752.0,fill=secondary_background,outline="")

davidPage_textfield = Text(davidPage, wrap=WORD, font=("Helvetica", 14))
davidPage_textfield.place(x=26, y=40, height=470, width=850)
davidPage_textfield.insert('1.0',preset_text)
davidPage_textfield.bind("<Button-1>",clear_text_on_focus)

davidPage_generateButton= Button(davidPage, text='Generate',bg=higlight_blue,fg='white',font=label_font,command=get_text_and_source)
davidPage_generateButton.place(x=26,y=515,width=850,height=70)

davidPage_output= Label(davidPage,text=regex_output,anchor='center',background=secondary_background,font=20,fg='white')
davidPage_output.place(x=25,y=625,width=750,height=75)

davidPage_copy= Button(davidPage,text='c',image = copy_image,command= lambda:copy_to_clipboard(davidPage,davidPage_output), borderwidth=0)
davidPage_copy.place(x=800,y=635,width=50,height=50)

davidPage_menuButton = Button(davidPage,text='RegEx Generator',background=higlight_blue,fg='white',command=lambda: show_frame(mainPage))
davidPage_menuButton.place(x=1055,y=660,width=150,height=30)

davidPage_model= Label(davidPage,text='KI-Ansatz',anchor='center',background=higlight_blue,font=('fixedsys',20),fg='white')
davidPage_model.place(x=944,y=82,width=375,height=75)

davidPage_loremlabel = Label(davidPage,wraplength=300,  justify="left", font=("Helvetica", 20 ), anchor=('n'),fg='white',bg=secondary_background, 
    text=(
        'This approach utilizes the Gemini API to send a request to the large language model "Gemini-1.5-pro." Its goal is to derive a valid regular expression based on the provided input.'
    )
)
davidPage_loremlabel.place(x=944,y=165,width=375,height=465)

#-----------jannes page ----------------

jannesPage_canvas = Canvas(jannesPage,bg = frame_background,height = 768,width = 1366,bd = 0,highlightthickness = 0,relief = "ridge")
jannesPage_canvas.place(x = 0, y = 0)
jannesPage_canvas.create_rectangle(15.0,16.0,890.0,752.0,fill=secondary_background,outline="")

jannesPage_textfield = Text(jannesPage, wrap=WORD, font=("Helvetica", 14))
jannesPage_textfield.place(x=26, y=40, height=470, width=850)
jannesPage_textfield.insert('1.0',preset_text)
jannesPage_textfield.bind("<Button-1>",clear_text_on_focus)

jannesPage_generateButton= Button(jannesPage, text='Generate',bg=higlight_blue,fg='white',font=label_font,command=get_text_and_source)
jannesPage_generateButton.place(x=26,y=515,width=850,height=70)

jannesPage_output= Label(jannesPage,text=regex_output,anchor='center',background=secondary_background,font=20,fg='white')
jannesPage_output.place(x=25,y=625,width=750,height=75)

jannesPage_copy= Button(jannesPage,text='c',image = copy_image,borderwidth=0,command=lambda: copy_to_clipboard(jannesPage,jannesPage_output))
jannesPage_copy.place(x=800,y=635,width=50,height=50)

jannesPage_menuButton = Button(jannesPage,text='RegEx Generator',background=higlight_blue,fg='white',command=lambda: show_frame(mainPage))
jannesPage_menuButton.place(x=1055,y=660,width=150,height=30)

jannesPage_model= Label(jannesPage,text='Jannes',anchor='center',background=higlight_blue,font=('fixedsys',20),fg='white')
jannesPage_model.place(x=944,y=82,width=375,height=75)

jannesPage_loremlabel = Label(jannesPage,wraplength=300,  justify="left", font=("Helvetica", 20 ), anchor=('n'),fg='white',bg=secondary_background, 
    text=(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
    )

)
jannesPage_loremlabel.place(x=944,y=165,width=375,height=465)

#-----------matti page ----------------

mattiPage_canvas = Canvas(mattiPage,bg = frame_background,height = 768,width = 1366,bd = 0,highlightthickness = 0,relief = "ridge")
mattiPage_canvas.place(x = 0, y = 0)
mattiPage_canvas.create_rectangle(15.0,16.0,890.0,752.0,fill=secondary_background,outline="")

mattiPage_textfield = Text(mattiPage, wrap=WORD, font=("Helvetica", 14))
mattiPage_textfield.place(x=26, y=40, height=470, width=850)
mattiPage_textfield.insert('1.0',preset_text)
mattiPage_textfield.bind("<Button-1>",clear_text_on_focus)

mattiPage_generateButton= Button(mattiPage, text='Generate',bg=higlight_blue,fg='white',font=label_font,command=get_text_and_source)
mattiPage_generateButton.place(x=26,y=515,width=850,height=70)

mattiPage_output= Label(mattiPage,text=regex_output,anchor='center',background=secondary_background,font=20,fg='white')
mattiPage_output.place(x=25,y=625,width=750,height=75)

mattiPage_copy= Button(mattiPage,text='c',image = copy_image,borderwidth=0,command=lambda: copy_to_clipboard(jannesPage,jannesPage_output))
mattiPage_copy.place(x=800,y=635,width=50,height=50)


mattiPage_menuButton = Button(mattiPage,text='RegEx Generator',background=higlight_blue,fg='white',command=lambda: show_frame(mainPage))
mattiPage_menuButton.place(x=1055,y=660,width=150,height=30)

mattiPage_model= Label(mattiPage,text='Matti',anchor='center',background=higlight_blue,font=('fixedsys',20),fg='white')
mattiPage_model.place(x=944,y=82,width=375,height=75)

mattiPage_loremlabel = Label(mattiPage,wraplength=300,  justify="left", font=("Helvetica", 20 ), anchor=('n'),fg='white',bg=secondary_background, 
    text=(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
    )
)
mattiPage_loremlabel.place(x=944,y=165,width=375,height=465)

#-----------check page ----------------

checkPage_canvas = Canvas(checkPage,bg = frame_background,height = 768,width = 1366,bd = 0,highlightthickness = 0,relief = "ridge")
checkPage_canvas.place(x = 0, y = 0)
checkPage_canvas.create_rectangle(15.0,16.0,890.0,752.0,fill=secondary_background,outline="")

checkPage_textfield_one = Text(checkPage,font=25,wrap=WORD)
checkPage_textfield_one.place(x=26,y=40,height=275,width=850)
checkPage_textfield_two = Text(checkPage,font=25,wrap=WORD)
checkPage_textfield_two.place(x=26,y=320,height=275,width=850)

checkPage_checkButton= Button(checkPage, text='RegEx Check',bg='#555A5E',fg='white',font=label_font,command=get_text_from_checkpage)
checkPage_checkButton.place(x=219,width=455,height=80,y=645)

checkPage_menuButton = Button(checkPage,text='RegEx Generator',background=higlight_blue,fg='white',command=lambda: show_frame(mainPage))
checkPage_menuButton.place(x=1055,y=660,width=150,height=30)

checkPage_model= Label(checkPage,text='Funktion',anchor='center',background=higlight_blue,font=('fixedsys',20),fg='white')
checkPage_model.place(x=944,y=82,width=375,height=75)

checkPage_loremlabel = Label(checkPage,wraplength=300,  justify="left", font=("Helvetica", 20 ), anchor=('n'),fg='white',bg=secondary_background, 
    text=(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
    )
)
checkPage_loremlabel.place(x=944,y=165,width=375,height=465)

window.mainloop()