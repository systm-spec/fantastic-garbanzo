import customtkinter as ctk

ctk.set_appearance_mode("dark")
app = ctk.CTk()

app.geometry("700x900")
app.grid_columnconfigure(0, weight=1)
app.configure(padx=20, pady=20)

class_frame = ctk.CTkFrame(master=app, width=200, height=400, border_width=1,
                           border_color="white")

class_frame.grid(row=0, column=0, sticky="EW")


def button_event():
    print("button pressed")

button = ctk.CTkButton(app, text="CTkButton", command=button_event)



app.mainloop()