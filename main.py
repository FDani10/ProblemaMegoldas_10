from tkinter import *
from PIL import Image,ImageTk
from infoinfo import runInfo
from szamolas import szamolj
import ctypes

def charOnLabel(char,om):
    text = Label(om,text=f"{variables[char].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
    text.place(x=30,y=15,width=18,height=40)

def numOnLabel(char,om):
    text = Label(om,text=f"{variables[char].get()}",font=('Ariel',25),bg="#AEFFA7",justify="center")
    text.place(x=30,y=15,width=18,height=40)

def whiteOnLabel(char,om):
    text = Label(om,text=f"{variables[char].get()}",font=('Ariel',25),bg="#FFFFFF",justify="center")
    text.place(x=30,y=15,width=18,height=40)

boardsArray = []
root = Tk()

root.geometry("670x714")
root["bg"] = "#BBFBFF"
root.title("Rejtvény megoldó")
ico = Image.open('./pics/greenBlock.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# OPCIÓK
chars = [' ','/', '*', '-', '+']
numbers = [' ',0,1,2,3,4,5,6,7,8,9]

# KÉPEK
image=Image.open(f'./pics/grayBlock.png')
grayBlock=ImageTk.PhotoImage(image)
image2=Image.open(f'./pics/pinkCircle.png')
pickCircle=ImageTk.PhotoImage(image2)
image3=Image.open(f'./pics/whiteBlock.png')
whiteBlock=ImageTk.PhotoImage(image3)
image4=Image.open(f'./pics/greenBlock.png')
greenBlock=ImageTk.PhotoImage(image4)

# BANNER
image5=Image.open(f'./pics/banner.png')
banner_img=ImageTk.PhotoImage(image5)
banner = Label(root,image=banner_img)
banner["bg"] = "#BBFBFF"
banner.place(x=0,y=0)

image6=Image.open(f'./pics/infoBtn.png')
infoBtn_img=ImageTk.PhotoImage(image6)
infoBtn = Button(root,image=infoBtn_img,command=runInfo)
infoBtn["bg"] = "#BBFBFF"
infoBtn["activebackground"] = "#BBFBFF"
infoBtn["border"] = "0"
infoBtn["highlightthickness"] = 0
infoBtn.place(x=590,y=20)

# ROW 1
variables = []
inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=20,y=110)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om1 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(0,om1))
om1.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om1.place(x=108,y=110)

inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=196,y=110)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om2 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(1,om2))
om2.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om2.place(x=284,y=110)

inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=372,y=110)

inputtxt = Label(root, text="=",font=('Ariel',50),justify="center")
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=460,y=110,width=50)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
sz1 = OptionMenu(root, variable, *numbers, command= lambda e:numOnLabel(2,sz1))
sz1.config(image=greenBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
sz1.place(x=520,y=110)

# ROW 2
variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om3 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(3,om3))
om3.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om3.place(x=20,y=208)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om4 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(4,om4))
om4.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om4.place(x=196,y=208)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om5 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(5,om5))
om5.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om5.place(x=372,y=208)


# ROW 3
inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=20,y=296)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om6 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(6,om6))
om6.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om6.place(x=108,y=296)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
wb = OptionMenu(root, variable, *numbers, command= lambda e:whiteOnLabel(7,wb))
wb.config(image=whiteBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
wb.place(x=196,y=296)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om7 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(8,om7))
om7.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om7.place(x=284,y=296)

inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=372,y=296)

inputtxt = Label(root, text="=",font=('Ariel',50),justify="center")
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=460,y=296,width=50)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
sz2 = OptionMenu(root, variable, *numbers, command= lambda e:numOnLabel(9,sz2))
sz2.config(image=greenBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
sz2.place(x=520,y=296)

# ROW 4
variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om8 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(10,om8))
om8.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om8.place(x=20,y=384)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om9 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(11,om9))
om9.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om9.place(x=196,y=384)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om10 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(12,om10))
om10.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om10.place(x=372,y=384)

# ROW 5
inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=20,y=472)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om11 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(13,om11))
om11.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om11.place(x=108,y=472)

inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=196,y=472)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om12 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(14,om12))
om12.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om12.place(x=284,y=472)

inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=372,y=472)

inputtxt = Label(root, text="=",font=('Ariel',50),justify="center")
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=460,y=472,width=50)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
sz3 = OptionMenu(root, variable, *numbers, command= lambda e:numOnLabel(15,sz3))
sz3.config(image=greenBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
sz3.place(x=520,y=472)


# ROW 6
inputtxt = Label(root, text="=",font=('Ariel',50),justify="center")
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=35,y=560,width=50,height=25)

inputtxt = Label(root, text="=",font=('Ariel',50),justify="center")
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=211,y=560,width=50,height=25)

inputtxt = Label(root, text="=",font=('Ariel',50),justify="center")
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=387,y=560,width=50,height=25)

# ROW 7
variable = StringVar(root)
variable.set(' ')
variables.append(variable)
sz4 = OptionMenu(root, variable, *numbers, command= lambda e:numOnLabel(16,sz4))
sz4.config(image=greenBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
sz4.place(x=20,y=600)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
sz5 = OptionMenu(root, variable, *numbers, command= lambda e:numOnLabel(17,sz5))
sz5.config(image=greenBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
sz5.place(x=196,y=600)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
sz6 = OptionMenu(root, variable, *numbers, command= lambda e:numOnLabel(18,sz6))
sz6.config(image=greenBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
sz6.place(x=372,y=600)

# SOLVE BUTTON
image_btn=Image.open(f'./pics/megoldasBtn.png')
solveBtn=ImageTk.PhotoImage(image_btn)
btn = Button(root, command=lambda: szamolj(variables), image=solveBtn)
btn["bg"] = "#BBFBFF"
btn["activebackground"] = "#BBFBFF"
btn["border"] = "0"
btn.place(x=500,y=600)

root.mainloop()