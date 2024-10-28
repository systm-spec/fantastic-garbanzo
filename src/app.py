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

# semi-globals
current_classlist= {"title":""}
current_classlist_dict = {}

###############
## Functions ##
###############

# Init-Fn zum rendern der user in btns


# todo:
#  - DOCSTRINGS
#  - Comments

def init():
    """
    Initializes the user interface with class list buttons.

    This function creates a button for each class list file in the directory,
    adds it to the scroll frame in the UI, and assigns a command that triggers
    when the button is clicked to load the corresponding class list.
    """
    # Iteriert durch alle gefundenen Klassendateien und erstellt Buttons dafür
    for item in render_json_classlists():
        user_btn = ctk.CTkButton(
            classlist_scroll_frame,
            width=32,  # Breite des Buttons
            text=item,  # Text des Buttons ist der Name der Klassendatei
            corner_radius=12,  # Abgerundete Ecken für ein besseres UI-Design
            fg_color="transparent",  # Hintergrundfarbe des Buttons
            # Weisst jedem Button eine Funktion zu, die beim Klick die Klasse lädt
            command=lambda cl_name=item: on_classlist_click(cl_name)
        )
        # Platziert den Button im Scroll-Frame der Benutzeroberfläche
        user_btn.grid(sticky="ew")

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
    title (str): Title used as the JSON filename and as the main key in the data.

    This function takes a list of user names, assigns each an ID and initial score,
    and then saves the data as a JSON file. It also updates global class list data.
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

# Funktion, die bei Klick auf einen Benutzer-Button ausgeführt wird
def on_user_click(current_user):
    """
    Increases the score for a clicked user and displays the updated score in the console.

    Parameters:
    current_user (str): The name of the user whose score will be incremented.

    This function locates the clicked user in the global class list dictionary,
    increments their score by 10, and prints the updated user data to the console.
    """
    # Benutzerinformationen aus dem aktuellen Klassenlisten-Dictionary abrufen
    user = current_classlist_dict[current_classlist['title']]
    user_score = user[current_user]["score"]

    # Erhöht den Score des angeklickten Benutzers um 10 Punkte
    user[current_user].update({"score": user_score + 10})

    # Gibt den aktualisierten Benutzerstatus in der Konsole aus (zur Kontrolle)
    print(user[current_user])

def on_classlist_click(cl_name):
    """
        Handles the event when a class list button is clicked.

        Parameters:
        cl_name (str): The name of the class list file that was clicked.

        This function opens the specified class list JSON file, reads its content,
        and updates the application's current class list data. It then renders the
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





#################################
## Classlist & User-Grid Frame ##
#################################

# Classlist- & User-Grid-Tab
class_user_grid_tab = ctk.CTkTabview(class_user_grid_frame)
users_tab = class_user_grid_tab.add("users")
lists_tab = class_user_grid_tab.add("lists")
class_user_grid_tab.set("lists")
class_user_grid_tab.grid(padx=7, pady=7, sticky="NWE")

# scrollable frame for classlist jsons
classlist_scroll_frame = ctk.CTkScrollableFrame(lists_tab)
lists_tab.grid_columnconfigure(0, weight=1)
classlist_scroll_frame.grid(column=1, pady=12, padx=8)

# parent frame for class-members
tab_users_frame = ctk.CTkFrame(users_tab, fg_color="transparent")
tab_users_frame.grid_columnconfigure((0,1,2), weight=1, minsize=200)
tab_users_frame.grid()








init()
## YOUR ARE NOT SUPPOSED TO WRITE CODE BELOW THIS LINE! ##
app.mainloop()