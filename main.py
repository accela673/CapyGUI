from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter.ttk import Notebook
from PIL import Image, ImageTk
import os

class CapybaraPhoto:
    def __init__(self):
        self.root = Tk()
        self.image_tabs = Notebook(self.root)
        self.opened_images = []
        self.init()

    def init(self):
        self.root.title('Capybara Photo Editor')
        self.root.bind("<Escape>", self.close)
        self.root.iconphoto(True, PhotoImage(file ="resourses/icon4.png"))
        self.image_tabs.enable_traversal()
    
    
    def window(self):
        self.draw_menu()
        self.draw_widgets()
        self.entry()
        self.root.mainloop()
    
    def entry(self):
        path = Entry(self.root)

    def draw_menu(self):
        menu_bar = Menu(self.root)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label = 'Select image or images', command = self.select_images)
        file_menu.add_command(label = 'Save as', command = self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.close)
        menu_bar.add_cascade(label = 'File', menu = file_menu)

        self.root.configure(menu = menu_bar)

    

    def draw_widgets(self):
        self.image_tabs.pack(fill="both", expand=1)

    def select_images(self):
        img_paths = fd.askopenfilenames(filetypes=(('Images', '*.jpeg;*.jpg;*.png'), ))
        for i in img_paths:
            self.add_new_img(i)


    def add_new_img(self, img_path):
        img = Image.open(img_path)
        img_tk = ImageTk.PhotoImage(img)
        self.opened_images.append([img_path, img])
        img_tab = Frame(self.image_tabs)
        img_label = Label(img_tab, image=img_tk)
        img_label.image = img_tk
        img_label.pack(side='bottom', fill='both', expand='yes')

        self.image_tabs.add(img_tab,text=img_path.split('/')[-1])
        self.image_tabs.select(img_tab)

    def close(self, event = None):
        self.root.quit()


    def save_as(self):
        current_tab = self.image_tabs.select()
        if not current_tab:
            return
        tab_number = self.image_tabs.index(current_tab) 

        old_path, old_ext = os.path.splitext(self.opened_images[tab_number][0])
        new_path = fd.asksaveasfilename(initialdir=old_path, filetypes=(('Images', '*.jpeg;*.jpg;*.png'), ))

        if not new_path:
            return

        new_path, new_ext = os.path.splitext(new_path)


        if not new_ext:
            new_ext = old_ext
        elif new_ext != old_ext:
            mb.showerror('Incorrect extention', f'This iincorrect extention "{new_ext}", old was "{old_ext}"')

        image = self.opened_images[tab_number][1]
        image.save(new_path + new_ext)
        image.close()

        del self.opened_images[tab_number]
        self.image_tabs.forget(current_tab)

        self.add_new_img(new_path + new_ext)



if __name__ == "__main__":
    CapybaraPhoto().window()
