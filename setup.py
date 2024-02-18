# to run the file use python setup.py in vs code
from tkinter import *
import speedtest
def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+"Mbps"
    up=str(round(sp.upload()/(10**6),3))+"Mbps"

    lab_down.config(text=down)
    lab_up.config(text=up)

    



#tkinter is used to make UI Graphic
sp=Tk()
sp.title("Test Internet speed")
sp.geometry("500x500")
sp.config(bg="black")
lab=Label(sp,text="Internet Speed Test",font=("Time New Roman",25,"bold"),bg="black",fg="yellow")
lab.place(x=60,y=40,height=50,width=380)

lab=Label(sp,text="Downloading Speed",font=("Time New Roman",25,"bold"),bg="black",fg="white")
lab.place(x=60,y=130,height=50,width=380)

lab_down=Label(sp,text="00",font=("Time New Roman",25,"bold"),bg="black",fg="green")
lab_down.place(x=60,y=200,height=50,width=380)

lab=Label(sp,text="Uploading Speed",font=("Time New Roman",25,"bold"),bg="black",fg="blue")
lab.place(x=60,y=250,height=50,width=380)

lab_up=Label(sp,text="00",font=("Time New Roman",25,"bold"),bg="black",fg="red")
lab_up.place(x=60,y=310,height=50,width=380)

button=Button(sp,text="Check Speed",font=("Time New Roman",25,"bold"),relief=RAISED,command=speedcheck)
button.place(x=60,y=430,height=50,width=380)


sp.mainloop()
