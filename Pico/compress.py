import os
from PIL import Image
from PIL import UnidentifiedImageError
import shutil


def  compress(file, c_path, path):
    os.chdir(path)
    filepath = os.path.join(os.getcwd(), file)
    try:
        picture = Image.open(filepath)
    except UnidentifiedImageError:
        return None
    os.chdir(c_path)
    picture.save(file,"JPEG",optimize=True,quality=80)

    
def shift(file, c_path, path):
    os.chdir(path)
    filepath = os.path.join(os.getcwd(), file)
    cfilepath = os.path.join(c_path, file)
    shutil.copy(filepath,cfilepath)

def main():
    path = os.getcwd()
    c_path = "/mnt/0C587C1F587C0A2A/Files/Python/Pico/Pico"
    os.chdir(path)
    #print(c_path)
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
                else:
                    shift(K,cPath,path)
                
        for j in folderNames:
            
            cPath,path=recall(j,cPath,path)
        return ctpath,tpath
        

                    
if __name__=="__main__":
    main()
