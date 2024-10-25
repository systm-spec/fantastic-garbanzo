import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Layout Beispiel")

root.geometry("800x600")

logo = ttk.Label(root, text="Logo", background="lightgray")
navigation = ttk.Label(root, text="Navigation", background="gray")
sidebar = ttk.Label(root, text="Box1", background="lightgray")
body = ttk.Label(root, text="Box2", background="white")
header = ttk.Label(root, text="Box3", background="darkgray")
footer = ttk.Label(root, text="Footer", background="darkgray")

box = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")
box1 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")
box2 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")
box3 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")

box4 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")
box5 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")
box6 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")
box7 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")

box8 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")
box9 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")
box10 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")
box11 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")

box12 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")
box13 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")
box14 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")
box15 = ttk.Label(root, text= 'x',relief='solid', padding=10, background="lightgray")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

logo.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=5, ipady=30)
navigation.grid(row=0, column=2, columnspan=2, sticky="nsew", padx=10, pady=5)

box.grid(row=1, column=0, padx=10, pady=10)
box1.grid(row=1, column=1, padx=10, pady=10)
box2.grid(row=1, column=2, padx=10, pady=10)
box3.grid(row=1, column=3, padx=10, pady=10)

box4.grid(row=3, column=0, padx=10, pady=10)
box5.grid(row=3, column=1, padx=10, pady=10)
box6.grid(row=3, column=2, padx=10, pady=10)
box7.grid(row=3, column=3, padx=10, pady=10)

box8.grid(row=4, column=0, padx=10, pady=10)
box9.grid(row=4, column=1, padx=10, pady=10)
box10.grid(row=4, column=2, padx=10, pady=10)
box11.grid(row=4, column=3, padx=10, pady=10)

box12.grid(row=5, column=0,padx=10, pady=10)
box13.grid(row=5, column=1,padx=10, pady=10)
box14.grid(row=5, column=2,padx=10, pady=10)
box15.grid(row=5, column=3,padx=10, pady=10)

sidebar.grid(row=6, column=0, sticky="nsew", padx=10, pady=5, ipady=30)
body.grid(row=6, column=1, sticky="nsew", padx=10, pady=5)
header.grid(row=6, column=2, sticky="nsew", padx=10, pady=5)
footer.grid(row=7, column=0, columnspan=4, sticky="nsew", padx=10, pady=5)




root.mainloop()