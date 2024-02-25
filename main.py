import tkinter as tk
from PIL import ImageDraw, ImageTk, ImageFont, Image
from tkinter import colorchooser
from tkinter import filedialog


class App:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry('1280x720')
        self.window.title('Image Watermarker')
        
        self.panelB = tk.Frame(self.window)
        self.panelB.grid(row=1, column=6, padx=20, pady=20)
        tk.Button(self.panelB, text='Upload', command=self.upload).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.panelB, text='Close Image', command=self.close_img).grid(row=1, column=1, padx=10, pady=10)
        self.watermark_text = tk.Entry(self.panelB)
        self.watermark_text.grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.panelB, text='Apply Watermark', command=self.apply_watermark).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.panelB, text='Choose Color', command=self.choose_color).grid(row=2, column=2, padx=10, pady=10)
        self.window.mainloop()

    def upload(self):
        self.close_img()
        f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')] 
        path = filedialog.askopenfilename(filetypes=f_types)
        image = Image.open(path)

        # Set the desired width
        new_width = 600  # replace with your desired width

        # Calculate the proportional height
        original_width, original_height = image.size
        new_height = int(original_height * (new_width / original_width))
        self.o_image = image.resize((new_width, new_height))
        image_tk = ImageTk.PhotoImage(self.o_image)

        self.panelA = tk.Label(image=image_tk, borderwidth=5, relief="sunken")
        self.panelA.image = image_tk
        self.panelA.grid(row= 1, column=1 , rowspan= 13, columnspan= 3, padx=20, pady=20)
        
        return image_tk
    
    def close_img(self):
        try:
            self.panelA.destroy()
        except AttributeError:
            pass

if __name__ == '__main__':
    app = App()