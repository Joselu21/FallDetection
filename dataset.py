import os

DIR_NAME = "Dataset"

def Exists() -> bool:
    return os.path.isdir(DIR_NAME) and os.listdir(DIR_NAME)

def Download() -> bool:
    CreateFolder()
    

def CreateFolder() -> None:
    if not os.path.isdir(DIR_NAME):
        os.makedirs(DIR_NAME)