# Bulk-Fil-and-Folder-Renameing

This simple python script can make a bulk renaming of files and folders. 
just for saving time.

1- change the path

option 1 : if you want to change bulk folders names
          uncomment line 11 and make you custom changes.
          #os.rename(os.path.join(path, file), os.path.join(path, ''.join(['put your folder name ' + str( 1 + index)])))
          change start folder name and change the starting index as you wish.


option 2 : if you want to change bulk file names
          uncomment line 11 and make you custom changes.
          #os.rename(os.path.join(path, file), os.path.join(path, ''.join(['put your file name ' + str( 1 + index), '.png'])))
          change start file name and change the starting index as you wish, and change the extention as the file is.
          
        


