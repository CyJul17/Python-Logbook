import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


def run_cli_mode():
    print("GUI display unavailable. Starting console login mode...")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    print(f"Console login attempt for user: {username}")
    if username and password:
        print("Login accepted in console mode.")
    else:
        print("Login failed: username and password are required.")


class Login(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Logbook System")
        self.geometry("600x400")
        self.configure(fg_color="#181818")
        self.resizable(True, True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_title = ctk.CTkLabel(
            self,
            text="Python Logbook System",
            font=("Courier", 28, "bold"),
            text_color="#FFFFFF"
        )
        self.main_title.grid(row=0, column=0, pady=(30, 0), sticky="s")

        self.card_frame = ctk.CTkFrame(
            self,
            width=360,
            height=320,
            corner_radius=20,
            fg_color="#3d3d3d"
        )
        self.card_frame.grid(row=1, column=0, pady=(10, 40), sticky="n")

        self.card_title = ctk.CTkLabel(
            self.card_frame,
            text="Login",
            font=("Courier", 24, "bold"),
            text_color="#FFFFFF"
        )
        self.card_title.pack(pady=(20, 15))

        self.name_field = ctk.CTkEntry(
            self.card_frame,
            placeholder_text="Username",
            width=230,
            height=38,
            corner_radius=15,
            border_width=1,
            border_color="#555555",
            fg_color="#333333",
            text_color="#FFFFFF",
            placeholder_text_color="#888888"
        )
        self.name_field.pack(pady=8, padx=15)

        self.password_field = ctk.CTkEntry(
            self.card_frame,
            placeholder_text="Password",
            show="*",
            width=230,
            height=38,
            corner_radius=15,
            border_width=1,
            border_color="#555555",
            fg_color="#333333",
            text_color="#FFFFFF",
            placeholder_text_color="#888888"
        )
        self.password_field.pack(pady=8, padx=15)

        self.forgot_pass = ctk.CTkButton(
            self.card_frame,
            text="forgot password",
            font=("Consolas", 12, "underline"),
            fg_color="transparent",
            hover_color="#3d3d3d",
            text_color="#2b82f6",
            cursor="hand2",
            height=20,
            command=self.forgotten
        )
        self.forgot_pass.pack(pady=8)

        self.submit = ctk.CTkButton(
            self.card_frame,
            text="Submit",
            font=("Consolas", 15, "bold"),
            width=110,
            height=35,
            corner_radius=18,
            fg_color="#2151d1",
            hover_color="#1a41a8",
            cursor="hand2",
            command=self.submit_action
        )
        self.submit.pack(pady=5)

        self.signin = ctk.CTkButton(
            self.card_frame,
            text="sign-in",
            font=("Consolas", 12, "underline"),
            fg_color="transparent",
            hover_color="#3d3d3d",
            text_color="#2b82f6",
            cursor="hand2",
            height=20,
            command=self.signing_in
        )
        self.signin.pack(pady=8)

    def forgotten(self):
        print("forgotten is clicked")

    def submit_action(self):
        print(f"Your name is {self.name_field.get()}")
        print(f"Your password: {self.password_field.get()}")

    def signing_in(self):
        print("sign-in is clicked")


if __name__ == "__main__":
    app = Login()
    app.mainloop()

