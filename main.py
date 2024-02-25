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
        
        self.panelB = tk.Frame(self.window)
        self.panelB.grid(row=1, column=6, padx=20, pady=20)
        tk.Label(self.panelB, text='Click the button below to upload image').pack()
        tk.Button(self.panelB, text='Upload', command=self.upload).pack()
        self.window.mainloop()

    def upload(self):
        f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')] 
        path = filedialog.askopenfilename(filetypes=f_types)
        self.o_image = Image.open(path) 

        # Set the desired width
        new_width = 600  # replace with your desired width

        # Calculate the proportional height
        original_width, original_height = self.o_image.size
        new_height = int(original_height * (new_width / original_width))

        image_tk = ImageTk.PhotoImage(self.o_image.resize((new_width, new_height)))

        self.panelA = tk.Label(image=image_tk, borderwidth=5, relief="sunken")
        self.panelA.image = image_tk
        self.panelA.grid(row= 1, column=1 , rowspan= 13, columnspan= 3, padx=20, pady=20)
        
        return image_tk

if __name__ == '__main__':
    app = App()