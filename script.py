#C:\Users\VGRA\AppData\Local\Programs\Python\Python36-32


import os
import fileTools

url = "https://www.dropbox.com/sh/02xkfrbaeu8iobk/AABR7T8FTbr_25T6OoDaYVHQa?&dl=1"
filesDir = ".\\files"
zipPath = os.path.join(filesDir, "MIAGE_folder.zip")

fileTools.downloadFile(url, zipPath)
fileTools.unzipFile(zipPath, filesDir)
fileTools.deleteDirectory(filesDir)
