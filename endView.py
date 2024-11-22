from tkinter import *
from EvolvingRegExGeneratorController import EvolvingRegExGeneratorController

# Initialize the main window
window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.geometry("1366x768")
window.title('RegEx Generator')

# Initialize Controller
controller = EvolvingRegExGeneratorController()

# Global variables
regex_output = "[A-Za-z0-9\\-\\_\\.\\+]{1,64}@[A-Za-z0-9\\-\\_\\.]+\\.[a-zA-Z]+"

# Function to show a specific frame
def show_frame(frame):
    frame.tkraise()

# Function to copy text to clipboard
def copy_to_clipboard(page, output):
    page.clipboard_clear()
    page.clipboard_append(output.cget("text"))
    page.update()

# Create frames dynamically
frames = {}
frame_names = ["mainPage", "davidPage", "jannesPage", "mattiPage", "checkPage"]
for name in frame_names:
    frame = Frame(window)
    frame.grid(row=0, column=0, sticky='nsew')
    frames[name] = frame

show_frame(frames["mainPage"])

# Function to create a canvas for a page
def create_canvas(parent, color, rect_color):
    canvas = Canvas(parent, bg=color, height=768, width=1366, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    canvas.create_rectangle(15.0, 16.0, 890.0, 752.0, fill=rect_color, outline="")
    return canvas

# Function to create navigation buttons
def create_nav_buttons(parent, main_frame):
    Button(parent, text='RegEx Generator', bg='#0184FF', fg='white', command=lambda: show_frame(main_frame)).place(
        x=1055, y=660, width=150, height=30
    )

# Common elements for all sub-pages
def create_subpage_elements(parent, name):
    Label(parent, text=name, anchor='center', background='#0184FF', font=('fixedsys', 20), fg='white').place(
        x=944, y=82, width=375, height=75
    )
    Label(
        parent,
        text=( 
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
            "when an unknown printer took a galley of type and scrambled it to make a type specimen book."
        ),
        wraplength=300,
        justify="left",
        font=("Helvetica", 20),
        anchor=('n'),
        fg='white',
        bg='#1B1C1E'
    ).place(x=944, y=165, width=375, height=465)

# Main page
main_canvas = create_canvas(frames["mainPage"], "black", "#2D3436")
main_canvas.create_text(
    200, 268, anchor="nw", text="RegEx Generator", fill="white", font=("Cooper Black", 64 * -1)
)
Label(frames["mainPage"], text='Choose your model', anchor='center', background='#0184FF', font=('fixedsys', 20), fg='white').place(
    x=115, y=359, width=675, height=100
)

# Main page buttons
buttons = [
    ("KI-Ansatz", "davidPage", 225),
    ("Jannes", "jannesPage", 344),
    ("Matti", "mattiPage", 463),
]
for text, frame, y_pos in buttons:
    Button(frames["mainPage"], text=text, width=50, height=5, anchor='center', bg='#0184FF', fg='white', command=lambda f=frame: show_frame(frames[f])).place(
        x=947, y=y_pos
    )

Button(frames["mainPage"], text='RegEx Check', width=30, height=2, bg='#0056A7', fg='white', command=lambda: show_frame(frames["checkPage"])).place(
    x=345, y=630
)

# Subpages (David, Jannes, Matti)
for name in ["davidPage", "jannesPage", "mattiPage"]:
    page = frames[name]
    canvas = create_canvas(page, "black", "#2D3436")
    
    # Erstellen des Eingabe-Widgets
    text_widget = Text(page, wrap="word", font=("Helvetica", 16), bg="white", fg="black")
    text_widget.place(x=26, y=40, height=450, width=850)

    # Ausgabe-Label
    output_label = Label(page, text=regex_output, anchor='center', background="#2D3436", font=20, fg='white')
    output_label.place(x=25, y=625, width=750, height=75)
    
    # Funktion zur Verarbeitung der Eingabe
    def process_regex():
        # Eingabe aus dem Text-Widget abrufen
        input_text = text_widget.get("1.0", END)  # Gesamte Eingabe abrufen
        print(f"DEBUG: Eingabe vor strip() -> '{input_text}'")  # Debugging der rohen Eingabe
        input_text = input_text.strip()
        print(f"DEBUG: Eingabe nach strip() -> '{input_text}'")  # Debugging nach Entfernen von Leerzeichen

        # Zeilenweise Verarbeitung
        string_list = [line.strip() for line in input_text.split("\n") if line.strip()]  # Leere Zeilen entfernen
        print(f"DEBUG: Verarbeitete Liste -> {string_list}")  # Debugging der Liste

        if not string_list:  # Wenn die Liste leer ist
            output_label.config(text="Bitte geben Sie einen oder mehrere gültige Strings ein!")  # Feedback
            return

        try:
            regex_result = controller.generateRegExFromStringList(string_list)  # Controller aufrufen
            print(f"DEBUG: Ergebnis -> {regex_result}")  # Debugging des Ergebnisses
            output_label.config(text=regex_result)
        except Exception as e:
            print(f"ERROR: {e}")  # Fehler ausgeben
            output_label.config(text="Fehler bei der Verarbeitung!")


    # Button zum Ausführen der Funktion
    Button(page, text='RegEx Check', bg='#0184FF', fg='white', command=process_regex).place(
        x=26, y=515, width=850, height=70
    )

    # Button zum Kopieren der Ausgabe
    Button(page, text='c', command=lambda p=page: copy_to_clipboard(p, output_label)).place(
        x=800, y=635, width=50, height=50
    )
    
    create_nav_buttons(page, frames["mainPage"])
    create_subpage_elements(page, name.split("Page")[0])



# Run the application
window.mainloop()
