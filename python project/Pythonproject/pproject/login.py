import tkinter as tk
from tkinter import messagebox
import pyrebase
firebaseConfig = {
  'apiKey': "AIzaSyDlX0i1j99ZzWI8Tc2-h3B2XzuE3MsljRs",
  'authDomain': "extp-4cf2f.firebaseapp.com",
  'databaseURL': "https://extp-4cf2f-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "extp-4cf2f",
  'storageBucket': "extp-4cf2f.appspot.com",
  'messagingSenderId': "356077691663",
  'appId': "1:356077691663:web:7602a26a7ca0552d06947a"
};
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

class LoginForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login Form")
        self.geometry("750x550")

        self.create_login_widgets()

    def create_login_widgets(self):
        self.label_name = tk.Label(self, text="Email:")
        self.label_name.pack(pady=5)
        self.entry_name = tk.Entry(self)
        self.entry_name.pack(pady=5)
   
        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.pack(pady=5)

        self.button_signup = tk.Button(self, text="Sign Up", command=self.signup)
        self.button_signup.pack(pady=5)

    def login(self):
        name = self.entry_name.get()
        password = self.entry_password.get()
        users_data = db.child("Users").get()
        
            # Check if there's any data
        if users_data.val():
                # Loop through each user's data
                for user_key, user_value in users_data.val().items():
                    # Check if the name and password match
                    if user_value.get('Email') == name and user_value.get('Password') == password:
                        self.show_ok_page()
                # If no matching user is found
                
        else:
             print("No users found")
                 
        

    def signup(self):
        self.destroy()
        signup_form = SignUpForm()
        signup_form.mainloop()

    def show_ok_page(self):
        self.destroy()
        ok_page = OkPage()
        ok_page.mainloop()

class SignUpForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sign Up Form")
        self.geometry("750x550")

        self.create_signup_widgets()

    def create_signup_widgets(self):
        self.label_name = tk.Label(self, text="Name:")
        self.label_name.pack(pady=5)
        self.entry_name = tk.Entry(self)
        self.entry_name.pack(pady=5)

        self.label_phone = tk.Label(self, text="Phone:")
        self.label_phone.pack(pady=5)
        self.entry_phone = tk.Entry(self)
        self.entry_phone.pack(pady=5)

        self.label_email = tk.Label(self, text="Email:")
        self.label_email.pack(pady=5)
        self.entry_email = tk.Entry(self)
        self.entry_email.pack(pady=5)


        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)


        self.button_register = tk.Button(self, text="Register", command=self.register)
        self.button_register.pack(pady=5)

        self.button_back = tk.Button(self, text="Back to Login", command=self.back_to_login)
        self.button_back.pack(pady=5)

    def register(self):
       name = self.entry_name.get()
       phone = self.entry_phone.get()
       email = self.entry_email.get()
       password = self.entry_password.get()
    
       if name==''or phone==''or email=='' or password=='':
         messagebox.showerror("Error", "Email already exists. Please choose another email.")
         return
       users_data = db.child("Users").get()
       if users_data.val():
           for user_key, user_value in users_data.val().items():
               if user_value.get('Email') == email:
                   messagebox.showerror("Error", "Email already exists. Please choose another email.")
                   return
    
       # If the email is unique, proceed with registration
       user = {'Name': name, 'Phone': phone, 'Email': email, 'Password': password}
       db.child('Users').push(user)
       messagebox.showinfo("Success", "User registered successfully.")
    

    def back_to_login(self):
        self.destroy()
        login_form = LoginForm()
        login_form.mainloop()

class OkPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("OK Page")
        self.geometry("750x550")

        self.label_ok = tk.Label(self, text="OK!")
        self.label_ok.pack(padx=20, pady=20)

if __name__ == "__main__":
    login_form = LoginForm()
    login_form.mainloop()
