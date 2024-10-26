import customtkinter as ctk
from PIL import Image
from customtkinter import CTkToplevel
import tkinter as tk
from tkinter import filedialog
import os



###############
## App Setup ##
###############
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("./config/theme/custom.json")
app = ctk.CTk()
app.title("Achim")
app.geometry("400x720")

parent_frame = ctk.CTkFrame(app, fg_color=None)
parent_frame.pack(expand=True, fill="both")
parent_frame.grid_columnconfigure(0, weight=1)


###############
## Functions ##
###############
def open_cl():
    label.cl_path = filedialog.askopenfilename(defaultextension=".txt",title="Open classlist", initialdir=r"./assets/classlists")
    if label.cl_path:
        stripped_path = label.cl_path.split("/")[-1].split(".")[0]
        label.configure(text=stripped_path if stripped_path else "no file selected")
        render_classlist_users(label.cl_path)

def render_classlist_users(cl_path):
    row_counter = 0
    col_counter = 0
    with open(cl_path, "r") as reader:
        users = reader.read().split('\n')
    for user in users:
        user_btn = ctk.CTkButton(frame_users,width=24, text=user, corner_radius=14)
        user_btn.grid(column=col_counter, row=row_counter, pady=(5,0))
        if col_counter > 1:
            row_counter += 1
            col_counter = 0
        else:
            col_counter += 1


#####################
## Classlist-Frame ##
#####################
# Main-Frame for classlist-controls
frame = ctk.CTkFrame(parent_frame, fg_color=None, height=50)
frame.grid(row=0, column=0, padx=7, pady=7, sticky="ewn")
frame.grid_columnconfigure(0, weight=1)

# Label to display current classlist
label = ctk.CTkLabel(frame, text="no file selected",  corner_radius=4 )
label.grid(row=0, column= 0, padx=4,pady=(4,0), ipadx=2, sticky="WE")

# Btn to load classlist
open_icon = ctk.CTkImage(dark_image=Image.open("./assets/img/open_icon.png"), size=(14,14))
open_btn = ctk.CTkButton(frame, text="", command=open_cl, image=open_icon, corner_radius=4, width=15)
open_btn.grid(row=0, column=1, ipadx=3, padx=(0,4), pady=(4,0) )


# Main-Frame for classlist-users
frame_users = ctk.CTkFrame(parent_frame, fg_color=None)
frame_users.grid(row=1, column=0, padx=7, ipady=3, sticky="ew")
frame_users.grid_columnconfigure((0,1,2), weight=1)












## YOUR ARE NOT SUPPOSED TO WRITE CODE BELOW THIS LINE! ##
app.mainloop()