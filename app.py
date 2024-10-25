import customtkinter

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()

def button_event():
    print("button pressed")

button = customtkinter.CTkButton(app, text="CTkButton", command=button_event)



app.mainloop()