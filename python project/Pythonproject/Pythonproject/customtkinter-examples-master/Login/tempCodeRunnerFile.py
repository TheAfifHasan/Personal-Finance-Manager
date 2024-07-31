from customtkinter import *
from PIL import Image
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyBl_4UHU8jd4v8p4ASQXAZOVcR4zK4ur4E",
    'authDomain': "pythonproject-ed3b1.firebaseapp.com",
    'databaseURL': "https://trialauth-7eea1.firebaseio.com",
    'projectId': "pythonproject-ed3b1",
    'storageBucket': "pythonproject-ed3b1.appspot.com",
    'messagingSenderId': "779158779079",
    'appId': "1:779158779079:web:f13198c42b6cf4495a7ae2"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Function to handle the login process
def login():
    print('log in')
    email = email_entry.get()  # Get email from Entry widget
    password = password_entry.get()  # Get password from Entry widget
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print('successfully login')
    except:
        print("invalid email or password")

# Function to handle the signup process
def signup():
    print('sign up')
    email = email_entry.get()  # Get email from Entry widget
    password = password_entry.get()  # Get password from Entry widget
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("User signed up successfully!")
    except:
        print("email already exists")

# Create a Tkinter instance
app = CTk()
app.geometry("800x480")
app.resizable(0, 0)

side_img_data = Image.open("C:/Users/vecis/OneDrive/Desktop/pypro/customtkinter-examples-master/Login/banner.png")
email_icon_data = Image.open("C:/Users/vecis/OneDrive/Desktop/pypro/customtkinter-examples-master/Login/side-img.png")
password_icon_data = Image.open("C:/Users/vecis/OneDrive/Desktop/pypro/customtkinter-examples-master/Login/side-img.png")
google_icon_data = Image.open("C:/Users/vecis/OneDrive/Desktop/pypro/customtkinter-examples-master/Login/side-img.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(400, 480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))
google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(17, 17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=400, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
email_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
email_entry.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
password_entry.pack(anchor="w", padx=(25, 0))

# Button to initiate the login process
CTkButton(master=frame, text="Sign In", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=login).pack(anchor="w", pady=(40, 0), padx=(25, 0))

# Button to initiate the signup process
CTkButton(master=frame, text="Sign UP", fg_color="#EEEEEE", hover_color="#E44982", font=("Arial Bold", 12), text_color="#601E88", width=225,  command=signup).pack(anchor="w", pady=(20, 0), padx=(25, 0))

app.mainloop()
