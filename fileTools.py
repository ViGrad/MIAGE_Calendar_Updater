#C:\Users\VGRA\AppData\Local\Programs\Python\Python36-32
# -*-coding:Latin-1 -*
import zipfile
import os
import urllib.request

def createParentDirIfNotExist(directory):
    absPath = os.path.abspath(directory)
    parentDir = os.path.split(absPath)[0]

    if not os.path.exists(parentDir):
        os.makedirs(parentDir)


def downloadFile(url, filePath):
    createParentDirIfNotExist(filePath)

    u = urllib.request.urlopen(url)
    data = u.read()
    u.close()

    with open(filePath, "wb") as f :
        f.write(data)


def unzipFile(filePath, zippedFile):
    createParentDirIfNotExist(filePath)

    zip_ref = zipfile.ZipFile(filePath, 'r')
    zip_ref.extractall(zippedFile)
    zip_ref.close()


def deleteFilesInDirectory(directory):
    fileList = os.listdir(directory)
    for fileName in fileList:
        filePaht = os.path.join(directory, fileName)
        os.remove(filePaht)


def deleteDirectory(directory):
    for root, dirs, files in os.walk(directory):
        for dirName in dirs:
            dirPath = os.path.join(directory, dirName)
            deleteDirectory(dirPath)

    deleteFilesInDirectory(directory)
    os.rmdir(directory)




#deleteFilesInDirectory(filesDir)