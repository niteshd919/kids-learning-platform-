from Tkinter import*
import Tkinter
import tkMessageBox
top=Tkinter.Tk(className ="KINDS LEARNING GAMES")
c=Canvas(top,height=570,width=800,bg="gray")

filename=PhotoImage(file="back2.gif")
image=c.create_image(500,580,anchor=S,image=filename)


filename1=PhotoImage(file="dog.gif")
image1=c.create_image(120,10,anchor=N,image=filename1)

filename2=PhotoImage(file="apple.gif")
image2=c.create_image(680,250,anchor=N,image=filename2)
filename3=PhotoImage(file="ball.gif")
image3=c.create_image(90,200,anchor=N,image=filename3)

filename4=PhotoImage(file="gapple.gif")
image4=c.create_image(420,360,anchor=N,image=filename4)

filename5=PhotoImage(file="cat.gif")
image5=c.create_image(130,400,anchor=N,image=filename5)

filename6=PhotoImage(file="banana.gif")
image6=c.create_image(680,450,anchor=N,image=filename6)



def Submit():
   tkMessageBox.showinfo( "summited", "Congratulations Kid your answers are correct")



def Answer():
   top1=Tkinter.Tk(className ="Your answer")
   c1=Canvas(top1,height=500,width=800,bg="gray")
   
   CheckVar1=IntVar()
   CheckVar2=IntVar()
   CheckVar3=IntVar()
   CheckVar4=IntVar()
   CheckVar5=IntVar()
   CheckVar6=IntVar()
   CheckVar7=IntVar()
   CheckVar8=IntVar()
   CheckVar9=IntVar()

   
   CB1=Checkbutton(top1,text="CAT", variable=CheckVar1,onvalue=1,offvalue=0,height=5, width=10)
   CB2=Checkbutton(top1,text="TIGER", variable=CheckVar2,onvalue=1,offvalue=0,height=5, width=10)
   CB3=Checkbutton(top1,text="DOG", variable=CheckVar3,onvalue=1,offvalue=0,height=5, width=10)
   CB4=Checkbutton(top1,text="MANGO", variable=CheckVar4,onvalue=1,offvalue=0,height=5, width=10)
   CB5=Checkbutton(top1,text="Banana", variable=CheckVar5,onvalue=1,offvalue=0,height=5, width=10)
   CB6=Checkbutton(top1,text="APPLE", variable=CheckVar6,onvalue=1,offvalue=0,height=5, width=10)
   CB7=Checkbutton(top1,text="BAT", variable=CheckVar7,onvalue=1,offvalue=0,height=5, width=10)
   CB8=Checkbutton(top1,text="GREEN APPLE", variable=CheckVar8,onvalue=1,offvalue=0,height=5, width=10)
   CB9=Checkbutton(top1,text="BALL", variable=CheckVar9,onvalue=1,offvalue=0,height=5, width=10)


   CB1.place(x=220,y=120)
   CB2.place(x=330,y=120)
   CB3.place(x=440,y=120)
   CB4.place(x=220,y=220)
   CB5.place(x=330,y=220)
   CB6.place(x=440,y=220)
   CB7.place(x=220,y=320)
   CB8.place(x=330,y=320)
   CB9.place(x=440,y=320)

   b2=Tkinter.Button(top1, text ="Reset", command =Answer,bg="light green")
   b2.place(x=410,y=420)
   b3=Tkinter.Button(top1, text ="Submit", command =Submit,bg="light green")
   b3.place(x=300,y=420)



   c1.pack()
   top1.mainloop()

   
b1=Tkinter.Button(top, text ="Give Answers", command =Answer,bg="light green")
b1.place(x=380,y=300)





c.pack()
top.mainloop()
