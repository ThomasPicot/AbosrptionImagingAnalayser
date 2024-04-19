# AnalyseOD: A class for analyzing optical density (OD) images of atomic clouds
# =============================================================================

# This class provides methods to analyze optical density (OD) images of atomic clouds obtained 
# from experiments. It includes functionalities to calculate the optical density, fit 1D and 
# 2D Gaussian profiles of the cloud, and estimate uncertainties in the fitting parameters.

# The class is designed to work with two input images: a dark image and a bright image, which
# represent the atomic cloud in its unexcited and excited states, respectively. Additionally, 
# regions of interest (ROIs) can be specified for both normalization and analysis purposes.

# Methods:
# - calculate_OD(): Computes the optical density of the cloud based on the dark and bright images.
# - fit_cloud_profile_gaussian1D(): Fits a 1D Gaussian profile to the cloud's optical density 
#                                    along specified ROIs.
# - fit_cloud_profile_gaussian2D(): Fits a 2D Gaussian profile to the cloud's optical density 
#                                    along specified ROIs.
# 


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class AnalyseOD:
    def __init__(self, images: list, analys_ROI: list = None, normalization_ROI: list = None) -> None:
        # Initialize with dark and bright images, and regions of interest
        self.dark_image: np.ndarray = np.array(images[0], dtype=float)
        self.bright_image: np.ndarray = np.array(images[1], dtype=float)
        self.analys_ROI: list = analys_ROI
        self.normalization_ROI: list = normalization_ROI

    def calculate_OD(self) -> np.ndarray:
        # Calculate optical density
        x_start: int = self.normalization_ROI[0]
        x_end: int = self.normalization_ROI[1]
        y_start: int = self.normalization_ROI[2]
        y_end: int = self.normalization_ROI[3]
        
        roi: np.ndarray = self.dark_image[y_start:y_end, x_start:x_end]
        mean_value: float = np.mean(roi)
        normalized_dark_image: np.ndarray = self.dark_image / mean_value
        normalized_bright_image: np.ndarray = self.bright_image / mean_value
        self.dark_image[self.dark_image == 0] = 1e-6
        mask: np.ndarray = (normalized_dark_image != 0) & (normalized_bright_image != 0)

        optical_density: np.ndarray = np.zeros_like(self.dark_image)
        optical_density[mask] = np.log10(normalized_bright_image[mask] / normalized_dark_image[mask])

        max_OD: float = np.amax(optical_density) 
        optical_density[optical_density == 0] = max_OD

        return optical_density
    
    def fit_cloud_profile_gaussian1D(self, OD: np.ndarray) -> tuple:
        # Fit 1D Gaussian profile of the cloud
        def gaussian(x: np.ndarray, amplitude: float, mean: float, stddev: float) -> np.ndarray:
            return amplitude * np.exp(-((x - mean) / stddev) ** 2 / 2)
        
        roi_x_start: int = self.analys_ROI[0]
        roi_x_end: int = self.analys_ROI[1]
        roi_y_start: int = self.analys_ROI[2]
        roi_y_end: int = self.analys_ROI[3]
        roi_OD: np.ndarray = OD[roi_y_end:roi_y_start, roi_x_start:roi_x_end]
        
        # Grid for the image 
        x: np.ndarray = np.arange(OD.shape[1])
        y: np.ndarray = np.arange(OD.shape[0])
        OD_x: np.ndarray = OD[int(roi_x_end - roi_x_start), :]
        OD_y: np.ndarray = OD[:, int(roi_y_start - roi_y_end)]

        # Initial guesses for the fits
        initial_guess_x: tuple = (np.amax(OD_x), np.mean(OD_x), np.std(OD_x))
        initial_guess_y: tuple = (np.amax(OD_y), np.mean(OD_y), np.std(OD_y))
        
        # Curve fitting
        poptx, pcovx = curve_fit(gaussian, x, OD_x, p0=initial_guess_x)
        popty, pcovy = curve_fit(gaussian, y, OD_y, p0=initial_guess_y)
        
        # Fitted profiles
        fitted_profile_x: np.ndarray = gaussian(x, *poptx)
        fitted_profile_y: np.ndarray = gaussian(y, *popty)

        # Calculate uncertainties
        def determine_uncertainty(popt: np.ndarray, pcov: np.ndarray, x: np.ndarray, OD_prof: np.ndarray) -> np.ndarray:
            residuals: np.ndarray = OD_prof - gaussian(x, *popt)
            OD_prof[OD_prof == 0] = 1e-6
            chi_squared: float = np.sum((residuals / OD_prof) ** 2)
            N: int = len(OD_prof)
            num_params: int = len(popt)
            dof: int = N - num_params
            reduced_chi_squared: float = chi_squared / dof
            parameter_variances: np.ndarray = np.diag(pcov)
            return np.sqrt(parameter_variances)
        
        parameters_uncertainty_x: np.ndarray = determine_uncertainty(poptx, pcovx, x, OD_prof=OD[int((roi_y_end - roi_y_start) / 2), :])
        parameters_uncertainty_y: np.ndarray = determine_uncertainty(popty, pcovy, y, OD_prof=OD[:, int((roi_x_end - roi_x_start) / 2)])
        
        return fitted_profile_x, fitted_profile_y, parameters_uncertainty_x, parameters_uncertainty_y

    def fit_cloud_profile_gaussian2D(self, OD: np.ndarray) -> tuple:
        # Fit 2D Gaussian profile of the cloud
        def gaussian_2d(xy: tuple, amplitude: float, xo: float, yo: float, sigma_x: float, sigma_y: float, theta: float) -> np.ndarray:
            x, y = xy
            xo = float(xo)
            yo = float(yo)
            a = (np.cos(theta)**2) / (2 * sigma_x**2) + (np.sin(theta)**2) / (2 * sigma_y**2)
            b = -(np.sin(2 * theta)) / (4 * sigma_x**2) + (np.sin(2 * theta)) / (4 * sigma_y**2)
            c = (np.sin(theta)**2) / (2 * sigma_x**2) + (np.cos(theta)**2) / (2 * sigma_y**2)
            g = amplitude * np.exp(- (a * ((x - xo)**2) + 2 * b * (x - xo) * (y - yo) + c * ((y - yo)**2)))
            return g.ravel()
        
        roi_x_start: int = self.analys_ROI[0]
        roi_x_end: int = self.analys_ROI[1]
        roi_y_start: int = self.analys_ROI[2]
        roi_y_end: int = self.analys_ROI[3]
        roi_OD: np.ndarray = OD[roi_y_end:roi_y_start, roi_x_start:roi_x_end]

        # Grid for the image 
        x: np.ndarray = np.arange(OD.shape[1])
        y: np.ndarray = np.arange(OD.shape[0])
        X, Y = np.meshgrid(x, y)

        # Calculate the number of atoms in the ROI of analysis 
        cross_section: float = 2.907e-13   # [m^2]
        density: np.ndarray = roi_OD / cross_section
        number_atoms: float = np.sum(density * (8.46e-6)**2)

        # Initial guess for the fit
        initial_guess: tuple = (np.max(OD), OD.shape[1] / 2, OD.shape[0] / 2, 400, 400, 0)
        
        # Curve fitting
        popt, pcov = curve_fit(gaussian_2d, (X, Y), OD.ravel(), p0=initial_guess)
        
        # Fitted profile
        fitted_profile: np.ndarray = gaussian_2d((X, Y), *popt).reshape(OD.shape)

        # Calculate uncertainties
        residuals: np.ndarray = OD.ravel() - gaussian_2d((X, Y), *popt)
        OD[OD == 0] = 1e-6
        chi_squared: float = np.sum((residuals / OD.ravel()) ** 2)
        N: int = len(OD.ravel())
        num_params: int = len(popt)
        dof: int = N - num_params
        reduced_chi_squared: float = chi_squared / dof
        parameter_variances: np.ndarray = np.diag(pcov)
        parameters_uncertainty: np.ndarray = np.sqrt(parameter_variances)
        
        return number_atoms, fitted_profile, parameters_uncertainty