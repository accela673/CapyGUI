from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Notebook

from PIL import Image, ImageOps

import os


'''Instructions to use program if you didn't read readme:

download
move file named "main.py" to folder with images that you want to edit
open via code editor the folder, where you moved the file "main.py"
run "main.py" (to run code you have to download Tkinter and pillow libary)"'''


class CapybaraPhoto:
    def __init__(self):
        self.root = Tk()
        self.label = Label(self.root, text="Choose a Button")
        self.label.grid(row=0,column=0)
        self.image_tabs = Notebook(self.root)
        self.count_bw = 1
        self.count_r = 1
        self.count_l = 1
        self.count_u = 1
        self.count_m = 1
        self.count_n = 1
        self.mes = "Done! Don't close the program window, just check the folder"
        self.init()

    def init(self):
        self.root.geometry('400x400')
        
        # you can change title name here 
        self.root.title('Capybara Photo Editor')
        self.root.bind("<Escape>", self.close)
        self.image_tabs.enable_traversal()
    
    def window(self):
        self.buttons()
        self.root.mainloop()


    #Creating buttons and setting commands
    def buttons(self):
        bw_filter = Button(self.root, width=18, height=5, text="Apply a BW filter", command=self.bw_filter_command)
        rotate_right = Button(self.root, width=18, height=5, text="Rotate image right", command=self.rotate_right_command)
        rotate_left = Button(self.root, width=18, height=5, text="Rotate image left", command=self.rotate_left_command)
        upside = Button(self.root, width=18, height=5, text="Upside image", command=self.upside_command)
        mirror = Button(self.root, width=18, height=5, text="Mirror image", command=self.mirror_command)
        negative = Button(self.root, width=18, height=5, text="Negative image", command=self.negative_command)
        bw_filter.grid(row=1, column=0)
        rotate_right.grid(row=1, column=2)
        rotate_left.grid(row=1, column=3)
        upside.grid(row=2, column=0)
        mirror.grid(row=2, column=2)
        negative.grid(row=2, column=3)


    def bw_filter_command(self):
        os.mkdir(f"bw filter {str(self.count_bw)}")
        folder_name = (f'bw filter {str(self.count_bw)}'+'/{}_bw{}')
        
        for i in os.listdir():
            img_n, img_ext = os.path.splitext(i)
            if img_ext in ['.jpg', '.png', ".jpeg", ".jfif", ".gif", ".webp"]:
                img = Image.open(i)
                new_img = img.convert('L')
                new_img.save(folder_name.format(img_n, img_ext))
        
        self.count_bw += 1
        mb.showinfo(title="Black/White filter", message=self.mes)


    
    def rotate_right_command(self):
        #There is I created new folder
        os.mkdir(f"rotate right {str(self.count_r)}")
        folder_name = (f'rotate right {str(self.count_r)}'+'/{}_right{}')
        
        for i in os.listdir():
            img_n, img_ext = os.path.splitext(i)
            if img_ext in ['.jpg', '.png', ".jpeg", ".jfif", ".gif", ".webp"]:
                img = Image.open(i)

                #There you can change the angle if you want
                new_img = img.rotate(angle=-90, expand=True)

                new_img.save(folder_name.format(img_n, img_ext))
       
        self.count_r += 1
        mb.showinfo(title="Rotate right", message=self.mes)

    
    
    #Same command as above but another angle
    def rotate_left_command(self):
        os.mkdir(f"rotate left {str(self.count_l)}")
        folder_name = (f'rotate left {str(self.count_l)}'+'/{}_left{}')
        
        for i in os.listdir():
            img_n, img_ext = os.path.splitext(i)
            if img_ext in ['.jpg', '.png', ".jpeg", ".jfif", ".gif", ".webp"]:
                img = Image.open(i)
                new_img = img.rotate(angle=90, expand=True)
                new_img.save(folder_name.format(img_n, img_ext))

        self.count_l += 1
        mb.showinfo(title="Rotate left", message=self.mes)


    def upside_command(self):
        os.mkdir(f"upside {str(self.count_u)}")
        folder_name = (f'upside {str(self.count_u)}'+'/{}_upside{}')
        
        for i in os.listdir():
            img_n, img_ext = os.path.splitext(i)
            if img_ext in ['.jpg', '.png', ".jpeg", ".jfif", ".gif", ".webp"]:
                img = Image.open(i)
                new_img = img.rotate(angle=180, expand=True)
                new_img.save(folder_name.format(img_n, img_ext))

        self.count_u += 1
        mb.showinfo(title="Upside image", message=self.mes)



    def mirror_command(self):
        os.mkdir(f"mirror {str(self.count_m)}")
        folder_name = (f'mirror {str(self.count_m)}'+'/{}_mirror{}')
        
        for i in os.listdir():
            img_n, img_ext = os.path.splitext(i)
            if img_ext in ['.jpg', '.png', ".jpeg", ".jfif", ".gif", ".webp"]:
                img = Image.open(i)
                new_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                new_img.save(folder_name.format(img_n, img_ext))

        self.count_m += 1
        mb.showinfo(title="Mirror image", message=self.mes)

    def negative_command(self):
        os.mkdir(f"negative {str(self.count_n)}")
        folder_name = (f'negative {str(self.count_n)}'+'/{}_negative{}')
        
        for i in os.listdir():
            img_n, img_ext = os.path.splitext(i)
            if img_ext in ['.jpg', '.png', ".jpeg", ".jfif", ".gif", ".webp"]:
                img = Image.open(i)
                new_img = ImageOps.invert(img)
                new_img.save(folder_name.format(img_n, img_ext))

        self.count_n += 1
        mb.showinfo(title="Negative image", message=self.mes)




    def close(self, event = None):
        self.root.quit()





if __name__ == "__main__":
    CapybaraPhoto().window()
