from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from numpy import imag

class CapybaraPhoto:
    def __init__(self):
        self.root = Tk()
        self.init()

    def init(self):
        self.root.title('Capybara Photo Editor')
        self.root.bind("<Escape>", self.close)
        self.root.iconphoto(True, PhotoImage(file ="resourses/icon4.png"))

    def window(self):
        self.draw_menu()
        self.draw_widgets()

        self.root.mainloop()

    def draw_menu(self):
        menu_bar = Menu(self.root)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label = 'Select image', command = self.select_image)
        file_menu.add_command(label = 'Select Folder', command = self.select_folder)
        menu_bar.add_cascade(label = 'Select', menu = file_menu)

        self.root.configure(menu = menu_bar)

    def select_image(self):
        img_path = fd.askopenfilename(filetypes=(('Images', '*.jpeg;*.jpg;*.png'), ))
        img = ImageTk.PhotoImage(Image.open(img_path))
        img_panel = Label(self.root, image=img)
        img_panel.image = img
        img_panel.pack()

    def select_folder(self):
        pass

    def draw_widgets(self):
        pass

    def close(self, event):
        self.root.quit()


if __name__ == "__main__":
    CapybaraPhoto().window()
