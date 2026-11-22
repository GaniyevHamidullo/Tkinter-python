#double window
from tkinter import Tk,Toplevel,Button,Label
class window:
  def __init__(self):
    self.root=Tk()
    self.first_w=Toplevel()
    self.btn=Button(self.root,text="next")
    self.lb=Label(self.root,text="first window")
    self.btn.grid(column=0,row=0)
    self.lb.grid(column=1,row=0)
    self.root.mainloop()
  def next_w(self):
    self.first_w.mainloop()
