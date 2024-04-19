#!d:\PythonProjects\AbsorptionGUI\absenv\Scripts\python.exe
""" Created by Clement Raphin on April 2nd 2024
#! is a shebang that needs to point to the virtual environment absenv python package"""

from vimba import *
import matplotlib.pyplot as plt
import numpy as np
import cv2
import threading

import logging
import time


import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from PyQt5 import QtWidgets, Qt

############################################################################
####                                                                    ####
####                            CLASSES                                 ####
####                                                                    ####
############################################################################


class VimbaDaemon(threading.Thread):
    """
    Instantiating this class creates the Vimba daemon, which keeps open the Vimba instance.
    This class inherits from the Thread class of threading library, more specifically daemon Thread.
    """
    def __init__(self, TIMEOUT = 15.):
        """
        Initializing the class.
        """
        super().__init__(name = 'VimbaDaemon',      # Initializing the inheritance tree
                         daemon=True)               # it is a daemon indeed
        
        # OUTPUT EVENTS : set by the Daemon
        self.isReadyForCapture = threading.Event()  # This event sets when the daemon is ready to begin acquisition.
        self.isStopped = threading.Event()          # Sets when the run function is stopped.
        
        # INTERNAL PARAMETERS OF THE VimbaDaemon
        self.id_to_detection = {"DEV_0xA4701120ABD31" : 1, "DEV_0xA4701120A77DD" : 2, "DEV_0xA4701120ABD33" : 3}
                                                    # Dictionary of the correspondence between cameras and camera Detection number
        self.detection_to_id = {num : identity for identity, num in self.id_to_detection.items()}
                                                    # Same as above but keys are detection numbers
                                                    
        self.detections_list = list()               # List of current cameras
            
        self.start()
        self.isReadyForCapture.wait(timeout = TIMEOUT)
        
    def getCameraList(self) -> list:
        """
        Returns a list of integers, where each value is the index of the Detection camera that is currently connected.
        """
        res = list()
        camera_list = self.vimba.get_all_cameras()
        for camera in camera_list:
            identity = camera.get_id()
            res.append(self.id_to_detection[identity])
        return res

    def openCamera(self, detection_number : int) -> Camera:
        """ 
        Opens camera whose index is detection_number.
        """
        camera_id = self.detection_to_id[detection_number]
        try:
            cam = self.vimba.get_camera_by_id(camera_id)
            logging.info(f"VimbaDaemon : Detection{detection_number} opened successfully !")
            return cam

        except VimbaCameraError:
            raise VimbaCameraError('Failed to access Camera \'{}\'. Abort.'.format(camera_id))

    def run(self) -> None:
        """ 
        Main loop of the daemon.
        """
        # Starting up
        while True:
            logging.info("VimbaDaemon : Starting connexion with Vimba")
            
            with Vimba.get_instance () as self.vimba: # Opening a Vimba connection.
                logging.info("VimbaDaemon : Vimba is connected and running. Ready for capture")
                self.isReadyForCapture.set()                    # Signalling that Vimba is ready for capture
                
                self.stopVimba = threading.Event()
                self.stopVimba.wait(None)
                
            logging.info("VimbaDaemon : Vimba is restarting")
            self.isStopped.set()
            self.isReadyForCapture.clear()
        
    def stop(self) -> None:
        logging.info("VimbaDaemon : Vimba is stopping...")
        self.stopVimba.set()
    
    def restart(self, timeout : float = 10.) -> None:
        """ 
        Restarts the Vimba instance. One should wait for the instance to be fully restarted (via isReadyForCapture event) to use it.
        """
        self.stop()
        self.isStopped.wait(timeout=timeout)
        logging.info("VimbaDaemon : Restarting Vimba...")
        self.isStopped.clear()
        
    def isAvailable(self):
        """
        Tests whether the VimbaDaemon is busy or not.
        """
        if not self.vd.isReadyForCapture.is_set():
            raise TimeoutError("VimbaDaemon not ready for capture ! It may be still loading or it is busy.")
        elif self.vd.start_acquisition.is_set():
            raise ValueError("VimbaDaemon is already in acquisition !")
        else:
            return True
        
