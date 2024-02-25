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
        
        self.upload()

        self.window.mainloop()

    def upload(self):
        f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')] 
        path = filedialog.askopenfilename(filetypes=f_types)
        self.o_image = Image.open(path) 


        image_tk = ImageTk.PhotoImage(self.o_image)

        self.panelA = tk.Label(image=image_tk, borderwidth=5, relief="sunken")
        self.panelA.image = image_tk
        self.panelA.grid(row= 1, column=1 , rowspan= 13, columnspan= 3, padx=20, pady=20)
        
        return image_tk

if __name__ == '__main__':
    app = App()