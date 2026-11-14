# =========================================
# FILE NAME : Dashboard.py
# =========================================

import customtkinter as ctk
from tkinter import ttk, messagebox
import Backend as Backend


# =========================================
# APP SETTINGS
# =========================================

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")


# =========================================
# DASHBOARD WINDOW
# =========================================

def open_dashboard():

    root = ctk.CTk()

    root.title("Student Management System")
    root.geometry("1600x900")
 


    # =========================================
    # THEME TOGGLE
    # =========================================

    current_mode = "light"

    def toggle_theme():

        nonlocal current_mode

        if current_mode == "light":

            ctk.set_appearance_mode("dark")
            current_mode = "dark"

        else:

            ctk.set_appearance_mode("light")
            current_mode = "light"


    # =========================================
    # SIDEBAR
    # =========================================

    sidebar = ctk.CTkFrame(
        root,
        width=250,
        corner_radius=0,
        fg_color="#0F8B4C"
    )

    sidebar.pack(side="left", fill="y")


    # =========================================
    # TITLE
    # =========================================

    title_label = ctk.CTkLabel(
        sidebar,
        text="STUDENT\nMANAGEMENT",
        font=("Arial", 30, "bold"),
        text_color="white"
    )

    title_label.pack(pady=40)


    # =========================================
    # THEME BUTTON
    # =========================================

    theme_btn = ctk.CTkButton(
        sidebar,
        text="Toggle Theme",
        command=toggle_theme,
        fg_color="white",
        text_color="green",
        hover_color="#E5E5E5",
        width=180,
        height=40
    )

    theme_btn.pack(pady=10)


    # =========================================
    # TOTAL STUDENTS CARD
    # =========================================

    total_card = ctk.CTkFrame(
        sidebar,
        width=180,
        height=120,
        corner_radius=15,
        fg_color="white"
    )

    total_card.pack(pady=30)

    total_title = ctk.CTkLabel(
        total_card,
        text="Total Students",
        font=("Arial", 18, "bold"),
        text_color="green"
    )

    total_title.pack(pady=15)

    total_count = ctk.CTkLabel(
        total_card,
        text="0",
        font=("Arial", 30, "bold"),
        text_color="black"
    )

    total_count.pack()


    # =========================================
    # MAIN FRAME
    # =========================================

    main_frame = ctk.CTkFrame(
        root,
        corner_radius=0
    )

    main_frame.pack(side="right", fill="both", expand=True)


    # =========================================
    # HEADING
    # =========================================

    heading = ctk.CTkLabel(
        main_frame,
        text="Dashboard",
        font=("Arial", 34, "bold"),
        text_color="green"
    )

    heading.pack(pady=20)


    # =========================================
    # FORM FRAME
    # =========================================

    form_frame = ctk.CTkFrame(
        main_frame,
        width=400,
        height=950,
        corner_radius=20
    )
    form_frame.place(x=30, y=90)
    
    


    # =========================================
    # REGISTER NUMBER
    # =========================================

    reg_label = ctk.CTkLabel(
        form_frame,
        text="Register Number",
        font=("Arial", 16, "bold")
    )

    reg_label.place(x=30, y=30)

    reg_entry = ctk.CTkEntry(
        form_frame,
        width=300,
        height=40
    )

    reg_entry.place(x=30, y=60)


    # =========================================
    # NAME
    # =========================================

    name_label = ctk.CTkLabel(
        form_frame,
        text="Name",
        font=("Arial", 16, "bold")
    )

    name_label.place(x=30, y=120)

    name_entry = ctk.CTkEntry(
        form_frame,
        width=300,
        height=40
    )

    name_entry.place(x=30, y=150)


    # =========================================
    # BRANCH
    # =========================================

    branch_label = ctk.CTkLabel(
        form_frame,
        text="Branch",
        font=("Arial", 16, "bold")
    )

    branch_label.place(x=30, y=210)

    branch_entry = ctk.CTkEntry(
        form_frame,
        width=300,
        height=40
    )

    branch_entry.place(x=30, y=240)


    # =========================================
    # SEMESTER
    # =========================================

    semester_label = ctk.CTkLabel(
        form_frame,
        text="Semester",
        font=("Arial", 16, "bold")
    )

    semester_label.place(x=30, y=300)

    semester_entry = ctk.CTkEntry(
        form_frame,
        width=300,
        height=40
    )

    semester_entry.place(x=30, y=330)


    # =========================================
    # PHONE NUMBER
    # =========================================

    phone_label = ctk.CTkLabel(
        form_frame,
        text="Phone Number",
        font=("Arial", 16, "bold")
    )

    phone_label.place(x=30, y=390)

    phone_entry = ctk.CTkEntry(
        form_frame,
        width=300,
        height=40
    )

    phone_entry.place(x=30, y=420)


    # =========================================
    # ADDRESS
    # =========================================

    address_label = ctk.CTkLabel(
        form_frame,
        text="Address",
        font=("Arial", 16, "bold")
    )

    address_label.place(x=30, y=480)

    address_entry = ctk.CTkEntry(
        form_frame,
        width=300,
        height=40
    )

    address_entry.place(x=30, y=510)

    selected_register_no = None


    # =========================================
    # FUNCTIONS
    # =========================================

    def clear_fields():

        nonlocal selected_register_no

        reg_entry.delete(0, "end")
        name_entry.delete(0, "end")
        branch_entry.delete(0, "end")
        semester_entry.delete(0, "end")
        phone_entry.delete(0, "end")
        address_entry.delete(0, "end")
        selected_register_no = None


    def read_form():
        values = (
            reg_entry.get().strip(),
            name_entry.get().strip(),
            branch_entry.get().strip(),
            semester_entry.get().strip(),
            phone_entry.get().strip(),
            address_entry.get().strip(),
        )
        labels = ("Register number", "Name", "Branch", "Semester", "Phone number", "Address")
        missing = [label for label, value in zip(labels, values) if not value]
        if missing:
            messagebox.showerror("Invalid details", "Please fill in: " + ", ".join(missing))
            return None

        try:
            semester = int(values[3])
        except ValueError:
            messagebox.showerror("Invalid semester", "Semester must be a number from 1 to 8.")
            return None
        if not 1 <= semester <= 8:
            messagebox.showerror("Invalid semester", "Semester must be from 1 to 8.")
            return None

        normalized_phone = values[4].replace(" ", "").replace("-", "")
        digits = normalized_phone[1:] if normalized_phone.startswith("+") else normalized_phone
        if not digits.isdigit() or not 7 <= len(digits) <= 15:
            messagebox.showerror("Invalid phone number", "Enter 7–15 digits, optionally starting with +.")
            return None

        return values[:3] + (str(semester), normalized_phone, values[5])


    def update_total():

        total_count.configure(
            text=str(len(Backend.students))
        )


    def show_students():

        student_table.delete(*student_table.get_children())

        count = 0

        for s in Backend.students:

            if count % 2 == 0:
                row_color = "evenrow"
            else:
                row_color = "oddrow"

            student_table.insert(
                "",
                "end",
                values=(
                    s.get("Register_no", ""),
                    s.get("Name", ""),
                    s.get("Branch", ""),
                    s.get("Semister", ""),
                    s.get("phone_no", ""),
                    s.get("Address", "")
                ),
                tags=(row_color,)
            )

            count += 1

        update_total()


    def insert_student():
        values = read_form()
        if values is None:
            return
        if Backend.insert(*values):
            messagebox.showinfo("Success", "Student inserted successfully.")
            show_students()
            clear_fields()
        else:
            messagebox.showerror("Could not insert", "A student with that register number may already exist.")


    def delete_student():
        register_no = selected_register_no or reg_entry.get().strip()
        if not register_no:
            messagebox.showerror("Select a student", "Select a table row or enter a register number to delete.")
            return
        if Backend.delete(register_no):
            messagebox.showinfo("Success", "Student deleted successfully.")
            show_students()
            clear_fields()
        else:
            messagebox.showerror("Delete failed", "No student with that register number was found.")


    def update_student():
        if selected_register_no is None or not any(
            str(s.get("Register_no", "")).strip() == selected_register_no for s in Backend.students
        ):
            messagebox.showerror("Select a student", "Select an existing table row before updating.")
            return
        values = read_form()
        if values is None:
            return
        if Backend.update(selected_register_no, *values):
            messagebox.showinfo("Success", "Student updated successfully.")
            show_students()
            clear_fields()
        else:
            messagebox.showerror("Update failed", "The student could not be updated. Check for a duplicate register number.")


    def populate_form_from_selection(_event=None):
        nonlocal selected_register_no
        selection = student_table.selection()
        if not selection:
            return
        values = student_table.item(selection[0], "values")
        if not values:
            return
        selected_register_no = str(values[0]).strip()
        entries = (reg_entry, name_entry, branch_entry, semester_entry, phone_entry, address_entry)
        for entry, value in zip(entries, values):
            entry.delete(0, "end")
            entry.insert(0, value)


    # =========================================
    # BUTTONS
    # =========================================

    insert_btn = ctk.CTkButton(
        form_frame,
        text="Insert",
        command=insert_student,
        width=130,
        height=40,
        fg_color="green",
        hover_color="darkgreen"
    )

    insert_btn.place(x=30, y=590)


    update_btn = ctk.CTkButton(
        form_frame,
        text="Update",
        command=update_student,
        width=130,
        height=40,
        fg_color="orange",
        hover_color="#CC7000"
    )

    update_btn.place(x=200, y=590)


    delete_btn = ctk.CTkButton(
        form_frame,
        text="Delete",
        command=delete_student,
        width=130,
        height=40,
        fg_color="red",
        hover_color="darkred"
    )

    delete_btn.place(x=30, y=640)


    clear_btn = ctk.CTkButton(
        form_frame,
        text="Clear",
        command=clear_fields,
        width=130,
        height=40,
        fg_color="gray",
        hover_color="black"
    )

    clear_btn.place(x=200, y=640)


    # =========================================
    # TABLE FRAME
    # =========================================

    table_frame = ctk.CTkFrame(
        main_frame,
        width=900,
        height=650,
        corner_radius=20
    )

    table_frame.place(x=450, y=90)


    # =========================================
    # SCROLLBARS
    # =========================================

    scroll_y = ttk.Scrollbar(
        table_frame,
        orient="vertical"
    )

    scroll_x = ttk.Scrollbar(
        table_frame,
        orient="horizontal"
    )


    # =========================================
    # TABLE
    # =========================================

    columns = (
        "Register_no",
        "Name",
        "Branch",
        "Semester",
        "Phone",
        "Address"
    )

    student_table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )

    scroll_y.config(
        command=student_table.yview
    )

    scroll_x.config(
        command=student_table.xview
    )

    scroll_y.pack(
        side="right",
        fill="y"
    )

    scroll_x.pack(
        side="bottom",
        fill="x"
    )


    # =========================================
    # HEADINGS
    # =========================================

    student_table.heading(
        "Register_no",
        text="Register No"
    )

    student_table.heading(
        "Name",
        text="Name"
    )

    student_table.heading(
        "Branch",
        text="Branch"
    )

    student_table.heading(
        "Semester",
        text="Semester"
    )

    student_table.heading(
        "Phone",
        text="Phone"
    )

    student_table.heading(
        "Address",
        text="Address"
    )


    # =========================================
    # COLUMN WIDTH
    # =========================================

    student_table.column(
        "Register_no",
        width=130
    )

    student_table.column(
        "Name",
        width=170
    )

    student_table.column(
        "Branch",
        width=120
    )

    student_table.column(
        "Semester",
        width=100
    )

    student_table.column(
        "Phone",
        width=150
    )

    student_table.column(
        "Address",
        width=220
    )


    # =========================================
    # STYLE
    # =========================================

    style = ttk.Style()

    style.configure(
        "Treeview",
        rowheight=35,
        font=("Arial", 11)
    )

    style.configure(
        "Treeview.Heading",
        font=("Arial", 12, "bold")
    )

    student_table.tag_configure(
        "evenrow",
        background="#E8F5E9"
    )

    student_table.tag_configure(
        "oddrow",
        background="white"
    )


    student_table.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    student_table.bind("<<TreeviewSelect>>", populate_form_from_selection)


    # =========================================
    # LOAD DATA
    # =========================================

    show_students()


    # =========================================
    # MAIN LOOP
    # =========================================

    root.mainloop()
