#C:\Users\VGRA\AppData\Local\Programs\Python\Python36-32


import os
import fileTools
import excelReader

url = "https://www.dropbox.com/sh/02xkfrbaeu8iobk/AABR7T8FTbr_25T6OoDaYVHQa?&dl=1"
filesDir = ".\\files"
zipFile = "MIAGE_folder.zip"
interestingFile = "M1-FA Miage-ETUD1.xlsx"

zipPath = os.path.join(filesDir, zipFile)
interestingFilePath = os.path.join(filesDir, interestingFile)

fileTools.downloadFile(url, zipPath)
fileTools.unzipFile(zipPath, filesDir)

excelReader.readFile(interestingFilePath)

fileTools.deleteDirectory(filesDir)
