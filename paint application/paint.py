import tkinter.font
from tkinter import *


class PaintApp:
# ------------------------ Define my Variables ----------------------------- #
    #Stores current drawing tool used
    drawing_tool = "text" #pencil, line, arc, oval, rectangle, text
    #Tracks whether left mouse is down
    left_but = "up"
    #x and y positions for drawing with pencil
    x_pos = None
    y_pos = None
    #Tracks x & y when the mouse is clicked and released
    x1_line_pt = None
    x2_line_pt = None
    y1_line_pt = None
    y2_line_pt = None

# --------------------------- Catch Mouse Up ------------------------------- #
    def left_but_down(self, event=None):
        self.left_but = "down"
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

# -------------------------- Catch Mouse Down ------------------------------ #
    def left_but_up(self, event=None):
        self.left_but = "up"
        self.x_pos = None
        self.y_pos = None
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y
        if(self.drawing_tool == "line"):
            self.line_draw(event)
        elif(self.drawing_tool == "arc"):
            self.arc_draw(event)
        elif(self.drawing_tool == "oval"):
            self.oval_draw(event)
        elif(self.drawing_tool == "rectangle"):
            self.rectangle_draw(event)
        elif(self.drawing_tool == "text"):
            self.text_draw(event)

# -------------------------- Catch Mouse Move ------------------------------ #
    def motion(self, event=None):
        if(self.drawing_tool == "pencil"):
            self.pencil_draw(event)

# ---------------------------- Draw Pencil --------------------------------- #
    def pencil_draw(self, event=None):
        if(self.left_but == "down"):
            if(self.x_pos is not None and self.y_pos is not None):
                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE, fill="aqua")
            self.x_pos = event.x
            self.y_pos = event.y

# ----------------------------- Draw Line ---------------------------------- #
    def line_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt,self.x2_line_pt, self.y2_line_pt, smooth=TRUE, fill="aqua")

# ----------------------------- Draw Arc ----------------------------------- #
    def arc_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt
            event.widget.create_arc(coords, start=0, extent=150, style=ARC) #ARC could be PIESLICE OR CHORD ASWELL, ex style=CHORD 

# ----------------------------- Draw Oval ---------------------------------- #
    def oval_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_oval(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, fill="yellow", outline="aqua", width=2)

# -------------------------- Draw Rectangle -------------------------------- #
    def rectangle_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, fill="blue", outline="red", width=2)

# ----------------------------- Draw Text ---------------------------------- #
    def text_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt):
            #print(tkinter.font.families()) to check all the available font families
            text_font = tkinter.font.Font(family='Myanmar Text', size=16, weight='bold', slant='italic')
            event.widget.create_text(self.x1_line_pt, self.y1_line_pt, fill="aqua", font=text_font, text="this is fun")

# ---------------------------- Initialize ---------------------------------- #
    def __init__(self, root):
        drawing_area = Canvas(root)
        drawing_area.pack()
        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

root = Tk()
paint_app = PaintApp(root)
root.mainloop()

"""
    _........_  
  .'     o    '.  
 /   o       o  \ 
|o        o     o|
/'-.._o     __.-'\
\      `````     \
|``............'`|
 \              / 
  `.__________.`     
  😊😊😊😊😊😊😊
"""
