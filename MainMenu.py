from tkinter import *
import ImageManager as imgMan

class MainMenu(Frame):

    def __init__(self,parent):
        super().__init__(parent)
        self.topFrame = parent        
        self.time = 0
        self.images = 0
        self.foldersSelected = []
        self.createFolderList(self)
        self.createTimeSelection(self)
        self.createImageSelection(self)
        self.avaliable = StringVar(value="Total Images Avaliable: 0")
        self.labelTotalImages = Label(self,textvariable=self.avaliable)
        self.labelTotalImages.place(anchor="n",relx=0.5,rely=0.5)
        self.btStart = Button(self,text="Start",height=3,width=15,command=self.prepareSession)
        self.btStart.place(anchor="center",relx=0.5,rely=0.5,y=200)
        self.btClose = Button(self,text="Exit",height=3,width=15,command=self.quit)
        self.btClose.place(anchor="center",relx=0.5,rely=0.5,y=270)



    def createFolderList(self,parent):
        self.foldersContainer = LabelFrame(parent,text="Select the folders: ")
        self.foldersContainer.place(anchor="s",relx=0.5,rely=0.5,relheight=0.5,relwidth=1)
        self.canvasScrollBar = Scrollbar(self.foldersContainer,orient="vertical")
        self.canvasScrollBar.pack(side="right",fill="y")
        self.canvasScrollBar.bind("<Configure>",self.updateScrollBar)
        self.folderCanvas = Canvas(self.foldersContainer,yscrollcommand=self.canvasScrollBar.set)
        self.canvasScrollBar.configure(command=self.folderCanvas.yview)
        self.foldersList = Frame(self.folderCanvas)
        self.folderCanvas.create_window(0,0,window=self.foldersList,anchor="nw")
        self.folderCanvas.pack(side="left",fill="both")
    
    def createTimeSelection(self,parent):
        self.menuTime = IntVar(value=30)
        self.menuTimeTxt = StringVar(value="30")
        btPlacementy=10
        self.labelTime = Label(parent,text="Select the Time in seconds:",height=3)
        self.labelTime.place(anchor="n",relx=0.5,rely=0.5,y=btPlacementy)
        self.bt00 = Radiobutton(parent,text="Inf", variable=self.menuTime, value=0,command=self.selectTime)
        btPlacementy+=60
        self.bt00.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=-240)
        self.bt15 = Radiobutton(parent,text="15s", variable=self.menuTime, value=15,command=self.selectTime)
        self.bt15.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=-180)
        self.bt30 = Radiobutton(parent,text="30s", variable=self.menuTime, value=30,command=self.selectTime)
        self.bt30.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=-120)
        self.bt45 = Radiobutton(parent,text="45s", variable=self.menuTime, value=45,command=self.selectTime)
        self.bt45.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=-60)
        self.bt60 = Radiobutton(parent,text="60s", variable=self.menuTime, value=60,command=self.selectTime)
        self.bt60.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=0)
        self.bt90 = Radiobutton(parent,text="90s", variable=self.menuTime, value=90,command=self.selectTime)
        self.bt90.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=60)
        self.bt120 = Radiobutton(parent,text="120s", variable=self.menuTime, value=120,command=self.selectTime)
        self.bt120.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=120)
        self.bt300 = Radiobutton(parent,text="300s", variable=self.menuTime, value=300,command=self.selectTime)
        self.bt300.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=180)
        self.btcustom = Radiobutton(parent,text="Custom", variable=self.menuTime, value=-1,command=self.selectTime)
        self.btcustom.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=240)
        self.entryTime = Entry(parent,width=6,textvariable=self.menuTimeTxt)
        self.entryTime.config(state=DISABLED)
        self.entryTime.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=300)

    def createImageSelection(self,parent):
        self.menuImages = IntVar(value=20)
        self.menuImagesTxt = StringVar(value="20")
        self.labelImages = Label(parent,text="Select the Number of images:",height=3)
        btPlacementy=80
        self.labelImages.place(anchor="n",relx=0.5,rely=0.5,y=btPlacementy)
        btPlacementy+=60
        self.bt00 = Radiobutton(parent,text="Max", variable=self.menuImages, value=0,command=self.selectImages)
        self.bt00.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=-240)
        self.bt15 = Radiobutton(parent,text="5imgs", variable=self.menuImages, value=5,command=self.selectImages)
        self.bt15.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=-180)
        self.bt30 = Radiobutton(parent,text="10imgs", variable=self.menuImages, value=10,command=self.selectImages)
        self.bt30.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=-120)
        self.bt45 = Radiobutton(parent,text="15imgs", variable=self.menuImages, value=15,command=self.selectImages)
        self.bt45.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=-60)
        self.bt60 = Radiobutton(parent,text="20imgs", variable=self.menuImages, value=20,command=self.selectImages)
        self.bt60.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=0)
        self.bt90 = Radiobutton(parent,text="30imgs", variable=self.menuImages, value=30,command=self.selectImages)
        self.bt90.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=60)
        self.bt120 = Radiobutton(parent,text="40imgs", variable=self.menuImages, value=40,command=self.selectImages)
        self.bt120.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=120)
        self.bt300 = Radiobutton(parent,text="50imgs", variable=self.menuImages, value=50,command=self.selectImages)
        self.bt300.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=180)
        self.btcustom = Radiobutton(parent,text="Custom", variable=self.menuImages, value=-1,command=self.selectImages)
        self.btcustom.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=240)
        self.entryImages = Entry(parent,width=6,textvariable=self.menuImagesTxt)
        self.entryImages.config(state=DISABLED)
        self.entryImages.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=300)

    def setFolders(self):
        for dir in imgMan.dirList:
            var = BooleanVar()
            self.foldersSelected.append(var)
            self.btca = Checkbutton(self.foldersList,text=dir,variable=var,command=self.getFolders)
            self.btca.pack(side="top",anchor="nw")


    def getFolders(self):
        list = []
        for b in self.foldersSelected:
            list.append(b.get())
        #print(self.passFolders(list))
        #self.avaliable.set("Total Images Avaliable: "+self.passFolders(list))
        self.avaliable.set("Total Images Avaliable: "+imgMan.updateImageCount(list))
        
        

    def selectTime(self):
        self.time = self.menuTime.get()
        if(self.time>-1):
           self.menuTimeTxt.set(self.time)
           self.entryTime.config(state=DISABLED)
        else:
            self.entryTime.config(state=NORMAL)

    def selectImages(self):
        self.images = self.menuImages.get()
        if(self.images>-1):
            self.menuImagesTxt.set(self.images)
            self.entryImages.config(state=DISABLED)
            pass
        else:
            self.entryImages.config(state=NORMAL)
            pass
    def updateScrollBar(self,event):
       self.folderCanvas.configure(scrollregion=self.folderCanvas.bbox("all"))

    def prepareSession(self):
        self.topFrame
        valid = False
        valid = self.validateNumber(self.menuTime,self.menuTimeTxt) \
        and self.validateNumber(self.menuImages,self.menuImagesTxt)
        if(valid):
            self.images = self.menuImages.get()
            self.time = self.menuTime.get()
            sessionOptions = (self.time,self.images)
            self.setSession(sessionOptions)
        pass

    def validateNumber(self,varI,varS):
        s=varS.get()
        if(s.isnumeric()):
            varI.set(int(s))
            return True

        else:
            varS.set("error")
            varI.set(-1)
            return False

    def bindStartSession(self,func):
        self.setSession = func
    
    def bindUpdateImageCount(self,func):
        self.passFolders = func
"""

"""
#create main menu GUI

#folder list display

#ll2 = Button(foldersList,text= "qwerty")
#ll2.grid(row=1,column=0)
#buttons for time
"""

#buttons for images


#create gesture GUI
gestureScreen = Frame(topFrame)
#gestureScreen.place(anchor="center",relx=0.5,rely=0.5,relwidth=1,relheight=1)
#mainmenu.rowconfigure(0,weight=1)
#mainmenu.columnconfigure(0,weight=1)
root.mainloop()"""