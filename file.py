import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Rajesh Jain/OneDrive/Desktop/Python/Project 102"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print("hey  {event.scr_path} has been created!!" )

    def on_modified(self,event):
        print("hey  {event.scr_path} has been modified!!" )

    def on_moved(self,event):
        print("hey  {event.scr_path} has been moved!!" )

    def on_deleted(self,event):
        print("hey  {event.scr_path} has been deleted!!" )


# initalize event handler class

event_handler = FileEventHandler()

# initalize observer

observer = Observer()

# schedule the observer

observer.schedule(event_handler,from_dir,recursive = True)

# start the observer

observer.start()

# to stop observer

try:
    while True:
        time.sleep(2)
        print("running....")
except KeyboardInterrupt :
    print("stopped!!")
    observer.stop()