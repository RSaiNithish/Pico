import os
from PIL import Image



def  compress(file, c_path, path):
    os.chdir(path)
    filepath = os.path.join(os.getcwd(), file)
    picture = Image.open(filepath)
    os.chdir(c_path)
    picture.save(file,"JPEG",optimize=True,quality=5)

    

def main():
    path = r"E:\New folder\OG"
    c_path = r"E:\New folder\C"
    os.chdir(path)
    fol=os.listdir()
    folders = []
    for i in fol:
        if os.path.isfile(i) == False:
            folders.append(i)
    for i in folders:
        if os.path.isfile(i) == False:
            print("Compressing :",i)
            recall(i,c_path,path)
            print("Compressed:", i)

def recall( i,coPath,path):
    print("in with recall",i)
    ctpath=coPath
    cPath= os.path.join(coPath, i)
    os.chdir(coPath)
    os.mkdir(i)
    tpath=path
    path = os.path.join(path, i)
    os.chdir(path)
    
    for folders,folderNames,file in os.walk(os.getcwd()):       
        print(folderNames, file)
        for K in file:
            #print(K)
            if os.path.isfile(i) == False:
                if K.endswith('.jpg') or K.endswith('.JPG'):
                    compress(K,cPath,path)
                
        for j in folderNames:
            
            cPath,path=recall(j,cPath,path)
        return ctpath,tpath
        

                    
if __name__=="__main__":
    main()
