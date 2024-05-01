from tkinter import *
from PIL import Image,ImageTk

def runInfo():
    info = Toplevel()
    info.geometry("500x500")
    info.resizable(False,False)
    info["bg"] = "#BBFBFF"
    info.title("Információ")

    ico = Image.open('./pics/greenBlock.ico')
    photo = ImageTk.PhotoImage(ico)
    info.wm_iconphoto(False, photo)

    image=Image.open(f'./pics/grayBlock.png')
    grayBlock=ImageTk.PhotoImage(image)
    image2=Image.open(f'./pics/pinkCircle.png')
    pickCircle=ImageTk.PhotoImage(image2)
    image3=Image.open(f'./pics/whiteBlock.png')
    whiteBlock=ImageTk.PhotoImage(image3)
    image4=Image.open(f'./pics/greenBlock.png')
    greenBlock=ImageTk.PhotoImage(image4)
    image5=Image.open(f'./pics/infoBanner.png')
    infoBanner_img=ImageTk.PhotoImage(image5)

    infoBanner = Label(info,image=infoBanner_img,bg="#BBFBFF")
    infoBanner.place(x=0,y=0)

    gb = Label(info,image=grayBlock,bg="#BBFBFF")
    gb.place(x=40,y=120)
    gb_info = Label(info,text="Ezeknek a kockáknak a tartalmát\n nem lehet átírni",font=('Ariel',15),bg="#BBFBFF")
    gb_info.place(x=170,y=130)

    gb = Label(info,image=pickCircle,bg="#BBFBFF")
    gb.place(x=40,y=220)
    gb_info = Label(info,text="Ebbe kerülnek a jelek\n('/', '*', '+', '-')",font=('Ariel',15),bg="#BBFBFF")
    gb_info.place(x=220,y=230)

    gb = Label(info,image=whiteBlock,bg="#BBFBFF")
    gb.place(x=40,y=320)
    gb_info = Label(info,text="Ebbe kerül a középső szám,\nami meg van adva",font=('Ariel',15),bg="#BBFBFF")
    gb_info.place(x=200,y=330)

    gb = Label(info,image=greenBlock,bg="#BBFBFF")
    gb.place(x=40,y=420)
    gb_info = Label(info,text="Ebbe kerül a sor/oszlop\n végeredménye",font=('Ariel',15),bg="#BBFBFF")
    gb_info.place(x=210,y=430)

    info.mainloop()