import os
import shutil

#os.remove("test.txt")

path="folder"
#os.remove(path)

try:
    #r.rmdir(path)
   shutil.rmtree(path)
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you dont have permission to delete that")
except rError:
    print("you cant delete it using that function")
else:
    print(path+" file was deleted")
