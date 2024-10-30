import customtkinter as ctk
from tkinter import filedialog
import os
import json
from PIL import Image


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("../config/theme/custom.json")
app = ctk.CTk()
app.title("Lurk.Alert()")
app.geometry("620x720")


buttons_frame= ctk.CTkFrame(master= app)
buttons_frame.grid()

add_icon= ctk.CTkImage(dark_image= Image.open('../assets/img/add_icon.png'),
                       size=(20,20))

add_button= ctk.CTkButton(master= buttons_frame,text='',image= add_icon,
                          width=65, height=32)
add_button.grid()



app.mainloop()