from customtkinter import *
from PIL import Image

# Function to navigate back to the main page
def navigate_to_main_page(root):
    root.deiconify()  # Restore the main window
    second_root.destroy()  # Destroy the second window

# Function to show the second page
def show_second_page(main_root):
    global second_root  # Declare second_root as a global variable

    # Create the Tkinter instance for the second page
    second_root = CTk()
    second_root.geometry("800x480")
    second_root.resizable(0, 0)

    # Load images for buttons/icons
    # You should adjust the paths according to your file structure
    back_button_image = CTkImage(image_path="back_button_image.png", size=(100, 50))

    # Create widgets for the second page
    label = CTkLabel(master=second_root, text="Second Page")
    label.pack()

    back_button = CTkButton(master=second_root, text="Back to Main Page", image=back_button_image, command=lambda: navigate_to_main_page(main_root))
    back_button.pack()

    second_root.mainloop()
