from tkinter import *

from MainMenu import MainMenu
from GestureScreen import GestureScreen
import ImageManager as imgMan

def startSession(tu):
    if(imgMan.getImageLen()>0):
        imgMan.randomizeImages()
        mainMenu.place_forget()
        #mainMenu.place(relx=0,relheight=1,relwidth=1)
        gestureScreen.setSession(tu)
        gestureScreen.place(relx=0,relheight=1,relwidth=1)
def exitSession():
    if(imgMan.getImageLen()>0):
        gestureScreen.place_forget()
        mainMenu.place(relx=0,relheight=1,relwidth=1)

root = Tk()
root.geometry("800x600")
root.title("DrawPoses")
root.iconphoto = ("DrawPoses_icon.ico")
topFrame = Frame(root)
imgMan.loadFolders()
#imgManager = ImageManager()
#imgManager.loadFolders()
#help(os)
#topFrame.pack(side="top",fill="both",expand=True)
topFrame.place(relx=0,relheight=1,relwidth=1)
mainMenu = MainMenu(topFrame)
mainMenu.place(relx=0,relheight=1,relwidth=1)
mainMenu.setFolders()
#mainMenu.bindUpdateImageCount(imgManager.updateImageCount)
mainMenu.bindStartSession(startSession)
gestureScreen = GestureScreen(topFrame)
gestureScreen.bindExitSession(exitSession)
#gestureScreen.place(relx=0,relheight=1,relwidth=1)
#root.bind("<ButtonPress>",teste)
root.mainloop()