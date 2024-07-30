from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkinter import filedialog

def display_image():
    url = entry.get()
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    photo = ImageTk.PhotoImage(image)

    def fit_image (path , window_size):
        path = image 
        image_width , image_height = path.size
        ratio = image_width/ image_height
        window_width , window_height = window_size
        if (window_width / window_height) > ratio:
            new_width = int(window_height * ratio)
            new_height = window_height
        else:
            new_width = window_width
            new_height = int(window_width / ratio)

        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)
    
    def resize_image(event):
        new_image = fit_image(image , (event.width , event.height))
        image_label.config(image = new_image)
        image_label.image = new_image
    
    image_copy = image.copy()
    new_window = Toplevel(root)
    new_window.title(" ")
    new_window.attributes('-topmost', True)

   
    image_label = Label(new_window, image=photo,bd = 0)
    image_label.pack(fill=BOTH, expand=YES)
    new_window.bind("<Configure>", resize_image)


def import_img():

    def fit_image (path , window_size):
        path = img_path
        image_width , image_height = path.size
        ratio = image_width/ image_height
        window_width , window_height = window_size
        if (window_width / window_height) > ratio:
            new_width = int(window_height * ratio)
            new_height = window_height
        else:
            new_width = window_width
            new_height = int(window_width / ratio)

        resized_image = path.resize((new_width, new_height), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)
    
    def resize_image(event):
        new_image = fit_image(path , (event.width , event.height))
        image_label.config(image = new_image)
        image_label.image = new_image
    
    path = filedialog.askopenfilename()
    if path :
        img_path = Image.open(path)
        img = ImageTk.PhotoImage(img_path)
        new_window = Toplevel(root)
        new_window.title(" ")
        new_window.attributes('-topmost', True)

    
        image_label = Label(new_window, image=img,bd = 0)
        image_label.pack(fill=BOTH, expand=YES)
        new_window.bind("<Configure>", resize_image)



def clear_entry():
    entry.delete(0, END)
root = Tk()
root.title("Input URL")

entry = Entry(root, width=50)
entry.pack(pady=10)

button = Button(root, text="Display Image", command=display_image)
button.pack(side=LEFT,padx=5)

clear_button = Button(root, text="Clear", command=clear_entry)
clear_button.pack(side=LEFT,padx=5)

disk_button = Button(root , text = "Import" , command=import_img)
disk_button.pack(side=RIGHT , padx = 5)

root.mainloop()
