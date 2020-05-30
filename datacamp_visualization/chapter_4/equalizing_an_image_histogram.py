import numpy as np
import matplotlib.pyplot as plt

image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

pixels = image.flatten()

cdf, bins, patches = plt.hist(pixels, bins=256, range=(0, 256),
                              normed=True, cumulative=True)

new_pixels = np.interp(pixels, bins[:-1], cdf*255)

new_image = new_pixels.reshape(image.shape)

plt.subplot(2, 1, 1)
plt.title('Equalized image')
plt.axis('off')
plt.imshow(new_image, cmap='gray')

plt.subplot(2, 1, 2)
pdf = plt.hist(new_pixels, bins=64, range=(0, 256),
               normed=False, color='red', alpha=0.4)
plt.grid('off')
plt.twinx()
plt.xlim((0, 256))
plt.grid('off')
plt.title('PDF & CDF (equalized image')

cdf = plt.hist(new_pixels, bins=64, range=(0, 256),
               cumulative=True, normed=False, color='red', alpha=0.4)

plt.show()
