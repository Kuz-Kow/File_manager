from pathlib import Path

folders_ext = {"Images" : [".jpeg",".gif",".png"] , "Documents":[".doc",".pdf",".txt"], "Music" : [".mp3", ".wav"], "Python":[".py"]}

def main() -> None:
    
   
    
    dir_path = ask_path()
    
    files = (Path(file) for file in dir_path.iterdir() if file.is_file())
    
    create_dirs(dir_path)
    
    for path in sort_files(dir_path,files):
        print(f"Moved {path.name} to {path}  ")
    

def ask_path():
    p = Path(input("Provide directory path: "))
    
    if p.is_dir():
        return p
    else:
        raise ValueError("Wrong path was provided")    


def create_dirs(dir_path):
    for dir in folders_ext:
        new_dir = dir_path / dir
        new_dir.mkdir(exist_ok = True)

def sort_files(dir_path,files):
    for file in files:
        for extensions in folders_ext.items():
            if file.suffix in extensions[1]:
                file_dir_path = Path(dir_path / file.name)
                yield file_dir_path.rename(dir_path /  extensions[0]/file.name)
        

if __name__ == "__main__":
    main()
