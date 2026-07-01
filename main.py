import customtkinter as ctk
from gui import MainWindow
from parser import load_pdf

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = MainWindow()
app.mainloop()

pdf = load_pdf("testfiles/64e860a94e40d5c6cb1a53fe.pdf")