import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from get_path import get_directory

# Define the folder to monitor (Downloads folder, for example)
DOWNLOADS_FOLDER = get_directory("Downloads")
# Base directory for organizing files
BASE_DESTINATION = get_directory("Organized Downloads")

# Event handler class to handle new file events
class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        # When a new file is detected
        if event.is_directory:
            return  # Ignore directories
        print(f"New file detected: {event.src_path}")
        print("Processing file...")
        time.sleep(5)
        print("Move successful")
        file_path = event.src_path
        file_name, file_extension = os.path.splitext(file_path)

        # Generate destination folder dynamically
        if file_extension == ".tmp":  # Temp files are required for initial download
            return
        if not file_extension:  # If no extension, classify as 'Others'
            destination_folder = os.path.join(BASE_DESTINATION, "Others")
        else:
            destination_folder = os.path.join(BASE_DESTINATION, file_extension.lstrip('.').upper())
        
        # Ensure the destination folder exists
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        # Construct the destination path and move the file
        destination_path = os.path.join(destination_folder, os.path.basename(file_path))
        print(f"Moving file: {file_path} to {destination_path}")
        shutil.move(file_path, destination_path)

# Function to start monitoring
def start_monitoring():
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, DOWNLOADS_FOLDER, recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)  # Keep the program running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_monitoring()
