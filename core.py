import json
import os

def checkFile(name):
    try:
        with open('data/'+name, 'r') as f :
            return True
    except FileNotFoundError:
         return False
    except IOError:
            return False

def saveInfo(name, data):
    if(checkFile(name) == False):        
        with open('data/'+name, 'w') as f :
             json.dump(data, f, indent=4)
             f.close()
    else:
        with open('data/'+name, 'r+') as write_file:
            file = json.load(write_file)
            file["data"].append(data)
            write_file.seek(0)
            json.dump(file, write_file,indent=4)
            write_file.close()

def loadFile(name):
     if checkFile(name):
        with open('data/'+name,'r') as f :
            dicc = json.load(f)
        return dicc 
     
def editFile(name,data):
    with open('data/'+name,'w') as f :
        json.dump(data, f, indent=4)
        f.close()