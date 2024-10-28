import customtkinter as ctk
from tkinter import filedialog
import os
import json
from util.windows import check_for_windows
from util.event_info import info_me

check_for_windows()

###############
## App Setup ##
###############
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("./config/theme/custom.json")
app = ctk.CTk()
app.title("Lurk.Alert()")
app.geometry("620x720")

class_user_grid_frame = ctk.CTkFrame(app)
class_user_grid_frame.pack(fill="both")
class_user_grid_frame.grid_columnconfigure(0, weight=1)

current_classlist= {"title":""}
current_classlist_dict = {}

###############
## Functions ##
###############

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
    tab_users_frame.configure(fg_color="gray17")

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


# todo:
#  - DOCSTRINGS
#  - Comments

def on_classlist_click(cl_name):
    with open (rf"config/user_data/{cl_name}", "r", encoding='UTF-8') as reader:
        names = reader.read()
    names_dict = json.loads(names)
    names_dict_keys = names_dict[cl_name.split(".")[0]].keys()
    current_classlist['title'] = cl_name.split(".")[0]
    current_classlist_dict.update(names_dict)
    render_classlist_users(names_dict_keys)
    class_user_grid_tab.set("users")

def render_json_classlists():
    path= "config/user_data"
    json_classlists=os.listdir(path)
    json_classlists.sort(reverse=True)
    return json_classlists



#################################
## Classlist & User-Grid Frame ##
#################################

# Classlist- & User-Grid-Tab
class_user_grid_tab = ctk.CTkTabview(class_user_grid_frame)
tab_users = class_user_grid_tab.add("users")
tab_lists = class_user_grid_tab.add("lists")
class_user_grid_tab.set("lists")
class_user_grid_tab.grid(padx=7, pady=7, sticky="NWE")

# scrollable frame for classlist jsons
scroll_classlists_frame = ctk.CTkScrollableFrame(tab_lists)
tab_lists.grid_columnconfigure(0, weight=1)
scroll_classlists_frame.grid(column=1, pady=12, padx=8)

# parent frame for class-members
tab_users_frame = ctk.CTkFrame(tab_users, fg_color="transparent")
tab_users_frame.grid_columnconfigure((0,1,2), weight=1, minsize=200)
tab_users_frame.grid()


#################################
## Cxxx ##
#################################

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