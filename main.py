import PIL
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from PIL import ImageFilter
from tkinter import filedialog


class App:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry('1280x720')
        self.window.title('Image Watermarker')
        
        self.window.mainloop()