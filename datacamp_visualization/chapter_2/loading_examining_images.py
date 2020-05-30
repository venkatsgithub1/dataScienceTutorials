import matplotlib.pyplot as plt

img = plt.imread('480px-Astronaut-EVA.jpg')

print(img.shape)

plt.imshow(img)

plt.axis("off")
plt.show()
