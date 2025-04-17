import os
import time

def rename_files_with_timestamp(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            new_filename = f"{filename.split('.')[0]}_{timestamp}.{filename.split('.')[-1]}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == "__main__":
    directory_path = "."
    rename_files_with_timestamp(directory_path)