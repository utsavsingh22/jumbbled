import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = [
      "python",
      "india",
      "swift",
      "canada",
      "java",
      "america",
      "london",
      "education"
      ]
words = [
      "nptoyh",
      "aidin",
      "wfsit",
      "cdanaa",
      "avja",
      "aiearcm",
      "odnlon",
      "cationude"
      ]
num = random.randrange(0,8,1)

def res():
      global words,answers,num
      num = random.randrange(0,7,1)
      lbl.config(text=words[num])
      e1.delete(0, END)

def default():
      global words,answers,num
      lbl.config(text = words[num])



def checkans():
      global words,answers,num
      var = e1.get()
      if var == answers[num]:
            messagebox.showinfo("Success", "this is a correct answer")
            res()
      else:
            messagebox.showerror("Error", "this is not correct")
            e1.delete(0, END)
            
root = tkinter.Tk()
root.geometry("350x400+400+300")
root.title("jumbbled")
root.configure(background = "#000000")

lbl = Label(
      root,
      text = "your here",
      font = ("verdana", 20),
      bg = "#000000",
      fg = "#ffffff",
)      
lbl.pack(ipady=10,ipadx=10)


ans1 = StringVar()
e1 = Entry(
      root,
      font = ("Verdana",18),
      textvariable = ans1,
)      
e1.pack(ipady=5,ipadx=5)
btncheck = Button(
      root,
      text = "check",
      font = ("comic sans ms", 18),
      width = 18,
      bg = "#4c4b4b",
      fg = "#6ab04c",
      relief = GROOVE,
      command = checkans,
)
btncheck.pack(ipady = 40)

btnreset = Button(
      root,
      text = "reset",
      font = ("comic sans ms", 18),
      width = 18,
      bg = "#4c4b4b",
      fg = "#EA425C",
      relief = GROOVE,
      command = res,
)
btnreset.pack()
default()

root.mainloop()
