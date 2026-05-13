from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"New file detected: {event.src_path}")
        # TODO: send email here

if __name__ == "__main__":
    path = "."
    observer = Observer()
    observer.schedule(Handler(), path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
