from tkinterdnd2 import *
from tkinter import *
from tkinter import ttk
import os

def get_file_name(event):
    file_path = event.data
    file_name = os.path.basename(file_path)
    file_name = file_name.replace('}', '')
    print("Dropped file name:", file_name)

    with open("path" + file_name.replace('}', ''), 'r') as f:
        my_csv_text = f.read()

    # Entire file conversion and edits omitted

    new_csv_path = "path" + file_name
    with open(new_csv_path, 'w') as f:
        f.write(new_csv_str)
    active_tab = notebook.index(notebook.select())
    if active_tab == 0:
        pathLabel_tab1.config(text=file_name + "  SUCCESSFULLY UPDATED")
    elif active_tab == 1:
        pathLabel_tab2.config(text=file_name + "  SUCCESSFULLY UPDATED")


def process_input():
    input_text = entryWidget_tab2.get("1.0", "end").strip()
    lines = input_text.split("\n")
    my_dict = {}
    for line in lines:
        if line:
            parts = line.split(" : ")
            if len(parts) == 2:
                key, value = parts
                my_dict[key.strip()] = value.strip()
    print("Converted:", my_dict)

    user_link = entryWidget_tab2_2.get("1.0", "end").strip()
    print("User Link:", user_link)
    entryWidget_tab2.delete("1.0", "end")
    entryWidget_tab2_2.delete("1.0", "end")


root = TkinterDnD.Tk()
root.geometry("500x300")
root.title("File Fix")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

tab1_frame = ttk.Frame(notebook)
tab2_frame = ttk.Frame(notebook)

notebook.add(tab1_frame, text="File Fix")
notebook.add(tab2_frame, text="Confirm")

entryWidget_tab1 = Text(tab1_frame, height=10)
entryWidget_tab1.pack(side=TOP, padx=50, pady=50)

entryWidget_tab2 = Text(tab2_frame, height=5)
entryWidget_tab2.pack(side=TOP, padx=50, pady=10)

entryWidget_tab2_2 = Text(tab2_frame, height=5)
entryWidget_tab2_2.pack(side=TOP, padx=50, pady=10)

pathLabel_tab1 = Label(tab1_frame, text="Drag and drop file in Tab 1")
root.mainloop()
