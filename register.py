import customtkinter as ctk
import login
import app



class Register(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#181818")
        self.controller = controller

        ctk.CTkLabel(self, text="Register", font=("Courier", 24, "bold")).pack(pady=40)

        self.new_username = ctk.CTkEntry(self, placeholder_text="New Username")
        self.new_username.pack(pady=8)

        self.new_password = ctk.CTkEntry(self, placeholder_text="New Password", show="*")
        self.new_password.pack(pady=8)

        ctk.CTkButton(self, text="Create account").pack(pady=10)

        ctk.CTkButton(
            self,
            text="Back to login",
            fg_color="transparent",
            text_color="#2b83f6",
            command=lambda: controller.show_frame(login.Login)
        ).pack(pady=8)

if __name__ == "__main__":
      start = app.App()
      start.mainloop()