import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('people.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cell_size = (8, 8)
block_size = (2, 2)
win_size = (8, 8)

nbins = 9
img_size = img.shape[:2]

# Create a HOG object
hog = cv.HOGDescriptor(
    _winSize=(win_size[1] * cell_size[1], win_size[0] * cell_size[0]),
    _blockSize=(block_size[1] * cell_size[1], block_size[0] * cell_size[0]),
    _blockStride=(cell_size[1], cell_size[0]),
    _cellSize=(cell_size[1], cell_size[0]),
    _nbins=nbins
)

# Calculate the number of cells
n_cells = (img_size[1] // cell_size[1], img_size[0] // cell_size[0])

# Compute HOG features
hog_feats = hog.compute(img)

# Reshape HOG features with an adjustable size
hog_feats = hog_feats.reshape((n_cells[1] - win_size[1] + 1, n_cells[0] - win_size[0] + 1, -1))

# Normalize the HOG features for display
hog_feats = np.uint8(hog_feats / np.max(hog_feats) * 255)

# Display the image
cv.imshow('Image of People', img)
cv.waitKey(0)

# Display HOG features using matplotlib
for i in range(hog_feats.shape[2]):
    plt.figure()
    plt.imshow(hog_feats[:, :, i], cmap='gray')
    plt.title(f'HOG Feature {i+1}')
    plt.show()

cv.destroyAllWindows()
