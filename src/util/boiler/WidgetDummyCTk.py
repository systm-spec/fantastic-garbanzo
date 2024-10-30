import customtkinter as ctk
import tkinter as tk

from customtkinter import CTkFrame

root = ctk.CTk()
root.geometry("1000x1000")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frame
frame = ctk.CTkFrame(root, width=200, height=200)
frame.grid()

# Button
def button_event():
    print("button pressed")

button = ctk.CTkButton(root, text="CTkButton", command=button_event)
button.grid()

# Checkbox
def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

check_var = ctk.StringVar(value="on")
checkbox = ctk.CTkCheckBox(root, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.grid()

# Combobox1
def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = ctk.CTkComboBox(root, values=["option 1", "option 2"],
                                     command=combobox_callback)
combobox.set("option 1")
combobox.grid()


# Combobox2
def combobox_callback2(choice):
    print("combobox dropdown clicked:", choice)

combobox_var = ctk.StringVar(value="option 2")
combobox2 = ctk.CTkComboBox(root, values=["option 1", "option 2"],
                                     command=combobox_callback2, variable=combobox_var)
combobox_var.set("option 2")

combobox2.grid()

# Entry
entry = ctk.CTkEntry(root, placeholder_text="CTkEntry")
entry.grid()

# Label
label = ctk.CTkLabel(root, text="CTkLabel", fg_color="transparent")
label.grid()

# Optionmenu1
def optionmenu_callback1(choice):
    print("optionmenu1 dropdown clicked:", choice)

optionmenu1 = ctk.CTkOptionMenu(root, values=["option 1", "option 2"],
                                         command=optionmenu_callback1)
optionmenu1.set("option 2")

# Optionmenu2
def optionmenu_callback2(choice):
    print("optionmenu2 dropdown clicked:", choice)

optionmenu_var = ctk.StringVar(value="option 2")
optionmenu2 = ctk.CTkOptionMenu(root,values=["option 1", "option 2"],
                                         command=optionmenu_callback2,
                                         variable=optionmenu_var)

# Progressbar
progressbar = ctk.CTkProgressBar(root, orientation="horizontal")
progressbar.grid()

# Radiobutton
def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

radio_var = tk.IntVar(value=0)
radiobutton_1 = ctk.CTkRadioButton(root, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value=1)
radiobutton_2 = ctk.CTkRadioButton(root, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value=2)
radiobutton_1.grid()
radiobutton_2.grid()
# Scrollable_Frame
# 2 BSP in Doku SUPER INTERESSTING
scrollable_frame = ctk.CTkScrollableFrame(root, width=200, height=200)
scrollable_frame.grid()


# create scrollable textbox
tk_textbox = ctk.CTkTextbox(root, activate_scrollbars=False)
tk_textbox.grid(row=0, column=0, sticky="nsew")

# create CTk scrollbar
ctk_textbox_scrollbar = ctk.CTkScrollbar(root, command=tk_textbox.yview)
ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

# connect textbox scroll event to CTk scrollbar
tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)
tk_textbox.grid()


# Slider
def slider_event(value):
    print(value)

slider = ctk.CTkSlider(root, from_=0, to=100, command=slider_event)


# Switch
def switch_event():
    print("switch toggled, current value:", switch_var.get())

switch_var = ctk.StringVar(value="on")
switch = ctk.CTkSwitch(root, text="CTkSwitch", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")


# Tabview
tabview = ctk.CTkTabview(master=root)

tabview.add("tab 1")  # add tab at the end
tabview.add("tab 2")  # add tab at the end
tabview.set("tab 2")  # set currently visible tab
tabview.grid()

tab_button1 = ctk.CTkButton(master=tabview.tab("tab 1"))
tab_button1.pack(padx=20, pady=20)

tab_button2 = ctk.CTkButton(master=tabview.tab("tab 2"))
tab_button2.pack(padx=20, pady=20)

# segmented btn
def segmented_button_callback(value):
    print("segmented button clicked:", value)

segemented_button = ctk.CTkSegmentedButton(root, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback)
segemented_button.set("Value 1")
segemented_button.grid()

# Textbox
textbox = ctk.CTkTextbox(root)

textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
textbox.delete("0.0", "end")  # delete all text
textbox.configure(state="normal")  # configure textbox to be read-only

textbox.grid()

root.mainloop()