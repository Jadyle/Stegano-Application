
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
import sys
from tkinter.font import Font


import tkinter as tk


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pathlib import Path
from extractexe import decode_exe


def gui_7_extract_exe(window, main_frame):

    # Add parent folder
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from pathlib import Path
    from hide import encode_message
    from tkinter import filedialog, messagebox

    # Determine the base path for assets
    def get_base_path():
        if hasattr(sys, "_MEIPASS"):
            return Path(sys._MEIPASS) / "assets" / "frame7"
        return Path(__file__).parent / "assets" / "frame7"

    ASSETS_PATH = get_base_path()

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    # Display page success 
    def show_page_extract_exe_success():
        page_hide_frame = tk.Frame(main_frame)
        
        from build.gui8 import gui_8_extract_exe_success
        gui_8_extract_exe_success(window, main_frame)

        page_hide_frame.pack(pady=20)

    main_frame.pack(fill=tk.BOTH, expand=True)

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 400,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        600.0,
        400.0,
        fill="#1E043F",
        outline="")

    button_image_hover_1 = PhotoImage(
        file=relative_to_assets("button_hover_1.png"))

    def button_1_hover(e):
        button_1.config(
            image=button_image_hover_1
        )
    def button_1_leave(e):
        button_1.config(
            image=button_image_1
        )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=343.0,
        y=291.0,
        width=66.0,
        height=27.0
    )
    button_1.bind('<Enter>', button_1_hover)
    button_1.bind('<Leave>', button_1_leave)

    button_image_hover_2 = PhotoImage(
        file=relative_to_assets("button_hover_2.png"))

    def button_2_hover(e):
        button_2.config(
            image=button_image_hover_2
        )
    def button_2_leave(e):
        button_2.config(
            image=button_image_2
        )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=343.0,
        y=291.0,
        width=66.0,
        height=27.0
    )

    button_2.bind('<Enter>', button_2_hover)
    button_2.bind('<Leave>', button_2_leave)

    
    button_image_hover_3 = PhotoImage(
        file=relative_to_assets("button_hover_3.png"))

    def button_3_hover(e):
        button_3.config(
            image=button_image_hover_3
        )
    def button_3_leave(e):
        button_3.config(
            image=button_image_3
        )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=343.0,
        y=221.0,
        width=66.0,
        height=27.0
    )
    button_3.bind('<Enter>', button_3_hover)
    button_3.bind('<Leave>', button_3_leave)

    button_image_hover_4 = PhotoImage(
        file=relative_to_assets("button_hover_4.png"))

    def button_4_hover(e):
        button_4.config(
            image=button_image_hover_4
        )
    def button_4_leave(e):
        button_4.config(
            image=button_image_4
        )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=56.0,
        y=342.0,
        width=135.0,
        height=38.0
    )
    button_4.bind('<Enter>', button_4_hover)
    button_4.bind('<Leave>', button_4_leave)



    def select_image1():
        try:
            # Open file dialog to select an image
            image_path = filedialog.askopenfilename(
                title="Select Image", filetypes=[("PNG files", "*.png")]
            )
            if image_path:
                # Display the selected file path in entry_1
                entry_2.delete(0, "end")  # Clear any existing text
                entry_2.insert(0, image_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to select image: {str(e)}")

    def select_image2():
        try:
           
            folder_path = filedialog.askdirectory(title="Select Folder")
            if folder_path:
                # Display the selected file path in entry_1
                entry_1.delete(0, "end")  # Clear any existing text
                entry_1.insert(0, folder_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to select image: {str(e)}")


    def decode():
        try:
            # Get the selected image path from entry_1
            output_path = entry_1.get().strip()
            if not output_path:
                messagebox.showerror("Error", "Please select an .exe file.")
                return

            # Get the secret message from entry_2
            image_path = entry_2.get().strip()
            if not image_path:
                messagebox.showerror("Error", "Please enter an image.")
                return


            output_path += "/decode.exe"

            print(output_path)

            hidden_data, result = decode_exe(image_path)

            with open(output_path, "wb") as file:
                file.write(hidden_data)
            print("Hidden file recovered successfully.")

            # Check if the encoding was successful
            if result == True or result is None:  # Adjust based on your encode_message behavior
                messagebox.showinfo("Success", "Message successfully hidden in the image!")
                show_page_extract_exe_success()  # Show success page only on success
            else:
                messagebox.showinfo("Error", f"Failed to hide the message: {result}")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))


    # Update button_2 to call select_image when clicked
    button_3.config(command=select_image1)
    button_2.config(command=select_image2)


    # Update button_1 to call hide_message when clicked
    button_4.config(command=decode)


    custom_font_l = Font(family="Terminal", size=20, weight="normal", underline=False)
    custom_font_s = Font(family="Terminal", size=15, weight="normal", underline=False)


    canvas.create_text(
        300.0,
        60.0,
        anchor="center",
        text="Stegano",
        fill="#FFFFFF",
        font=custom_font_l
    )

    canvas.create_text(
        60.0,
        270.0,
        anchor="nw",
        text="Choose a folder to extract the exe",
        fill="#FFFFFF",
        font=custom_font_s
    )

    canvas.create_text(
        204.0,
        316.0,
        anchor="nw",
        text="*Only .png format is supported",
        fill="#7D35D5",
        font=("AnekKannada Regular", 10 * -1)
    )

    canvas.create_text(
        60.0,
        200.0,
        anchor="nw",
        text="Choose an image to extract the exe",
        fill="#FFFFFF",
        font=custom_font_s
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        196.5,
        305.0,
        image=entry_image_1
    )
    
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=60.0,
        y=296.0,
        width=273.0,
        height=16.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        196.5,
        235.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=60.0,
        y=226.0,
        width=273.0,
        height=16.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        157.0,
        63.0,
        image=image_image_1
    )
    canvas.image_image_1 = image_image_1  # Keep a reference

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        441.0,
        63.0,
        image=image_image_2
    )
    canvas.image_image_2 = image_image_2  # Keep a reference