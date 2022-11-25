import os
import time
from PIL import Image
from tkinter import Tk,Label,Entry,Toplevel,PhotoImage,Scale,Button,Message,StringVar,messagebox



convPath = "E:\test"
mpath = ""

root=Tk()
root.title("PICO v1.0")
iconp=PhotoImage(file='''assets/icon.png''')
#root.logo(file=iconp)
#root.geometry("1366x768")
root.resizable(width=False, height=False)
Bg=PhotoImage(file='''/assets/Bg.png''')
comp=PhotoImage(file='''/assets/comp.png''')
comping=PhotoImage(file='''/assets/compressing.png''')
comped=PhotoImage(file='''assets/compressed.png''')
backg=Label(root,image=Bg)
mPathEntry=Entry (root,bd=3,width=40)
cRate=Entry (root,bd=3,width=10)
textvar=StringVar()
textlabel=Message(root,textvariable=textvar,width=25)
compingl=Label(root,image=comping,bd=0)
compedl=Label(root,image=comped,bd=0)

def compress(file,cPath,path,percent):
    os.chdir(path)
    filepath = os.path.join(os.getcwd(), file)
    picture = Image.open(filepath)
    os.chdir(cPath)
    picture.save(file,"JPEG",optimize=True,quality=percent)
    
	
def recall(i,coPath,path,percent):
    print(i)
    #time.sleep(1)
    #textvar.set("Compressing "+i)
    messagebox.showinfo("compressing",i)
    ctpath=coPath
    cPath= os.path.join(coPath, i)
    os.chdir(coPath)
    os.mkdir(i)
    tpath=path
    path = os.path.join(path, i)
    os.chdir(path)
    
    for folders,folderNames,file in os.walk(os.getcwd()):       
        for K in file:
            if K.endswith('.jpg') or K.endswith('.JPG'):
                compress(K,cPath,path,percent)
                
        for j in folderNames:
            
            cPath,path=recall(j,cPath,path,percent)
        return ctpath,tpath
    
    #root.mainloop()
def start():

    percent=cRate.get()
    if int(percent)<0 or int(percent)>100:
        messagebox.showerror("Error","Enter value between 0 to 100")
        return
    compingl.place(x=120,y=520)
    mpath=mPathEntry.get()
    path=mpath
    os.chdir(path)
    convPath=os.getcwd()
    os.chdir(convPath)
    os.mkdir("Pico Compressed")
    convPath = os.path.join(convPath,"Pico Compressed")
    
    print(percent)
    os.chdir(mpath)
    folders=os.listdir()
    
    for i in folders:
        recall(i,convPath,mpath,int(percent))
    messagebox.showinfo("Finished","Compression is over you can close the application")
    
    compedl.place(x=120,y=520)
                              
def main():
    
    
    
    backg.pack()
    
    mPathEntry.place(x=50,y=330)
    
    
    cRate.place(x=140,y=420)
   
    
    button = Button(root, image=comp, command=start)
    button.place(x=120,y=470)

    textlabel.place(x=120,y=490)
    
    
    
    

    root.mainloop()
    

                    
if __name__=="__main__":
    main()
