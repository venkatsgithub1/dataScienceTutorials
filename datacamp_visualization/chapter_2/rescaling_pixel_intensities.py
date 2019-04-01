import matplotlib.pyplot as plt

image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

pmin, pmax = image.min(), image.max()

rescaled_image = 256*(image-pmin)/(pmax-pmin)

plt.subplot(2, 1, 1)
plt.title("original image")
plt.axis("off")
plt.imshow(image)

plt.subplot(2, 1, 2)
plt.title("scaled image")
plt.axis("off")
plt.imshow(rescaled_image)

plt.show()
