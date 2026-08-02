import customtkinter as ctk
import register
import app

class Login(ctk.CTkFrame):
    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="#181818")
        self.controller = controller

        ctk.CTkLabel(self, text="Login", font=("Courier", 24, "bold")).pack(pady=40)
        self.name_field = ctk.CTkEntry(self, placeholder_text="Username")
        self.name_field.pack(pady=8)

        self.password_field = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_field.pack(pady=8)

        ctk.CTkButton(self, text="Submit").pack(pady=10)

        ctk.CTkButton(
            self,
            text="sign-in",
            fg_color="transparent",
            text_color="#2b82f6",
            command=lambda: controller.show_frame(register.Register)
        ).pack(pady=8)
        
if __name__ == "__main__":
      start = app.App()
      start.mainloop()