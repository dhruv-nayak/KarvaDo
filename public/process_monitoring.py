import os
import time
import logging

def monitor_directory(directory):
    logging.basicConfig(filename='file_creation.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    while True:
        files = os.listdir(directory)
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                logging.info(f"File created: {file}")
        time.sleep(5)

if __name__ == "__main__":
    directory_to_monitor = "."
    monitor_directory(directory_to_monitor)