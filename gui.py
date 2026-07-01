import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageTk
from parser import load_pdf, render_page, parse_recipe

class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("HelloFresh Card Maker")
        self.geometry("1100x700")

        self.create_widgets()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text="HelloFresh Card Maker",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        button = ctk.CTkButton(
            self,
            text="📂 PDF laden",
            command=self.open_pdf
        )
        button.pack(pady=15)

        self.image_frame = ctk.CTkFrame(self)

        self.image_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.left_image = ctk.CTkLabel(self.image_frame, text="")

        self.left_image.pack(side="left", expand=True, padx=10)

        self.right_image = ctk.CTkLabel(self.image_frame, text="")

        self.right_image.pack(side="right", expand=True, padx=10)

    def open_pdf(self):

        filename = filedialog.askopenfilename(
            filetypes=[("PDF", "*.pdf")]
        )

        if not filename:
            return

        pdf = load_pdf(filename)
        
        recipe = parse_recipe(pdf)
        print(recipe.title)

        page1 = render_page(pdf, 0)
        page2 = render_page(pdf, 1)

        page1.thumbnail((400, 550))
        page2.thumbnail((400, 550))

        self.tk_page1 = ImageTk.PhotoImage(page1)
        self.tk_page2 = ImageTk.PhotoImage(page2)

        self.left_image.configure(image=self.tk_page1)
        self.right_image.configure(image=self.tk_page2)
