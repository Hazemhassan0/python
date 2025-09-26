
import os
import shutil

def manage_files(directory_path):
    if not os.path.isdir(directory_path):
        print("Invalid directory. Please try again.")
        return
    
    backup_dir = os.path.join(directory_path, 'backup')
    os.makedirs(backup_dir, exist_ok=True)
    
    txt_files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]
    for file in txt_files:
        shutil.copy(os.path.join(directory_path, file), backup_dir)
    
    return len(txt_files)
