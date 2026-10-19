import os
import shutil

folder = input("Enter folder path to organize: ")

if not os.path.isdir(folder):
    print("Folder not found. Please check the path.")
    exit()

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if os.path.isdir(file_path):
        continue

    extension = os.path.splitext(filename)[1].lower()

    if extension in [".jpg", ".jpeg", ".png"]:
        category = "Images"
    elif extension in [".pdf", ".txt", ".docx"]:
        category = "Documents"
    elif extension in [".mp3", ".wav"]:
        category = "Music"
    else:
        category = "Others"

    destination = os.path.join(folder, category)
    os.makedirs(destination, exist_ok=True)
    shutil.move(file_path, os.path.join(destination, filename))
    print("Moved", filename, "to", category)