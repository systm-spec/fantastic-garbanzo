import customtkinter as ctk
from tkinter import filedialog as fd
from tkinter import messagebox
import os
import json
from util.windows import check_for_windows
from PIL import Image
from tkinter import messagebox
import datetime
import random
from numpy import random

check_for_windows()

###############
## Functions ##
###############

# Init-Fn zum rendern der user in btns
def init():
    """
    Initializes the user interface with class list buttons.

    This function creates a button for each class list file in the directory,
    adds it to the scroll frame in the UI, and assigns a command that triggers
    when the button is clicked to load the corresponding class list.
    """
    tab_row_count = 0
    # Iteriert durch alle gefundenen Klassendateien und erstellt Buttons dafür
    for item in render_json_classlists():
        user_btn = ctk.CTkButton(
            classlist_scroll_frame,
            text=item,
            corner_radius=0,
            border_width=1,
            border_color="#3f3f46",
            fg_color="transparent",
            # Weisst jedem Button eine Funktion zu, die beim Klick die Klasse lädt
            command=lambda cl_name=item: on_classlist_click(cl_name)
        )
        delete_button = ctk.CTkButton(
            classlist_scroll_frame,
            text='',
            image=delete_icon,
            width=32,
            hover_color="#920b3a",
            corner_radius=0,
            fg_color="transparent",
            bg_color="#4f000b",
            command=lambda crazy_name = item: delete_btn_click(crazy_name)
        )
        # Platziert den Button im Scroll-Frame der Benutzeroberfläche
        user_btn.grid(row=tab_row_count, column=0, sticky="EW", pady=(0, 4))
        delete_button.grid(row=tab_row_count, column=1, pady=(0, 4))
        tab_row_count += 1

