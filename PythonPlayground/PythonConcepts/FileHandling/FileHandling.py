import os 

project_path = "c:\\Users\\jon\\Documents\\Projects\\Tech\\CodePlay\\CodingPlaygroundPython\\PythonPlayground"
data_files_path = project_path+"\\DataFiles"

with open(data_files_path+"\\west.txt") as file:
    file.readlines()