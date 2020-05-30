import matplotlib.pyplot as plt

img = plt.imread('480px-Astronaut-EVA.jpg')

print(img.shape)

intensity = img.sum(axis=2)

print(intensity.shape)

plt.imshow(intensity, cmap='gray')

plt.colorbar()

plt.axis('off')
plt.show()
