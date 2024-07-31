from tkinter import *
import tkinter.messagebox as tkMessageBox
import pyrebase

root = Tk()
root.title("Python - Basic Register and Login Form")

width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# Initialize Firebase
firebaseConfig = {
    'apiKey': "YOUR_API_KEY",
    'authDomain': "YOUR_AUTH_DOMAIN",
    'databaseURL': "YOUR_DATABASE_URL",
    'projectId': "YOUR_PROJECT_ID",
    'storageBucket': "YOUR_STORAGE_BUCKET",
    'messagingSenderId': "YOUR_MESSAGING_SENDER_ID",
    'appId': "YOUR_APP_ID"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()

#=======================================VARIABLES=====================================
USER = StringVar()
PASS = StringVar()
LOGIN_USER = StringVar()
LOGIN_PASS = StringVar()

#=======================================METHODS=======================================
def Register():
    if USER.get() == "" or PASS.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="orange")
    else:
        try:
            user = auth.create_user_with_email_and_password(USER.get(), PASS.get())
            # You can adjust the data structure according to your Firebase Realtime Database structure
            data = {
                "username": USER.get(),
                "password": PASS.get()
            }
            # Push user data to the database
            database.child("users").child(user['localId']).set(data)
            USER.set("")
            PASS.set("")
            lbl_result.config(text="Successfully Created!", fg="green")
        except Exception as e:
            lbl_result.config(text=str(e), fg="red")

def Login():
    try:
        user = auth.sign_in_with_email_and_password(LOGIN_USER.get(), LOGIN_PASS.get())
        lbl_login_result.config(text="Successfully Logged In!", fg="green")
        # You can implement further actions upon successful login
    except Exception as e:
        lbl_login_result.config(text=str(e), fg="red")


def ShowLoginForm():
    RegisterFrame.pack_forget()
    LoginForm.pack()


def ShowRegisterForm():
    LoginForm.pack_forget()
    RegisterFrame.pack()


#=====================================FRAMES====================================
TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame = Frame(root)
RegisterFrame.pack(side=TOP, pady=20)
LoginForm = Frame(root)


#=====================================LABEL WIDGETS=============================
lbl_title = Label(TitleFrame, text="IT SOURCECODE - Register and Login Form", font=('arial', 18), bd=1, width=640)
lbl_title.pack()
lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
lbl_result.grid(row=5, columnspan=2)
lbl_login_result = Label(LoginForm, text="", font=('arial', 18))
lbl_login_result.grid(row=3, columnspan=2)

#=======================================ENTRY WIDGETS===========================
user = Entry(RegisterFrame, font=('arial', 20), textvariable=USER, width=15)
user.grid(row=1, column=1)
pass1 = Entry(RegisterFrame, font=('arial', 20), textvariable=PASS, width=15, show="*")
pass1.grid(row=2, column=1)

login_user = Entry(LoginForm, font=('arial', 20), textvariable=LOGIN_USER, width=15)
login_user.grid(row=1, column=1)
login_pass = Entry(LoginForm, font=('arial', 20), textvariable=LOGIN_PASS, width=15, show="*")
login_pass.grid(row=2, column=1)

#========================================BUTTON WIDGETS=========================
btn_register=Button(RegisterFrame, font=('arial', 20), text="Register", command=Register)
btn_register.grid(row=6, columnspan=2)

btn_login=Button(LoginForm, font=('arial', 20), text="Login", command=Login)
btn_login.grid(row=3, columnspan=2)

btn_show_login = Button(RegisterFrame, font=('arial', 20), text="Login", command=ShowLoginForm)
btn_show_login.grid(row=7, columnspan=2)

btn_show_register = Button(LoginForm, font=('arial', 20), text="Register", command=ShowRegisterForm)
btn_show_register.grid(row=4, columnspan=2)

#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
