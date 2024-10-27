import customtkinter as ctk
from PIL import Image
from customtkinter import CTkToplevel
import tkinter as tk
from tkinter import filedialog
import os
import json
from event_info import ei

###############
## App Setup ##
###############
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("./config/theme/custom.json")
app = ctk.CTk()
app.title("Achim")
app.geometry("620x720")

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


# Funktion zum Rendern der Benutzerliste
def render_classlist_users(users):
    # Zähler für die Position in der grid
    row_counter = 0
    col_counter = 0
    # Button für jeden Benutzer erstellen und mit grid-Zählern platzieren
    for user in users:
        # Lambda-Ausdruck in 'command', um 'user' als Argument an 'on_user_click' zu übergeben
        user_btn = ctk.CTkButton(
            tab_users_frame,
            height=50,
            text=user,
            corner_radius=0,
            fg_color="transparent",
            command=lambda u=user: on_user_click(u)
        )

        # Button in grid an der durch Zähler bestimmten Position platzieren
        user_btn.grid(column=col_counter, row=row_counter, sticky="nsew")

        # Spalten-Zähler erhöhen bis max. 2, danach Zeilen-Zähler erhöhen
        if col_counter < 2:
            col_counter += 1
        else:
            row_counter += 1
            col_counter = 0  # Zurücksetzen des Spalten-Zählers
    tab_users_frame.configure(width = 500)


# Funktion zum Erstellen und Speichern einer JSON-Datei aus einer Liste
def create_save_json(liste, title):
    # Liste in ein Dictionary umwandeln mit Titel als Schlüssel
    cool_list = {title: {}}

    # Schleife, um jedes Element der Liste mit ID und Details in das Dictionary zu packen
    for i, elem in enumerate(liste):
        cool_list[title][elem] = {
            "id": i,
            "name": elem,
            "score": 0  # Startscore für jeden Benutzer festlegen
        }

    # Klassenliste im globalen Dictionary speichern
    current_classlist['title'] = title
    current_classlist_dict.update(cool_list)

    # JSON-Datei mit den Benutzerdaten in 'config/user_data/' speichern
    with open(f"config/user_data/{title}.json", "w") as f:
        json.dump(cool_list, f)


# Funktion, die bei Klick auf einen Benutzer-Button ausgeführt wird
def on_user_click(current_user):
    # Zugriff auf den Benutzer im aktuellen Klassenlisten-Dictionary
    user = current_classlist_dict[current_classlist['title']]
    user_score = user[current_user]["score"]

    # Erhöhen des Scores für den angeklickten Benutzer um 10
    user[current_user].update({"score": user_score + 10})

    # Aktuellen Benutzerstatus in der Konsole ausgeben (zur Kontrolle)
    print(user[current_user])

def on_classlist_click(cl_name):
    with open (rf"config/user_data/{cl_name}", "r", encoding='UTF-8') as reader:
        names = reader.read()
    names_dict = json.loads(names)
    names_dict_keys = names_dict[cl_name.split(".")[0]].keys()
    current_classlist['title'] = cl_name.split(".")[0]
    current_classlist_dict.update(names_dict)
    render_classlist_users(names_dict_keys)
    class_tab.set("users")

def render_json_classlists():
    path= "config/user_data"
    json_classlists=os.listdir(path)
    json_classlists.sort(reverse=True)
    return json_classlists



#####################
## Classlist-Frame ##
#####################
# Main-Frame for classlist-controls
# frame = ctk.CTkFrame(parent_frame, fg_color=None, height=50)
# frame.grid(row=0, column=0, padx=7, pady=7, sticky="ewn")
# frame.grid_columnconfigure(0, weight=1)

## Label to display current classlist
#label = ctk.CTkLabel(frame, text="no file selected",  corner_radius=4 )
#label.grid(row=0, column= 0, padx=4,pady=(4,0), ipadx=2, sticky="WE")
#
## Btn to load classlist
#open_icon = ctk.CTkImage(dark_image=Image.open("./assets/img/open_icon.png"), size=(14,14))
#open_btn = ctk.CTkButton(frame, text="", command=open_cl, image=open_icon, corner_radius=4, width=15)
#open_btn.grid(row=0, column=1, ipadx=3, padx=(0,4), pady=(4,0) )

# Main-Frame for classlist-users
frame_users = ctk.CTkFrame(parent_frame, fg_color=None)
frame_users.grid(row=1, column=0, padx=7, ipady=3, sticky="ew")
frame_users.grid_columnconfigure((0,1,2), weight=1)


# Classlist-Tab
class_tab = ctk.CTkTabview(parent_frame)
tab_users = class_tab.add("users")
tab_lists = class_tab.add("lists")
class_tab.set("lists")
class_tab.grid(sticky="ewn",padx=7, pady=7,row=0, column=0)

# scrollable frame for classlist jsons
scroll_classlists_frame = ctk.CTkScrollableFrame(tab_lists)
tab_lists.grid_columnconfigure((0,1), weight=1)
scroll_classlists_frame.grid(column=2, pady=12, padx=8)

# parent frame for class-members
tab_users_frame = ctk.CTkFrame(tab_users)
tab_users_frame.grid_columnconfigure((0,1,2), weight=1, minsize=200)
tab_users_frame.grid()



for item in render_json_classlists():
    user_btn = ctk.CTkButton(
        scroll_classlists_frame,
        width=32,
        text=item,
        corner_radius=12,
        fg_color="transparent",
        command=lambda cl_name=item:on_classlist_click(cl_name)
    )
    user_btn.grid(sticky="ew")








## YOUR ARE NOT SUPPOSED TO WRITE CODE BELOW THIS LINE! ##
app.mainloop()