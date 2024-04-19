import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from ClassAnalysOD import AnalyseOD



image_transmitted = np.array(pd.read_csv('DATA/image.csv', delimiter=';'))
image_incident = np.array(pd.read_csv('DATA/bright.csv', delimiter=';'))
images = [image_transmitted, image_incident]
a_ROI = [100, 350, 375, 150]
n_ROI = [500, 620, 80, 425]
aod = AnalyseOD(images=images, analys_ROI=a_ROI, normalization_ROI=n_ROI)
OD = aod.calculate_OD()
number_atoms, fitted_profile, parameters_uncertainty = aod.fit_cloud_profile_gaussian2D(OD=OD)

H_cut, V_cut, hcut_param_uncertainty, vcut_param_uncertainty = aod.fit_cloud_profile_gaussian1D(OD=OD)

plt.figure(1)
plt.imshow(OD, cmap='hot')
plt.colorbar(label='Optical Density (OD)')
plt.title('Optical Density with ROI')
plt.tight_layout()

plt.figure(2)
plt.title(r'Gaussian 2D Profile, $N_{at}$' f'$ = {np.round(number_atoms*1e-6, 2)} M$')
plt.imshow(fitted_profile, cmap='hot')
plt.colorbar(label='Optical Density (OD)')
plt.tight_layout()

plt.figure(3)
plt.plot(V_cut)

plt.figure(4)
plt.plot(H_cut)
plt.show()
