from tkinter import *

# Initialize the main window
window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.geometry("1366x768")
window.title('RegEx Generator')

# Function to show a specific frame
def show_frame(frame):
    frame.tkraise()

# Function to generate output
def generate_output(entries, output_label, frame_name):
    inputs = [entry.get() for entry in entries]  # Get values from all entry fields
    non_empty_inputs = [text for text in inputs if text.strip()]  # Filter out empty strings
    result = " by ".join(non_empty_inputs) if non_empty_inputs else "Hello"  # Concatenate or default to "Hello"
    output_label.config(text=result)
    # Log details in the terminal
    print(f"Entry Fields: {entries}")
    print(f"Frame: {frame_name}")
    print(f"Inputs: {inputs}")
    print(f"Output: {result}")

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
    entries = [Entry(page) for _ in range(5)]
    for i, entry in enumerate(entries):
        entry.place(x=26, y=40 + i * 90, height=75, width=850)
    output_label = Label(page, text="", anchor='center', background="#2D3436", font=20, fg='white')
    output_label.place(x=25, y=625, width=750, height=75)
    Button(
        page, text='Generate Output', bg='#0184FF', fg='white',
        command=lambda e=entries, o=output_label, f=name: generate_output(e, o, f)
    ).place(x=26, y=515, width=850, height=70)
    create_nav_buttons(page, frames["mainPage"])
    create_subpage_elements(page, name.split("Page")[0])

# Check page
check_canvas = create_canvas(frames["checkPage"], "black", "#0184FF")
entries_check = [Entry(frames["checkPage"]) for _ in range(5)]
for i, entry in enumerate(entries_check):
    entry.place(x=26, y=40 + i * 60, height=50, width=850)
output_label_check = Label(frames["checkPage"], text="", anchor='center', background="#2D3436", font=20, fg='white')
output_label_check.place(x=25, y=625, width=750, height=75)
Button(
    frames["checkPage"], text='Generate Output', bg='#555A5E', fg='white',
    command=lambda e=entries_check, o=output_label_check, f="checkPage": generate_output(e, o, f)
).place(x=219, y=645)
create_nav_buttons(frames["checkPage"], frames["mainPage"])
create_subpage_elements(frames["checkPage"], "Funktion")

# Run the application
window.mainloop()
