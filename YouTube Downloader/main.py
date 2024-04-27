# Youtube video downloader in python

from pytube import YouTube
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Video Downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)

# Keep a reference to the Entry widget
link_enter = Entry(root, width = 70, textvariable = link)
link_enter.place(x = 32, y = 90)

#function to download video
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    messagebox.showinfo("Downloaded", "Downloaded Successfully")
    # Clear the entry
    link_enter.delete(0, 'end')
    
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()