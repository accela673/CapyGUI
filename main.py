from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Notebook
import os

'''abs_path = os.path.abspath(__file__)
path = abs_path[:-7] + f"bw_filter_{str(self.count_bw)}"'''

count_bw = 1
class CapybaraPhoto:
    def __init__(self):
        self.root = Tk()
        self.image_tabs = Notebook(self.root)
        self.opened_images = []
        self.count_bw = 1
        self.count_r = 1
        self.count_l = 1
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
        bw_filter.grid(row=0,column=0)
        rotate_right.grid(row=0,column=2)
        rotate_left.grid(row=0,column=3)


    def bw_filter_command(self):
        os.mkdir(f"bw filter {str(self.count_bw)}")
        folder_name = (f'bw filter {str(self.count_bw)}'+'/{}_bw{}')
        
        for i in os.listdir():
            img_n, img_ext = os.path.splitext(i)
            if img_ext in ['.jpg', '.png', ".jpeg", ".jfif", ".gif", ".webp"]:
                img = Image.open(i)
                new_img = img.convert('L')
                new_img.save(folder_name.format(img_n, img_ext))
        print(folder_name)
        self.count_bw += 1
        mb.showinfo(title="Black/White filter", message="Done! Don't close the program window, just check the folder ")


    
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
        print(folder_name)
        self.count_r += 1
        mb.showinfo(title="Rotate right", message="Done! Don't close the program window, just check the folder ")

    
    
    #Same command as above but another angle
    def rotate_left_command(self):
        os.mkdir(f"rotate left {str(self.count_r)}")
        folder_name = (f'rotate left {str(self.count_r)}'+'/{}_left{}')
        
        for i in os.listdir():
            img_n, img_ext = os.path.splitext(i)
            if img_ext in ['.jpg', '.png', ".jpeg", ".jfif", ".gif", ".webp"]:
                img = Image.open(i)
                new_img = img.rotate(angle=90, expand=True)
                new_img.save(folder_name.format(img_n, img_ext))
        print(folder_name)
        self.count_r += 1
        mb.showinfo(title="Rotate left", message="Done! Don't close the program window, just check the folder ")






    def close(self, event = None):
        self.root.quit()





if __name__ == "__main__":
    CapybaraPhoto().window()
