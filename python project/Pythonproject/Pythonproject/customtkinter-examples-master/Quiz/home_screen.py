import tkinter as tk
from tkinter import messagebox
from customtkinter import *
from PIL import Image, ImageTk
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
        self.geometry("800x550+200+50")
        self.configure(bg='white')
        self.resizable(width=False, height=False)
        self.create_login_widgets()

    def create_login_widgets(self):
        image_path = "pythonProject/banner.png"  
        image = Image.open(image_path)
        image.thumbnail((450, 550))
        photo = ImageTk.PhotoImage(image)
        frame = tk.Frame(self, bg="white", width=450, height=550,highlightthickness=0,borderwidth=0)
        frame.pack_propagate(0)
        frame.pack(side='left')
        label = tk.Label(frame, image=photo,highlightthickness=0,borderwidth=0)
        label.image = photo  
        label.pack(pady=40)
        self.label_name=tk.Label(self,text="Personal Finance Manager",bg=self.cget('bg'), font=("Arial", 18,'bold'), fg="VioletRed4")
        self.label_name.place(x=60,y=355)
        self.label_name = tk.Label(self, text="Sign In",bg=self.cget('bg'), font=("Arial", 23), fg="VioletRed4").pack(pady=10)
        self.label_name = tk.Label(self, text="                           ",bg=self.cget('bg'),).pack(pady=20)
        self.label_name = tk.Label(self, text="Email:",bg=self.cget('bg'), font=("Arial", 13), fg="VioletRed4")
        self.label_name.place(x=470,y=90)
        
        self.entry_name = tk.Entry(self,width=50,highlightbackground="VioletRed3", highlightcolor="VioletRed4", highlightthickness=1)
        self.entry_name.pack(pady=5,ipady=6)
        self.label_name = tk.Label(self, text="                           ",bg=self.cget('bg'),).pack(pady=10)
        self.label_password = tk.Label(self, text="Password:",bg=self.cget('bg'), font=("Arial", 13), fg="VioletRed4")
        self.label_password.place(x=470,y=173)
        self.entry_password = tk.Entry(self, show="*",width=50, highlightbackground="VioletRed3", highlightcolor="VioletRed4", highlightthickness=1)
        self.entry_password.pack(pady=5,ipady=6)
        self.label_name = tk.Label(self, text="                           ",bg=self.cget('bg'),).pack(pady=10)
        self.button_login = tk.Button(self, text="Sign In", command=self.login,width=40 ,bg="VioletRed3", fg="white")
        self.button_login.pack(pady=5)
        self.label_password = tk.Label(self, text="or",bg=self.cget('bg'), font=("Arial", 10), fg="VioletRed4").pack(padx=5)
        self.button_signup = tk.Button(self, text="Sign Up", command=self.signup,width=40 ,bg="VioletRed3", fg="white")
        self.button_signup.pack(pady=5)

    def login(self):
        name = self.entry_name.get()
        password = self.entry_password.get()
        users_data = db.child("Users").get()
        

        
        if users_data.val():
                flag=0
                for user_key, user_value in users_data.val().items():
                    if user_value.get('Email') == name and user_value.get('Password') == password:
                        flag=1
                        self.show_ok_page()
                if flag==0:
                    messagebox.showerror("Error", "No User found with this email and password")
                    
                        
                    
                
        else:
             messagebox.showerror("Error", "No User")
                 
        

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
        self.geometry("800x550+200+50")
        self.configure(bg='white')
        self.create_signup_widgets()

    def create_signup_widgets(self):
        image_path = "pythonProject/Signup.png" 
        image = Image.open(image_path)
        image.thumbnail((450, 550))
        photo = ImageTk.PhotoImage(image)
        frame = tk.Frame(self, bg="white", width=450, height=550,highlightthickness=0,borderwidth=0)
        frame.pack_propagate(0)
        frame.pack(side='left')
        label = tk.Label(frame, image=photo,highlightthickness=0,borderwidth=0)
        label.image = photo  
        label.pack(pady=60)
        
        self.label_name = tk.Label(self, text="Sign Up",bg=self.cget('bg'), font=("Arial", 23), fg="VioletRed4").pack(pady=10)
        self.label_name = tk.Label(self, text="                           ",bg=self.cget('bg'),).pack(pady=20)

        self.label_name = tk.Label(self, text="Name:",bg=self.cget('bg'), font=("Arial", 13), fg="VioletRed4")
        self.label_name.place(x=470,y=83)
        self.entry_name = tk.Entry(self,width=50,highlightbackground="VioletRed3", highlightcolor="VioletRed4", highlightthickness=1)
        self.entry_name.place(x=470, y=108, height=25)

        self.label_phone = tk.Label(self, text="Phone:",bg=self.cget('bg'), font=("Arial", 13), fg="VioletRed4")
        self.label_phone.place(x=470, y=150)
        self.entry_phone = tk.Entry(self,width=50,highlightbackground="VioletRed3", highlightcolor="VioletRed4", highlightthickness=1)
        self.entry_phone.place(x=470, y=175, height=25) 

        self.label_email = tk.Label(self, text="Email:",bg=self.cget('bg'), font=("Arial", 13), fg="VioletRed4")
        self.label_email.place(x=470, y=217)
        self.entry_email = tk.Entry(self,width=50,highlightbackground="VioletRed3", highlightcolor="VioletRed4", highlightthickness=1)
        self.entry_email.place(x=470, y=242, height=25)


        self.label_password = tk.Label(self, text="Password:",bg=self.cget('bg'), font=("Arial", 13), fg="VioletRed4")
        self.label_password.place(x=470, y=285)
        self.entry_password = tk.Entry(self, show="*",width=50,highlightbackground="VioletRed3", highlightcolor="VioletRed4", highlightthickness=1)
        self.entry_password.place(x=470, y=310, height=25)

        self.label_name = tk.Label(self, text="                           ",bg=self.cget('bg'),).pack(pady=20)
        self.button_register = tk.Button(self, text="Register", command=self.register,width=40 ,bg="VioletRed3", fg="white")
        self.button_register.place(x=475,y=370)

        self.button_back = tk.Button(self, text="Back to Login", command=self.back_to_login,width=40 ,bg="VioletRed3", fg="white")
        self.button_back.place(x=475,y=410)

    def register(self):
       name = self.entry_name.get()
       phone = self.entry_phone.get()
       email = self.entry_email.get()
       password = self.entry_password.get()
    
       if name==''or phone==''or email=='' or password=='':
         messagebox.showerror("Error", "Please Fill up the form completly")
         return
       users_data = db.child("Users").get()
       if users_data.val():
           for user_key, user_value in users_data.val().items():
               if user_value.get('Email') == email:
                   messagebox.showerror("Error", "Email already exists. Please choose another email.")
                   return
    
       
       user = {'Name': name, 'Phone': phone, 'Email': email, 'Password': password}
       db.child('Users').push(user)
       messagebox.showinfo("Success", "User registered successfully.")
       self.back_to_login()
    

    def back_to_login(self):
        self.destroy()
        login_form = LoginForm()
        login_form.mainloop()

class OkPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("OK Page")
        self.geometry("800x550+200+50")

        self.label_ok = tk.Label(self, text="OK!")
        self.label_ok.pack(padx=20, pady=20)

if __name__ == "__main__":
    login_form = LoginForm()
    login_form.mainloop()
