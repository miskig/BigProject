import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            # A new file has been created, pass it to the other script
            print(f"New file found: {event.src_path}")
            # TODO: pass the file to the other script by argument

# Set the folder to watch
folder_to_watch = "path/to/folder"

# Set the script to run when a new file is found
script_to_run = "path/to/script.py"

# Create an event handler for new files
event_handler = NewFileHandler()

# Create an observer to watch the folder
observer = Observer()
observer.schedule(event_handler, folder_to_watch, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

import subprocess

# ...

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            # A new file has been created, pass it to the other script
            print(f"New file found: {event.src_path}")
            # Run the other script, passing the file as an argument
            subprocess.run([script_to_run, event.src_path])