# Funktion zum Rendern der Benutzerliste
def render_classlist_users(users):
    """
    Displays each user from the given list in a grid layout within the UI.

    Parameters:
    users (list): List of user names to be displayed as buttons.

    This function iterates through the list of users, creates a button for each,
    and places it in a grid layout with up to three columns. Clicking a button
    calls the 'on_user_click' function with the user's name as the argument.
    """
    # Zähler für die Position in der grid
    row_counter = 0
    col_counter = 0
    # Button für jeden Benutzer erstellen und mit grid-Zählern platzieren
    for user in users:
        # Lambda-Ausdruck in 'command', um 'user' als Argument an 'on_user_click' zu übergeben
        user_btn = ctk.CTkButton(
            tab_users_frame,
            height=50,
            width=197,
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
def create_save_json(user_list, title):
    """
    Creates a JSON file from a list of user names and saves it with a given title.

    Parameters:
    user_list (list): List of user names to be stored in the JSON file.
    title (str): Title used as the JSON filename and as the main key in the history.

    This function takes a list of user names, assigns each an ID and initial score,
    and then saves the history as a JSON file. It also updates global class list history.
    """
    # Erstellt ein Dictionary mit dem Titel als Schlüssel für die JSON-Datei
    class_list_data = {title: {}}

    # Fügt jedem Benutzer in der Liste eine ID und einen Start-Score hinzu
    for i, elem in enumerate(user_list):
        class_list_data[title][elem] = {
            "id": i,
            "name": elem,
            "score": 0  # Startscore für jeden Benutzer festlegen
        }

    # Aktuelle Klassenliste und Benutzer-Daten aktualisieren
    current_classlist['title'] = title
    current_classlist_dict.update(class_list_data)

    # Speichert die Benutzerdaten in einer JSON-Datei im Ordner "config/user_data"
    with open(f"config/user_data/{title}.json", "w") as f:
        json.dump(class_list_data, f)

        
def on_classlist_click(cl_name):
    """
        Handles the event when a class list button is clicked.

        Parameters:
        cl_name (str): The name of the class list file that was clicked.

        This function opens the specified class list JSON file, reads its content,
        and updates the application's current class list history. It then renders the
        list of users from that class in the user interface.
        """
    # Öffnet die JSON-Datei der angeklickten Klasse im Lesemodus
    with open(rf"config/user_data/{cl_name}", "r", encoding='UTF-8') as reader:
        names = reader.read()  # Liest den Inhalt der Datei
    # Konvertiert den gelesenen JSON-String in ein Python-Dictionary
    names_dict = json.loads(names)
    # Holt die Schlüssel (Namen) der Benutzer in der Klasse
    names_dict_keys = names_dict[cl_name.split(".")[0]].keys()
    # Setzt den Titel der aktuellen Klassenliste auf den Dateinamen ohne Endung
    current_classlist['title'] = cl_name.split(".")[0]
    # Aktualisiert das globale Dictionary für die aktuelle Klassenliste
    current_classlist_dict.update(names_dict)
    # Zeigt die Benutzernamen der Klassenliste in der Benutzeroberfläche an
    render_classlist_users(names_dict_keys)
    # Wechselt zur Benutzeransicht im Interface
    class_user_grid_tab.set("users")


# Funktion, die eine Liste von JSON-Dateien sortiert und in einer Var ausgibt
def on_user_click(current_user):
    """
    Increases the score for a clicked user and displays the updated score in the console.

    Parameters:
    current_user (str): The name of the user whose score will be incremented.

    This function locates the clicked user in the global class list dictionary,
    increments their score by 10, and prints the updated user history to the console.
    """
    # Benutzerinformationen aus dem aktuellen Klassenlisten-Dictionary abrufen
    user = current_classlist_dict[current_classlist['title']]
    user_score = user[current_user]["score"]

    # Erhöht den Score des angeklickten Benutzers um 10 Punkte
    user[current_user].update({"score": user_score + 10})

    # Save the action to the history
    add_to_history(current_user)


def render_json_classlists():
    """
    Retrieves and sorts the list of JSON files in the class list directory.

    Returns:
    list: A sorted list of JSON file names representing different class lists.

    This function looks in the 'config/user_data' folder, finds all JSON files
    representing class lists, sorts them in reverse alphabetical order, and
    returns this list.
    """
    # Pfad zum Ordner mit den Klassendateien
    path = "config/user_data"
    # Holt alle Dateien im Ordner und filtert nur JSON-Klassendateien
    json_classlists = os.listdir(path)
    # Sortiert die Klassendateien in umgekehrter alphabetischer Reihenfolge
    json_classlists.sort(reverse=True)
    return json_classlists  # Gibt die sortierte Liste der Klassendateien zurück

# Funktion, die bei Klick auf den Add-Button ausgeführt wird
def on_add_button_click():
    # Definieren der zu nutzenden Dateitypen
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))
    # Bestimmung des Downloadpfads (muss bei egal welchem User funktionieren)
    user_download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    # Auswählen der einzulesenden Textdatei
    file_path = fd.askopenfilename(initialdir=user_download_dir, filetypes=filetypes)
    # Extrahieren des Dateinamens
    file_name = file_path.split("/")[-1].split(".")[0]
    # Einlesen der Txt-Datei
    with open(file_path, "r", encoding="utf-8") as read_file:
        file = read_file.read().split("\n")
        file.sort()
    # Aufrufen der Funktion zum Transferieren in eine JSON-Datei
    create_save_json(file, file_name)
    # Erstellte JSON_Datei rendern
    for child in classlist_scroll_frame.winfo_children():
        child.destroy()
    init()

# Funktion, die bei Klick auf den Del-Button ausgeführt wird
def delete_btn_click(crazy_name):
    # Ruft einen Dialog auf welcher das Löschen verifiziert
    if messagebox.askyesno(message=f'{crazy_name} asks: Do you really '
                                           f'want to hurt me?'):
        # Ruft den Pfad auf, löscht die JSON-Datei, löscht alle Button und
        # führt das init-Rendering neu aus.
        del_path = f"./config/user_data/{crazy_name}"
        os.remove(del_path)
        for child in classlist_scroll_frame.winfo_children():
            child.destroy()
        init()

# create log string with time and details, save & render it
def add_to_history(new_history_entry):
    # get time and format hour:minute:second
    now = datetime.datetime.now().strftime("%H:%M:%S")
    # make a format string
    converted_entry = f"{now} | {str(new_history_entry)} +10 Pts. \n"
    # fill log list
    session_history.append(converted_entry)
    # start render of labels
    render_history_labels(converted_entry)

# renders history label and destroys oldest one
def render_history_labels(label_text):
    children = metric_frame.winfo_children()
    # delete the oldest label everytime, if the log is >2 items
    if len(session_history) > 3:
        children[0].destroy()
    # render label
    history_label = ctk.CTkLabel(metric_frame, text=label_text)
    history_label.grid(padx=7, pady=(10, 0), sticky="NSWE")

