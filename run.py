# Application Start

___author__ = "Gowtham Bavireddy"

import logging
from tkinter import *
from tkinter import messagebox
from ui_screens.login_screen import LoginPage

logging.basicConfig(filename='output.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')


def on_exit():
    if messagebox.askyesno("EXIT", "Do you want to EXIT Application?"):
        tk_obj.destroy()


if __name__ == "__main__":
    tk_obj = Tk()
    tk_obj.geometry("%dx%d+0+0" % (tk_obj.winfo_screenwidth(), tk_obj.winfo_screenheight()))
    tk_obj.title("Login Page")
    tk_obj.iconbitmap('logo\\philipsicon.ico')
    tk_obj.protocol("WM_DELETE_WINDOW", on_exit)
    login = LoginPage(tk_obj)

    tk_obj.mainloop()
