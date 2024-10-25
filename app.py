import customtkinter as ctk
import os

ctk.set_appearance_mode("dark")
app = ctk.CTk()

app.geometry("700x900")
app.grid_columnconfigure(0, weight=1)
app.configure(padx=20, pady=20)

class_frame = ctk.CTkFrame(master=app, border_width=1, border_color="white")

class_frame.grid(row=0, column=0, sticky="EW")

assets_path = "assets"
def load_assets(path):
    # Auflistung der Files in Dir:
    content = os.listdir(assets_path)
    column_counter = 0
    row_counter = 0
    # Iteration der Dateien und Generierung Button
    for liste in content:
        box = ctk.CTkButton(master=class_frame, text=liste, width=50, height=50)
        box.grid(row=row_counter, column=column_counter, padx=5, pady=5)
        # Positionierung der Button
        # row = max. 3 Button, next row
        if column_counter > 2:
            row_counter += 1
            column_counter = 0
        else:
            column_counter += 1

load_assets(assets_path)



# class_list_label = ctk.CTkLabel(master=app, text=students)
# class_list_label.grid()


def button_event():
    print("button pressed")

button = ctk.CTkButton(app, text="CTkButton", command=button_event)



app.mainloop()