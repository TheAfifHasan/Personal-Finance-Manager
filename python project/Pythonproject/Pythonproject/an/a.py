import tkinter as tk
from tkinter import messagebox

# Dummy username and password (replace with your own)
valid_username = "user123"
valid_password = "password123"

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == valid_username and password == valid_password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register():
    messagebox.showinfo("Registration", "Redirecting to registration page...")

# Create main window
root = tk.Tk()
root.title("Login Page")

# Set the size of the main window
root.geometry("600x300")

# Set background color
root.configure(bg="#f0f0f0")

# Username Label and Entry
username_label = tk.Label(root, text="Username:", bg="#f0f0f0")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

username_entry = tk.Entry(root, width=40)  # Increase width to make it bigger
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password Label and Entry
password_label = tk.Label(root, text="Password:", bg="#f0f0f0")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

password_entry = tk.Entry(root, show="*", width=40)  # Increase width to make it bigger
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=login, bg="#4CAF50", fg="white")
login_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Registration Button
register_button = tk.Button(root, text="Register", command=register, bg="#008CBA", fg="white")
register_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

# Run the main event loop
root.mainloop()
