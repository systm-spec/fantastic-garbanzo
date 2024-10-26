import customtkinter as ctk
from PIL import Image
from customtkinter import CTkToplevel
import tkinter as tk
from tkinter import filedialog
import os
import json



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


current_classlist= {"title":""}
current_classlist_dict = {}

###############
## Functions ##
###############

# Dialogue: for opening classlist
def open_cl():
    label.cl_path = filedialog.askopenfilename(defaultextension=".txt",title="Open classlist", initialdir=r"./assets/classlists")
    if label.cl_path:
        # if cl_path exists strip filename for label
        file_name = label.cl_path.split("/")[-1].split(".")[0]

        label.configure(text=file_name if file_name else "no file selected")
        # then start open & render process with cl_path
        with open(label.cl_path, "r") as reader:
            # open & remove linebreaks ("\n") & save to list
            users = reader.read().split('\n')
        users.sort()
        # init render
        render_classlist_users(users)
        # save list to json
        create_save_json(users, file_name)

# render fn
def render_classlist_users(users):
    # counter for grid
    row_counter = 0
    col_counter = 0
    # create & render btn with row_ & col_ counter for auto_grid
    for user in users:
        # we call the LAMBDA into command to get the user as arg
        user_btn = ctk.CTkButton(frame_users,width=24, text=user, corner_radius=14, command=lambda u=user:on_user_click(u))
        user_btn.grid(column=col_counter, row=row_counter, pady=(5,0))
        if col_counter < 2:
            col_counter += 1
        else:
            row_counter += 1
            col_counter = 0


def create_save_json(liste, title):
    # convert list to dict
    cool_list = {title:{}}
    for i,elem in enumerate(liste):
        cool_list[title][elem] = {
            "id":i,
            "name":elem,
            "score": 0
        }
    current_classlist['title']=title
    current_classlist_dict.update(cool_list)
    # dump it & save as json in config/user_data
    with open(f"config/user_data/{title}.json", "w") as f:
        json.dump(cool_list, f)

def on_user_click(current_user):
    user = current_classlist_dict[current_classlist['title']]
    user_score = user[current_user]["score"]
    user[current_user].update({ "score": user_score + 10})
    print(user[current_user]["score"])






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