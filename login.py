# =========================
# FILE NAME : login.py
# CUSTOM TKINTER LOGIN UI
# =========================

import customtkinter as ctk
from tkinter import messagebox
import Dashboard
import Backend
from auth import authenticate


# =========================
# APP SETTINGS
# =========================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


# =========================
# LOGIN FUNCTION
# =========================

def login():
    username = username_entry.get().strip()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning("Login", "Enter both username and password.")
        return

    if authenticate(username, password):

        messagebox.showinfo(
            "Login",
            "Login Successful"
        )

        root.destroy()
        Dashboard.open_dashboard()
    else:
        messagebox.showerror(
            "Error",
            "Invalid username or password."
        )
        password_entry.delete(0, "end")
        password_entry.focus()


# =========================
# MAIN WINDOW
# =========================

root = ctk.CTk()

root.title("Student Management System")
root.geometry("1200x700")
root.minsize(900, 600)
root.resizable(False, False)


# =========================
# LEFT SIDE DESIGN
# =========================

left_frame = ctk.CTkFrame(
    root,
    width=600,
    height=700,
    corner_radius=0,
    fg_color="#0F8B4C"
)

left_frame.pack(side="left", fill="both")


# =========================
# LOGO TEXT
# =========================

logo_label = ctk.CTkLabel(
    left_frame,
    text="STUDENT\nMANAGEMENT\nSYSTEM",
    font=("Arial", 42, "bold"),
    text_color="white"
)

logo_label.place(x=120, y=180)


# =========================
# SMALL TEXT
# =========================

small_label = ctk.CTkLabel(
    left_frame,
    text="Manage Students Efficiently",
    font=("Arial", 18),
    text_color="white"
)

small_label.place(x=150, y=350)


# =========================
# RIGHT SIDE LOGIN CARD
# =========================

right_frame = ctk.CTkFrame(
    root,
    width=600,
    height=700,
    corner_radius=0,
    fg_color="#F5F5F5"
)

right_frame.pack(side="right", fill="both", expand=True)


# =========================
# LOGIN CARD
# =========================

login_card = ctk.CTkFrame(
    right_frame,
    width=420,
    height=450,
    corner_radius=20,
    fg_color="white"
)

login_card.place(x=90, y=120)


# =========================
# LOGIN TITLE
# =========================

login_title = ctk.CTkLabel(
    login_card,
    text="Login",
    font=("Arial", 34, "bold"),
    text_color="#0F8B4C"
)

login_title.place(x=160, y=60)


# =========================
# USERNAME
# =========================

username_label = ctk.CTkLabel(
    login_card,
    text="Username",
    font=("Arial", 16, "bold")
)

username_label.place(x=50, y=130)

username_entry = ctk.CTkEntry(
    login_card,
    width=320,
    height=45,
    corner_radius=10,
    placeholder_text="Enter Username"
)

username_entry.place(x=50, y=160)
username_entry.focus()


# =========================
# PASSWORD
# =========================

password_label = ctk.CTkLabel(
    login_card,
    text="Password",
    font=("Arial", 16, "bold")
)

password_label.place(x=50, y=230)

password_entry = ctk.CTkEntry(
    login_card,
    width=320,
    height=45,
    corner_radius=10,
    placeholder_text="Enter Password",
    show="*"
)

password_entry.place(x=50, y=260)
password_entry.bind("<Return>", lambda event: login())


# =========================
# LOGIN BUTTON
# =========================

login_button = ctk.CTkButton(
    login_card,
    text="Login",
    width=320,
    height=45,
    corner_radius=10,
    font=("Arial", 18, "bold"),
    fg_color="#0F8B4C",
    hover_color="#0B6B3A",
    command=login
)

login_button.place(x=50, y=340)


# =========================
# MAIN LOOP
# =========================

root.mainloop()
