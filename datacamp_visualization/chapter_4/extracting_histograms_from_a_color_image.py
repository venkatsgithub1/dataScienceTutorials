import matplotlib.pyplot as plt

image = plt.imread('hs-2004-32-b-small_web.jpg')

plt.subplot(2, 1, 1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image)

red, green, blue = image[:, :, 0], image[:, :, 1], image[:, :, 2]

red_pixels = red.flatten()
blue_pixels = blue.flatten()
green_pixels = green.flatten()

plt.subplot(2, 1, 2)
plt.title('Histograms from color image')
plt.xlim((0, 256))
plt.hist(red_pixels, bins=64, normed=True, color='red', alpha=0.2)
plt.hist(green_pixels, bins=64, normed=True, color='green', alpha=0.2)
plt.hist(blue_pixels, bins=64, normed=True, color='blue', alpha=0.2)

plt.show()
