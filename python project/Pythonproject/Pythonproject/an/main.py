from customtkinter import *
from PIL import Image
import second_page

# Create the main Tkinter instance
root = CTk()
root.geometry("800x480")
root.resizable(0, 0)

# Load images for buttons/icons
# You should adjust the paths according to your file structure
button_image = CTkImage(image_path="button_image.png", size=(100, 50))

# Function to navigate to the second page
def navigate_to_second_page():
    root.withdraw()  # Hide the main window
    second_page.show_second_page(root)  # Show the second page

# Create widgets for the main page
label = CTkLabel(master=root, text="Main Page")
label.pack()

button = CTkButton(master=root, text="Go to Second Page", image=button_image, command=navigate_to_second_page)
button.pack()

root.mainloop()
