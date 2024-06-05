import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

# Global variables to store user-selected angle and speed
angle_var = None
speed_var = None

# Default angle and speed values
angle_default = 90
speed_default = 50

# Function to execute the selected code option with specified angle and speed
def execute_code(code_option):
    angle = angle_var.get()  # Get the selected angle from the global variable
    speed = speed_var.get()  # Get the selected speed from the global variable
    os.system(f"python {code_option} {angle} {speed}")  # Pass angle and speed as arguments

def create_dashboard():
    global angle_var, speed_var
    # Create the main window
    root = tk.Tk()
    root.title("Robot Arm Control Dashboard")
    root.geometry("1000x700")
    root.config(bg="white")  # Set background color to white

    # Load the background image
    background_img = Image.open("C:/Users/henis/Downloads/IoT-Robot/wallpaper.jpeg")
    background_img = background_img.resize((1000, 700))
    background_img = ImageTk.PhotoImage(background_img)

    # Create a label to display the background image
    background_label = tk.Label(root, image=background_img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Check if user settings have been applied
    if angle_var is None or speed_var is None:
        # Initialize angle and speed variables with default values
        angle_var = tk.IntVar(value=angle_default)
        speed_var = tk.IntVar(value=speed_default)

    # Function to handle code option selection
    def handle_code_option(code_option):
        execute_code(code_option)
        messagebox.showinfo("Option Executed", "Robot arm task executed successfully.")

    # Function to create the selection window
    def create_selection_window():
        # Create the selection window
        selection_window = tk.Toplevel(root)
        selection_window.title("Select Task")
        selection_window.geometry("1000x700")
        selection_window.config(bg="white")  # Set background color to white
        selection_window.focus_set()

        # Add buttons for each code option
        btn_leaf_picker = tk.Button(selection_window, text="Leaf Picker", command=lambda: handle_code_option("leaf-picker.py"), bg="#70c1b3", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10, bd=0)
        btn_leaf_picker.grid(row=0, column=0, padx=20, pady=20)
        
        btn_weed_removal = tk.Button(selection_window, text="Weed Removal", command=lambda: handle_code_option("weed-removal.py"), bg="#ff847c", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10, bd=0)
        btn_weed_removal.grid(row=0, column=1, padx=20, pady=20)
        
        btn_flower_pollination = tk.Button(selection_window, text="Flower Pollination", command=lambda: handle_code_option("flower-pollination.py"), bg="#84a59d", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10, bd=0)
        btn_flower_pollination.grid(row=0, column=2, padx=20, pady=20)
        
        # Add a button to go back to the main dashboard window
        btn_back = tk.Button(selection_window, text="Back to Home Screen", command=selection_window.destroy, bg="#bcbabe", fg="white", font=("Arial", 10), padx=10, pady=5, bd=0)
        btn_back.grid(row=1, column=1, columnspan=2, padx=20, pady=20)


    # Function to open the settings window
    def open_settings():
        # Create the settings window
        settings_window = tk.Toplevel(root)
        settings_window.title("Settings")
        settings_window.geometry("400x300")
        settings_window.config(bg="white")  # Set background color to white
        settings_window.focus_set()

        # Function to apply settings
        def apply_settings():
            # Update the global angle and speed variables with user-selected values
            global angle_var, speed_var
            angle_var = angle_scale.get()
            speed_var = speed_scale.get()
            messagebox.showinfo("Settings Applied", f"Angle: {angle_var}, Speed: {speed_var}")
            settings_window.destroy()

        # Add labels and scale widgets for angle and speed adjustment
        lbl_angle = tk.Label(settings_window, text="Angle:", bg="white", font=("Arial", 12))
        lbl_angle.pack(pady=5)
        angle_scale = tk.Scale(settings_window, from_=0, to=180, orient=tk.HORIZONTAL, bg="white", length=200, variable=angle_var)
        angle_scale.set(angle_var.get())  # Set the scale to last user-selected value
        angle_scale.pack()

        lbl_speed = tk.Label(settings_window, text="Speed:", bg="white", font=("Arial", 12))
        lbl_speed.pack(pady=5)
        speed_scale = tk.Scale(settings_window, from_=1, to=100, orient=tk.HORIZONTAL, bg="white", length=200, variable=speed_var)
        speed_scale.set(speed_var.get())  # Set the scale to last user-selected value
        speed_scale.pack()

        # Add a button to apply settings and close the window
        btn_apply_settings = tk.Button(settings_window, text="Apply", command=apply_settings, bg="#70c1b3", fg="white", font=("Arial", 12), padx=20, pady=10, bd=0)
        btn_apply_settings.pack(pady=10)

    # Function to close the application
    def exit_app():
        root.destroy()

    # Add a button to open the selection window
    btn_select_task = tk.Button(root, text="Select Task", command=create_selection_window, bg="#2a363b", fg="white", font=("Arial", 16, "bold"), padx=20, pady=10, bd=0)
    btn_select_task.pack(pady=20)

    # Add an exit button to close the application
    btn_exit = tk.Button(root, text="Exit", command=exit_app, bg="#ff847c", fg="white", font=("Arial", 12), padx=20, pady=10, bd=0)
    btn_exit.pack(side=tk.BOTTOM, pady=20)

    # Load the settings image
    settings_img = Image.open("C:/Users/henis/Downloads/IoT-Robot/settings.png")
    settings_img = settings_img.resize((40, 40))
    settings_img = ImageTk.PhotoImage(settings_img)

    # Create a button with the settings image
    btn_settings = tk.Button(root, image=settings_img, command=open_settings, bg="white", bd=0)
    btn_settings.image = settings_img
    btn_settings.place(relx=1, rely=1, anchor=tk.SE)

    root.mainloop()

# Create the main dashboard
create_dashboard()