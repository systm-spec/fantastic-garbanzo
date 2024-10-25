import customtkinter as ctk
import os

ctk.set_appearance_mode("dark")
app = ctk.CTk()

app.geometry("1000x720")
app.grid_columnconfigure(0, weight=1)
app.configure(padx=20, pady=20)
app.grid_columnconfigure(1, weight=5)


class_frame = ctk.CTkFrame(master=app, border_width=1, border_color="white")

class_frame.grid(row=0, column=1, sticky="EW")


assets_path = "assets"
def load_assets(path):
    # Auflistung der Files in Dir:
    content = os.listdir(assets_path)
    column_counter = 0
    row_counter = 0
    # Iteration der Dateien und Generierung Button
    for liste in content:
        box = ctk.CTkButton(master=class_frame, text=liste, width=50, height=50)
        box.grid(row=row_counter, column=column_counter, padx=5, pady=3)
        # Positionierung der Button
        # row = max. 3 Button, next row
        # Zeilenumbruch von >2 auf >1 angepasst debugged
        if column_counter > 1:
            row_counter += 1
            column_counter = 0
        else:
            column_counter += 1

load_assets(assets_path)

def button_event():
    print("button pressed")

#den neuen frame rendern
def render_classlist():
    controls_classlist_frame = ctk.CTkFrame(master=app)
    controls_classlist_frame.grid(row=0, column=0, sticky='EW')
    cln_add_btn = ctk.CTkButton(master=controls_classlist_frame, text='+', command= button_event)
    cln_del_btn = ctk.CTkButton(master=controls_classlist_frame, text='-', command= button_event)

    cln_add_btn.grid(padx= 5, pady= 3)
    cln_del_btn.grid(padx= 5, pady= 3)

render_classlist()
# class_list_label = ctk.CTkLabel(master=app, text=students)
# class_list_label.grid()


app.mainloop()