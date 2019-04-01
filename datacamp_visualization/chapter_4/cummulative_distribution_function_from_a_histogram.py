import matplotlib.pyplot as plt

image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

plt.subplot(2, 1, 1)

plt.title('original image')
plt.axis('off')
plt.imshow(image, cmap='gray')

pixels = image.flatten()

plt.subplot(2, 1, 2)
plt.xlim((0, 255))
pdf = plt.hist(pixels, bins=64, range=(0, 256),
               normed=True, color='red', alpha=0.4)

plt.grid('off')
plt.twinx()

cdf = plt.hist(pixels, bins=64, range=(0, 256), normed=True,
               cumulative=True, color='blue', alpha=0.4)

plt.xlim((0, 256))
plt.grid('off')
plt.title('PDF & CDF (original image)')

plt.show()
