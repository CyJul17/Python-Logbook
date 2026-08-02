import customtkinter as ctk
import login
import register


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Logbook System")
        self.geometry("600x400")

        self.container = ctk.CTkFrame(self, fg_color="#181818")
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (login.Login, register.Register):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(login.Login)

    def show_frame(self, type_frame):
        frame = self.frames[type_frame]
        frame.tkraise()


if __name__ == "__main__":
    start = App()
    start.mainloop()
                  
            



