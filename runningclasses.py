from Classes.ClassAnalysOD import AnalyseOD
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

bright = np.array(pd.read_csv('DATA/bright.csv', delimiter=';'))
dark = np.array(pd.read_csv('DATA/image.csv', delimiter=';'))

a_ROI = [100, 400, 100, 400]
n_ROI = [500, 620, 80, 425]

images = [dark, bright]
analysis = AnalyseOD(images=images, analys_ROI=a_ROI, normalization_ROI=n_ROI)
OD = analysis.calculate_OD()

N_at, gaussian_fit_2D, _ = analysis.fit_cloud_profile_gaussian2D(OD)
raw_gaussian_profile, fit_gauss_1D, params_1D, uncertainty_1D = analysis.fit_cloud_profile_gaussian1D(OD)

plt.figure(1)
plt.imshow(OD, cmap='afmhot')
plt.tight_layout()
plt.colorbar()

plt.figure(2)
plt.title(r'Gaussian 2D Profile, $N_{at}$' f'$ = {np.round(N_at*1e-6, 2)} M$')
plt.imshow(gaussian_fit_2D, cmap='twilight')
plt.colorbar()
plt.tight_layout()

plt.figure(3)
plt.title('fit_1D')
plt.plot(raw_gaussian_profile)
plt.plot(fit_gauss_1D)
plt.tight_layout()

plt.show()