class GuppyPro():
    def __init__(self, vimba: VimbaDaemon, detection_number: int):
        """Instantiates the camera object.
        Args:
            vimba (VimbaDaemon): the opened vimba instance
            detection_number (int): index of the camera (1, 2, 3...)
        """
        self.vimba = vimba
        self.camera = self.vimba.openCamera(detection_number)
        self.stopAcquisition = threading.Event()
        self.imagesAcquired = threading.Event()
        
    def getCameraSettings(self) -> dict:
        """Retrieves the settings of the Guppy camera.
        Returns:
            settings: dictionary of settings containing "ExposureTime", "Gain", "AcquisitionMode", "TriggerSource" and "TriggerMode" values.
        """
        res = dict()
        with self.camera as cam:
            logging.info("GuppyCam    : Updating current camera information")
            res["ExposureTime"] = cam.ExposureTime.get()
            res["Gain"] = cam.Gain.get()
            res["AcquisitionMode"] = cam.AcquisitionMode.get().as_tuple()[0]
            res["TriggerSource"] = cam.TriggerSource.get().as_tuple()[0]
            res["TriggerMode"] = cam.TriggerMode.get().as_tuple()[0]
        return res
    
    def changeCameraSettings(self, settings: dict) -> None:
        """Changes the settings of the Guppy camera to the settings passed as an argument.
        Args:
            settings (dict): dictionary of settings containing "ExposureTime", "Gain", "AcquisitionMode" and "TriggerSource" values.
        """
        with self.camera as cam:
            logging.info("GuppyCam    : Changing camera settings")
            cam.ExposureTime.set(settings["ExposureTime"])
            cam.Gain.set(settings["Gain"])
            cam.AcquisitionMode.set(settings["AcquisitionMode"])
            cam.TriggerSource.set(settings["TriggerSource"])
            cam.TriggerMode.set(settings["TriggerMode"])
    
    def setExposureTime(self, exposure_time: float) -> None:
        """
        Sets exposure time of "camera" to specified value "exposure_time" (in µs).
        Args:
            exposure_time (float) : new exposure time in µs
        """
        with self.camera as cam:
            logging.info(f"GuppyCam    : Changing exposure time to {exposure_time:.0f}")
            cam.ExposureTime.set(exposure_time)                  # changing on the camera
            
    def getExposureTime(self) ->  float:
        """Gets value of exposure time of the camera.
        Returns:
            float: exposure time of the camera (in µs)
        """
        with self.camera as cam:
            logging.info(f"GuppyCam    : Retrieving exposure time from camera")
            return cam.ExposureTime.get()
    
    def takePicture(self) -> Frame:
        """Manually trigger the camera and retrieve a picture.
        Returns:
            Frame: opencv image
        """
        self.res = list()
        def handler_single(cam : Camera, frame : Frame):
            logging.info("GuppyCam    : Handling frame")
            frame.convert_pixel_format(PixelFormat.Mono8)
            self.res = frame.as_opencv_image()
            cam.queue_frame(frame)  # Resetting the queue frame seems to be the best practice
            self.stopAcquisition.set()
            
        with self.camera as cam:
            cam.TriggerSource.set("Software")
            cam.start_streaming(handler_single)
            cam.TriggerSoftware.run()
            self.stopAcquisition.wait()
            logging.info("GuppyCam    : Frame taken. Closing camera")
            self.stopAcquisition.clear()
            return self.res
    
    def startAcquisition(self, N_IMAGES: int = 1, TIMEOUT: float = None, BUFFER_COUNT: int = 5) -> list:
        """Starts acquisition of the camera,  and returns the images captured as a list.
        Args:
            N_IMAGES (int, optional): Number of images to capture. Defaults to 1.
            TIMEOUT (float, optional): Delay (in s) before a TimeoutError is raised. Defaults to None (no timeout).
            BUFFER_COUNT (int, optional): Number of buffers to pass to the camera. 5 is largely enough in our case. Defaults to 5.
        Returns:
            res: list of the frames that were taken.
        """
        res = list()                # list of Frame objects
        self.n_images = 0           # number of images taken
        self.stopAcquisition.clear()
        self.imagesAcquired.clear()
        
        def handler(cam : Camera, frame : Frame):
            """ 
            Function that is called after each acquisition of a frame.
            """
            logging.info("GuppyCam    : Handling frame")
            self.n_images += 1
            res.append(frame)
            if self.n_images == N_IMAGES:
                self.stopAcquisition.set()
            cam.queue_frame(frame)  # Resetting the queue frame
        
        with self.camera as cam:
            logging.info("GuppyCam    : Starting acquisition")
            cam.TriggerSource.set("InputLines")
            cam.TriggerMode.set("On")
            cam.start_streaming(handler, buffer_count=BUFFER_COUNT)
            self.stopAcquisition.wait(timeout=TIMEOUT)
            self.stopAcquisition.set()
            logging.info("GuppyCam    : Stopping acquisition")
            if self.n_images == 0:
                pass
                # raise TimeoutError("No trigger detected on camera during capture window !")
            else:
                self.imagesAcquired.set()
                self.stopAcquisition.clear()
                logging.info(f"GuppyCam    : {len(res)} images acquired !")
                return [np.array(im.as_opencv_image().transpose()[0, :, :]) for im in res] # Changing the frame format for easier handling later

# ############################################################################
# ####                                                                    ####
# ####                            GuppyCam                                ####
# ####                                                                    ####
# ############################################################################

    
# if __name__ == "__main__":
    
#     ### Setting up logging
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
#     logging.info("GuppyCam    : Starting up")
    
#     ### Calling the daemon to initiate communication with Vimba
#     vimba = VimbaDaemon()
#     detection = GuppyPro(vimba, 3)
    
#     # Example of usage of the VimbaDaemon object: Retrieving the camera list
#     print(vimba.getCameraList())
    
#     # Example of usage of the GuppyPro object: Retrieving and changing the camera settings
#     settings = detection.getCameraSettings()
#     print(settings)
#     settings["ExposureTime"] = 1000
#     settings["TriggerMode"] = "On"
#     detection.changeCameraSettings(settings)
#     print(detection.getCameraSettings())
    
#     # Retrieving frames asynchronously (external trigger)
#     frames = detection.startAcquisition(N_IMAGES=2)
    
#     # # Showing the images
#     app = pg.mkQApp()
#     win = QtWidgets.QMainWindow()

#     cw = QtWidgets.QWidget()
#     win.setCentralWidget(cw)
#     layout = QtWidgets.QVBoxLayout()
#     cw.setLayout(layout)

#     im1 = pg.ImageView()
#     im1.setImage(frames[0])
#     layout.addWidget(im1)

#     im2 = pg.ImageView()
#     im2.setImage(frames[1])
#     layout.addWidget(im2)
    
#     win.show()
#     app.exec_()
#     logging.info("GuppyCam    : All done")