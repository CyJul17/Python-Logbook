import tkinter
import login

if __name__ == "__main__":
    try:
        start = login.Login()
    except tkinter.TclError:
        login.run_cli_mode()
    else:
        start.mainloop()
