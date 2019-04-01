import matplotlib.pyplot as plt

img = plt.imread('480px-Astronaut-EVA.jpg')

plt.subplot(2, 2, 1)
plt.title('extent=(-1,1,-1,1),\naspect=0.5')

plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])

plt.imshow(img, extent=(-1, 1, -1, 1), aspect=0.5)

plt.subplot(2, 2, 2)
plt.title('extent=(-1,1,-1,1),\naspect=1')

plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])

plt.imshow(img, extent=(-1, 1, -1, 1), aspect=1)

plt.subplot(2, 2, 3)
plt.title('extent=(-1,1,-1,1),\naspect=2')

plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])

plt.imshow(img, extent=(-1, 1, -1, 1), aspect=2)

plt.subplot(2, 2, 4)
plt.title('extent=(-2,2,-1,1),\naspect=2')

plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])

plt.imshow(img, extent=(-2, 2, -1, 1), aspect=2)

plt.show()
