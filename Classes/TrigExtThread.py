from PyQt5.QtCore import QThread
import logging, threading

logging.basicConfig(level=logging.DEBUG)


class Worker(QThread):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.requestStop = False

    def run(self):
        try:
            logging.info("WorkerThread   : Starting")
            while True:

                # Perform your thread's operation here
                self.window._acquire_images()

                # Check for thread interruption request
                #if self.isInterruptionRequested():
                if self.requestStop:
                    logging.info("WorkerThread   : Shutting down")

                    break
                
        except Exception as e:
            logging.exception(f"Exception in thread: {str(e)}")
