import numpy as np
import matplotlib.pyplot as plt

def gaussian_2d(x, y, x0, y0, sigma, A):
    """
    Compute the value of a 2D Gaussian function at given coordinates.

    Parameters:
        x (numpy array): x-coordinates where to evaluate the Gaussian.
        y (numpy array): y-coordinates where to evaluate the Gaussian.
        x0 (float): x-coordinate of the center of the Gaussian.
        y0 (float): y-coordinate of the center of the Gaussian.
        sigma (float): Standard deviation along both x and y axes.
        A (float): Amplitude of the Gaussian.

    Returns:
        numpy array: Values of the Gaussian at the given coordinates.
    """
    exponent = ((x - x0) ** 2 + (y - y0) ** 2) / (2 * sigma ** 2)
    return A * np.exp(-exponent)

# Example usage:
image_width = 100
image_height = 100
x = np.linspace(0, image_width - 1, image_width)
y = np.linspace(0, image_height - 1, image_height)
x_mesh, y_mesh = np.meshgrid(x, y)
x0 = image_width / 2  # Center of the Gaussian in x-direction
y0 = image_height / 2  # Center of the Gaussian in y-direction
sigma = 10
A = 1
z_values = gaussian_2d(x_mesh, y_mesh, x0, y0, sigma, A)

# Plotting
plt.imshow(z_values, cmap='viridis', extent=[0, image_width, 0, image_height])
plt.colorbar(label='Intensity')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Gaussian')
plt.show()