# "X"-Button Event manipulation to save (history-) log
def on_closing():
    now = datetime.datetime.now()
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        with open(f"history/log/{current_classlist['title']}__{now.year}_{now.month}_{now.day}_{now.minute}_{now.second}.txt", "w") as writer:
            writer.writelines(session_history)
        app.destroy()

# Bind ESC-Click to quit
def destroy_anyway(e):
    app.destroy()

def do_random():
    r = random.randint(1,10)
    scores =current_classlist_dict[current_classlist["title"]].items()
    b = [{'score': b['score'], 'name':b["name"]} for a,b in scores]
    low_count = [x["name"] for x in filter(lambda a: a["score"]<30, b)]
    rnd_user = random.choice(low_count)
    messagebox.showinfo(title="RNG", message=f"Folgender Studi lurkt sehr "
                                             f"gern:\n 🕵🏼 {rnd_user} 🕵🏼 ")

###############
## App Setup ##
###############
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("./config/theme/custom.json")
app = ctk.CTk()
app.title("Lurk.Alert()")
app.geometry("620x740")
# app_icon = Image.open(r"./assets/img/trash.png")
# app_icon.save("icon.ico", format="ICO", sizes=[(32, 32)])
# app.wm_icon(bitmap=r"./assets/img/icon.ico")
app.resizable(False, False)
app.protocol("WM_DELETE_WINDOW", on_closing)
app.bind("<Escape>", destroy_anyway)


##########
## Main ##
##########

class_user_grid_frame = ctk.CTkFrame(app)
class_user_grid_frame.pack(fill="both")
class_user_grid_frame.grid_columnconfigure(0, weight=1)

# Var
current_classlist= {"title":""}
current_classlist_dict = {}
session_history = []

#################################
## Classlist & User-Grid Frame ##
#################################

# Classlist- & User-Grid-Tab
class_user_grid_tab = ctk.CTkTabview(class_user_grid_frame)
users_tab = class_user_grid_tab.add("users")
lists_tab = class_user_grid_tab.add("lists")
class_user_grid_tab.set("lists")
class_user_grid_tab.grid(padx=7, pady=7, sticky="NWE")

#######################
## Scrollable  Frame ##
#######################

# scrollable frame for classlist jsons
classlist_scroll_frame = ctk.CTkScrollableFrame(lists_tab, width=235)
classlist_scroll_frame.grid(row=1, column=0, pady=12, padx=8, ipadx=22, ipady=14)
classlist_scroll_frame.grid_columnconfigure(0, weight=1)
lists_tab.grid_columnconfigure(0, weight=1)
lists_tab.grid_rowconfigure(0, weight=10)
lists_tab.grid_rowconfigure(1, weight=1)

# Add- and Delete-Buttons
# Parent Frame
buttons_frame = ctk.CTkFrame(master=app)
buttons_frame.pack(fill="both", pady=(5, 0))
buttons_frame.grid_columnconfigure(index=0, weight=1)

# Add-Button Icon
add_icon = ctk.CTkImage(dark_image=Image.open('./assets/img/add_icon.png'),
                       size=(20,20))
# Add-Button
add_button = ctk.CTkButton(master=buttons_frame, text='', image=add_icon,
                           corner_radius=0, fg_color="transparent",
                           command=lambda: on_add_button_click())
add_button.grid(sticky="NWE")

# Del-Button Icon
delete_icon = ctk.CTkImage(dark_image=Image.open('./assets/img/delete_icon.png'),
                       size=(18,18))

# parent frame for class-members
tab_users_frame = ctk.CTkFrame(users_tab, fg_color="transparent")
tab_users_frame.grid_columnconfigure((0,1,2), weight=1, minsize=200)
tab_users_frame.grid()

###################
## Random Frame ##
###################

random_btn_frame = ctk.CTkFrame(app)
random_btn_frame.pack(fill="both", pady=(5, 0))
random_btn_frame.grid_columnconfigure(index=0, weight=1)

rng_btn = ctk.CTkButton(random_btn_frame, corner_radius=0, text="Random Lurker",
                        fg_color="transparent", command=do_random)
rng_btn.grid(sticky="nwe")



###################
## History Frame ##
###################

metric_frame = ctk.CTkFrame(app)
metric_frame.pack(fill="both", pady=5)
metric_frame.grid_columnconfigure(0, weight=1)






init()
## YOUR ARE NOT SUPPOSED TO WRITE CODE BELOW THIS LINE! ##
app.mainloop()