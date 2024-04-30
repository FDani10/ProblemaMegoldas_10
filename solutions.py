from tkinter import *
from PIL import Image,ImageTk

canvases = []

canvas1x = 0

root = None

def showSolutions(boardsArray,variables):
    global root
    root = Toplevel()
    root.geometry("870x714")
    root["bg"] = "#BBFBFF"
    root.title("Megoldások")

    ico = Image.open('./pics/greenBlock.ico')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    if len(boardsArray) != 0:

        # KÉPEK
        image=Image.open(f'./pics/grayBlock.png')
        grayBlock=ImageTk.PhotoImage(image)
        image2=Image.open(f'./pics/pinkCircle.png')
        pickCircle=ImageTk.PhotoImage(image2)
        image3=Image.open(f'./pics/whiteBlock.png')
        whiteBlock=ImageTk.PhotoImage(image3)
        image4=Image.open(f'./pics/greenBlock.png')
        greenBlock=ImageTk.PhotoImage(image4)
        image_al=Image.open(f'./pics/arrowLeft.png')
        arrow_left_img=ImageTk.PhotoImage(image_al)
        image_ar=Image.open(f'./pics/arrowRight.png')
        arrow_r_img=ImageTk.PhotoImage(image_ar)
        for i in range(0,len(boardsArray)):
            
            canvas = Canvas(root,bg="#BBFBFF")
            canvas.place(x=i*870,y=0,width=870,height=714)
            canvases.append(canvas)

            # BANNER
            image5=Image.open(f'./pics/megoldasokBanner.png')
            banner_img=ImageTk.PhotoImage(image5)
            banner = Label(root,image=banner_img)
            banner["bg"] = "#BBFBFF"
            banner.place(x=0,y=0)

            # ROW 1
            inputtxt = Label(canvases[i], image=grayBlock)
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=140,y=110)
            text = Label(inputtxt,text=f"{boardsArray[i].r11}",font=('Ariel',25),bg="#575757",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            om1 = Label(canvases[i])
            om1.config(image=pickCircle,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            om1.place(x=228,y=110)
            text = Label(om1,text=f"{variables[0].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            inputtxt = Label(canvases[i], image=grayBlock)
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=316,y=110)
            text = Label(inputtxt,text=f"{boardsArray[i].r12}",font=('Ariel',25),bg="#575757",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            om2 = Label(canvases[i])
            om2.config(image=pickCircle,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            om2.place(x=404,y=110)
            text = Label(om2,text=f"{variables[1].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            inputtxt = Label(canvases[i], image=grayBlock)
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=492,y=110)
            text = Label(inputtxt,text=f"{boardsArray[i].r13}",font=('Ariel',25),bg="#575757",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            inputtxt = Label(canvases[i], text="=",font=('Ariel',50),justify="center")
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=580,y=110,width=50)

            sz1 = Label(canvases[i])
            sz1.config(image=greenBlock,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            sz1.place(x=640,y=110)
            text = Label(sz1,text=f"{variables[2].get()}",font=('Ariel',25),bg="#AEFFA7",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            # ROW 2
            om3 = Label(canvases[i])
            om3.config(image=pickCircle,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            om3.place(x=140,y=208)
            text = Label(om3,text=f"{variables[3].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            om4 = Label(canvases[i])
            om4.config(image=pickCircle,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            om4.place(x=316,y=208)
            text = Label(om4,text=f"{variables[4].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            om5 = Label(canvases[i])
            om5.config(image=pickCircle,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            om5.place(x=492,y=208)
            text = Label(om5,text=f"{variables[5].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
            text.place(x=30,y=15,width=18,height=40)


            # ROW 3
            inputtxt = Label(canvases[i], image=grayBlock)
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=140,y=296)
            text = Label(inputtxt,text=f"{boardsArray[i].r21}",font=('Ariel',25),bg="#575757",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            om6 = Label(canvases[i])
            om6.config(image=pickCircle,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            om6.place(x=228,y=296)
            text = Label(om6,text=f"{variables[6].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            wb = Label(canvases[i])
            wb.config(image=whiteBlock,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            wb.place(x=316,y=296)
            text = Label(wb,text=f"{boardsArray[i].r22}",font=('Ariel',25),bg="#FFFFFF",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            om7 = Label(canvases[i])
            om7.config(image=pickCircle,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            om7.place(x=404,y=296)
            text = Label(om7,text=f"{variables[8].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            inputtxt = Label(canvases[i], image=grayBlock)
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=492,y=296)
            text = Label(inputtxt,text=f"{boardsArray[i].r23}",font=('Ariel',25),bg="#575757",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            inputtxt = Label(canvases[i], text="=",font=('Ariel',50),justify="center")
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=580,y=296,width=50)

            sz2 = Label(canvases[i])
            sz2.config(image=greenBlock,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            sz2.place(x=640,y=296)
            text = Label(sz2,text=f"{variables[9].get()}",font=('Ariel',25),bg="#AEFFA7",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            # ROW 4
            om8 = Label(canvases[i])
            om8.config(image=pickCircle,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            om8.place(x=140,y=384)
            text = Label(om8,text=f"{variables[10].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            om9 = Label(canvases[i])
            om9.config(image=pickCircle,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            om9.place(x=316,y=384)
            text = Label(om9,text=f"{variables[11].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            om10 = Label(canvases[i])
            om10.config(image=pickCircle,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            om10.place(x=492,y=384)
            text = Label(om10,text=f"{variables[12].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            # ROW 5
            inputtxt = Label(canvases[i], image=grayBlock)
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=140,y=472)
            text = Label(inputtxt,text=f"{boardsArray[i].r31}",font=('Ariel',25),bg="#575757",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            om11 = Label(canvases[i])
            om11.config(image=pickCircle,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            om11.place(x=228,y=472)
            text = Label(om11,text=f"{variables[13].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            inputtxt = Label(canvases[i], image=grayBlock)
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=316,y=472)
            text = Label(inputtxt,text=f"{boardsArray[i].r32}",font=('Ariel',25),bg="#575757",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            om12 = Label(canvases[i])
            om12.config(image=pickCircle,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            om12.place(x=404,y=472)
            text = Label(om12,text=f"{variables[14].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            inputtxt = Label(canvases[i], image=grayBlock)
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=492,y=472)
            text = Label(inputtxt,text=f"{boardsArray[i].r33}",font=('Ariel',25),bg="#575757",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            inputtxt = Label(canvases[i], text="=",font=('Ariel',50),justify="center")
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=580,y=472,width=50)

            sz3 = Label(canvases[i])
            sz3.config(image=greenBlock,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            sz3.place(x=640,y=472)
            text = Label(sz3,text=f"{variables[15].get()}",font=('Ariel',25),bg="#AEFFA7",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            # ROW 6
            inputtxt = Label(canvases[i], text="=",font=('Ariel',50),justify="center")
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=155,y=560,width=50,height=25)

            inputtxt = Label(canvases[i], text="=",font=('Ariel',50),justify="center")
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=331,y=560,width=50,height=25)

            inputtxt = Label(canvases[i], text="=",font=('Ariel',50),justify="center")
            inputtxt["bg"] = "#BBFBFF"
            inputtxt.place(x=507,y=560,width=50,height=25)

            # ROW 7
            sz4 = Label(canvases[i])
            sz4.config(image=greenBlock,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            sz4.place(x=140,y=600)
            text = Label(sz4,text=f"{variables[16].get()}",font=('Ariel',25),bg="#AEFFA7",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            sz5 = Label(canvases[i])
            sz5.config(image=greenBlock,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            sz5.place(x=316,y=600)
            text = Label(sz5,text=f"{variables[17].get()}",font=('Ariel',25),bg="#AEFFA7",justify="center")
            text.place(x=30,y=15,width=18,height=40)

            sz6 = Label(canvases[i])
            sz6.config(image=greenBlock,border=0,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
            sz6.place(x=492,y=600)
            text = Label(sz6,text=f"{variables[18].get()}",font=('Ariel',25),bg="#AEFFA7",justify="center")
            text.place(x=30,y=15,width=18,height=40)
        
            if i != 0:
                al = Button(canvases[i],image=arrow_left_img,bg="#BBFBFF",command=slideLeft)
                al["bg"] = "#BBFBFF"
                al["activebackground"] = "#BBFBFF"
                al["border"] = "0"
                al["highlightthickness"] = 0
                al.place(x=41,y=350,width=58,height=94)

            if i != len(boardsArray)-1:
                ar = Button(canvases[i],image=arrow_r_img,bg="#BBFBFF",command=slideRight)
                ar["bg"] = "#BBFBFF"
                ar["activebackground"] = "#BBFBFF"
                ar["border"] = "0"
                ar["highlightthickness"] = 0
                ar.place(x=795,y=350,width=58,height=94)

    else:
        nincs = Label(root,text="Nincs megoldása ennek a rejtvénynek!")
        nincs.place(x=50,y=300)

    root.mainloop()


def slideLeft():
    for i in range(0,len(canvases)):
        canvases[i].place(x=canvases[i].winfo_x()+870,y=0)
    
def slideRight():
    for i in range(0,len(canvases)):
        canvases[i].place(x=canvases[i].winfo_x()-870,y=0)
