from watchdog.events import PatternMatchingEventHandler

class VideoHandler (PatternMatchingEventHandler):
    patterns = [ "*.mkv" , "*.mp4", "*.avi"]

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print(event.src_path, event.event_type)  # print now only for debug

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)