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

plt.subplot(2, 2, 1)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('red')
plt.ylabel('green')
plt.hist2d(red_pixels, green_pixels, bins=(32, 32))

plt.subplot(2, 2, 2)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('green')
plt.ylabel('blue')
plt.hist2d(green_pixels, blue_pixels, bins=(32, 32))

plt.subplot(2, 2, 3)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('blue')
plt.ylabel('red')
plt.hist2d(blue_pixels, red_pixels, bins=(32, 32))

plt.show()
