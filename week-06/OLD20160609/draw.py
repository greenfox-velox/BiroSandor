from tkinter


class Draw():
    def __init__(self):
        root = Tk()
        self.canvas = Canvas(root, width = 720, height = 720)
        self.canvas.pack()
        root.mainloop()


    def draw(self, x , y, img):
        canvas.create_image(y*size, x*size, image=img, anchor=NW)
