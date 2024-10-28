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